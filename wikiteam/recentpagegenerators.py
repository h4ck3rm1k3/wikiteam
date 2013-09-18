#!/usr/bin/python
# -*- coding: utf-8  -*-
"""
This module offers a wide variety of page generators. A page generator is an
object that is iterable (see http://www.python.org/dev/peps/pep-0255/ ) and
that yields page objects on which other scripts can then work.

In general, there is no need to run this script directly. It can, however,
be run for testing purposes. It will then print the page titles to standard
output.

These parameters are supported to specify which pages titles to print:

&params;
"""
#
# (C) Pywikipedia bot team, 2005-2010
#
# Distributed under the terms of the MIT license.
#
__version__='$Id: pagegenerators.py 10218 2012-05-16 15:10:55Z xqt $'

import wikipedia as pywikibot
import re
from time import sleep
from dateutil import parser
import speedydeletion

parameterHelp = u"""\
-recentchangessince

"""

docuReplacements = {'&params;': parameterHelp}

# if a bot uses GeneratorFactory, the module should include the line
#   docuReplacements = {'&params;': pywikibot.pagegenerators.parameterHelp}
# and include the marker &params; in the module's docstring

# For python 2.4 compatibility
# see http://www.mail-archive.com/python-dev@python.org/msg12668.html
try:
  GeneratorExit
except NameError:
  class GeneratorExit(Exception): pass


class GeneratorFactory(object):
    """Process command line arguments and return appropriate page generator.
    This factory is responsible for processing command line arguments
    that are used by many scripts and that determine which pages to work on.
    """
    def __init__(self):
        self.gens = []
        self.namespaces = []
        self.limit = None



    def handleArg(self, arg):
        """Parse one argument at a time.

        If it is recognized as an argument that specifies a generator, a
        generator is created and added to the accumulation list, and the
        function returns true.  Otherwise, it returns false, so that caller
        can try parsing the argument. Call getCombinedGenerator() after all
        arguments have been parsed to get the final output generator.

        """
        #not used site = pywikibot.getSite()
        gen = None

        if arg.startswith('-recentchangessince'):
          name ='-recentchangessince'

          since=(arg[len(name)+1:])
          pywikibot.output("Since:%s" % since)
          self.gen = RecentchangesSincePageGenerator(since = since)
          return self.gen

        elif arg.startswith('-'):
            mode, log, user = arg.partition('log')
            if log == 'log' and mode not in ['-', '-no']: #exclude -log, -nolog
                #number = 500
                if not user:
                    user = None
                else:
                    try:
                        #number = int(user[1:])
                        user = None
                    except ValueError:
                        user = user[1:]
                if user:
                    result = user.split(';')
                    user = result[0]


        if gen:
            return gen
        else:
            return False



def RecentchangesPageGenerator(number=100, site=None):
    """Generate pages that are in the recent changes list.

    @param number: iterate no more than this number of entries

    """
    if site is None:
        site = pywikibot.getSite()
    for item in site.recentchanges(number=number):
        yield item[0]

def RecentchangesSincePageGenerator(since=None, site=None):
    """Generate pages that are in the recent changes list.

    @param since: time since you want to check

    """
    if site is None:
        site = pywikibot.getSite()

    #nto used fd = date.FormatDate(site)

    for item in site.recentchanges(
        number=5000,
        rcstart=since,
        rctype = 'edit',
        #rcprop = ['user','comment','timestamp','title','ids','loginfo','sizes']
    ):
      #      print item
      yield item


prog = re.compile(r'(delete|deletion|Afd)', re.IGNORECASE)
    
class Processor :
  def __init__(self):
    pass

  def process_page(self,page):
    timev=page[1]
    #length=page[2]
    user=page[4]
    comment=page[5]
    pagename=page[0]
    timeo=parser.parse(timev)
    result = prog.search(comment) 
    if result :
      try:
        #      print "\tgetting",pagename,timev,timeo, comment
        content=pagename.get()
        #  print "\tgot",content
        self.out.proc(pagename,user,timev,timeo, comment,content)
        #  else:
        #    print "\tSKIP\t",pagename,time,timeo, comment
        return (timeo,timev)
      except Exception, e:
        pywikibot.output(str(e))
        pywikibot.output("\tSKIP error\t",pagename,time,timeo, comment)
        return (timeo,timev)
    else:
      return (timeo,timev)


  def process_until(self,starttimeo, starttimev):
    i=0
    #starttimeo=parser.parse(starttime)
    while (True):
        pywikibot.output( "Looking back to %s " % starttimev)
        gen = RecentchangesSincePageGenerator(since = starttimev)
        for page in gen:
          i+=1
          if isinstance(page, (list, tuple)):
            
            data= self.process_page(page)
            if data is None:
              return None
            else:
              (timeo,timev) = data
          if timeo < starttimeo :
            return timev

  def process_continue(self,last_timev):
    gen = RecentchangesSincePageGenerator()
    maxtime = None
    i=0
    for page in gen:
      i+=1

      if isinstance(page, (list, tuple)):
        #print page
        data= self.process_page(page)
        if data is None:
          print "data is none"
          #return None
          pass
        else:
          (timeo,timev) = data

        if maxtime is None:
          maxtime=timeo
          maxtimev=timev
        elif timeo > maxtime :
          maxtime=timeo
          maxtimev=timev

        if last_timev is not None:
          if timev < last_timev:
            pywikibot.output("up to date for %s %s" % (timev, timeo))
            return maxtime, maxtimev
      else:
        raise Exception("single page")
    return maxtime, maxtimev


def main(*args):

  in_proc=Processor()
  out_proc=speedydeletion.SpeedyDeletion()
  in_proc.out=out_proc

  #print args
  #  since = "2013-09-15T00:00:01Z"
  since = ""
  #maxtime=None
  last_time=None
  last_timev=None
  #i = 0

  while (True):
    pywikibot.output( "restarting with %s" % since)

    data = in_proc.process_continue(last_timev)
    if data is None :
      raise Exception("bla")
      continue
      
    (new_last_time,new_last_timev) =data
    pywikibot.output( "got up to  %s %s" % (new_last_time,new_last_timev))

    if last_time is None :
      last_time=new_last_time
      last_timev=new_last_timev
    else:
      final_time =in_proc.process_until(last_time, last_timev)
      pywikibot.output( "now got up to  %s" % final_time)
      last_time=new_last_time
      last_timev=new_last_timev

    sleep(10)
       
if __name__=="__main__":
    main()

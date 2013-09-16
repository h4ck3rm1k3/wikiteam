# -*- coding: utf-8 -*-
__version__='$Id: speedydeletion.py 9692 2011-10-30 15:03:29Z xqt $'
#
import re, sys, string
import wikipedia as pywikibot
from pywikibot import i18n
import config, pagegenerators, catlib
import replace
import xmlreader


import signal
import sys
def signal_handler(signal, frame):
        print 'You pressed Ctrl+C!'
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)
pywikibot.setAction("Speedydeletion realtime Bot")
import unicodedata

def decode(link) :
    b = link
    link = unicode(link, 'utf-8')
    link = unicodedata.normalize('NFKD', link)
    return strip(link)

def decodeuc(link) :
    b = link
    link = unicode(link)
    link = unicodedata.normalize('NFKD', link)
    return strip(link)


def strip(link) :
    b = link
    link = link.encode('ascii','ignore')
    return link


import subprocess    

class SpeedyDeletion :
        def __init__(self):
                importsite = "speedydeletion"
                self.site = pywikibot.getSite("en",importsite)
                self.site.forceLogin()

        def push(self,page , usernames, contents):
                title= page.title()
                #print "push BEGIN%sEND" % title
                # if  re.search(r'^Wikipedia:' , title):
                #         return
                # elif  re.search("^User:" , title):
                #         return
                # elif  re.search("^User Talk:" , title):
                #         return
                # elif  re.search(".css$" , title):
                #         return
                # elif  re.search("^Main Page" , title):
                #         return 
                
#                title = title.replace(":","_")
                title = title.replace("!","_")
                title = title.replace("/","_")
                title = title.replace("\\","_")
                #title = decode(title)
                if (len(title) < 1):
                        pywikibot.output(u'empty title:%s' % entry.title)
                        return

                outpage = pywikibot.Page(
                        site=self.site, 
                        title=title, 
                        insite=self.site)
                try:
			exists = outpage.exists()
		except :
			pywikibot.output(u'key error exiting article %s transformed to %s' % (entry.title , title) )                           

                pywikibot.output(u'is not there, adding  %s' % title)

                if re.search('Template:', title):
                        contents = contents +  "<noinclude>{{wikipedia-template|%s}}</noinclude>" % usernames
                else:
                        contents = contents +  "\n{{wikipedia-deleted|%s}}" % usernames
                outpage._site=self.site
                try :
                        outpage.put(contents)
                except :
                        pywikibot.output(u'cannot put article %s / %s' % (page.title() , title) )                           

        def proc(self,pagename,user,timev,timeo, comment,content):
                #print pagename,timev,timeo, comment,content
                pywikibot.setAction("Speedydeletion Real-Time Bot, changes from %s with comment %s" % (user,comment))
                try :
                        self.push(pagename,user,content)
                except:
                        pywikibot.output(u'cannot put article %s ' % (page.title() ))

def main(*args):

    print "ARGS:%s\n" % sys.argv

    genFactory = pagegenerators.GeneratorFactory()
    # If xmlfilename is None, references will be loaded from the live wiki.
    xmlfilename = None
    user = None
    skip = False
    timestamp = None
    # read command line parameters
    for arg in pywikibot.handleArgs(*args):
        xmlfilename = arg
    print xmlfilename 
    insite = pywikibot.getSite("en","wikipedia")
    importsite = "speedydeletion"
    outsite = pywikibot.getSite("en",importsite)
    outsite.forceLogin()

    try :
        print "try to open %s\n" % xmlfilename
        with open(xmlfilename) as f: pass
    except :
        print "cannot open %s\n" % xmlfilename
        exit (0)

    if sys.argv[1] == "--validate" :
        tempfile = "%s.tmp" % xmlfilename
        status = subprocess.call("xmllint --recover  %s -o %s" % (xmlfilename,tempfile) , shell=True)
        print "status %d\n" % status
    else:
        tempfile = xmlfilename
        

    dump = xmlreader.XmlDump(tempfile)
    count = 0
    
    for entry in dump.parse():
#        print  file_store[entry.title] 
        title=entry.title.encode("utf8","ignore")

        if  re.search("^Wikipedia:" , entry.title):
#            pywikibot.output(u'skipping %s' % entry.title)
            continue
        if  re.search("^User:" , entry.title):
#            pywikibot.output(u'skipping %s' % entry.title)
            continue
        if  re.search("^User Talk:" , entry.title):
#            pywikibot.output(u'skipping %s' % entry.title)
            continue
        if  re.search(".css$" , entry.title):
#            pywikibot.output(u'skipping %s' % entry.title)
            continue
        if  re.search("^Main Page" , entry.title):
#            pywikibot.output(u'skipping %s' % entry.title)
            continue
#        pywikibot.output(u'Considering %s' % entry.title)
        title = title.replace(":","_")
        title = title.replace("!","_")
        title = title.replace("/","_")
        title = title.replace("\\","_")
	title = decode(title)
        try :
            if (len(title) < 1):
                pywikibot.output(u'empty title:%s' % entry.title)
                continue;

            if (file_store[title] ) :
                count = count +1
            else:
                    pywikibot.output(u'not exists %s' % entry.title)
        except KeyError :
            try :
                outpage = pywikibot.Page(site=outsite, title=entry.title, insite=outsite)

		exists =False
                try:
			exists = outpage.exists()
		except :
			pywikibot.output(u'key error exiting article %s transformed to %s' % (entry.title , title) )                           

                if exists :
                    #pywikibot.output(u'there is an article %s' % entry.title)
                    try:
                        file_store[title] = 1
                    except  KeyError :
                        pywikibot.output(u'key error saving article %s transformed to %s' % (entry.title , title) )                           

                else:
                    pywikibot.output(u'is not there, adding  %s' % entry.title)
                    contents = entry.text
                    usernames = entry.username
                    if re.search('Template:', title):
                        contents = contents +  "<noinclude>{{wikipedia-template|%s}}</noinclude>" % usernames
                    else:
                        contents = contents +  "\n{{wikipedia-deleted|%s}}" % usernames
                    outpage._site=outsite
		    try :
			    outpage.put(contents)
		    except :
                        pywikibot.output(u'cannot put article %s / %s' % (entry.title , title) )                           
                try :
                    file_store[title] = 1
                except KeyboardInterrupt:
                    print "Bye"
                    sys.exit()

                except KeyError:
                    pywikibot.output(u'could not save %s! to the list of article' % entry.title)


            except KeyboardInterrupt:
                print "Bye"
                sys.exit()
            except KeyError:
                pywikibot.output(u'problem with  %s! ' % entry.title)

            finally:
                count = count + 1

        except KeyboardInterrupt:
            print "Bye"
            sys.exit()
        except KeyError:
            pywikibot.output(u'problem2 with  %s! ' % entry.title)

        finally:
            count = count + 1

if __name__ == "__main__":
    try:
        main()
    finally:
        pywikibot.stopme()

##See also 
# http://stackoverflow.com/questions/1112343/how-do-i-capture-sigint-in-python

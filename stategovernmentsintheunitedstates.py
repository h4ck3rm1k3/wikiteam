# -*- coding: utf-8 -*-
__version__='$Id: stategovernmentsintheunitedstates.py 9692 2011-10-30 15:03:29Z xqt $'
#
import re, sys, string
import wikipedia as pywikibot
from pywikibot import i18n
import config, pagegenerators, catlib
import replace
import xmlreader

from shove import Shove
file_store = Shove('file://wikiaupload')

import signal
import sys
def signal_handler(signal, frame):
        print 'You pressed Ctrl+C!'
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)


import subprocess    

def main(*args):
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
    importsite = "stategovernmentsintheunitedstates"
    outsite = pywikibot.getSite("en",importsite)
    outsite.forceLogin()

    try :
        print "try to open %s\n" % xmlfilename
        with open(xmlfilename) as f: pass
    except :
        print "cannot open %s\n" % xmlfilename
        exit (0)

    tempfile = "%s.tmp" % xmlfilename

    status = subprocess.call("xmllint --recover  %s -o %s" % (xmlfilename,tempfile) , shell=True)
    print "status %d\n" % status

    dump = xmlreader.XmlDump(tempfile)
    count = 0
    
    for entry in dump.parse():
        title=entry.title.encode("utf8","ignore")
        if  re.search("^Wikipedia:" , entry.title):
            pywikibot.output(u'skipping %s' % entry.title)
            continue
        if  re.search("^User:" , entry.title):
            pywikibot.output(u'skipping %s' % entry.title)
            continue
        if  re.search("^User Talk:" , entry.title):
            pywikibot.output(u'skipping %s' % entry.title)
            continue
        if  re.search(".css$" , entry.title):
            pywikibot.output(u'skipping %s' % entry.title)
            continue
        if  re.search("^Main Page" , entry.title):
            pywikibot.output(u'skipping %s' % entry.title)
            continue
        title = title.replace(":","_")
        title = title.replace("!","_")
        title = title.replace("/","_")
        title = title.replace("\\","_")

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

                
                if outpage.exists():
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
                        contents = contents +  "\n{{wikipedia|%s}}" % usernames
                    outpage._site=outsite
                    outpage.put(contents)
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

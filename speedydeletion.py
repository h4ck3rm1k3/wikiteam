# -*- coding: utf-8 -*-
__version__='$Id: speedydeletion.py 9692 2011-10-30 15:03:29Z xqt $'
#
import re, sys, string
import wikipedia as pywikibot
from pywikibot import i18n
import config, pagegenerators, catlib
import replace
import xmlreader


from shove import Shove

mem_store = Shove()
file_store = Shove('file://mystore')


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

    importsite = "speedydeletion"

    outsite = pywikibot.getSite("en",importsite)
    outsite.forceLogin()

    dump = xmlreader.XmlDump(xmlfilename)
    count = 0
    for entry in dump.parse():
#        print  file_store[entry.title] 
        title=entry.title.encode("ascii","ignore")
        

        m = re.search("Wikipedia:" , entry.title)
        if  m:
            pywikibot.output(u'skipping %s' % entry.title)
            next;
        if entry.title != "Main Page" :
            try :
                if (file_store[title] ) :
                    count = count +1
#                    pywikibot.output(u'was cached %s' % entry.title)
                else:
                    pywikibot.output(u'not exists %s' % entry.title)
            except KeyError :
                print sys.exc_type, ":", "%s is not in the list." % sys.exc_value
                pywikibot.output(u'key error %s' % entry.title)
                try :
                    outpage = pywikibot.Page(site=outsite, title=entry.title, insite=outsite)
                    if outpage.exists():
                        pywikibot.output(u'there is an article %s' % entry.title)
                        file_store[title] = 1
                    else:
                        pywikibot.output(u'is not there  %s' % entry.title)
                        contents = entry.text
                        usernames = entry.username
                        contents = contents +  "\n{{wikipedia-deleted|%s}}" % usernames
                        print "going to put outpage"
                        outpage._site=outsite
                        print outpage.site
                        print outpage.site.family.name
                        print outpage.site.lang
                        outpage.put(contents)
                    try :
                        file_store[title] = 1
                    except:
                        pywikibot.output(u'could not save %s! to the list of article' % entry.title)
                finally:
                    count = count + 1
            finally:
                count = count + 1
                #print "done with %s %d" % (entry.title, count)


if __name__ == "__main__":
    try:
        main()
    finally:
        pywikibot.stopme()

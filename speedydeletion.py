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
file_store = Shove('file://wikiaupload')

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
    importsite = "speedydeletion"
    outsite = pywikibot.getSite("en",importsite)
    outsite.forceLogin()
    dump = xmlreader.XmlDump(xmlfilename)
    count = 0

    try :
        print "try to open %s\n" % xmlfilename
        with open(xmlfilename) as f: pass
    except :
        print "cannot open %s\n" % xmlfilename
        exit (0)

    for entry in dump.parse():
#        print  file_store[entry.title] 
        title=entry.title.encode("ascii","ignore")

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
        pywikibot.output(u'Considering %s' % entry.title)
        try :
            if (file_store[title] ) :
                count = count +1
            else:
                    pywikibot.output(u'not exists %s' % entry.title)
        except KeyError :
            try :
                outpage = pywikibot.Page(site=outsite, title=entry.title, insite=outsite)
                if outpage.exists():
                    pywikibot.output(u'there is an article %s' % entry.title)
                    try:
                        file_store[title] = 1
                    except  KeyError :
                        pywikibot.output(u'key error saving article %s' % entry.title)                           
                else:
                    pywikibot.output(u'is not there, adding  %s' % entry.title)
                    contents = entry.text
                    usernames = entry.username
                    if re.search('Template:', title):
                        contents = contents +  "<noinclude>{{wikipedia-template|%s}}</noinclude>" % usernames
                    else:
                        contents = contents +  "\n{{wikipedia-deleted|%s}}" % usernames
                    outpage._site=outsite
                    outpage.put(contents)
                try :
                    file_store[title] = 1
                except:
                    pywikibot.output(u'could not save %s! to the list of article' % entry.title)
            finally:
                count = count + 1
        finally:
            count = count + 1

if __name__ == "__main__":
    try:
        main()
    finally:
        pywikibot.stopme()

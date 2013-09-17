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


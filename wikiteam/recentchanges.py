
u'''
we want to listen to all the changes to wikipedia and pick up any speedy deletion marked article
'''

url='https://en.wikipedia.org/w/index.php?title=Special:RecentChanges&feed=atom'


import feedparser
d = feedparser.parse(url, modified=None)
#print d['feed']
print d['feed']['updated']
print d


#self.modified = util.get(d, 'modified', None)
# {'updated': u'2013-09-07T00:41:54Z', 
#  'subtitle': u'Track the most recent changes to the wiki in this feed.', 
#  'links': [{'href': u'http://en.wikipedia.org/w/index.php?title=Special:RecentChanges&feed=atom', 
#             'type': u'application/atom+xml', 
#             'rel': u'self'}, 
#            {'href': u'http://en.wikipedia.org/wiki/Special:RecentChanges', 
#             'type': u'text/html', 'rel': u'alternate'}], 
#  'language': u'en', 
#  'title': u'Wikipedia  - Recent changes [en]', 
#  'generator': u'MediaWiki 1.22wmf15', 
#  'generator_detail': {'name': u'MediaWiki 1.22wmf15'}, 
#  'subtitle_detail': {'base': u'https://en.wikipedia.org/w/index.php?title=Special:RecentChanges&feed=atom', 
#                      'type': u'text/plain', 'value': u'Track the most recent changes to the wiki in this feed.',
#                      'language': u'en'}, 
#  'guidislink': True, 
#  'title_detail': {
#      'base': u'https://en.wikipedia.org/w/index.php?title=Special:RecentChanges&feed=atom', 
#      'type': u'text/plain', 
#      'value': u'Wikipedia  - Recent changes [en]', 
#      'language': u'en'}, 
#  'link': u'http://en.wikipedia.org/wiki/Special:RecentChanges', 
#  'id': u'http://en.wikipedia.org/w/index.php?title=Special:RecentChanges&feed=atom',
#  'updated_parsed': time.struct_time(tm_year=2013, tm_mon=9, tm_mday=7, tm_hour=0, tm_min=41, tm_sec=54, tm_wday=5, tm_yday=250, tm_isdst=0)}

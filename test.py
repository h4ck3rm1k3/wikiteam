import re
name="<Key: wikipedia-delete-2012-06,wtarchive090612064145.zip>"
#name="<Key: wikipedia-delete-2012-05,archive2012-05-28T21:34:02.302183.zip>"
print "name %s " % (name)
match = re.search(r'.+(wtarchive\d+\.zip).+',name)
print match
if (match) :
    print "match %s" % match
    print "g1 %s" % match.group(1)
    print "g0 %s" % match.group(0)
print "done"    

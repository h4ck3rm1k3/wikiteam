import os
import glob
import re
import sys

print "starting"

path = './'
for infile in glob.glob( os.path.join(path, '*') ):
    print "current file is: " + infile
    match = re.search(r'(\d\d\d\d)(\d\d)(\d\d)(\d\d)(\d\d)(\d\d)',infile)
    match = re.search(r'w\-(\d+)\-wiki',infile)
#    match = re.search(r'.+(dddddddddddddd).+',infile)
#    match = re.search(r'.+(\dddddddddddddd).+',infile)
    if (match) :
        print "match %s" % match
        print "g1 %s" % match.group(1)
#        print "g0 %s" % match.group(0)
        ts=match.group(1)
        fn="enwikipediaorg_w-%s-wikidump/enwikipediaorg_w-%s-history.xml" % (ts, ts)
        pn="enwikipediaorg_w-%s-wikidump*" % (ts)
        zn="wtarchive%s*" % (ts)
        cmd = "python ../speedydeletion.py --validate ./%s" % fn
        print cmd
        stat=os.system(cmd)
        print stat
        if (stat >0) :
            sys.exit (stat)

        dn="enwikipediaorg_w-%s-wikidump/" % ts
        target= "./done/%s" % dn
        if not(os.path.exists(target)):
            cmd = "rm -rf ./%s" % pn

            print cmd
            stat = os.system(cmd)
            print stat
            if (stat >0) :
                sys.exit(stat)

            cmd = "rm -rf ./%s" % zn
            print cmd
            stat = os.system(cmd)
            print stat
            if (stat >0) :
                sys.exit(stat)


        else:
            cmd = "rm -rf ./%s" % dn
            print cmd
            stat = os.system(cmd)
            print stat
            if (stat >0) :
                sys.exit(stat)

        
    else:
        print "no match %s" % infile

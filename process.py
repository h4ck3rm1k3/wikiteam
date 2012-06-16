import os
import glob
import re
import sys



path = '../wikiteam/data/'
for infile in glob.glob( os.path.join(path, '*') ):
#    print "current file is: " + infile
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
        cmd = "python speedydeletion.py ../wikiteam/data/%s" % fn
        print cmd
        stat=os.system(cmd)
        print stat
        if (stat >0) :
            sys.exit (stat)

        dn="enwikipediaorg_w-%s-wikidump/" % ts
        target= "../wikiteam/data/done/%s" % dn
        if not(os.path.exists(target)):
            cmd = "rm -rf ../wikiteam/data/%s" % pn
            # removing the old data, we have it on archive.org
#            cmd = "mv ../wikiteam/data/%s ../wikiteam/data/done/" % dn
            print cmd
            stat = os.system(cmd)
            print stat
            if (stat >0) :
                sys.exit(stat)

            cmd = "rm -rf ../wikiteam/data/%s" % zn
            print cmd
            stat = os.system(cmd)
            print stat
            if (stat >0) :
                sys.exit(stat)


        else:
            cmd = "rm -rf ../wikiteam/data/%s" % dn
            print cmd
            stat = os.system(cmd)
            print stat
            if (stat >0) :
                sys.exit(stat)

        
    else:
        print "no match %s" % infile

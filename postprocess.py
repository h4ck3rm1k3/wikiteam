import boto
import re
import os
import StringIO
import zipfile 
#bucket wikipedia-delete-2012-05
# algorithm 
#  get each wtarchive*.zip, get the list of articles first, check if there are any we need, then download them
url = "http://archive.org/download/wikipedia-delete-2012-05/wtarchive300512081506.zip/enwikipediaorg_w-20120530-wikidump/enwikipediaorg_w-20120530-titles.txt"
#http://ia601203.us.archive.org/zipview.php?zip=/24/items/wikipedia-delete-2012-05/wtarchive300512081506.zip&file=enwikipediaorg_w-20120530-wikidump/enwikipediaorg_w-20120530-titles.tx
conn = boto.connect_s3(host='s3.us.archive.org', is_secure=False)
buckets =conn.get_all_buckets()
from boto.s3.key import Key


def process_zip(fname, data) :
    output = StringIO.StringIO()
    output.write(data)
    zf = zipfile.ZipFile(output, mode='r')
    il= zf.infolist()
    for zi in il :
        print("%s %s" % (fname,zi.filename))
#            d = zf.open(zi)
#            self.indexfile=d
#            self.readindex (fname,zi.filename,position,block)

for b in buckets:
#            print "compare %s and %s " % (b.name , bucket)
    #if re.search(r'wikipedia-delete-(\d\d\d\d)-(\d\d)',b.name):
    if re.search(r'wikipedia-delete-(\d\d\d\d)-(\d\d)',b.name):
        print "found %s" % b.name
        store = b
        print store

        keys = store.get_all_keys()
        for k in keys :
            print k
            rkey = Key(store)
            rkey.key = k
            print "name %s type %s" % (rkey.name, rkey.content_type)
            name = "%s" % rkey.name
            match = re.search(r'.+(wtarchive\d+\.zip)>',name)

            if (match) :
                print "match %s" % match.group(1)
#                print "g1 %s" % match.group(1)
#                print "g0 %s" % match.group(0)

                zipfilename = match.group(1)

#                data = rkey.get_contents_as_string()
                outfilename="data/old%s" % zipfilename
                data = rkey.get_contents_to_filename(outfilename)
                print outfilename
                os.system("unzip %s-d data/" % outfilename)


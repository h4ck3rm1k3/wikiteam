import boto
import sys
from boto.s3.key import Key
import datetime
def percent_cb(complete, total):
    sys.stdout.write('.')
    sys.stdout.flush()

def push_zip (file):
    d =datetime.datetime.now()

    year = d.year
    month= d.month
    block= "wikipedia-delete-v2-%0.4d-%02d" % (year, month)
    print "going to use %s" % block
    conn = boto.connect_s3(host='s3.us.archive.org', is_secure=False)
    bucket = conn.get_bucket(block)
    if not bucket:
        bucket = conn.create_bucket(block)
    k = Key(bucket)
    k.key = file
    hdrs = {}
    hdrs['x-archive-queue-derive'] = '0'
    hdrs['x-archive-queue-derive'] = '0'
    hdrs['x-archive-meta-mediatype']= "texts"
    hdrs['x-archive-meta-collection']="opensource"
    hdrs['x-archive-meta-title']="fosm node index "
    hdrs['x-archive-meta-description']="fosm index object"
    hdrs['x-archive-meta-creator']="james michael dupont<jamesmikedupont@gmail.com>"
    hdrs['x-archive-meta-subject']="fosm,osm"
    hdrs['x-archive-meta-licenseurl']='http://creativecommons.org/licenses/by-nc/3.0/'

    k.set_contents_from_filename(file,
                                 headers=hdrs,
                                 cb=percent_cb, 
                                 num_cb=10)
    print "Uploaded %s" % file

zipfilename = sys.argv[1]
push_zip (zipfilename)
push_zip ("%s.md5" % zipfilename)

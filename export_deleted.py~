import wikipedia as pywikibot
import pagegenerators
import config
import catlib
import distutils.dir_util
import pagegenerators
import os.path
import boto
from datetime import datetime
from boto.s3.key import Key
import sys
import zipfile 
from datetime import datetime

def percent_cb(complete, total):
    sys.stdout.write('.')
    sys.stdout.flush()

def push_zip (file):
    d =datetime.today()
    datestring =d.isoformat()
    year = d.year
    month= d.month
    block= "wikipedia-delete-%0.4d-%02d" % (year, month)
    print "going to use %s" % block
    conn = boto.connect_s3(host='s3.us.archive.org', is_secure=False)
    bucket = conn.get_bucket(block)
    if not bucket:
        bucket = conn.create_bucket(block)
    k = Key(bucket)
    k.key = file
    k.set_contents_from_filename(file,
                                 cb=percent_cb, num_cb=10)
    print "Uploaded %s" % file

def GetXml (page):
     headers = {'User-Agent': 'PythonWikipediaBot/1.0'} # Needs to fool Wikipedia so it will give us the file
     params = urllib.urlencode({'title': 'Special:Export','pages': page.title(), 'action': 'submit', 'limit': limit, 'offset' : offset})
     req = urllib2.Request(url='http://en.wikipedia.org/w/index.php',data=params, headers=headers)
     fIN = urllib2.urlopen(req)
     string =fIN.read()
     fIN.close()
     return string

def Main () :
    site = pywikibot.getSite()
    d =datetime.today()
    datestring =d.isoformat()
    zipfilename="archive%s.zip" % datestring
    z = zipfile.ZipFile(zipfilename, "w") 
    for x in ('Candidates_for_speedy_deletion_as_hoaxes',
              'Candidates_for_speedy_deletion_as_importance_or_significance_not_asserted',
              'Candidates_for_speedy_deletion_for_unspecified_reason') :
        cat = catlib.Category(site, x)
        pages = cat.articlesList(False)
        gen = pagegenerators.PreloadingGenerator(pages,100)
        for Page in gen:
            outfile = "PAGES/%s.txt" % Page.urlname()
            text= Page.get()
            sutf8 = text.encode('UTF-8')
            print outfile
            z.writestr(outfile,sutf8)
        
        count=0


        for strings in gen.data:
            for string in strings:
                for string2 in string:
                    count = count +1
#                    sutf8 = string2.encode('UTF-8')
                    z.writestr("RawFiles/%s%d.xml" % (x,count) ,string2)

            
    z.close()
    push_zip(zipfilename)

Main()

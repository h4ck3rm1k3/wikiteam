import sys
import re
import os
import urllib
from shove import Shove
file_store = Shove('file://mystore2')

def saveName(title):
#    an = title.encode("ascii","ignore")
    an = title
    print "storing %s" % an
    file_store[an] = title

def isNewTitle(name):
    name = urllib.unquote(name)
    print "checking %s" % name

    try :
        if (file_store[name] ) :
            print "Skipping %s" % name
            return 0
        else:
            return 1
    except KeyError :
        print "not seen %s" % name 
        return 1
#    except:
#        print "other except"
#        return 1

def domain2prefix(config={}):
    """  """
    domain = ''
    if config['api']:
        domain = config['api']
    elif config['index']:
        domain = config['index']
    domain = domain.lower()
    domain = re.sub(r'(https?://|www\.|/index\.php|/api\.php)', '', domain)
    domain = re.sub(r'/', '_', domain)
    domain = re.sub(r'\.', '', domain)
    domain = re.sub(r'[^A-Za-z0-9]', '_', domain)
    return domain

def checkAPI(api):
    return True
def checkIndexphp(indexphp):
    return True


#resume()

def getParameters(datestamp,params=[]):
    if not params:
        params = sys.argv[1:]
    config = {
        'curonly': False,
        'date': datestamp,
        'api': "http://en.wikipedia.org/w/api.php",
        'index': '',
        'xml': True,
        'namespaces': ['all'],
        'exnamespaces': [],
        'path': '',
        'delay': 0,
    }
    other = {
        'resume': False,
        'filenamelimit': 100, #do not change
        'force': False,
    }
    #console params

    if (not config['api'] and not config['index']) or \
       (config['api'] and not re.search('/api\.php', config['api'])) or \
       not (config["xml"] ) or \
       (other['resume'] and not config['path']):
        usage()
        sys.exit()
    
    #user chosen --api, --index it is neccesary for special:export, we generate it
    if config['api'] and not config['index']:
        config['index'] = config['api'].split('api.php')[0] + 'index.php'
        #print 'You didn\'t provide a path for index.php, trying to wonder one:', config['index']
    
    if config['api']:
        #check api.php
        if checkAPI(config['api']):
            print 'api.php is OK'
        else:
            print 'Error in api.php, please, provide a correct path to api.php'
            sys.exit()
    
    if config['index']:
        #check index.php
        if checkIndexphp(config['index']):
            print 'index.php is OK'
        else:
            print 'Error in index.php, please, provide a correct path to index.php'
            sys.exit()
    
    #calculating path, if not defined by user with --path=
    if not config['path']:
        config['path'] = './%s-%s-wikidump' % (domain2prefix(config=config), config['date'])
    
    return config, other

def undoHTMLEntities(text=''):
    """  """
    text = re.sub('&lt;', '<', text) # i guess only < > & " need conversion http://www.w3schools.com/html/html_entities.asp
    text = re.sub('&gt;', '>', text)
    text = re.sub('&amp;', '&', text)
    text = re.sub('&quot;', '"', text)
    text = re.sub('&#039;', '\'', text)
    return text


def parseAfdName(title):
    ret=0
    # now, let check if this is an Afd, and extract the page name
    if re.search('Wikipedia.Articles.for.deletion', title):
        ret=1
    if re.search('Wikipedia%3AArticles.for.deletion',title):
        ret =1
    return ret


def parseAfd(xml):
    # now, let check if this is an Afd, and extract the page name
    m = re.search('===\[\[(.+)\]\]===', xml)
    if (m):
        name=m.group(1)
        print "found new page %s" % name
        return name
    return 0

def resume (config):
    xmlsubtitles = []

    lasttitle = ''
    try:
        fname = '%s/%s-%s-titles.txt' % (config['path'], domain2prefix(config=config), config['date'])
        print fname 
        f = open(fname, 'r')
        raw = f.read()
        titles = raw.split('\n')
        lasttitle = titles[-1]
        if not lasttitle: #empty line at EOF ?
            lasttitle = titles[-2]
            f.close()
    except:
        print "error in reading"
        return #
    if lasttitle == '--END--':
                #titles list is complete
        print 'Title list was completed in the previous session'
    else:
        print 'Title list is incomplete. Reloading...'
                #do not resume, reload, to avoid inconsistences, deleted pages or so


    xmliscomplete = False
    lastxmltitle = ''
 #   try:
    fname = '%s/%s-%s-%s.xml' % (config['path'], domain2prefix(config=config), config['date'], config['curonly'] and 'current' or 'history')
    print "check %s" % fname
    f = open(fname, 'r')
    inafd=0
    for l in f:
#        print l
        if re.findall('</mediawiki>', l):
            xmliscomplete = True
        xmltitles = re.search(r'<title>([^<]+)</title>', l) #weird if found more than 1, but maybe

        if (xmltitles):
            name =xmltitles.group(1)
#            print "titles1:%s" % name
            inafd=parseAfdName(name)
            if (inafd):
                if isNewTitle(name):
                    print "titles:%s" % name
                    saveName(name)

        xmlsubtitles = re.search(r'===\[\[(.+)\]\]===', l) 
        if (xmlsubtitles):
            name=xmlsubtitles.group(1)
            if (inafd):
                if isNewTitle(name):
                    print "Afd:%s" % name
                    saveName(name)


#    print xmlsubtitles
#    print titles 

#    while titles and titles[-1] in ['', '--END--']:
#        titles = titles[:-1]

    if xmliscomplete:
        print 'XML dump was completed in the previous session'

def main (params=[]) :
    datestamp="20120623090939"
    configfilename = 'config.txt'
    
    config, other = getParameters(datestamp,params=params)
        
    print 'Analysing %s' % (config['api'] and config['api'] or config['index'])

    originalpath = config['path'] # to avoid concat blabla-2, blabla-2-3, and so on...
#    config['path'] = '%s-%d' % (originalpath, c)
    print 'Trying "%s"...' % (config['path'])
    
    resume(config)

main()

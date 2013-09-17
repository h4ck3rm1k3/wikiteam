# -*- coding: utf-8  -*-
"""
Basic HTTP access interface.

This module handles communication between the bot and the HTTP threads.

This module is responsible for
    - Providing a (blocking) interface for HTTP requests
    - Urlencoding all data
    - Basic HTTP error handling
"""

#
# (C) Pywikipedia bot team, 2012
#
# Distributed under the terms of the MIT license.
#

__version__ = '$Id: http.py 9910 2012-02-19 12:49:35Z drtrigon $'

import urllib2

import config
from pywikibot import *
import wikipedia as pywikibot


# global variables

# import useragent and MyURLopener from global namespace
useragent   = pywikibot.useragent
MyURLopener = pywikibot.MyURLopener

def request(site, uri, retry = None, sysop = False, data = None, compress = True,
            no_hostname = False, cookie_only=False, refer=None, back_response=False):
    """
    Low-level routine to get a URL from any source (may be the wiki).

    Parameters:
      @param site        - The Site to connect to.
      @param uri         - The absolute uri, without the hostname.
      @param retry       - If True, retries loading the page when a network error
                         occurs.
      @param sysop       - If True, the sysop account's cookie will be used.
      @param data        - An optional dict providing extra post request
                         parameters.
      @param cookie_only - Only return the cookie the server sent us back

      @return: Returns the HTML text of the page converted to unicode.
    """

    if retry is None:
        retry = config.retry_on_fail

    headers = {
        'User-agent': useragent,
        #'Accept-Language': config.mylang,
        #'Accept-Charset': config.textfile_encoding,
        #'Keep-Alive': '115',
        #'Connection': 'keep-alive',
        #'Cache-Control': 'max-age=0',
        #'': '',
    }

    if not no_hostname and site.cookies(sysop = sysop):
        headers['Cookie'] = site.cookies(sysop = sysop)
    if compress:
        headers['Accept-encoding'] = 'gzip'

    if refer:
        headers['Refer'] = refer

    if no_hostname: # This allow users to parse also toolserver's script
        url = uri   # and other useful pages without using some other functions.
    else:
        url = '%s://%s%s' % (site.protocol(), site.hostname(), uri)
    data = site.urlEncode(data)

    # Try to retrieve the page until it was successfully loaded (just in
    # case the server is down or overloaded).
    # Wait for retry_idle_time minutes (growing!) between retries.
    retry_idle_time = 1
    retry_attempt = 0
    while True:
        try:
            req = urllib2.Request(url, data, headers)
            f = MyURLopener.open(req)

            # read & info can raise socket.error
            text = f.read()
            headers = f.info()
            break
        except KeyboardInterrupt:
            raise
        except urllib2.HTTPError, e:
            if e.code in [401, 404]:
                raise PageNotFound(
u'Page %s could not be retrieved. Check your family file.'
                                   % url)
            elif e.code in [403]:
                raise PageNotFound(
u'Page %s could not be retrieved. Check your virus wall.'
                                   % url)
            elif e.code == 504:
                pywikibot.output(u'HTTPError: %s %s' % (e.code, e.msg))
                if retry:
                    retry_attempt += 1
                    if retry_attempt > config.maxretries:
                        raise MaxTriesExceededError()
                    pywikibot.output(
u"WARNING: Could not open '%s'.Maybe the server or\n your connection is down. Retrying in %i minutes..."
                           % (url, retry_idle_time))
                    time.sleep(retry_idle_time * 60)
                    # Next time wait longer,
                    # but not longer than half an hour
                    retry_idle_time *= 2
                    if retry_idle_time > 30:
                        retry_idle_time = 30
                    continue
                raise
            else:
                pywikibot.output(u"Result: %s %s" % (e.code, e.msg))
                raise
        except Exception, e:
            pywikibot.output(u'%s' %e)
            if retry:
                retry_attempt += 1
                if retry_attempt > config.maxretries:
                    raise MaxTriesExceededError()
                pywikibot.output(
u"WARNING: Could not open '%s'. Maybe the server or\n your connection is down. Retrying in %i minutes..."
                       % (url, retry_idle_time))
                time.sleep(retry_idle_time * 60)
                retry_idle_time *= 2
                if retry_idle_time > 30:
                    retry_idle_time = 30
                continue

            raise
    # check cookies return or not, if return, send its to update.
    if hasattr(f, 'sheaders'):
        ck = f.sheaders
    else:
        ck = f.info().getallmatchingheaders('set-cookie')
    if not no_hostname and ck:
        Reat=re.compile(': (.*?)=(.*?);')
        tmpc = {}
        for d in ck:
            m = Reat.search(d)
            if m: tmpc[m.group(1)] = m.group(2)
        site.updateCookies(tmpc, sysop)

    if cookie_only:
        return headers.get('set-cookie', '')
    contentType = headers.get('content-type', '')
    contentEncoding = headers.get('content-encoding', '')

    # Ensure that all sent data is received
    # In rare cases we found a douple Content-Length in the header.
    # We need to split it to get a value
    content_length = int(headers.get('content-length', '0').split(',')[0])
    if content_length != len(text) and 'content-length' in headers:
        pywikibot.output(
            u'Warning! len(text) does not match content-length: %s != %s'
            % (len(text), content_length))
        return request(site, uri, retry, sysop, data, compress, no_hostname,
                           cookie_only, back_response)

    if compress and contentEncoding == 'gzip':
        text = pywikibot.decompress_gzip(text)

    R = re.compile('charset=([^\'\";]+)')
    m = R.search(contentType)
    if m:
        charset = m.group(1)
    else:
        if pywikibot.verbose:
            pywikibot.output(u"WARNING: No character set found.")
        # UTF-8 as default
        charset = 'utf-8'
    # Check if this is the charset we expected
    site.checkCharset(charset)
    # Convert HTML to Unicode
    try:
        text = unicode(text, charset, errors = 'strict')
    except UnicodeDecodeError, e:
        print e
        if no_hostname:
            pywikibot.output(u'ERROR: Invalid characters found on %s, replaced by \\ufffd.' % uri)
        else:
            pywikibot.output(u'ERROR: Invalid characters found on %s://%s%s, replaced by \\ufffd.' % (site.protocol(), site.hostname(), uri))
        # We use error='replace' in case of bad encoding.
        text = unicode(text, charset, errors = 'replace')

    if back_response:
        return f, text

    return text

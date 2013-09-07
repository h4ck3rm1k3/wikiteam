# -*- coding: utf-8 -*-
#
# (C) Pywikipedia bot team, 2003-2012
#
# Distributed under the terms of the MIT license.
#
__version__ = '$Id: terminal_interface_unix.py 10046 2012-03-26 08:10:48Z valhallasw $'

import config
import terminal_interface_base

# TODO: other colors:
         #0 = Black
         #1 = Blue
         #2 = Green
         #3 = Aqua
         #4 = Red
         #5 = Purple
         #6 = Yellow
         #7 = White
         #8 = Gray
         #9 = Light Blue
        #10 = Light Green
        #11 = Light Aqua
        #12 = Light Red
        #13 = Light Purple
        #14 = Light Yellow
        #15 = Bright White

unixColors = {
    'default':     chr(27) + '[0m',     # Unix end tag to switch back to default
    'lightblue':   chr(27) + '[94;1m',  # Light Blue start tag
    'lightgreen':  chr(27) + '[92;1m',  # Light Green start tag
    'lightaqua':   chr(27) + '[36;1m',  # Light Aqua start tag
    'lightred':    chr(27) + '[91;1m',  # Light Red start tag
    'lightpurple': chr(27) + '[35;1m',  # Light Purple start tag
    'lightyellow': chr(27) + '[33;1m',  # Light Yellow start tag
}

class UnixUI(terminal_interface_base.UI):
    def printColorized(self, text, targetStream):
        lastColor = None
        for key, value in unixColors.iteritems():
            text = text.replace('\03{%s}' % key, value)
        # just to be sure, reset the color
        text += unixColors['default']

        targetStream.write(text.encode(self.encoding, 'replace'))

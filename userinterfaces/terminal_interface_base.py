# -*- coding: utf-8 -*-
#
# (C) Pywikipedia bot team, 2003-2012
#
# Distributed under the terms of the MIT license.
#
__version__ = '$Id: terminal_interface_base.py 10187 2012-05-05 19:22:03Z valhallasw $'

import config, transliteration
import traceback, re, sys
import wikipedia

transliterator = transliteration.transliterator(config.console_encoding)

colors = [
    'default',
    'black',
    'blue',
    'green',
    'aqua',
    'red',
    'purple',
    'yellow',
    'lightgray',
    'gray',
    'lightblue',
    'lightgreen',
    'lightaqua',
    'lightred',
    'lightpurple',
    'lightyellow',
    'white',
]

colorTagR = re.compile('\03{(?P<name>%s)}' % '|'.join(colors))

class UI:
    def __init__(self):
        self.stdin  = sys.stdin
        self.stdout = sys.stdout
        self.stderr = sys.stderr
        self.encoding = config.console_encoding
        self.transliteration_target = config.transliteration_target

    def printNonColorized(self, text, targetStream):
        # We add *** after the text as a whole if anything needed to be colorized.
        lines = text.split('\n')
        for line in lines:
            line, count = colorTagR.subn('', line)
            if count > 0:
                line += '***'
            line += '\n'
            targetStream.write(line.encode(self.encoding, 'replace'))

    printColorized = printNonColorized
        
    def _print(self, text, targetStream):
        if config.colorized_output:
            self.printColorized(text, targetStream)
        else:
            self.printNonColorized(text, targetStream)    

    def output(self, text, toStdout = False):
        """
        If a character can't be displayed in the encoding used by the user's
        terminal, it will be replaced with a question mark or by a
        transliteration.
        """
        if config.transliterate:
            # Encode our unicode string in the encoding used by the user's console,
            # and decode it back to unicode. Then we can see which characters
            # can't be represented in the console encoding.
            # We need to take min(console_encoding, transliteration_target)
            # the first is what the terminal is capable of
            # the second is how unicode-y the user would like the output
            codecedText = text.encode(self.encoding, 'replace').decode(self.encoding)
            if self.transliteration_target:
                codecedText = codecedText.encode(self.transliteration_target, 'replace').decode(self.transliteration_target)
            transliteratedText = ''
            # Note: A transliteration replacement might be longer than the original
            # character, e.g. ч is transliterated to ch.
            prev = "-"
            for i in xrange(len(codecedText)):
                # work on characters that couldn't be encoded, but not on
                # original question marks.
                if codecedText[i] == '?' and text[i] != u'?':
                    try:
                        transliterated = transliterator.transliterate(text[i], default = '?', prev = prev, next = text[i+1])
                    except IndexError:
                        transliterated = transliterator.transliterate(text[i], default = '?', prev = prev, next = ' ')
                    # transliteration was successful. The replacement
                    # could consist of multiple letters.
                    # mark the transliterated letters in yellow.
                    transliteratedText += '\03{lightyellow}%s\03{default}' % transliterated
                    transLength = len(transliterated)
                    # memorize if we replaced a single letter by multiple letters.
                    if len(transliterated) > 0:
                        prev = transliterated[-1]
                else:
                    # no need to try to transliterate.
                    transliteratedText += codecedText[i]
                    prev = codecedText[i]
            text = transliteratedText

        if toStdout:
            targetStream = self.stdout
        else:
            targetStream = self.stderr
        self._print(text, targetStream)

    def _raw_input(self):
        return raw_input()
        
    def input(self, question, password = False):
        """
        Works like raw_input(), but returns a unicode string instead of ASCII.

        Unlike raw_input, this function automatically adds a space after the
        question.
        """

        # sound the terminal bell to notify the user
        if config.ring_bell:
            sys.stdout.write('\07')
        # TODO: make sure this is logged as well
        self.output(question + ' ')
        if password:
            import getpass
            text = getpass.getpass('')
        else:
            text = self._raw_input()
        text = unicode(text, self.encoding)
        return text

    def inputChoice(self, question, options, hotkeys, default = None):
        options = options[:] # we don't want to edit the passed parameter
        for i in range(len(options)):
            option = options[i]
            hotkey = hotkeys[i]
            # try to mark a part of the option name as the hotkey
            m = re.search('[%s%s]' % (hotkey.lower(), hotkey.upper()), option)
            if hotkey == default:
                caseHotkey = hotkey.upper()
            else:
                caseHotkey = hotkey
            if m:
                pos = m.start()
                options[i] = '%s[%s]%s' % (option[:pos], caseHotkey, option[pos+1:])
            else:
                options[i] = '%s [%s]' % (option, caseHotkey)
        # loop until the user entered a valid choice
        while True:
            prompt = '%s (%s)' % (question, ', '.join(options))
            answer = self.input(prompt)
            if answer.lower() in hotkeys or answer.upper() in hotkeys:
                return answer
            elif default and answer=='':        # empty string entered
                return default

    def editText(self, text, jumpIndex = None, highlight = None):
        """
        Uses a Tkinter edit box because we don't have a console editor

        Parameters:
            * text      - a Unicode string
            * jumpIndex - an integer: position at which to put the caret
            * highlight - a substring; each occurence will be highlighted
        """
        try:
            import gui
        except ImportError, e:
            print 'Could not load GUI modules: %s' % e
            return text
        editor = gui.EditBoxWindow()
        return editor.edit(text, jumpIndex = jumpIndex, highlight = highlight)

    def askForCaptcha(self, url):
        try:
            import webbrowser
            wikipedia.output(u'Opening CAPTCHA in your web browser...')
            if webbrowser.open(url):
                return wikipedia.input(u'What is the solution of the CAPTCHA that is shown in your web browser?')
            else:
                raise
        except:
            wikipedia.output(u'Error in opening web browser: %s' % sys.exc_info()[0])
            wikipedia.output(u'Please copy this url to your web browser and open it:\n %s' % url)
            return wikipedia.input(u'What is the solution of the CAPTCHA at this url ?')

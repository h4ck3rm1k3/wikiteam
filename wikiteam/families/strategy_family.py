# -*- coding: utf-8  -*-

__version__ = '$Id: strategy_family.py 10214 2012-05-15 14:16:54Z shizhao $'

import family, config

# The Wikimedia Strategy family

class Family(family.Family):
    def __init__(self):
        family.Family.__init__(self)
        self.name = 'strategy'
        self.langs = {
            'strategy': 'strategy.wikimedia.org',
        }

        self.namespaces[4] = {
            '_default': [u'Strategic Planning', 'Project'],
        }
        self.namespaces[5] = {
            '_default': [u'Strategic Planning talk', 'Project talk'],
        }
        self.namespaces[106] = {
            '_default': [u'Proposal'],
        }
        self.namespaces[107] = {
            '_default': [u'Proposal talk'],
        }

        self.interwiki_forward = 'wikipedia'

    def dbName(self, code):
        return 'strategywiki_p'

    def shared_image_repository(self, code):
        return ('commons', 'commons')

    if config.SSL_connection:

        def protocol(self, code):
            return 'https'
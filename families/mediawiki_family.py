# -*- coding: utf-8  -*-

__version__ = '$Id: mediawiki_family.py 10214 2012-05-15 14:16:54Z shizhao $'

import family

# The MediaWiki family
# user-config.py: usernames['mediawiki']['mediawiki'] = 'User name'

class Family(family.Family):
    def __init__(self):
        family.Family.__init__(self)
        self.name = 'mediawiki'

        self.langs = {
            'mediawiki': 'www.mediawiki.org',
        }

        self.namespaces[4] = {
            '_default': [u'Project', self.namespaces[4]['_default']],
        }
        self.namespaces[5] = {
            '_default': [u'Project talk', self.namespaces[5]['_default']],
        }
        self.namespaces[90] = {
            '_default': u'Thread',
        }
        self.namespaces[91] = {
            '_default': u'Thread talk',
        }
        self.namespaces[92] = {
            '_default': u'Summary',
        }
        self.namespaces[93] = {
            '_default': u'Summary talk',
        }
        self.namespaces[100] = {
            '_default': u'Manual',
        }
        self.namespaces[101] = {
            '_default': u'Manual talk',
        }
        self.namespaces[102] = {
            '_default': u'Extension',
        }
        self.namespaces[103] = {
            '_default': u'Extension talk',
        }
        self.namespaces[104] = {
            '_default': u'API',
        }
        self.namespaces[105] = {
            '_default': u'API talk',
        }
        self.namespaces[1198] = {
            '_default': u'Translations',
        }
        self.namespaces[1199] = {
            '_default': u'Translations talk',
        }
        self.cross_projects = [
            'wikipedia', 'wiktionary', 'wikibooks', 'wikiquote', 'wikisource',
            'wikinews', 'wikiversity', 'meta', 'test', 'incubator', 'commons',
            'species',
        ]

    def shared_image_repository(self, code):
        return ('commons', 'commons')

    if family.config.SSL_connection:

        def protocol(self, code):
            return 'https'
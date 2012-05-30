# -*- coding: utf-8  -*-
import family

__version__ = '$Id: wikiversity_family.py 10214 2012-05-15 14:16:54Z shizhao $'

# The Wikimedia family that is known as Wikiversity

class Family(family.Family):
    def __init__(self):
        family.Family.__init__(self)
        self.name = 'wikiversity'

        self.languages_by_size = [
            'en', 'fr', 'de', 'beta', 'ru', 'cs', 'it', 'es', 'pt', 'ar', 'el',
            'fi', 'sv', 'sl', 'ja',
        ]

        self.langs = dict([(lang, '%s.wikiversity.org' % lang) for lang in self.languages_by_size])

        # Override defaults
        self.namespaces[3]['cs'] = [u'Diskuse s uživatelem', u'Uživatel diskuse', u'Uživatelka diskuse', u'Diskuse s uživatelkou']
        self.namespaces[2]['cs'] = [u'Uživatel', u'Uživatelka']
        self.namespaces[3]['fr'] = [u'Discussion utilisateur', u'Discussion Utilisateur']
        self.namespaces[2]['fr'] = [u'Utilisateur']
        self.namespaces[3]['de'] = [u'Benutzer Diskussion', u'Benutzerin Diskussion']
        self.namespaces[13]['de'] = [u'Hilfe Diskussion']
        self.namespaces[12]['de'] = [u'Hilfe']
        self.namespaces[3]['pt'] = [u'Utilizador Discussão', u'Usuário Discussão', u'Utilizadora Discussão']
        self.namespaces[2]['pt'] = [u'Utilizador', u'Usuário', u'Utilizadora']

        # Most namespaces are inherited from family.Family.
        # Translation used on all wikis for the different namespaces.
        # (Please sort languages alphabetically)
        # You only need to enter translations that differ from _default.
        self.namespaces[4] = {
            '_default': self.namespaces[4]['_default'],
            'ar': [u'ويكي الجامعة', u'وج'],
            'beta': u'Wikiversity',
            'cs': [u'Wikiverzita', u'WV', u'Wikiversity'],
            'de': u'Wikiversity',
            'el': [u'Βικιεπιστήμιο', u'Wikiversity'],
            'en': [u'Wikiversity', u'WV'],
            'es': [u'Wikiversidad', u'Wikiversity'],
            'fi': [u'Wikiopisto', u'Wikiversity'],
            'fr': [u'Wikiversité', u'Wikiversity'],
            'it': [u'Wikiversità', u'Wikiversity'],
            'ja': u'Wikiversity',
            'pt': [u'Wikiversidade', u'Wikiversity'],
            'ru': [u'Викиверситет', u'Wikiversity'],
            'sl': [u'Wikiverza', u'Wikiversity'],
            'sv': u'Wikiversity',
        }
        self.namespaces[5] = {
            '_default': self.namespaces[5]['_default'],
            'ar': u'نقاش ويكي الجامعة',
            'beta': u'Wikiversity talk',
            'cs': [u'Diskuse k Wikiverzitě', u'Wikiversity diskuse', u'Wikiversity talk', u'Wikiverzita diskuse'],
            'de': u'Wikiversity Diskussion',
            'el': u'Συζήτηση Βικιεπιστημίου',
            'en': u'Wikiversity talk',
            'es': u'Wikiversidad discusión',
            'fi': u'Keskustelu Wikiopistosta',
            'fr': u'Discussion Wikiversité',
            'it': u'Discussioni Wikiversità',
            'ja': [u'Wikiversity・トーク', u'Wikiversity talk', u'Wikiversity‐ノート'],
            'pt': u'Wikiversidade Discussão',
            'ru': u'Обсуждение Викиверситета',
            'sl': u'Pogovor o Wikiverzi',
            'sv': u'Wikiversitydiskussion',
        }

        self.namespaces[100] = {
            'ar': u'مدرسة',
            'cs': u'Fórum',
            'el': u'Σχολή',
            'en': u'School',
            'it': u'Facoltà',
            'ja': u'School',
            'sv': u'Portal',
        }
        self.namespaces[101] = {
            'ar': u'نقاش المدرسة',
            'cs': u'Diskuse k fóru',
            'el': u'Συζήτηση Σχολής',
            'en': u'School talk',
            'it': u'Discussioni facoltà',
            'ja': u'School‐ノート',
            'sv': u'Portaldiskussion',
        }
        self.namespaces[102] = {
            'ar': u'بوابة',
            'el': u'Τμήμα',
            'en': u'Portal',
            'fr': u'Projet',
            'it': u'Corso',
            'ja': u'Portal',
        }
        self.namespaces[103] = {
            'ar': u'نقاش البوابة',
            'el': u'Συζήτηση Τμήματος',
            'en': u'Portal talk',
            'fr': u'Discussion Projet',
            'it': u'Discussioni corso',
            'ja': u'Portal‐ノート',
        }
        self.namespaces[104] = {
            'ar': u'موضوع',
            'en': u'Topic',
            'fr': u'Recherche',
            'it': u'Materia',
            'ja': u'Topic',
        }
        self.namespaces[105] = {
            'ar': u'نقاش الموضوع',
            'en': u'Topic talk',
            'fr': u'Discussion Recherche',
            'it': u'Discussioni materia',
            'ja': u'Topic‐ノート',
        }
        self.namespaces[106] = {
            'ar': u'مجموعة',
            'de': u'Kurs',
            'en': u'Collection',
            'fr': u'Faculté',
            'it': u'Dipartimento',
        }
        self.namespaces[107] = {
            'ar': u'نقاش المجموعة',
            'de': u'Kurs Diskussion',
            'en': u'Collection talk',
            'fr': u'Discussion Faculté',
            'it': u'Discussioni dipartimento',
        }
        self.namespaces[108] = {
            'de': u'Projekt',
            'fr': u'Département',
        }
        self.namespaces[109] = {
            'de': u'Projekt Diskussion',
            'fr': u'Discussion Département',
        }
        self.namespaces[110] = {
            'fr': u'Transwiki',
            'ja': u'Transwiki',
        }
        self.namespaces[111] = {
            'fr': u'Discussion Transwiki',
            'ja': u'Transwiki‐ノート',
        }

        # CentralAuth cross avaliable projects.
        self.cross_projects = [
            'wiktionary', 'wikibooks', 'wikiquote', 'wikisource', 'wikinews',
            'wikiversity', 'meta', 'mediawiki', 'test', 'incubator', 'commons',
            'species',
        ]

        # Global bot allowed languages on http://meta.wikimedia.org/wiki/Bot_policy/Implementation#Current_implementation
        self.cross_allowed = ['ja',]

    def shared_image_repository(self, code):
        return ('commons', 'commons')

    if family.config.SSL_connection:

        def protocol(self, code):
            return 'https'
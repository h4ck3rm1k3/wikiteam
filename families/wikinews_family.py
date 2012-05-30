# -*- coding: utf-8  -*-
import family

__version__ = '$Id: wikinews_family.py 10214 2012-05-15 14:16:54Z shizhao $'

# The Wikimedia family that is known as Wikinews

class Family(family.Family):
    def __init__(self):
        family.Family.__init__(self)
        self.name = 'wikinews'

        self.languages_by_size = [
            'sr', 'en', 'pl', 'fr', 'de', 'it', 'es', 'pt', 'zh', 'ru', 'ja',
            'sv', 'ta', 'ca', 'el', 'cs', 'fa', 'ar', 'fi', 'ro', 'he', 'bg',
            'tr', 'sd', 'sq', 'uk', 'no', 'bs', 'eo', 'ko',
        ]

        self.langs = dict([(lang, '%s.wikinews.org' % lang) for lang in self.languages_by_size])

        # Override defaults
        self.namespaces[14]['en'] = [u'Category', u'CAT']
        self.namespaces[10]['zh'] = [u'Template', u'模板', u'样板', u'樣板']
        self.namespaces[12]['zh'] = [u'Help', u'帮助', u'幫助']
        self.namespaces[14]['zh'] = [u'Category', u'分类', u'分類']
        self.namespaces[3]['ca'] = [u'Usuari Discussió']
        self.namespaces[2]['ca'] = [u'Usuari']
        self.namespaces[3]['cs'] = [u'Diskuse s redaktorem', u'Diskuse s redaktorkou', u'Diskuse s uživatelem', u'Redaktor diskuse', u'Redaktorka diskuse', u'Uživatel diskuse', u'Uživatelka diskuse', u'Diskuse s uživatelkou']
        self.namespaces[2]['cs'] = [u'Redaktor', u'Redaktorka', u'Uživatel', u'Uživatelka']
        self.namespaces[3]['pt'] = [u'Utilizador Discussão', u'Usuário Discussão', u'Utilizadora Discussão']
        self.namespaces[2]['pt'] = [u'Utilizador', u'Usuário', u'Utilizadora']
        self.namespaces[3]['pl'] = [u'Dyskusja wikireportera', u'Dyskusja wikireporterki']
        self.namespaces[2]['pl'] = [u'Wikireporter', u'Wikireporterka']
        self.namespaces[3]['fr'] = [u'Discussion utilisateur', u'Discussion Utilisateur']
        self.namespaces[2]['fr'] = [u'Utilisateur']
        self.namespaces[3]['de'] = [u'Benutzer Diskussion', u'Benutzerin Diskussion']
        self.namespaces[13]['de'] = [u'Hilfe Diskussion']
        self.namespaces[12]['de'] = [u'Hilfe']

        # Most namespaces are inherited from family.Family.
        # Translation used on all wikis for the different namespaces.
        # (Please sort languages alphabetically)
        # You only need to enter translations that differ from _default.
        self.namespaces[4] = {
            '_default': self.namespaces[4]['_default'],
            'ar': [u'ويكي الأخبار', u'Wikinews'],
            'bg': [u'Уикиновини', u'Wikinews'],
            'bs': [u'Wikivijesti', u'Wikinews'],
            'ca': [u'Viquinotícies', u'Wikinews'],
            'cs': [u'Wikizprávy', u'WN', u'WZ', u'Wikinews'],
            'de': u'Wikinews',
            'el': [u'Βικινέα', u'Wikinews'],
            'en': [u'Wikinews', u'WN'],
            'eo': [u'Vikinovaĵoj', u'Wikinews'],
            'es': [u'Wikinoticias', u'Wikinews'],
            'fa': [u'ویکی‌خبر', u'وخ'],
            'fi': [u'Wikiuutiset', u'Wikinews'],
            'fr': [u'Wikinews', u'WN'],
            'he': [u'ויקיחדשות', u'Wikinews'],
            'hu': u'Wikihírek',
            'it': [u'Wikinotizie', u'Wikinews'],
            'ja': u'ウィキニュース',
            'ko': [u'위키뉴스', u'뉴'],
            'no': [u'Wikinytt', u'Wikinews'],
            'pl': u'Wikinews',
            'pt': [u'Wikinotícias', u'Wikinews'],
            'ro': [u'Wikiștiri', u'Wikiştiri', u'Wikinews'],
            'ru': [u'Викиновости', u'ВикиНовости', u'ВН'],
            'sd': u'Wikinews',
            'sq': [u'Wikilajme', u'WL'],
            'sr': [u'Викивести', u'Wikinews'],
            'sv': [u'Wikinews', u'WN'],
            'ta': [u'விக்கிசெய்தி', u'Wikinews', u'விக்கிபீடியா'],
            'th': u'วิกิข่าว',
            'tr': [u'Vikihaber', u'Wikinews'],
            'uk': [u'ВікіНовини', u'Wikinews'],
            'zh': u'Wikinews',
        }
        self.namespaces[5] = {
            '_default': self.namespaces[5]['_default'],
            'ar': u'نقاش ويكي الأخبار',
            'bg': u'Уикиновини беседа',
            'bs': u'Razgovor s Wikivijestima',
            'ca': u'Viquinotícies Discussió',
            'cs': [u'Diskuse k Wikizprávám', u'Wikinews diskuse', u'Wikinews talk', u'Wikizprávy diskuse'],
            'de': u'Wikinews Diskussion',
            'el': u'Βικινέα συζήτηση',
            'en': u'Wikinews talk',
            'eo': u'Vikinovaĵoj diskuto',
            'es': u'Wikinoticias discusión',
            'fa': u'بحث ویکی‌خبر',
            'fi': u'Keskustelu Wikiuutisista',
            'fr': u'Discussion Wikinews',
            'he': u'שיחת ויקיחדשות',
            'hu': u'Wikihírek-vita',
            'it': u'Discussioni Wikinotizie',
            'ja': [u'ウィキニュース・トーク', u'ウィキニュース‐ノート'],
            'ko': [u'위키뉴스토론', u'뉴토'],
            'nl': u'Overleg Wikinews',
            'no': u'Wikinytt-diskusjon',
            'pl': u'Dyskusja Wikinews',
            'pt': u'Wikinotícias Discussão',
            'ro': [u'Discuție Wikiștiri', u'Discuţie Wikiştiri', u'Discuţie Wikiștiri'],
            'ru': [u'Обсуждение Викиновостей', u'Обсуждение ВикиНовостей'],
            'sd': u'Wikinews بحث',
            'sq': u'Wikilajme diskutim',
            'sr': [u'Разговор о Викивестима', u'Razgovor o Викивести'],
            'sv': u'Wikinewsdiskussion',
            'ta': [u'விக்கிசெய்தி பேச்சு', u'விக்கிபீடியா பேச்சு'],
            'th': u'คุยเรื่องวิกิข่าว',
            'tr': u'Vikihaber tartışma',
            'uk': u'Обговорення ВікіНовини',
            'zh': u'Wikinews talk',
        }

        self.namespaces[90] = {
            'en': u'Thread',
        }

        self.namespaces[91] = {
            'en': u'Thread talk',
        }

        self.namespaces[92] = {
            'en': u'Summary',
        }

        self.namespaces[93] = {
            'en': u'Summary talk',
        }

        self.namespaces[100] = {
            'ar': u'بوابة',
            'ca': u'Transwiki',
            'cs': u'Portál',
            'de': u'Portal',
            'en': u'Portal',
            'es': u'Comentarios',
            'fa': u'درگاه',
            'he': u'פורטל',
            'it': u'Portale',
            'ja': u'ポータル',
            'no': u'Kommentarer',
            'pl': u'Portal',
            'pt': u'Portal',
            'ru': u'Портал',
            'sq': u'Portal',
            'sv': u'Portal',
            'ta': u'வலைவாசல்',
            'tr': u'Portal',
            'zh': u'频道',
        }

        self.namespaces[101] = {
            'ar': u'نقاش البوابة',
            'ca': u'Transwiki talk',
            'cs': u'Diskuse k portálu',
            'de': u'Portal Diskussion',
            'en': u'Portal talk',
            'es': u'Comentarios Discusión',
            'fa': u'بحث درگاه',
            'he': u'שיחת פורטל',
            'it': u'Discussioni portale',
            'ja': [u'ポータル・トーク', u'ポータル‐ノート'],
            'no': u'Kommentarer-diskusjon',
            'pl': u'Dyskusja portalu',
            'pt': u'Portal Discussão',
            'ru': u'Обсуждение портала',
            'sq': u'Portal diskutim',
            'sv': u'Portaldiskussion',
            'ta': u'வலைவாசல் பேச்சு',
            'tr': u'Portal tartışma',
            'zh': u'频道 talk',
        }

        self.namespaces[102] = {
            'ar': u'تعليقات',
            'bg': u'Мнения',
            'ca': u'Secció',
            'de': u'Meinungen',
            'el': u'Σχόλια',
            'en': u'Comments',
            'fa': u'نظرها',
            'fr': u'Transwiki',
            'hu': u'Portál',
            'pt': u'Efeméride',
            'ru': u'Комментарии',
            'sq': u'Komentet',
            'sr': u'Коментар',
        }

        self.namespaces[103] = {
            'ar': u'نقاش التعليقات',
            'bg': u'Мнения беседа',
            'ca': u'Secció Discussió',
            'de': u'Meinungen Diskussion',
            'el': u'Συζήτηση σχολίων',
            'en': u'Comments talk',
            'fa': u'بحث نظرها',
            'fr': u'Discussion Transwiki',
            'hu': u'Portálvita',
            'pt': u'Efeméride Discussão',
            'ru': u'Обсуждение комментариев',
            'sq': u'Komentet diskutim',
            'sr': u'Разговор о коментару',
        }

        self.namespaces[104] = {
            'fr': u'Page',
            'pt': u'Transwiki',
        }

        self.namespaces[105] = {
            'fr': u'Discussion Page',
            'pt': u'Transwiki Discussão',
        }

        self.namespaces[106] = {
            'fr': u'Dossier',
            'no': u'Portal',
            'tr': u'Yorum',
        }

        self.namespaces[107] = {
            'fr': u'Discussion Dossier',
            'no': u'Portal-diskusjon',
            'tr': u'Yorum tartışma',
        }

        self.namespaces[108] = {
            'ja': u'短信',
        }

        self.namespaces[109] = {
            'ja': u'短信‐ノート',
        }

        # CentralAuth cross avaliable projects.
        self.cross_projects = [
            'wiktionary', 'wikibooks', 'wikiquote', 'wikisource', 'wikinews',
            'wikiversity', 'meta', 'mediawiki', 'test', 'incubator', 'commons',
            'species',
        ]

        # Global bot allowed languages on http://meta.wikimedia.org/wiki/Bot_policy/Implementation#Current_implementation
        self.cross_allowed = ['ca', 'cs', 'en', 'fa',]

        # Which languages have a special order for putting interlanguage links,
        # and what order is it? If a language is not in interwiki_putfirst,
        # alphabetical order on language code is used. For languages that are in
        # interwiki_putfirst, interwiki_putfirst is checked first, and
        # languages are put in the order given there. All other languages are
        # put after those, in code-alphabetical order.
        self.interwiki_putfirst = {
            'en': self.alphabetic,
            'fi': self.alphabetic,
            'fr': self.alphabetic,
            'he': ['en'],
            'hu': ['en'],
            'pl': self.alphabetic,
        }

        self.obsolete = {
            'hu': None, # https://bugzilla.wikimedia.org/show_bug.cgi?id=28342
            'jp': 'ja',
            'nb': 'no',
            'nl': None, # https://bugzilla.wikimedia.org/show_bug.cgi?id=20325
            'th': None, # https://bugzilla.wikimedia.org/show_bug.cgi?id=28341
            'zh-tw': 'zh',
            'zh-cn': 'zh'
        }

    def code2encoding(self, code):
        return 'utf-8'

    def shared_image_repository(self, code):
        return ('commons', 'commons')

    if family.config.SSL_connection:

        def protocol(self, code):
            return 'https'
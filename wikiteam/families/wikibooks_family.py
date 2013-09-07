# -*- coding: utf-8  -*-
import family

__version__ = '$Id: wikibooks_family.py 10253 2012-05-26 12:46:40Z xqt $'

# The Wikimedia family that is known as Wikibooks

class Family(family.Family):
    def __init__(self):
        family.Family.__init__(self)
        self.name = 'wikibooks'

        self.languages_by_size = [
            'en', 'de', 'fr', 'hu', 'ja', 'pt', 'nl', 'pl', 'it', 'es', 'he',
            'sq', 'fi', 'ca', 'id', 'ru', 'vi', 'cs', 'zh', 'hr', 'sv', 'tr',
            'da', 'th', 'gl', 'ta', 'fa', 'no', 'ko', 'sr', 'ar', 'tl', 'mk',
            'is', 'tt', 'lt', 'ka', 'az', 'eo', 'ro', 'bg', 'uk', 'hy', 'sl',
            'sk', 'el', 'si', 'li', 'la', 'ang', 'ia', 'cv', 'et', 'ur', 'mr',
            'bn', 'ms', 'hi', 'oc', 'ml', 'kk', 'eu', 'fy', 'ie', 'ne', 'te',
            'af', 'tg', 'sa', 'pa', 'bs', 'ky', 'mg', 'cy', 'be', 'zh-min-nan',
            'ast', 'ku', 'tk', 'uz', 'su', 'vo', 'mn', 'my',
        ]

        self.langs = dict([(lang, '%s.wikibooks.org' % lang) for lang in self.languages_by_size])

        # Override defaults
        self.namespaces[3]['fr'] = [u'Discussion utilisateur', u'Discussion Utilisateur']
        self.namespaces[2]['fr'] = [u'Utilisateur']
        self.namespaces[14]['en'] = [u'Category', u'CAT']
        self.namespaces[10]['zh'] = [u'Template', u'模板', u'样板', u'樣板']
        self.namespaces[12]['zh'] = [u'Help', u'帮助', u'幫助']
        self.namespaces[14]['zh'] = [u'Category', u'分类', u'分類']
        self.namespaces[3]['pt'] = [u'Utilizador Discussão', u'Usuário Discussão', u'Utilizadora Discussão']
        self.namespaces[2]['pt'] = [u'Utilizador', u'Usuário', u'Utilizadora']
        self.namespaces[3]['ca'] = [u'Usuari Discussió']
        self.namespaces[2]['ca'] = [u'Usuari']
        self.namespaces[13]['de'] = [u'Hilfe Diskussion']
        self.namespaces[12]['de'] = [u'Hilfe']
        self.namespaces[3]['de'] = [u'Benutzer Diskussion', u'Benutzerin Diskussion']
        self.namespaces[14]['tr'] = [u'Kategori', u'KAT']
        self.namespaces[13]['da'] = [u'Hjælp diskussion', u'Hjælp-diskussion']
        self.namespaces[9]['da'] = [u'MediaWiki diskussion', u'MediaWiki-diskussion']
        self.namespaces[11]['hi'] = [u'साँचा वार्ता']
        self.namespaces[10]['hi'] = [u'साँचा']
        self.namespaces[15]['hi'] = [u'श्रेणी वार्ता']
        self.namespaces[14]['hi'] = [u'श्रेणी']
        self.namespaces[3]['hi'] = [u'सदस्य वार्ता']
        self.namespaces[2]['hi'] = [u'सदस्य']
        self.namespaces[9]['hi'] = [u'मीडियाविकि वार्ता']
        self.namespaces[8]['hi'] = [u'मीडियाविकि']
        self.namespaces[3]['cs'] = [u'Diskuse s uživatelem', u'Uživatel diskuse', u'Uživatelka diskuse', u'Diskuse s uživatelkou']
        self.namespaces[2]['cs'] = [u'Uživatel', u'Uživatelka']
        self.namespaces[12]['nl'] = [u'Help']
        self.namespaces[9]['ro'] = [u'Discuție MediaWiki', u'Discuţie MediaWiki']
        self.namespaces[15]['bn'] = [u'বিষয়শ্রেণী আলোচনা']
        self.namespaces[14]['bn'] = [u'বিষয়শ্রেণী']
        self.namespaces[3]['pl'] = [u'Dyskusja wikipedysty', u'Dyskusja wikipedystki', u'Dyskusja użytkownika', u'Dyskusja użytkowniczki']
        self.namespaces[2]['pl'] = [u'Wikipedysta', u'Wikipedystka', u'Użytkownik', u'Użytkowniczka']

        # Most namespaces are inherited from family.Family.
        # Translation used on all wikis for the different namespaces.
        # (Please sort languages alphabetically)
        # You only need to enter translations that differ from _default.
        self.namespaces[4] = {
            '_default': self.namespaces[4]['_default'],
            'af': u'Wikibooks',
            'ang': u'Wikibooks',
            'ar': [u'ويكي الكتب', u'Wikibooks'],
            'ast': u'Wikibooks',
            'az': u'Wikibooks',
            'be': u'Wikibooks',
            'bg': [u'Уикикниги', u'Wikibooks'],
            'bn': [u'উইকিবই', u'WB', u'Wikibooks'],
            'bs': [u'Wikiknjige', u'Wikibooks'],
            'ca': [u'Viquillibres', u'Wikibooks'],
            'cs': [u'Wikiknihy', u'WB', u'WK', u'Wikibooks'],
            'cv': u'Wikibooks',
            'cy': [u'Wicilyfrau', u'Wikibooks'],
            'da': u'Wikibooks',
            'de': u'Wikibooks',
            'el': [u'Βικιβιβλία', u'Wikibooks'],
            'en': [u'Wikibooks', u'WB'],
            'eo': [u'Vikilibroj', u'Wikibooks'],
            'es': [u'Wikilibros', u'Wikibooks'],
            'et': [u'Vikiõpikud', u'Wikibooks'],
            'eu': u'Wikibooks',
            'fa': [u'ویکی‌نسک', u'Wikibooks'],
            'fi': [u'Wikikirjasto', u'Wikibooks'],
            'fr': [u'Wikilivres', u'WL'],
            'fy': u'Wikibooks',
            'ga': u'Vicíleabhair',
            'gl': u'Wikibooks',
            'he': [u'ויקיספר', u'Wikibooks'],
            'hi': u'Wikibooks',
            'hr': [u'Wikiknjige', u'Wikibooks'],
            'hu': [u'Wikikönyvek', u'Wikibooks'],
            'hy': [u'Վիքիգրքեր', u'Wikibooks'],
            'ia': u'Wikibooks',
            'id': [u'Wikibuku', u'Wikibooks'],
            'ie': u'Wikibooks',
            'is': [u'Wikibækur', u'Wikibooks'],
            'it': [u'Wikibooks', u'WB'],
            'ja': u'Wikibooks',
            'ka': [u'ვიკიწიგნები', u'Wikibooks'],
            'kk': [u'Уикикітап', u'Wikibooks'],
            'ko': [u'위키책', u'Wikibooks'],
            'ku': u'Wikibooks',
            'ky': u'Wikibooks',
            'la': [u'Vicilibri', u'Wikibooks'],
            'li': [u'Wikibeuk', u'Wikibooks'],
            'lt': u'Wikibooks',
            'mg': u'Wikibooks',
            'mk': u'Wikibooks',
            'ml': [u'വിക്കിപാഠശാല', u'വിക്കി‌‌ പുസ്തകശാല', u'Wikibooks'],
            'mn': u'Wikibooks',
            'mr': u'Wikibooks',
            'ms': u'Wikibooks',
            'my': u'Wikibooks',
            'ne': u'Wikibooks',
            'nl': u'Wikibooks',
            'no': [u'Wikibøker', u'Wikibooks'],
            'oc': [u'Wikilibres', u'Wikibooks'],
            'pa': u'Wikibooks',
            'pl': [u'Wikibooks', u'WB'],
            'ps': u'ويکيتابونه',
            'pt': [u'Wikilivros', u'Wikibooks'],
            'ro': [u'Wikimanuale', u'Wikibooks'],
            'ru': [u'Викиучебник', u'ВУ'],
            'sa': u'Wikibooks',
            'si': [u'විකිපොත්', u'Wikibooks'],
            'sk': u'Wikibooks',
            'sl': [u'Wikiknjige', u'Wikibooks'],
            'sq': u'Wikibooks',
            'sr': [u'Викикњиге', u'Wikibooks'],
            'su': u'Wikibooks',
            'sv': u'Wikibooks',
            'ta': [u'விக்கிநூல்கள்', u'Wikibooks', u'விக்கிபீடியா'],
            'te': u'Wikibooks',
            'tg': u'Wikibooks',
            'th': u'Wikibooks',
            'tk': u'Wikibooks',
            'tl': u'Wikibooks',
            'tr': [u'Vikikitap', u'VK'],
            'tt': u'Wikibooks',
            'uk': [u'Вікіпідручник', u'ВП'],
            'ur': [u'وکی کتب', u'Wikibooks'],
            'uz': [u'Vikikitob', u'Wikibooks'],
            'vi': u'Wikibooks',
            'vo': [u'Vükibuks', u'Wikibooks'],
            'zh': [u'Wikibooks', u'维基教科书', u'維基教科書', u'WB'],
            'zh-min-nan': u'Wikibooks',
        }

        self.namespaces[5] = {
            '_default': self.namespaces[5]['_default'],
            'af': u'Wikibooksbespreking',
            'als': u'Wikibooks Diskussion',
            'ang': u'Wikibooks talk',
            'ar': u'نقاش ويكي الكتب',
            'ast': [u'Wikibooks alderique', u'Wikibooks discusión'],
            'ay': u'Wikibooks Discusión',
            'az': u'Wikibooks müzakirəsi',
            'ba': u'Wikibooks б-са фекер алышыу',
            'be': u'Wikibooks размовы',
            'bg': u'Уикикниги беседа',
            'bm': u'Discussion Wikibooks',
            'bn': [u'উইকিবই আলোচনা', u'উইকিবই আলাপ'],
            'bs': u'Razgovor s Wikiknjigama',
            'ca': u'Viquillibres Discussió',
            'cs': [u'Diskuse k Wikiknihám', u'Wikibooks diskuse', u'Wikibooks talk', u'Wikiknihy diskuse'],
            'cv': u'Wikibooks сӳтсе явмалли',
            'cy': u'Sgwrs Wicilyfrau',
            'da': [u'Wikibooks diskussion', u'Wikibooks-diskussion'],
            'de': u'Wikibooks Diskussion',
            'el': u'Βικιβιβλία συζήτηση',
            'en': u'Wikibooks talk',
            'eo': [u'Vikilibroj-Diskuto', u'Vikilibroj diskuto'],
            'es': u'Wikilibros discusión',
            'et': [u'Vikiõpikute arutelu', u'Vikiõpikud arutelu'],
            'eu': u'Wikibooks eztabaida',
            'fa': u'بحث ویکی‌نسک',
            'fi': u'Keskustelu Wikikirjastosta',
            'fr': u'Discussion Wikilivres',
            'fy': u'Wikibooks oerlis',
            'ga': u'Plé Vicíleabhar',
            'gl': u'Conversa Wikibooks',
            'gn': u'Wikibooks myangekõi',
            'he': u'שיחת ויקיספר',
            'hi': u'Wikibooks वार्ता',
            'hr': u'Razgovor Wikiknjige',
            'hu': [u'Wikikönyvek-vita', u'Wikikönyvek vita'],
            'hy': u'Վիքիգրքերի քննարկում',
            'ia': u'Discussion Wikibooks',
            'id': [u'Pembicaraan Wikibuku', u'Pembicaraan Wikibooks'],
            'ie': u'Wikibooks Discussion',
            'is': u'Wikibækurspjall',
            'it': u'Discussioni Wikibooks',
            'ja': [u'Wikibooks・トーク', u'Wikibooks‐ノート'],
            'ka': u'ვიკიწიგნები განხილვა',
            'kk': [u'Уикикітап талқылауы', u'Уикикітап talqılawı', u'Уикикітап تالقىلاۋى'],
            'km': u'ការពិភាក្សាអំពីWikibooks',
            'kn': u'Wikibooks ಚರ್ಚೆ',
            'ko': u'위키책토론',
            'ku': u'Wikibooks nîqaş',
            'ky': u'Wikibooks talk',
            'la': u'Disputatio Vicilibrorum',
            'lb': u'Wikibooks Diskussioun',
            'li': u'Euverlèk Wikibeuk',
            'ln': u'Discussion Wikibooks',
            'lt': u'Wikibooks aptarimas',
            'lv': u'Wikibooks diskusija',
            'mg': [u'Dinika amin\'ny Wikibooks', u'Discussion Wikibooks'],
            'mk': u'Разговор за Wikibooks',
            'ml': [u'വിക്കിപാഠശാല സംവാദം', u'വിക്കി‌‌ പുസ്തകശാല സംവാദം', u'Wikibooks talk'],
            'mn': u'Wikibooks-н хэлэлцүүлэг',
            'mr': u'Wikibooks चर्चा',
            'ms': [u'Perbincangan Wikibooks', u'Perbualan Wikibooks'],
            'my': u'Wikibooks talk',
            'nah': u'Wikibooks Discusión',
            'nds': u'Wikibooks Diskuschoon',
            'ne': u'Wikibooks वार्ता',
            'nl': u'Overleg Wikibooks',
            'no': u'Wikibøker-diskusjon',
            'oc': u'Discussion Wikilibres',
            'pa': u'Wikibooks ਚਰਚਾ',
            'pl': u'Dyskusja Wikibooks',
            'ps': u'د ويکيتابونه خبرې اترې',
            'pt': [u'Wikilivros Discussão', u'Wikibooks Talk', u'Wikibooks Discussão'],
            'qu': u'Wikibooks rimanakuy',
            'ro': [u'Discuție Wikimanuale', u'Discuţie Wikibooks', u'Discuţie Wikimanuale'],
            'ru': u'Обсуждение Викиучебника',
            'sa': [u'Wikibooksसम्भाषणम्', u'Wikibooksसंभाषणं'],
            'si': [u'විකිපොත් සාකච්ඡාව', u'Wikibooks talk'],
            'sk': [u'Diskusia k Wikibooks', u'Komentár k Wikipédii'],
            'sl': u'Pogovor o Wikiknjigah',
            'sq': u'Wikibooks diskutim',
            'sr': [u'Разговор о викикњигама', u'Razgovor o Викикњиге'],
            'su': u'Obrolan Wikibooks',
            'sv': u'Wikibooksdiskussion',
            'sw': u'Majadiliano ya Wikibooks',
            'ta': [u'விக்கிநூல்கள் பேச்சு', u'விக்கிபீடியா பேச்சு'],
            'te': u'Wikibooks చర్చ',
            'tg': u'Баҳси Wikibooks',
            'th': u'คุยเรื่องWikibooks',
            'tk': u'Wikibooks çekişme',
            'tl': u'Usapang Wikibooks',
            'tr': u'Vikikitap tartışma',
            'tt': [u'Wikibooks бәхәсе', u'Обсуждение Wikibooks', u'Wikibooks bäxäse'],
            'uk': u'Обговорення Вікіпідручника',
            'ur': u'تبادلۂ خیال وکی کتب',
            'uz': u'Vikikitob munozarasi',
            'vi': u'Thảo luận Wikibooks',
            'vo': u'Bespik dö Vükibuks',
            'wa': u'Wikibooks copene',
            'za': u'Wikibooks讨论',
            'zh': u'Wikibooks talk',
            'zh-min-nan': u'Wikibooks talk',
        }

        self.namespaces[90] = {
            'pt': u'Tópico',
        }

        self.namespaces[91] = {
            'pt': u'Tópico discussão',
        }

        self.namespaces[92] = {
            'pt': u'Resumo',
        }

        self.namespaces[93] = {
            'pt': u'Resumo discussão',
        }

        self.namespaces[100] = {
            'bn': u'উইকিশৈশব',
            'fr': u'Transwiki',
            'he': u'שער',
            'id': u'Resep',
            'it': u'Progetto',
            'ja': u'Transwiki',
            'ml': u'പാചകപുസ്തകം',
            'ms': u'Resipi',
            'ro': u'Raft',
            'ru': u'Полка',
            'tl': u'Pagluluto',
            'tr': u'Yemek',
            'uk': u'Полиця',
        }

        self.namespaces[101] = {
            'bn': u'উইকিশৈশব আলাপ',
            'fr': u'Discussion Transwiki',
            'he': u'שיחת שער',
            'id': u'Pembicaraan Resep',
            'it': u'Discussioni progetto',
            'ja': u'Transwiki‐ノート',
            'ml': u'പാചകപുസ്തകസം‌വാദം',
            'ms': u'Perbualan Resipi',
            'ro': u'Discuţie Raft',
            'ru': u'Обсуждение полки',
            'tl': u'Usapang pagluluto',
            'tr': u'Yemek tartışma',
            'uk': u'Обговорення полиці',
        }

        self.namespaces[102] = {
            'az': u'Resept',
            'bn': u'বিষয়',
            'ca': u'Viquiprojecte',
            'cy': u'Silff lyfrau',
            'de': u'Regal',
            'en': u'Cookbook',
            'es': u'Wikiversidad',
            'fr': u'Wikijunior',
            'id': u'Wisata',
            'it': u'Ripiano',
            'ml': u'വിഷയം',
            'nl': u'Transwiki',
            'ro': u'Wikijunior',
            'ru': u'Импортировано',
            'sr': u'Кувар',
            'uk': u'Рецепт',
            'vi': u'Chủ đề',
        }

        self.namespaces[103] = {
            'az': u'Resept müzakirəsi',
            'bn': u'বিষয় আলাপ',
            'ca': u'Viquiprojecte Discussió',
            'cy': u'Sgwrs Silff lyfrau',
            'de': u'Regal Diskussion',
            'en': u'Cookbook talk',
            'es': u'Wikiversidad Discusión',
            'fr': u'Discussion Wikijunior',
            'id': u'Pembicaraan Wisata',
            'it': u'Discussioni ripiano',
            'ml': u'വിഷയസം‌വാദം',
            'nl': u'Overleg transwiki',
            'ro': u'Discuţie Wikijunior',
            'ru': u'Обсуждение импортированного',
            'sr': u'Разговор о кувару',
            'uk': u'Обговорення рецепта',
            'vi': u'Thảo luận Chủ đề',
        }

        self.namespaces[104] = {
            'az': u'Vikikitab',
            'he': u'מדף',
            'ka': u'თარო',
            'nl': u'Wikijunior',
            'pl': u'Wikijunior',
            'ro': u'Carte de bucate',
            'ru': u'Рецепт',
            'vi': u'Trẻ em',
        }

        self.namespaces[105] = {
            'az': u'Vikikitab müzakirəsi',
            'he': u'שיחת מדף',
            'ka': u'თარო განხილვა',
            'nl': u'Overleg Wikijunior',
            'pl': u'Dyskusja Wikijuniora',
            'ro': u'Discuţie Carte de bucate',
            'ru': u'Обсуждение рецепта',
            'vi': u'Thảo luận Trẻ em',
        }

        self.namespaces[106] = {
            'ru': u'Задача',
            'vi': u'Nấu ăn',
        }

        self.namespaces[107] = {
            'ru': u'Обсуждение задачи',
            'vi': u'Thảo luận Nấu ăn',
        }

        self.namespaces[108] = {
            'en': u'Transwiki',
        }

        self.namespaces[109] = {
            'en': u'Transwiki talk',
        }

        self.namespaces[110] = {
            'en': u'Wikijunior',
            'tr': u'Vikiçocuk',
        }

        self.namespaces[111] = {
            'en': u'Wikijunior talk',
            'tr': u'Vikiçocuk tartışma',
        }

        self.namespaces[112] = {
            'en': u'Subject',
            'si': u'විෂයය',
            'tr': u'Kitaplık',
        }

        self.namespaces[113] = {
            'en': u'Subject talk',
            'si': u'විෂයය සාකච්ඡාව',
            'tr': u'Kitaplık tartışma',
        }

        self.namespaces[114] = {
            'si': u'කණිෂ්ඨ විකි',
        }

        self.namespaces[115] = {
            'si': u'කණිෂ්ඨ විකි සාකච්ඡාව',
        }

        # CentralAuth cross avaliable projects.
        self.cross_projects = [
            'wiktionary', 'wikibooks', 'wikiquote', 'wikisource', 'wikinews',
            'wikiversity', 'meta', 'mediawiki', 'test', 'incubator', 'commons',
            'species',
        ]

        # Global bot allowed languages on http://meta.wikimedia.org/wiki/Bot_policy/Implementation#Current_implementation
        self.cross_allowed = [
            'af', 'ang', 'ca', 'fa', 'fy', 'it', 'nl', 'ru', 'th', 'zh',
        ]

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
            'simple': self.alphabetic
        }

        self.obsolete = {
            'aa': None, # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Afar_Wikibooks
            'ak': None, # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Akan_Wikibooks
            'als': None, # http://als.wikipedia.org/wiki/Wikipedia:Stammtisch/Archiv_2008-1#Afterwards.2C_closure_and_deletion_of_Wiktionary.2C_Wikibooks_and_Wikiquote_sites
            'as': None, # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Assamese_Wikibooks
            'ay': None, # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Aymar_Wikibooks
            'ba': None, # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Bashkir_Wikibooks
            'bi': None, # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Bislama_Wikibooks
            'bm': None, # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Bambara_Wikibooks
            'bo': None, # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Tibetan_Wikibooks
            'ch': None, # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Chamorro_Wikibooks
            'co': None, # https://bugzilla.wikimedia.org/show_bug.cgi?id=28644
            'dk': 'da',
            'ga':None, # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Gaeilge_Wikibooks
            'got': None, # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Gothic_Wikibooks
            'gn': None, # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Guarani_Wikibooks
            'gu': None, # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Gujarati_Wikibooks
            'jp': 'ja',
            'km': None, # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Khmer_Wikibooks
            'kn': None, # https://bugzilla.wikimedia.org/show_bug.cgi?id=20325
            'ks': None, # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Kashmiri_Wikibooks
            'lb': None, # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_L%C3%ABtzebuergesch_Wikibooks
            'ln': None, # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Lingala_Wikibooks
            'lv': None, # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Latvian_Wikibooks
            'mi': None, # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Maori_Wikibooks
            'minnan':'zh-min-nan',
            'na': None, #http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Nauruan_Wikibooks
            'nah': None, # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Nahuatl_Wikibooks
            'nb': 'no',
            'nds': None, #http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Plattd%C3%BC%C3%BCtsch_Wikibooks
            'ps': None, # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Pashto_Wikibooks
            'qu': None, # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Quechua_Wikibooks
            'rm': None, # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Rumantsch_Wikibooks
            'se': None, # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Sami_Wikibooks
            'simple' : 'en', # https://bugzilla.wikimedia.org/show_bug.cgi?id=20325
            'sw' : None, #https://bugzilla.wikimedia.org/show_bug.cgi?id=25170
            'tokipona': None,
            'ug': None, # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Uyghur_Wikibooks
            'wa': None, # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Walon_Wikibooks
            'xh': None, # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Xhosa_Wikibooks
            'yo': None, # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Yoruba_Wikibooks
            'za': None, # https://bugzilla.wikimedia.org/show_bug.cgi?id=20325
            'zh-tw': 'zh',
            'zh-cn': 'zh',
            'zu': None, # https://bugzilla.wikimedia.org/show_bug.cgi?id=25425
        }

    def shared_image_repository(self, code):
        return ('commons', 'commons')

    if family.config.SSL_connection:

        def protocol(self, code):
            return 'https'
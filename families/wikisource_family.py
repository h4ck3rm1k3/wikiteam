# -*- coding: utf-8  -*-
import family

__version__ = '$Id: wikisource_family.py 10227 2012-05-20 13:01:53Z xqt $'

# The Wikimedia family that is known as Wikisource

class Family(family.Family):
    def __init__(self):
        family.Family.__init__(self)
        self.name = 'wikisource'

        self.languages_by_size = [
            'fr', 'en', 'de', 'ru', 'it', 'zh', 'pt', 'he', 'pl', 'es', 'sv',
            'fa', 'hu', 'ar', 'ca', 'cs', 'sl', 'ko', 'ro', 'fi', 'vi', 'te',
            'sa', 'el', 'bn', 'th', 'hr', 'hy', 'nl', 'no', 'sr', 'la', 'vec',
            'ml', 'tr', 'ja', 'yi', 'uk', 'br', 'mk', 'id', 'is', 'ta', 'da',
            'eo', 'li', 'be', 'bg', 'sah', 'gu', 'bs', 'et', 'az', 'gl', 'lt',
            'kn', 'mr', 'cy', 'zh-min-nan', 'sk', 'fo',
        ]

        for lang in self.languages_by_size:
            self.langs[lang] = '%s.wikisource.org' % lang
        self.langs['-'] = 'wikisource.org'

        # Override defaults
        self.namespaces[10]['zh'] = [u'Template', u'模板', u'样板', u'樣板']
        self.namespaces[12]['zh'] = [u'Help', u'帮助', u'幫助']
        self.namespaces[14]['zh'] = [u'Category', u'分类', u'分類']
        self.namespaces[3]['ca'] = [u'Usuari Discussió']
        self.namespaces[2]['ca'] = [u'Usuari']
        self.namespaces[3]['cs'] = [u'Diskuse s uživatelem', u'Uživatel diskuse', u'Uživatelka diskuse', u'Diskuse s uživatelkou']
        self.namespaces[2]['cs'] = [u'Uživatel', u'Uživatelka']
        self.namespaces[12]['nl'] = [u'Help']
        self.namespaces[3]['pt'] = [u'Utilizador Discussão', u'Usuário Discussão', u'Utilizadora Discussão']
        self.namespaces[2]['pt'] = [u'Utilizador', u'Usuário', u'Utilizadora']
        self.namespaces[6]['vec'] = [u'File', u'Imagine']
        self.namespaces[3]['pl'] = [u'Dyskusja wikiskryby', u'Dyskusja użytkownika', u'Dyskusja użytkowniczki']
        self.namespaces[2]['pl'] = [u'Wikiskryba', u'Użytkownik', u'Użytkowniczka']
        self.namespaces[3]['fr'] = [u'Discussion utilisateur', u'Discussion Utilisateur']
        self.namespaces[2]['fr'] = [u'Utilisateur']
        self.namespaces[15]['bn'] = [u'বিষয়শ্রেণী আলোচনা']
        self.namespaces[14]['bn'] = [u'বিষয়শ্রেণী']
        self.namespaces[3]['de'] = [u'Benutzer Diskussion', u'Benutzerin Diskussion']
        self.namespaces[13]['de'] = [u'Hilfe Diskussion']
        self.namespaces[12]['de'] = [u'Hilfe']
        self.namespaces[9]['da'] = [u'MediaWiki diskussion', u'MediaWiki-diskussion']
        self.namespaces[13]['da'] = [u'Hjælp diskussion', u'Hjælp-diskussion']
        self.namespaces[9]['ro'] = [u'Discuție MediaWiki', u'Discuţie MediaWiki']

        # Most namespaces are inherited from family.Family.
        # Translation used on all wikis for the different namespaces.
        # (Please sort languages alphabetically)
        # You only need to enter translations that differ from _default.
        self.namespaces[4] = {
            '_default': self.namespaces[4]['_default'],
            '-': u'Wikisource',
            'ang': u'Wicifruma',
            'ar': [u'ويكي مصدر', u'وم'],
            'az': u'VikiMənbə',
            'be': [u'Вікікрыніцы', u'Wikisource'],
            'bg': u'Уикиизточник',
            'bn': [u'উইকিসংকলন', u'Wikisource'],
            'br': u'Wikimammenn',
            'bs': [u'Wikizvor', u'Wikisource'],
            'ca': u'Viquitexts',
            'cs': [u'Wikizdroje', u'WS', u'WZ', u'Wikisource'],
            'cy': [u'Wicitestun', u'Wikisource'],
            'da': u'Wikisource',
            'de': [u'Wikisource', u'WS'],
            'el': u'Βικιθήκη',
            'en': u'Wikisource',
            'eo': [u'Vikifontaro', u'Wikisource'],
            'es': u'Wikisource',
            'et': u'Vikitekstid',
            'fa': [u'ویکی‌نبشته', u'ون'],
            'fi': [u'Wikiaineisto', u'Wikisource'],
            'fo': [u'Wikiheimild', u'Wikisource'],
            'fr': u'Wikisource',
            'gl': u'Wikisource',
            'gu': [u'વિકિસ્રોત', u'Wikisource'],
            'he': u'ויקיטקסט',
            'hr': u'Wikizvor',
            'ht': u'Wikisòrs',
            'hu': u'Wikiforrás',
            'hy': u'Վիքիդարան',
            'id': u'Wikisource',
            'is': [u'Wikiheimild', u'Wikisource'],
            'it': u'Wikisource',
            'ja': u'Wikisource',
            'kn': u'Wikisource',
            'ko': [u'위키문헌', u'Wikisource'],
            'la': [u'Vicifons', u'Wikisource'],
            'li': [u'Wikibrónne', u'Wikisource'],
            'lt': [u'Vikišaltiniai', u'Wikisource'],
            'mk': u'Wikisource',
            'ml': [u'വിക്കിഗ്രന്ഥശാല', u'Wikisource', u'WS'],
            'mr': u'विकिस्रोत',
            'nb': u'Wikikilden',
            'nl': u'Wikisource',
            'no': u'Wikikilden',
            'pl': [u'Wikiźródła', u'WS'],
            'pt': u'Wikisource',
            'ro': u'Wikisource',
            'ru': u'Викитека',
            'sa': u'Wikisource',
            'sah': [u'Бикитиэкэ', u'Wikisource'],
            'sk': u'Wikisource',
            'sl': u'Wikivir',
            'sr': [u'Викизворник', u'Wikisource'],
            'sv': u'Wikisource',
            'ta': [u'Wikisource', u'விக்கிபீடியா'],
            'te': u'Wikisource',
            'th': [u'วิกิซอร์ซ', u'Wikisource'],
            'tr': u'VikiKaynak',
            'uk': [u'Wikisource', u'ВД'],
            'vec': u'Wikisource',
            'vi': u'Wikisource',
            'yi': [u'װיקיביבליאָטעק', u'וויקיביבליאטעק'],
            'zh': u'Wikisource',
            'zh-min-nan': u'Wikisource',
        }
        self.namespaces[5] = {
            '_default': self.namespaces[5]['_default'],
            '-': u'Wikisource talk',
            'ang': u'Wicifruma talk',
            'ar': [u'نقاش ويكي مصدر', u'نو'],
            'az': u'VikiMənbə müzakirəsi',
            'be': u'Размовы пра Вікікрыніцы',
            'bg': u'Уикиизточник беседа',
            'bn': [u'উইকিসংকলন আলোচনা', u'উইকিসংকলন আলাপ'],
            'br': u'Kaozeadenn Wikimammenn',
            'bs': u'Razgovor s Wikizvor',
            'ca': u'Viquitexts Discussió',
            'cs': [u'Diskuse k Wikizdrojům', u'Wikisource diskuse', u'Wikisource talk', u'Wikizdroje diskuse'],
            'cy': u'Sgwrs Wicitestun',
            'da': [u'Wikisource diskussion', u'Wikisource-diskussion'],
            'de': u'Wikisource Diskussion',
            'el': u'Βικιθήκη συζήτηση',
            'en': u'Wikisource talk',
            'eo': u'Vikifontaro diskuto',
            'es': u'Wikisource discusión',
            'et': [u'Vikitekstide arutelu', u'Vikitekstid arutelu'],
            'fa': u'بحث ویکی‌نبشته',
            'fi': u'Keskustelu Wikiaineistosta',
            'fo': [u'Wikiheimild-kjak', u'Wikiheimild kjak'],
            'fr': u'Discussion Wikisource',
            'gl': u'Conversa Wikisource',
            'gu': u'વિકિસ્રોત ચર્ચા',
            'he': u'שיחת ויקיטקסט',
            'hr': u'Razgovor o Wikizvoru',
            'ht': u'Diskisyon Wikisòrs',
            'hu': [u'Wikiforrás-vita', u'Wikiforrás vita'],
            'hy': u'Վիքիդարանի քննարկում',
            'id': u'Pembicaraan Wikisource',
            'is': u'Wikiheimildspjall',
            'it': u'Discussioni Wikisource',
            'ja': [u'Wikisource・トーク', u'Wikisource‐ノート'],
            'kn': u'Wikisource ಚರ್ಚೆ',
            'ko': [u'위키문헌토론', u'Wikisource talk'],
            'la': u'Disputatio Vicifontis',
            'li': u'Euverlèk Wikibrónne',
            'lt': u'Vikišaltiniai aptarimas',
            'mk': u'Разговор за Wikisource',
            'ml': u'വിക്കിഗ്രന്ഥശാല സംവാദം',
            'mr': u'विकिस्रोत चर्चा',
            'nb': u'Wikikilden-diskusjon',
            'nl': u'Overleg Wikisource',
            'no': u'Wikikilden-diskusjon',
            'pl': u'Dyskusja Wikiźródeł',
            'pt': u'Wikisource Discussão',
            'ro': [u'Discuție Wikisource', u'Discuţie Wikisource'],
            'ru': u'Обсуждение Викитеки',
            'sa': [u'Wikisourceसम्भाषणम्', u'Wikisourceसंभाषणं'],
            'sah': u'Бикитиэкэ Ырытыы',
            'sk': [u'Diskusia k Wikisource', u'Komentár k Wikipédii'],
            'sl': u'Pogovor o Wikiviru',
            'sr': [u'Разговор о Викизворнику', u'Razgovor o Викизворник'],
            'sv': u'Wikisourcediskussion',
            'ta': [u'Wikisource பேச்சு', u'விக்கிபீடியா பேச்சு'],
            'te': u'Wikisource చర్చ',
            'th': u'คุยเรื่องวิกิซอร์ซ',
            'tr': u'VikiKaynak tartışma',
            'uk': u'Обговорення Wikisource',
            'vec': u'Discussion Wikisource',
            'vi': u'Thảo luận Wikisource',
            'yi': [u'װיקיביבליאָטעק רעדן', u'וויקיביבליאטעק רעדן'],
            'zh': u'Wikisource talk',
            'zh-min-nan': u'Wikisource talk',
        }

        self.namespaces[90] = {
            'sv': u'Tråd',
        }

        self.namespaces[91] = {
            'sv': u'Tråddiskussion',
        }

        self.namespaces[92] = {
            'sv': u'Summering',
        }

        self.namespaces[93] = {
            'sv': u'Summeringsdiskussion',
        }

        self.namespaces[100] = {
            'ar': u'بوابة',
            'az': u'Portal',
            'bg': u'Автор',
            'bn': u'লেখক',
            'br': u'Meneger',
            'cs': u'Autor',
            'el': u'Σελίδα',
            'en': u'Portal',
            'fa': [u'درگاه', u'Portal'],
            'fr': u'Transwiki',
            'he': u'קטע',
            'hr': u'Autor',
            'hu': u'Szerző',
            'hy': u'Հեղինակ',
            'id': u'Pengarang',
            'ko': u'저자',
            'ml': u'രചയിതാവ്',
            'mr': u'दालन',
            'nl': u'Hoofdportaal',
            'pl': u'Strona',
            'pt': u'Portal',
            'sl': u'Stran',
            'sr': u'Аутор',
            'te': u'ద్వారము',
            'tr': u'Kişi',
            'vec': u'Autor',
            'vi': u'Chủ đề',
        }

        self.namespaces[101] = {
            'ar': u'نقاش البوابة',
            'az': u'Portal müzakirəsi',
            'bg': u'Автор беседа',
            'bn': u'লেখক আলাপ',
            'br': u'Kaozeadenn meneger',
            'cs': u'Diskuse k autorovi',
            'el': u'Συζήτηση σελίδας',
            'en': u'Portal talk',
            'fa': [u'بحث درگاه', u'Portal talk'],
            'fr': u'Discussion Transwiki',
            'he': u'שיחת קטע',
            'hr': u'Razgovor o autoru',
            'hu': u'Szerző vita',
            'hy': u'Հեղինակի քննարկում',
            'id': u'Pembicaraan Pengarang',
            'ko': u'저자토론',
            'ml': u'രചയിതാവിന്റെ സംവാദം',
            'mr': u'दालन चर्चा',
            'nl': u'Overleg hoofdportaal',
            'pl': u'Dyskusja strony',
            'pt': u'Portal Discussão',
            'sl': u'Pogovor o strani',
            'sr': u'Разговор о аутору',
            'te': u'ద్వారము చర్చ',
            'tr': u'Kişi tartışma',
            'vec': u'Discussion autor',
            'vi': u'Thảo luận Chủ đề',
        }

        self.namespaces[102] = {
            'ar': u'مؤلف',
            'az': u'Müəllif',
            'be': u'Аўтар',
            'bn': u'নির্ঘণ্ট',
            'br': u'Pajenn',
            'ca': u'Pàgina',
            'da': u'Forfatter',
            'de': u'Seite',
            'el': u'Βιβλίο',
            'en': u'Author',
            'eo': u'Aŭtoro',
            'es': u'Página',
            'et': u'Lehekülg',
            'fa': [u'پدیدآورنده', u'Author'],
            'fr': u'Auteur',
            'hr': u'Stranica',
            'hy': u'Պորտալ',
            'id': u'Indeks',
            'it': u'Autore',
            'la': u'Scriptor',
            'mk': u'Автор',
            'ml': u'കവാടം',
            'mr': [u'साहित्यिक', u'Author'],
            'nb': u'Forfatter',
            'nl': u'Auteur',
            'no': u'Forfatter',
            'pl': u'Indeks',
            'pt': u'Autor',
            'ro': u'Autor',
            'te': u'రచయిత',
            'vec': u'Pagina',
            'vi': u'Tác gia',
            'zh': u'Author',
        }

        self.namespaces[103] = {
            'ar': u'نقاش المؤلف',
            'az': u'Müəllif müzakirəsi',
            'be': u'Размовы пра аўтара',
            'bn': u'নির্ঘণ্ট আলাপ',
            'br': u'Kaozeadenn pajenn',
            'ca': u'Pàgina Discussió',
            'da': u'Forfatterdiskussion',
            'de': u'Seite Diskussion',
            'el': u'Συζήτηση βιβλίου',
            'en': u'Author talk',
            'eo': u'Aŭtoro-Diskuto',
            'es': u'Página Discusión',
            'et': u'Lehekülje arutelu',
            'fa': [u'گفتگو پدیدآورنده', u'Author talk'],
            'fr': u'Discussion Auteur',
            'hr': u'Razgovor o stranici',
            'hy': u'Պորտալի քննարկում',
            'id': u'Pembicaraan Indeks',
            'it': u'Discussioni autore',
            'la': u'Disputatio Scriptoris',
            'mk': u'Разговор за автор',
            'ml': u'കവാടത്തിന്റെ സംവാദം',
            'mr': [u'साहित्यिक चर्चा', u'Author talk'],
            'nb': u'Forfatterdiskusjon',
            'nl': u'Overleg auteur',
            'no': u'Forfatterdiskusjon',
            'pl': u'Dyskusja indeksu',
            'pt': u'Autor Discussão',
            'ro': u'Discuție Autor',
            'te': u'రచయిత చర్చ',
            'vec': u'Discussion pagina',
            'vi': u'Thảo luận Tác gia',
            'zh': u'Author talk',
        }

        self.namespaces[104] = {
            '-': u'Page',
            'ar': u'صفحة',
            'be': u'Старонка',
            'bn': u'পাতা',
            'br': [u'Oberour', u'Author'],
            'ca': [u'Llibre', u'Index'],
            'da': u'Side',
            'de': u'Index',
            'en': u'Page',
            'eo': u'Paĝo',
            'es': u'Índice',
            'et': [u'Register', u'Index'],
            'fa': [u'برگه', u'Page'],
            'fr': u'Page',
            'gu': u'પૃષ્ઠ',
            'he': u'עמוד',
            'hr': [u'Sadržaj', u'Index'],
            'hu': u'Oldal',
            'hy': u'Էջ',
            'id': u'Halaman',
            'it': u'Progetto',
            'la': u'Pagina',
            'ml': [u'സൂചിക', u'Index'],
            'mr': u'पान',
            'no': u'Side',
            'pl': [u'Autor', u'Author'],
            'pt': [u'Galeria', u'Index'],
            'ro': u'Pagină',
            'ru': u'Страница',
            'sa': u'पुटम्',
            'sl': [u'Kazalo', u'Index'],
            'sv': u'Sida',
            'te': [u'పుట', u'పేజీ', u'Page'],
            'vec': [u'Indice', u'Index'],
            'vi': u'Trang',
            'zh': u'Page',
        }

        self.namespaces[105] = {
            '-': u'Page talk',
            'ar': u'نقاش الصفحة',
            'be': u'Размовы пра старонку',
            'bn': u'পাতা আলাপ',
            'br': [u'Kaozeadenn oberour', u'Author talk'],
            'ca': [u'Llibre Discussió', u'Index talk'],
            'da': u'Sidediskussion',
            'de': [u'Index Diskussion', u'Index talk'],
            'en': u'Page talk',
            'eo': u'Paĝo-Diskuto',
            'es': u'Índice Discusión',
            'et': [u'Registri arutelu', u'Index talk'],
            'fa': u'گفتگوی برگه',
            'fr': u'Discussion Page',
            'gu': u'પૃષ્ઠ ચર્ચા',
            'he': u'שיחת עמוד',
            'hr': [u'Razgovor o sadržaju', u'Index talk'],
            'hu': u'Oldal vita',
            'hy': u'Էջի քննարկում',
            'id': u'Pembicaraan Halaman',
            'it': u'Discussioni progetto',
            'la': u'Disputatio Paginae',
            'ml': [u'സൂചികയുടെ സംവാദം', u'Index talk'],
            'mr': u'पान चर्चा',
            'no': u'Sidediskusjon',
            'pl': [u'Dyskusja autora', u'Author talk'],
            'pt': [u'Galeria Discussão', u'Index talk'],
            'ro': u'Discuție Pagină',
            'ru': u'Обсуждение страницы',
            'sa': u'पुटसंवाद',
            'sl': [u'Pogovor o kazalu', u'Index talk'],
            'sv': u'Siddiskussion',
            'te': [u'పుట చర్చ', u'పేజీ చర్చ', u'Page talk'],
            'vec': [u'Discussion indice', u'Index talk'],
            'vi': u'Thảo luận Trang',
            'zh': u'Page talk',
        }

        self.namespaces[106] = {
            '-': u'Index',
            'ar': u'فهرس',
            'be': u'Індэкс',
            'bn': u'প্রবেশদ্বার',
            'ca': u'Autor',
            'da': u'Indeks',
            'en': u'Index',
            'eo': u'Indekso',
            'et': u'Autor',
            'fa': u'فهرست',
            'fr': u'Portail',
            'gu': u'સૂચિ',
            'he': u'ביאור',
            'hu': u'Index',
            'hy': u'Ինդեքս',
            'id': u'Portal',
            'it': u'Portale',
            'la': u'Liber',
            'ml': u'താൾ',
            'mr': [u'अनुक्रमणिका', u'Index'],
            'no': u'Indeks',
            'pt': u'Página',
            'ro': u'Index',
            'ru': u'Индекс',
            'sa': u'अनुक्रमणिका',
            'sv': u'Författare',
            'te': u'సూచిక',
            'vi': u'Mục lục',
            'zh': u'Index',
        }

        self.namespaces[107] = {
            '-': u'Index talk',
            'ar': u'نقاش الفهرس',
            'be': u'Размовы пра індэкс',
            'bn': u'প্রবেশদ্বার আলাপ',
            'ca': u'Autor Discussió',
            'da': u'Indeksdiskussion',
            'en': u'Index talk',
            'eo': u'Indekso-Diskuto',
            'et': u'Autori arutelu',
            'fa': u'گفتگوی فهرست',
            'fr': u'Discussion Portail',
            'gu': u'સૂચિ ચર્ચા',
            'he': u'שיחת ביאור',
            'hu': u'Index vita',
            'hy': u'Ինդեքսի քննարկում',
            'id': u'Pembicaraan Portal',
            'it': u'Discussioni portale',
            'la': u'Disputatio Libri',
            'ml': u'താളിന്റെ സംവാദം',
            'mr': [u'अनुक्रमणिका चर्चा', u'Index talk'],
            'no': u'Indeksdiskusjon',
            'pt': u'Página Discussão',
            'ro': u'Discuție Index',
            'ru': u'Обсуждение индекса',
            'sa': u'अनुक्रमणिकासंवाद',
            'sv': u'Författardiskussion',
            'te': u'సూచిక చర్చ',
            'vi': u'Thảo luận Mục lục',
            'zh': u'Index talk',
        }

        self.namespaces[108] = {
            '-': u'Author',
            'be': u'Аўтар',
            'gu': u'સર્જક',
            'he': u'מחבר',
            'it': u'Pagina',
            'pt': u'Em Tradução',
            'sv': u'Index',
        }

        self.namespaces[109] = {
            '-': u'Author talk',
            'be': u'Размовы_пра_аўтара',
            'gu': u'સર્જક ચર્ચા',
            'he': u'שיחת מחבר',
            'it': u'Discussioni pagina',
            'pt': u'Discussão Em Tradução',
            'sv': u'Indexdiskussion',
        }

        self.namespaces[110] = {
            'he': u'תרגום',
            'it': u'Indice',
            'pt': u'Anexo',
        }

        self.namespaces[111] = {
            'he': u'שיחת תרגום',
            'it': u'Discussioni indice',
            'pt': u'Anexo Discussão',
        }

        self.namespaces[112] = {
            'fr': u'Livre',
            'he': u'מפתח',
        }

        self.namespaces[113] = {
            'fr': u'Discussion Livre',
            'he': u'שיחת מפתח',
        }

        # CentralAuth cross avaliable projects.
        self.cross_projects = [
            'wiktionary', 'wikibooks', 'wikiquote', 'wikisource', 'wikinews',
            'wikiversity', 'meta', 'mediawiki', 'test', 'incubator', 'commons',
            'species',
        ]

        # Global bot allowed languages on http://meta.wikimedia.org/wiki/Bot_policy/Implementation#Current_implementation
        self.cross_allowed = [
            'ca', 'el', 'fa', 'it', 'ko', 'no', 'pl', 'vi', 'zh',
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
            'ang': None, # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Old_English_Wikisource
            'dk': 'da',
            'ht': None, # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Haitian_Creole_Wikisource
            'jp': 'ja',
            'minnan':'zh-min-nan',
            'nb': 'no',
            'tokipona': None,
            'zh-tw': 'zh',
            'zh-cn': 'zh'
        }

        self.authornamespaces = {
            '_default': [0],
            'ar': [102],
            'bg': [100],
            'cs': [100],
            'da': [102],
            'en': [102],
            'fa': [102],
            'fr': [102],
            'hr': [100],
            'hu': [100],
            'hy': [100],
            'it': [102],
            'ko': [100],
            'la': [102],
            'nl': [102],
            'no': [102],
            'pl': [104],
            'pt': [102],
            'sv': [106],
            'tr': [100],
            'vi': [102],
            'zh': [102],
            }

        self.crossnamespace[0] = {
            '_default': self.authornamespaces,
        }
        self.crossnamespace[100] = {
            'bg': self.authornamespaces,
            'cs': self.authornamespaces,
            'hr': self.authornamespaces,
            'hu': self.authornamespaces,
            'hy': self.authornamespaces,
            'ko': self.authornamespaces,
            'tr': self.authornamespaces,
        }

        self.crossnamespace[102] = {
            'ar': self.authornamespaces,
            'da': self.authornamespaces,
            'en': self.authornamespaces,
            'fa': self.authornamespaces,
            'fr': self.authornamespaces,
            'it': self.authornamespaces,
            'la': self.authornamespaces,
            'nl': self.authornamespaces,
            'no': self.authornamespaces,
            'pt': self.authornamespaces,
            'vi': self.authornamespaces,
            'zh': self.authornamespaces,
        }

        self.crossnamespace[104] = {
            'pl': self.authornamespaces,
        }

        self.crossnamespace[106] = {
            'sv': self.authornamespaces,
        }

    def shared_image_repository(self, code):
        return ('commons', 'commons')

    if family.config.SSL_connection:

        def protocol(self, code):
            return 'https'
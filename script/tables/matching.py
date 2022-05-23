# normalised data to link entries in our database to entries in
# wikidata; of course, these conversion tables do not cover all
# of our entries, but there are fallbacks: if a person's function
# doesn't have an equivalent in the "function" dictionary, we can
# still get a full name, dates of birth/death...

# all of the charaters are in lowercase to ease the matching process

# first names ; to be used on tei:trait
# - keys: the abbreviation, found in catalogues;
# - values: the full, normalised orthograph for wikidata
names = {
    "ad": "adam",
    "alex": "alexandre",
    "alph": "alphonse",
    "ant": "antoine",
    "arm": "armand",
    "aug": "auguste",
    "ch": "charles",
    "cl": "claude",
    "emm": "emmanuel",
    "ed": "edouard",
    "et": "etienne",
    "ét": "etienne",
    "ferd": "ferdinand",
    "fr": "françois",
    "franc": "françois",
    "franç": "françois",
    "fréd": "frédéric",
    "g": "guillaume",
    "guill": "guillaume",
    "gab": "gabriel",
    "jacq": "jacques",
    "jh": "joseph",
    "jos": "joseph",
    "math": "matthieu",
    "nic": "nicolas",
    "ph": "philippe",
    "v": "victor",
    "vr": "victor",
}

# composed first names; for composed names, this table is queried first,
# since a composed name gives context to the parts of the name
# else, we try to resole the abbreviated composed names inititials by initials
# to be used on tei:name
# - keys: the abbreviation, found in catalogues;
# - values: the full, normalised orthograph for wikidata
comp_names = {
    "arm ch": "armand-charles",
    "ch m": "charles-marie",
    "f m": "francois-marie",
    "fr emm.": "françois-emmanuel",
    "j f": "jean-francois",
    "j m": "jean-marie",
    "j j": "jean-jacques",
    "j l": "jean-louis",
    "j b": "jean-baptiste",
    "j p": "jean-pierre",
    "j pierre": "jean-pierre",
    "l f": "louis-françois",
    "m f": "marius-felix",
    "franc rené": "francois-rené",
    "m madeleine": "marie-madeleine",
    "ph h": "philippe henri",
    "p alex": "pierre alexandre",
    "p j": "pierre-jean",
    "j sylvain": "jean-sylvain",
    "l ph": "louis-philippe",
    "edm ch": "edmond-charles",
    "ch marie": "charles-marie"
}

# french nobility and clerical title. only the most important
# titles are translated because people are not referred to using those
# terms in wikidata;
# to be used on the tei:name
# - keys: the term to be used in wikidata;
# - values: a list of corresponding terms in the tei:traits
status = {
    "empereur": "",
    "impératrice": "",
    "géneral": "general",
    "reine": "queen",
    "roi": "king",
    "princesse": "princess",
    "prince": "prince",
    "archiduchesse": "",
    "archiduc": "",
    "duchesse": "duchess",
    "duc": "duke",
    "famille": "family",
    "seigneur": "",
    "vicomtesse": "",
    "victesse": "",
    "vicomte": "",
    "victe": "",
    "comtesse palatine": "countess palatine",
    "comtesse": "",
    "ctesse": "",
    "comte": "",
    "cte": "",
    "cardinal": "",
    "pape": "pope",
    "lord": "",
    "chevalier": "",
    "marquise": "",
    "marquis": "",
    "sire": "",
    "baronnesse": "",
    "baronne": "",
    "baron": "",
    "abbé": "",
    "madame": "",
    "mme": "",
    "monsieur": "",
    "mr": "",
    "docteur": "",
    "maréchale": "",
    "maréchal": "",
    "mademoiselle": "",
    "melle": "",
    "mlle": "",
    "sir": ""
}

# a person's function; to be found in the tei:trait; not all words
# here have a perfect duplicate in wikidata ; in turn, some very
# frequent words in the tei:trait's are not present here
# - keys: the term to be used in wikidata;
# - values: a list of corresponding terms in the tei:traits
functions = {
    "général": "general",
    "maréchal": "marshal",
    "lieutenant": "military",
    "officier": "military",
    "colonel": "military",
    "lieutenant-colonel": "military",
    "commandant": "military",
    "capitaine": "military",  # "less important" military positions
    "roi": "king",
    "empereur": "emperor",
    "president": "president",
    "homme politique": "politician",
    "président de l'assemblée": "politician",
    "orateur": "politician",
    "député": "politician",
    "secrétaire d'état": "politician",
    "écrivain": "writer",
    "auteur": "writer",
    "romancier": "writer",
    "acteur": "actor",
    "actrice": "actress",
    "cantatrice": "singer",
    "chanteur": "singer",
    "chanteuse": "singer",
    "peintre": "painter",
    "sculpteur": "sculptor",
    "statutaire": "sculptor",
    "compositeur": "composer",
    "musicien": "musician",
    "musicienne": "musician",
    "tragédien": "actor",
    "chansonnier": "chansonnier",
    "achitecte": "architect",
    "journaliste": "journalist",
    "inventeur": "inventor",
    "chimiste": "chemist",
    "connétable": "constable"
}

# messy regex to match roman numerals and their french number suffixes:
# "Ier", "IInd", "IIIème" ...
rgx_roman = r"(^|\s)((I|V|X|D|C|M)+)(er|ère|ere|ème|eme|nd|nde)?(\s|$)"  # only keep $1 of that regex

# hybrid of the list of departments created in 1790 + list of 1811 departments
# (largest number of departments in the french history)
# https://fr.wikipedia.org/wiki/liste_des_d%c3%a9partements_fran%c3%a7ais_de_1790
# https://fr.wikipedia.org/wiki/liste_des_d%c3%a9partements_fran%c3%a7ais_de_1811
dpts = [
    "ain",
    "aisne",
    "allier",
    "basses-alpes",
    "hautes-alpes",
    "alpes-maritimes",
    "annepins",
    "provence",
    "ardèche",
    "ardennes",
    "arriège",
    "arno",
    "aube",
    "aude",
    "aveyron",
    "bouches-de-l'elbe",
    "bouches-de-l'escaut",
    "bouches-de-l'yssel",
    "bpuches-de-la-meuse",
    "bouches-du-rhin",
    "bouches-du-rhône",
    "bouches-du-weser",
    "calvados",
    "cantal",
    "charente",
    "charente-inférieure",
    "cher",
    "corrèze",
    "corse",
    "côte-d'or",
    "côtes-du-nord",
    "creuse",
    "deux-nèthes",
    "deux-sèvres",
    "doire",
    "dordogne",
    "doubs",
    "drôme",
    "dyle",
    "ems-occidental",
    "ems-oriental",
    "ems-supérieur",
    "escaut",
    "eure",
    "eure-et-loir",
    "finistère",
    "forêts",
    "gard",
    "haute-garonne",
    "gers",
    "gironde",
    "hérault",
    "ille-et-villaine",
    "indre",
    "indre-et-loire",
    "isère",
    "jemappes",
    "jura",
    "landes",
    "léman",
    "loire",
    "loir-et-cher",
    "haute-loire",
    "loire-inférieure",
    "loiret",
    "lot",
    "lot-et-garonne",
    "lozère",
    "lys",
    "maine-et-loire",
    "manche",
    "marengo",
    "marne",
    "haute-marne",
    "méditerrannée",
    "mayenne",
    "meurthe",
    "meuse",
    "meuse-inférieure",
    "mont-blanc",
    "mont-tonnerre",
    "montenotte",
    "morbihan",
    "meuse",
    "moselle",
    "nièvre",
    "nord",
    "oise",
    "ombrone",
    "orne",
    "ourte",
    "paris",
    "pas-de-calais",
    "pô",
    "puy-de-dôme",
    "hautes-pyrénées",
    "basses-pyrénées",
    "pyrénées-orientales",
    "haut-rhin",
    "bas-rhin",
    "rhin-et-moselle",
    "rhône",
    "rhône-et-loire",
    "roer",
    "rome",
    "haute-saône",
    "saône-et-loire",
    "sambre-et-meuse",
    "sarre",
    "sarthe",
    "seine",
    "seine-et-marne",
    "seine-et-oise",
    "seine-inférieure",
    "sézia",
    "simplon",
    "deux-sèvres",
    "somme",
    "stura",
    "tarn",
    "tarn-et-garonne",
    "taro",
    "trasimène",
    "var",
    "vaucluse",
    "vendée",
    "vienne",
    "haute-vienne",
    "vosges",
    "yonne",
    "yssel-supérieur",
    "zuyderzée"
]

# pre-revolution french provinces
provinces = [
    "île-de-france",
    "berry",
    "orléanais",
    "normandie",
    "languedoc",
    "lyonnais",
    "dauphiné",
    "champagne",
    "aunis",
    "saintonge",
    "poitou",
    "guyenne et gascogne",
    "bourgogne",
    "picardie",
    "anjou",
    "provence",
    "angoumois",
    "bourbonnais",
    "marche",
    "bretagne",
    "maine",
    "touraine",
    "limousin",
    "comté de foix",
    "auvergne",
    "béarn",
    "alsace",
    "artois",
    "roussillon",
    "flandre française et hainaut français",
    "franche-comté",
    "lorraine et trois-évêchés",
    "corse",
    "nivernais",
]

# list of french colonies; alternate and old orthographs
# are in the list too, in order to facilitate the matching process
colonies = [
    "québec",
    "ontario",
    "saint-pierre-et-miquelon",
    "mississippi",
    "missouri",
    "louisiane",
    "anguilla",
    "antigua",
    "dominique",
    "saint-domingue",
    "guadeloupe",
    "monsterrat",
    "saint-martin",
    "saint-barthélémy",
    "sainte-lucy",
    "saint-vincent-et-les-grenadines",
    "saint-eustache",
    "saint-christophe",
    "martinique"
    "guyane française",
    "guyane",
    "maroc",  # unfortunately the morocco referred to in XIXth century france is a french protectorate
    "algérie",  # same
    "algérie française",  # same
    "tunisie",  # same
    "fezzan",
    "dahomey",
    "haute-volta",
    "oubangui-chari",
    "congo français",
    "moyen-congo",
    "guinée française",
    "soudan français",
    "gorée",
    "tigi",
    "djibouti",
    "cheikh saïd",
    "comores",
    "fort-dauphin",
    "îles maurice",
    "mayotte",
    "la réunion",
    "îles éparses",
    "île amsterdam",
    "île saint-paul",
    "archipel crozet",
    "îles kerguelen",
    "castellorizo",
    "grand-liban",
    "sandjak d'alexandrette",
    "indes françaises",
    "pondichéry",
    "karikal",
    "yanaon",
    "mahé",
    "chanderngor",
    "tonkin",
    "annam",
    "cochinchine",
    "guangzhou wan",
    "shanghai",
    "guangzhou",
    "tianjin",
    "hankou",
    "clipperton",
    "nouvelle-calédonie",
    "polynésie française",
    "vanuatu",
    "nouvelles-hébrides",
    "wallis et futuna"
]

countries = {
    "états-unis d'amérique": "united states of america",
    "etats-unis d'amérique": "united states of america",
    "états-unis": "united states of america",
    "etats-unis": "united states of america",
    "grèce": "greece",
    "canada": "canada",
    "chine": "china",
    "haïti": "haiti",
    "tobago": "tobago",
    "brésil": "brasil",
    "burkina-faso": "burkina-faso",
    "cameroun": "cameroun",
    "tchad": "tchad",
    "congo": "congo",
    "gabon": "gabon",
    "guinée": "guinea",
    "côte d'ivoire": "ivory coast",
    "mali": "mali",
    "mauritanie": "mauritania",
    "niger": "niger",
    "sénégal": "senegal",
    "madagascar": "madagascar",
    "seychelles": "seychelles",
    "tanzanie": "tanzania",
    "zanzibar": "zanzibar",
    "liban": "lebanon",
    "syrie": "syria",
    "inde": "india",
    "laos": "laos",
    "viet-nâm": "vietnam"
}

# events are translated to something that returns a result in wikidata
events = {
    "guerre": "war",
    "insurrection": "war",
    "siège": "siege",
    "commune": "commune",
    "défense": "battle",
    "révolution française": "french revolution",
    "révolution": "revolution"
}

other = {
    "louvre": "louvre",
    "arc de triomphe du carrousel": "arc de triomphe du carrousel",
    "université": "university"
}
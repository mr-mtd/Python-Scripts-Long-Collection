class Suffix:
    def __init__(self, suffix, definition, example):
        self.suffix = suffix
        self.definition = definition
        self.example = example

    def __str__(self):
        return f"{self.suffix}: {self.definition} ({self.example})"

suffix_list = [
    Suffix("-able, -ible", "is; can be", "affordable, sensible"),
    Suffix("-al, -ial", "having characteristics of", "universal, facial"),
    Suffix("-ed", "past tense verbs; adjectives", "the dog walked, the walked dog"),
    Suffix("-en", "made of", "golden"),
    Suffix("-er, -or", "one who; person connected with", "teacher, professor"),
    Suffix("-er", "more", "taller"),
    Suffix("-est", "the most", "tallest"),
    Suffix("-ful", "full of", "helpful"),
    Suffix("-ic", "having characteristics of", "poetic"),
    Suffix("-ing", "verb forms; present participles", "sleeping"),
    Suffix("-ion, -tion, -ation, -ition", "act; process", "submission, motion, relation, edition"),
    Suffix("-ity, -ty", "state of", "activity, society"),
    Suffix("-ive, -ative, -itive", "adjective form of noun", "active, comparative, sensitive"),
    Suffix("-less", "without", "hopeless"),
    Suffix("-ly", "how something is", "lovely"),
    Suffix("-ment", "state of being; act of", "contentment"),
    Suffix("-ness", "state of; condition of", "openness"),
    Suffix("-ous, -eous, -ious", "having qualities of", "riotous, courageous, gracious"),
    Suffix("-s, -es", "more than one", "trains, trenches"),
    Suffix("-y", "characterized by", "gloomy")
]

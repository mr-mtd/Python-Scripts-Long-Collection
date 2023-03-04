class GreekRoot:
    def __init__(self, root, definition, example):
        self.root = root
        self.definition = definition
        self.example = example

    def __str__(self):
        return f"{self.root}: {self.definition} ({self.example})"

root_list = [
    GreekRoot("anthropo", "man; human; humanity", "anthropologist, philanthropy"),
    GreekRoot("auto", "self", "autobiography, automobile"),
    GreekRoot("bio", "life", "biology, biography"),
    GreekRoot("chron", "time", "chronological, chronic"),
    GreekRoot("dyna", "power", "dynamic, dynamite"),
    GreekRoot("dys", "bad; hard; unlucky", "dysfunctional, dyslexic"),
    GreekRoot("gram", "thing written", "epigram, telegram"),
    GreekRoot("graph", "writing", "graphic, phonograph"),
    GreekRoot("hetero", "different", "heteronym, heterogeneous"),
    GreekRoot("homo", "same", "homonym, homogenous"),
    GreekRoot("hydr", "water", "hydration, dehydrate"),
    GreekRoot("hyper", "over; above; beyond", "hyperactive, hyperbole"),
    GreekRoot("hypo", "below; beneath", "hypothermia, hypothetical"),
    GreekRoot("logy", "study of", "biology, psychology"),
    GreekRoot("meter/metr", "measure", "thermometer, perimeter"),
    GreekRoot("micro", "small", "microbe, microscope"),
    GreekRoot("mis/miso", "hate", "misanthrope, misogyny"),
    GreekRoot("mono", "one", "monologue, monotonous"),
    GreekRoot("morph", "form; shape", "morphology, morphing"),
    GreekRoot("nym", "name", "antonym, synonym"),
    GreekRoot("phil", "love", "philanthropist, philosophy"),
    GreekRoot("phobia", "fear", "claustrophobia, phobic"),
    GreekRoot("photo/phos", "light", "photograph, phosphorous"),
    GreekRoot("pseudo", "false", "pseudonym, pseudoscience"),
    GreekRoot("psycho", "soul; spirit", "psychology, psychic"),
    GreekRoot("scope", "viewing instrument", "microscope, telescope"),
    GreekRoot("techno", "art; science; skill", "technique, technological"),
    GreekRoot("tele", "far off", "television, telephone"),
    GreekRoot("therm", "heat", "thermal, thermometer")
]

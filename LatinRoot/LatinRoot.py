class LatinRoot:
    def __init__(self, root, definition, example):
        self.root = root
        self.definition = definition
        self.example = example

    def __str__(self):
        return f"{self.root}: {self.definition} ({self.example})"

root_list = [
    LatinRoot("ambi", "both", "ambiguous, ambidextrous"),
    LatinRoot("aqua", "water", "aquarium, aquamarine"),
    LatinRoot("aud", "to hear", "audience, audition"),
    LatinRoot("bene", "good", "benefactor, benevolent"),
    LatinRoot("cent", "one hundred", "century, percent"),
    LatinRoot("circum", "around", "circumference, circumstance"),
    LatinRoot("contra/counter", "against", "contradict, encounter"),
    LatinRoot("dict", "to say", "dictation, dictator"),
    LatinRoot("duc/duct", "to lead", "conduct, induce"),
    LatinRoot("fac", "to do; to make", "factory, manufacture"),
    LatinRoot("form", "shape", "conform, reform"),
    LatinRoot("fort", "strength", "fortitude, fortress"),
    LatinRoot("fract", "break", "fracture, fraction"),
    LatinRoot("ject", "throw", "projection, rejection"),
    LatinRoot("jud", "judge", "judicial, prejudice"),
    LatinRoot("mal", "bad", "malevolent, malefactor"),
    LatinRoot("mater", "mother", "maternal, maternity"),
    LatinRoot("mit", "to send", "transmit, admit"),
    LatinRoot("mort", "death", "mortal, mortician"),
    LatinRoot("multi", "many", "multimedia, multiple"),
    LatinRoot("pater", "father", "paternal, paternity"),
    LatinRoot("port", "to carry", "portable, transportation"),
    LatinRoot("rupt", "to break", "bankrupt, disruption"),
    LatinRoot("scrib/script", "to write", "inscription, prescribe"),
    LatinRoot("sect/sec", "to cut", "bisect, section"),
    LatinRoot("sent", "to feel; to send", "consent, resent"),
    LatinRoot("spect", "to look", "inspection, spectator"),
    LatinRoot("struct", "to build", "destruction, restructure"),
    LatinRoot("vid/vis", "to see", "televise, video"),
    LatinRoot("voc", "voice; to call", "vocalize, advocate")
]

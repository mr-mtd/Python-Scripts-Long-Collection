class Prefix:
    def __init__(self, prefix, definition, example):
        self.prefix = prefix
        self.definition = definition
        self.example = example

    def __str__(self):
        return f"{self.prefix}: {self.definition} ({self.example})"

prefix_list = [
    Prefix("anti-", "against", "anticlimax"),
    Prefix("de-", "opposite", "devalue"),
    Prefix("dis-", "not; opposite of", "discover"),
    Prefix("en-, em-", "cause to", "enact, empower"),
    Prefix("fore-", "before; front of", "foreshadow, forearm"),
    Prefix("in-, im-", "in", "income, impulse"),
    Prefix("in-, im-, il-, ir-", "not", "indirect, immoral, illiterate, irreverent"),
    Prefix("inter-", "between; among", "interrupt"),
    Prefix("mid-", "middle", "midfield"),
    Prefix("mis-", "wrongly", "misspell"),
    Prefix("non-", "not", "nonviolent"),
    Prefix("over-", "over; too much", "overeat"),
    Prefix("pre-", "before", "preview"),
    Prefix("re-", "again", "rewrite"),
    Prefix("semi-", "half; partly; not fully", "semifinal"),
    Prefix("sub-", "under", "subway"),
    Prefix("super-", "above; beyond", "superhuman"),
    Prefix("trans-", "across", "transmit"),
    Prefix("un-", "not; opposite of", "unusual"),
    Prefix("under-", "under; too little", "underestimate")
]

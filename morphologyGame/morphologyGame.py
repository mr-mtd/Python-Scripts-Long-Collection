import random

# Define a list of words and their meanings
words = {
    "unhappy": "not happy",
    "reheat": "heat again",
    "prepay": "pay in advance",
    "postcard": "card sent after a trip",
    "misunderstand": "understand wrongly",
    "nonstop": "without stopping",
    "disagree": "not agree",
    "incomplete": "not complete",
    "impossible": "not possible",
    "happiness": "the state of being happy",
    "movement": "the act of moving",
    "decision": "the act of deciding",
    "readable": "able to be read",
    "helpful": "full of help",
    "fearless": "without fear",
    "reddish": "somewhat red",
    "natural": "relating to nature",
    "walked": "past tense of walk",
    "talked": "past tense of talk"
}

# Define a list of prefixes and suffixes
affixes = {
    "un-": "not or opposite",
    "re-": "again or back",
    "pre-": "before",
    "post-": "after",
    "mis-": "wrong or badly",
    "non-": "not or opposite",
    "dis-": "not or opposite",
    "in-": "not or opposite",
    "im-": "not or opposite",
    "-ness": "a state or quality",
    "-ment": "an action or process",
    "-ion": "an action or state",
    "-able": "capable of being",
    "-ful": "full of",
    "-less": "without",
    "-ish": "somewhat",
    "-al": "relating to",
    "-ed": "past tense or completed action"
}

# Define a function to play the game
def play_game():
    # Choose a random word and affix
    word = random.choice(list(words.keys()))
    affix = random.choice(list(affixes.keys()))

    # Print the word and ask the user to guess its meaning or syntax
    print("What is the meaning or syntax of the "+  affix + " in " + word. + "?")
    guess = input("Enter your guess: ")

    # Check if the user's guess is correct
    if guess.lower() == words[word]:
        print("Congratulations, you guessed the meaning or syntax correctly!")
    else:
        print("Sorry, the correct meaning or syntax is '{words[word]}'.")

# Play the game
play_game()

if __name__ == '__main__':
    play_game()
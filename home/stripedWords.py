# You are given a block of text with different words. 
# These words are separated by white-spaces and punctuation marks. 
# Numbers are not considered words in this mission (a mix of letters and digits is not a word either). 
# You should count the number of words (striped words) where the vowels with consonants are alternating, that is;
# words that you count cannot have two consecutive vowels or consonants.
# The words consisting of a single letter are not striped -- do not count those.


import re

VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"

def checkio(string):
    count = 0
    for word in re.split('\W+',string):
        temp = ''
        for ch in word:
            if ch.upper() in VOWELS:
                temp += 'v'
            elif ch.upper() in CONSONANTS: 
                temp += 'c'
            else:
                temp += 'd'    
        if (not 'cc' in temp) and (not 'vv' in temp) and len(temp) > 1 and (not 'd' in temp):    
            count += 1 
    return count    

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"

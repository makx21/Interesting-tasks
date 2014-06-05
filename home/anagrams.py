# An anagram is a type of word play, the result of rearranging the letters of a word or phrase to produce 
# a new word or phrase, using all the original letters exactly once. Two words are anagrams to each other
# if we can get one from another by rearranging the letters. Anagrams are case-insensitive and don't take account 
# whitespaces. For example: "Gram Ring Mop" and "Programming" are anagrams. But "Hello" and "Ole Oh" are not. 


def verify_anagrams(p1,p2):
    return sorted([c.lower() for c in p1 if c != ' ']) == sorted([c.lower() for c in p2 if c != ' '])

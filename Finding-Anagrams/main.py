# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    if len(word) == len(anagram):
        counts = 0
        wordlist = list(word)
        for wd in wordlist:
            if anagram.__contains__(wd):
                counts += 1
        if counts == len(wordlist):
            result = True
        else:
            result = False
    else:
        result = False
    return result

print(find_anagram("hello", "check"))

print(find_anagram("below", "elbow"))
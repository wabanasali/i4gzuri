# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
import string
def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename) as f:
        contents = f.read()
        contents = contents.translate(str.maketrans('', '', string.punctuation))
    return contents


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    wordDictionary = {}
    wordList = text.split()
    for wd in wordList:
        if wd in wordDictionary.keys():
            wordDictionary[wd] += 1
        else:
            wordDictionary[wd] = 1
    return wordDictionary

#print(count_words())
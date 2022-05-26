#You will be prompted for a sentence and the number of words in the string will be counted

word_string = input('Enter a sentence of your choice: ')

#list of words
word_list = word_string.split()

#calculate number of words
number_of_words = len(word_list)

#display number of counted words
print('The string you entered has {} words'.format(number_of_words))
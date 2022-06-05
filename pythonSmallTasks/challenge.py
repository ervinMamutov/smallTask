sample_string = 'To be or not to be'
occurrences = {}
for word in sample_string.split():
    occurrences[word] = occurrences.get(word, 0) + 1
for word in occurrences:
    print('The word' , word, 'occurs', occurrences[word], \
          'times in the string')

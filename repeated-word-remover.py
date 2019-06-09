import collections

file_name = 'worldlist.txt'
final_file_name = 'new_wordlist.txt'

file = open(file_name,'r')
sentence = file.read()
words = sentence.split('\n')
word_counts = collections.Counter(words)
final_words = []
removed_words = 0
for word, count in sorted(word_counts.items()):
    if count == 1:
        final_words.append(word)
    if count > 1:
        print('"%s" = %d time%s.' % (word, count, "s"))
        removed_words = removed_words + (count - 1)
        final_words.append(word)

final_words = '\n'.join(final_words)
final_file = open(final_file_name,'w')
final_file.write(final_words)
final_file.close()

print('Total removed words:',removed_words)

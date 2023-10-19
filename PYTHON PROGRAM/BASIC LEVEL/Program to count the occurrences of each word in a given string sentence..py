from collections import Counter
def count_word_occurrences(sentence):
 words = sentence.split()
 word_count = Counter(words)
 return word_count
input_sentence = "A parallelogram is a two-dimensional geometrical shape whose sides are parallel to each other.  "
occurrences = count_word_occurrences(input_sentence)
for word, count in occurrences.items():
 print(f"'{word}' is  {count} times")

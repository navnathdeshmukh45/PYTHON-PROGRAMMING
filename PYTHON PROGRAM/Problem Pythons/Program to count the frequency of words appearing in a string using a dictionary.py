def count_word_frequency(sentence):
    word_frequency = {}
    words = sentence.split()

    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1

    return word_frequency


# Example usage
input_sentence = "A paraphrase is a restatement of the meaning of a text or passage using other words. The term itself is derived via Latin paraphrasis, xpression'. "
word_frequency = count_word_frequency(input_sentence)
print(word_frequency)

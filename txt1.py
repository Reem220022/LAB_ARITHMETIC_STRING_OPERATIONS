sentence1=" Success does not happen overnight it comes from small efforts repeated consistently over time"
sentence2="overnight"

# length of the sentence
print(len(sentence1))
# index of the first occurrence of the word
print(sentence1.index(sentence2))
# number of times the word appears
print(sentence1.count(sentence2))
# sentence in all uppercase letters
print(sentence1.upper())
# sentence in all lowercase letters
print(sentence1.lower())
# Replace the sentence2 with a new word
sentence1=sentence1.replace(sentence2, "instantly")
print(sentence1)
#last character of the sentence
print(sentence1[-1])

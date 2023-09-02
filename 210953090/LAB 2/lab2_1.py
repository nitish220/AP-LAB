sentence = input("Enter a sentence : ").split()
print("Total words are : " , len(sentence))
words = {}
for key in sentence:
    words[key] = sentence.count(key)
print("Dictionary : " , words)
total_words = 0
for key in words:
     total_words += words[key]
print("Total words are : " , total_words)
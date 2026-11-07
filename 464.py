text = input("enter a text: ")
words = text.split()

word_index = int(input("enter the word number: ")) - 1

if 0 <= word_index < len(words):
    target_word = words[word_index]
    firstletter = target_word[0]
    print(firstletter)
else:
    print("There is no word with such a number in the text.")

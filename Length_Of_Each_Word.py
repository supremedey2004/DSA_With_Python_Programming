text = input("Enter a string: ")
s = text.split(" ")
print(s)
min_len = 0
max_word = ""
for word in s:
    print(word, ":", len(word))
    if len(word) > min_len:
        min_len = len(word)
        max_word = word
print("Longest word:", max_word)
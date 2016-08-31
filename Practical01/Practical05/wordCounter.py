
string = input("Enter String: ")
word_list = string.strip().split()
longest_length = 0
word_dict = {}
for word in word_list:
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1
    length = len(word)
    if length > longest_length:
        longest_length = length
for word,count in sorted(word_dict.items()):
    print("{:{}} : {}".format(word,longest_length,count))


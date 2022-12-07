# # sentence = "Hey fellow warriors"

# # new_sentence = sentence.split(" ")
# # final_sentence = []
# # print(new_sentence)
# # for word in new_sentence:
# #     if len(word) >= 5:
# #         final_sentence.append(word[::-1])
# #     else:
# #         final_sentence.append(word)

# # final_sentence = " ".join(final_sentence)
# abcd = [
#     "a",
#     "b",
#     "c",
#     "d",
#     "e",
#     "f",
#     "g",
#     "h",
#     "i",
#     "j",
#     "l",
#     "k",
#     "m",
#     "n",
#     "o",
#     "p",
#     "q",
#     "r",
#     "s",
#     "t",
#     "u",
#     "v",
#     "w",
#     "x",
#     "y",
#     "z",
# ]

# sentence = "The quick, brown fox jumps over the lazy dog!"
# new_char = "".join(set(sentence.replace(" ", "").lower()))
# new_sentence = []

# for n in new_char:
#     if ord(n) >= 97 and ord(n) <= 122:
#         new_sentence.append(n)

# print(new_sentence)
# print(len(new_sentence))


# # list_of = [char for char in new_char]


# # print(f"splitted new char: {list_of}")

# # print(f"new_char normal: {new_char}")
# # print(abcd)
# # print(len(new_char))
# # print(len(abcd))
# # for n in range(0, len(list_of)):
# # print(f"is {abcd[n]} in list_of: {abcd[n] in list_of}")

# with open(
#     "C:\\Users\\Repik\\OneDrive - Slovenská technická univerzita v Bratislave\\Python 100 days\\Day 26\\text.txt"
# ) as p:
# print(p.read())

# LIST COMPREHENSION
numbers = [1, 2, 3]
new_numbers = [n * 2 for n in numbers]
print(numbers)
print(new_numbers)

name = "Jackob"
letters_list = [letter for letter in name]
print(letters_list)

range_list = [num * 2 for num in range(1, 5)]
print(range_list)

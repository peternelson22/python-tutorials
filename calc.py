# user = input('Enter: ')
#
# length = 0
# for q in user:
#     if q != " ":
#         length = length + 1
#
# print(length)


def common_characters(string_1, string_2) :
    for letter in string_1:
        if letter in string_2:
            print(f"Character '{letter}' is found in both the strings")


common_characters("kambok","dunbok")

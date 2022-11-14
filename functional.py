####### LAMBDA ###########
# def calc(x):
#     y = x + 10
#     return y
#
# print(calc(5))
#
# calc = lambda x: x + 10
# print(calc(5))

# calc = lambda x, y: x * y
# print(calc(5,6))

# def calc(x):
#     return lambda y: y*x
#
# z = calc(3)
# print(z(10))

# user = input('Enter a word ')
# reverse = lambda word: word.upper()[::-1]
# print(reverse(user))

# max_ = lambda x, y: x if (x>y) else y
# print(max_(30,10))

# x = [lambda num = nu: num ** 2 for nu in range(0, 5)]
# for sq in x:
#     print(sq())

######### MAP #########
# nums = (3,5,8,9,0)
# multi = tuple(map(lambda x: x*2, nums))
# print(multi)

# def nums(x):
#     y = x*2
#     return y
#
#
# z = map(nums, (3, 5, 8, 9, 0))
# print(tuple(z))

####### FILTER ########

# x = filter(lambda y: (y<=6), (2,5,3,6,7,9))
# print(list(x))

# def nums(x):
#     if x<=6:
#        return x
#
# y = filter(nums, (2,5,3,6,7,9))
# print(list(y))

### This is the solution to the palindrome task...Try and solve other
### problems yourself
### Run this and see how it works
words = ('madam', 'nelson', 'ada', 'lagos', 'asaba')
detect_palindrome = list(filter(lambda word: word == word[::-1], words))
print(detect_palindrome)

### peace and love!!!












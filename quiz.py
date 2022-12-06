print('welcome to jae\'s quiz')
play = input('do you want to play: ').lower()

if play != 'yes':
    quit()
score = 0

print('what is the capital of n igeria?')
answer = input('Ans: ' ).lower()
if answer == 'abuja':
    print('correct')
    score = score + 1
else:
    print('incorrect')

print('what is the capital of ghana?')
answer = input('Ans: ').lower()
if answer == 'accra':
    print('correct')
    score = score + 1
else:
    print('incorrect')

#print(f'you got {score} points and {score/2*100}%')
print('you got ' + str(score) + ' points')



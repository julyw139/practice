# file path
# OneDrive\Documents\GitHub\practice\py4e\c6exercise.py

# chapter 6
# exercise 1
def e1():
    string = input('Enter a word: ')
    index = len(string) - 1
    while index >= 0:
        print(string[index])
        index -= 1

# exercise 3
def count(string, letter):
    count = 0
    for char in string:
        if letter == char:
            count += 1
    print('Count:', count)
    
# string = input('Please enter a word: ')
# letter = input('Please enter the letter you wish you count: ')
# count(string, letter)

# exercise 5
str = 'X-DSPAM-Confidence:0.8475'
copos = str.find(':')
result = str[copos+1 :]
print(float(result)
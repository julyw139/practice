# 5.9
# Exercise 1
def e1():
    total = 0
    count = 0
    while True:
        line = input('Enter a number: ')
        if line == 'done':
            break
        try:
            num = int(line)
            total += num
            count += 1
        except:
            print('Invalid input')
            continue
    avg = total/count
    print(total, count, avg)

# exercise 1
def e2():
    largest = None
    smallest = None
    while True:
        line = input('Enter a number: ')
        if line == 'done':
            break
        try:
            num = int(line)
            if largest == None or num > largest:
                largest = num
            if smallest == None or num < smallest:
                smallest = num
        except:
            print('Invalid input')
    print('Min:', smallest, 'Max:', largest)

e2()
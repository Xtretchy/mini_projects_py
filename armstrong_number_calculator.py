# Armstrong number

print('Program to check for Armstrong numbers before an integer.\n')

end = int(input('Enter the integer here: '))
power = int(input('Enter highest power of armstrong number: '))
print()

for num in range (1, end+1):
    for curr_pow in range(power):
        if num == 1 or curr_pow == 1: continue
        check = 0
        num = str(num)

        for i in num:
            i = int(i)
            check += i**curr_pow
        
        num = int(num)
        
        if num == check:
            print('%d is an armstrong number of power %d.' % (num, curr_pow))
    
print('\nDone.')
input('Press Enter to exit...')

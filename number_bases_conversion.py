# Python program to convert a number between two bases

# function to convert base 10 to other bases
def conv_to_other_b(orig_num, conv_base):
    print()
    orig_num = int(orig_num)
    new_num = ''
    print('{} | {}'.format(conv_base, orig_num))

    while(orig_num > 0):
        rem = orig_num % conv_base
        if rem > 9: rem = chr(64 + rem - 9) # to take care of base 16
        new_num = str(rem) + new_num
        print('{} | {} r {}'.format(conv_base, (orig_num // conv_base), (orig_num % conv_base)))
        orig_num = (orig_num // conv_base)

    return new_num


# function to convert other bases to base 10
def conv_to_b_10(orig_num, orig_base):
    print()
    orig_num = str(orig_num)
    mult = 0
    new_num = 0

    for i in orig_num.upper()[::-1]:
        if i.isalpha(): i = (ord(i) - 55) # to take care of base 16
        new_num += (int(i) * (orig_base ** mult))
        print('{} x {} = {}'.format(i, (orig_base ** mult), (int(i) * (orig_base ** mult))))
        mult += 1

    return new_num


# the main program
orig_num = input('Enter the original number: ')
orig_base = int(input('Enter the original base: '))

conv_base = int(input('\nEnter the new base: '))

if orig_base != 10 and conv_base == 10: # conversion from other bases to base 10
    conv_num = conv_to_b_10(orig_num, orig_base)
elif orig_base == 10 and conv_base != 10: # conversion from base 10 to other bases
    conv_num = conv_to_other_b(orig_num, conv_base)
else: # conversion between any other two bases i.e convert first to base 10, then to desired base
    conv_num = conv_to_b_10(orig_num, orig_base)
    conv_num = conv_to_other_b(conv_num, conv_base)

print('\nThe converted number is {}'.format(conv_num))
print('Thus, {} in base {} == {} in base {}'.format(orig_num, orig_base, conv_num, conv_base))
input('\nPress Enter to exit...')

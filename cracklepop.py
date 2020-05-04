
'''
Write a program that prints out the numbers 1 to 100 (inclusive).
If the number is divisible by 3, print Crackle instead of the number.
If it's divisible by 5, print Pop.
If it's divisible by both 3 and 5, print CracklePop.
You can use any language.
'''


def print_crackle_pop():
    indexing_length = range(1,101)
    my_list = []

    for i in indexing_length:
        if i % 3 == 0 and i % 5 == 0:
            state = 'CracklePop'
        elif i % 3 == 0:
            state = 'Crackle'
        elif i % 5 == 0:
            state = 'Pop'
        else:
            state = i
        my_list.append(state)

    return my_list


print(print_crackle_pop())



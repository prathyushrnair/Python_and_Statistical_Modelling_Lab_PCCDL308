"""
Write a program to **print the multiplication table of a number n
"""
def time_table(number):
    print('// TIME TABLE //')
    for i in range(1,11):
        print(f'{i * number}')
time_table(8)
import random

print('This is a random password generator.')

chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()?.,0987654321'

amount_of_passwords = int(input('How many passwords do you need?'))
length_of_pass = int(input('How long should the passwords be?'))

print('\nHere you go:')

for psw in range(amount_of_passwords):
    passwords = ''
    for x in range(length_of_pass):
        passwords += random.choice(chars)
    print(passwords)
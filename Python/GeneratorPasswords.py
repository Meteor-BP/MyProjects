import random

print("Generator by MeteorBP")
while True:
    chars = list('-_wabcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')
    length = int(input('Length Password?'+ "\n"))
    random.shuffle(chars)
    pasw = ''.join([random.choice(chars) for x in range(length)])
    print('')
    print(f'Your Password: {pasw}')
    print('Press Enter to exit')
    print('')
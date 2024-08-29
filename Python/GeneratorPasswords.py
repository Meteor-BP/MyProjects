import random

print("Генератор сделан MeteorBP // Версия 2.0")
while True:
    chars = list('-_wabcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')
    length = int(input('Длина пароля:'+ "\n"))
    random.shuffle(chars)
    pasw = ''.join([random.choice(chars) for x in range(length)])
    print('')
    print(f'Ваш паоль: {pasw}')
    print('Нажмите enter чтобы выйти...')
    print('')
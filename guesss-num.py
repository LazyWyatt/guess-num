import random

r = random.randint(1, 100)
while True:
    num = input('請猜1-100之內的數字: ')
    num = int(num)
    if num == r:
        print('你猜中了')
        break
    elif num > r:
        print('猜錯了，比答案大，猜小一點，再猜一次')
    elif num < r:
        print('猜錯了，比答案小，猜大一點，再猜一次')


import random
start = input('請決定隨機數字範圍開始值:')
end = input('請決定隨機數字範圍結束值:')

start = int(start);
end = int(end);

r = random.randint(start, end)
count = 0
while True:
    count += 1
    num = input('請猜範圍內的數字: ')
    num = int(num)
    if num == r:
        print('你猜中了','這是你猜的第', count, '次')
        break
    elif num > r:
        print('猜錯了，比答案大，猜小一點，再猜一次')
    elif num < r:
        print('猜錯了，比答案小，猜大一點，再猜一次')
    print('這是你猜的第', count, '次')


from random import randint
rock = randint(4, 30)
print("камней в куче ", rock)

while rock >= 1:
    while True:
        try:
            print("первый игрок берет камни(от 1 до 3): ")
            take1 = int(input())
            if take1 >= 1 and take1 <= 3:
                rock -= take1
                print("камней в куче ", rock)
                break
            else:
                print("неверное значение")
                if rock == 1:
                    print("первый игрок победил")
                    exit()
        except:
            print("неверное значение")
    if rock == 1:
        print("первый игрок победил")
        exit()

    while True:
        try:
            print("второй игрок берет камни(от 1 до 3): ")
            take2 = int(input())
            if take2 >= 1 and take1 <= 3:
                rock -= take2
                print("камней в куче ", rock)
                break
            else:
                print("неверное значение")
                if rock == 1:
                    print("второй игрок победил")
                    exit()
        except:
            print("неверное значение")
    if rock == 1:
        print("второй игрок победил")
        exit()

    if rock < 1:
        print("оба игрока проиграли")

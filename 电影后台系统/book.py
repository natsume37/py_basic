import time

# 预定座位
class SeatBooking:
    # 打印座位
    def choice_books(self,seat):
        print('正在为你查询电影的预定状态')
        print('总共1~6排，1~8列')
        print('==============================================')
        for row in seat:
            print('  '.join(row))
            time.sleep(0.3)
        print('==============================================')

    # 预定座位
    def book_seat(self,seat):
        while True:
            row = int(input('\n你想选择第几排呢？(｡￫v￩｡) \n')) -1
            column = int(input('你想选择这一排的第几列呢？ε(*･ω･)_/ﾟ:･☆ \n')) -1
            if (row < 0 or row >6) or (column < 0 or column >8) :
                print ('客官你输入的内容好像超出我的认知范围了  (ಥ﹏ಥ) ')
                time.sleep(0.5)
                continue
            if seat[row][column] == '●' :
                print('这个座位已经被预定了欧！˃̣̣̥᷄⌓˂̣̣̥᷅ \n')
                time.sleep(0.5)
                print("客官换换个座位吧！  (❀｣╹□╹)｣*･ ")
                time.sleep(1)
            else:
                print('预定中.......')
                seat[row][column] = '●'
                time.sleep(1)
                print(f'预定成功，{row}排{column}号  祝你观影愉快！')
                break

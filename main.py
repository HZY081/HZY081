#库
import random
import math
win = 0
while True:#输入玩家人数
    player = int(input('How many players do you want?'))
    if 2 <= player <= 6:
        break
    else:
        print('invalid number')
while True:#输入筹码数
    chip = int(input('How many chip each one do you want?'))
    if 3 <= chip <= 5:
        you_chip = chip
        break
    else:
        print('invalid number')
#游戏开始
print('You\'re the first')
#输入数
def game_start():
    while True:
        number = int(input('Say a number:'))
        if player <= number <= player * 6:
            break
        else:
            print('invalid number')
    #下注
    while True:
        number_chip = int(input('How mane chip:'))
        if 1 <= number_chip <= you_chip:
            break
        else:
            print('invalid number')
def saizi():#骰子
    return random.randint(player,player * 6)
#玩家
p1_chip,p2_chip,p3_chip,p4_chip,p5_chip = 0,0,0,0,0
players_chip = [you_chip,p1_chip,p2_chip,p3_chip,p4_chip,p5_chip]
you_number,p1_number,p2_number,p3_number,p4_number,p5_number = 0,0,0,0,0,0
players_number = [you_number,p1_number,p2_number,p3_number,p4_number,p5_number]
players = ['you','p1','p2','p3','p4','p5']
you_outchip,p1_outchip,p2_outchip,p3_outchip,p4_outchip,p5_outchip = 0,0,0,0,0,0
players_outchip = [you_outchip,p1_outchip,p2_outchip,p3_outchip,p4_outchip,p5_outchip]
#人机——数字
def player_number():
    for i in range(1,player):
        players_number[i] = saizi()
#人机——筹码
def player_chipout():
    for i in range(1,player):
        if players_chip[i] >= number_chip:
            players_outchip[i] = number_chip
        elif players_chip[i] < number_chip:
            players_outchip[i] = players_chip[i]
#更新玩家数据
def p_chip():
    players_chip[0] = chip
    for i in range(1,player):
        players_chip[i] = chip
#显示战况
def now_chip():
    for i in range(0,player):
        print(players[i],'chip:',players_chip[i])
while win == 0:
    p_chip()
    now_chip()

    game_start()
    if you_chip == player * chip:
        print('You win')
        win = 1
    #一定要记得删！
    win = 1
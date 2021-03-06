#! /usr/bin/env python3

import argparse
import random
from copy import deepcopy
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

from texasholdem_Plot import ReadPlot

from texasholdem_Dealer import Card, Dealer
from texasholdem_Play import Game
from texasholdem_Player import Player
from texasholdem_Kawada import KawadaAI
from texasholdem_Shirai import ShiraiAI
from texasholdem_Takahashi import TakahashiAI
from texasholdem_Human import Human
from texasholdem_Shiraiopt import ShiraioptAI

#  create list of players #
Player1 = ShiraiAI()
Player2 = TakahashiAI()
Player3 = KawadaAI()
Player4 = Player()
Player5 = ShiraioptAI()
###########################

players_list = [Player1, Player2, Player3, Player4, Player5 ]
game = Game(players_list)
############WARNING!!!!#############
##Playのshuffleはコメントアウトしてから##
####################################

g=open("tour.txt","w")
g.close

MAX=2000
n=50
dif = int(MAX/n)

output='st3.csv'


###MAX回トーナメント###
f=open(output, "w")
f.write("num")
p=''
for i in range(len(players_list)):
    p += ", " + str(players_list[i].__class__.__name__)
p+="\n"
f.write(p)

_i = 0
while _i < MAX: 
    win_list = [0]*len(game.accounts)
    game = Game(players_list)
    label = [i.__class__.__name__ for i in players_list]
    c=0
    while game.accounts.count(0) < len(players_list)-1: #残り人数の設定
        game.play()
        c+=1
    win_list[game.accounts.index(max(game.accounts))] += 1
    ff=open("tour.txt","a")
    p=str(_i)
    ff.write(p+"\n")
    ff.close()
    for i in range(len(win_list)):
        p+=", "+str(win_list[i])
    p+="\n"
    f.write(p)
    _i += 1
f.close()
######


##以下では，トーナメント回数ごとの勝率を計算してグラフ化します．統計のための統計用プログラムです．
df = pd.read_csv(output, header=0, encoding='utf-8')
color=["red","green","blue","black","orange"]
win_list = [0]*len(game.accounts)
num=dif # initial
y=[0]*len(players_list)
delta=100
while num < MAX:
    j=0
    while j < 10 and delta+num+j < MAX:#試料数
        for i in range(len(players_list)):
            print("num,i,j",num,i,j)
            y[i]=df.iloc[num+j:num+delta+j,i+1].values.tolist()
            win_list[i]=sum(y[i])
        tot=sum(win_list)
        for i in range(len(win_list)):
            win_list[i]=win_list[i]/tot
        print("---",win_list)
        x=[num]
        for i in range(len(win_list)):
            plt.scatter(x, win_list[i], s=10, c=color[i], alpha=0.2) # label=players_list[i].__class__.__name__)
        j+=1
    num+=dif
plt.show()

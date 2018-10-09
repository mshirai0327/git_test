from texasholdem_Dealer import Card,Dealer
import random
from texasholdem_Player import Player

#カードタプルを生成して関数に渡して動作確認するためのプログラム#

player1 = Player()
player2 = Player()
player3 = Player()
player4 = Player()

players_list = [player1, player2, player3, player4]
random.shuffle(players_list)
dealer=Dealer(players_list)

score_list=[0]*9
for k in range(100000):
    print("")
    print("game=",k)
    cards=[0]*7
    suit=['S','C','H','D']

    for i in range(7):#7cards
        k=random.randrange(4)
        number=random.randrange(13)+1
        card=Card(suit[k],number)
        cards[i]=card

    (sc,rtcards)=dealer.calc_hand_score(cards)
    score_list[sc]+=1
    print("score--",sc)
    print("best--",rtcards)

print("#####################################")
print("SCORE:",score_list)
print("#####################################")

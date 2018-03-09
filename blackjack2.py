#Copyright DPZK, >95% by Tom Zhou because he typed so many '#'
################################################################################################################################################################################################################################################################################################################################################################################################
import random
print("Blackjack Game")
deck=[]
for card in range (1, 14):
    for i in range (1, 5):
        deck.append(card)
game=False

def dealcard():
    global reader
    reader+=1
    return deck[reader-1]

def cardsum(cards):
    csum=[0,0]
    for i in range (0,len(cards)):
        crd=cards[i]
        if crd>10:
            crd=10
        if crd==1:
            if csum[1]==0:
                csum[0]=csum[0]+crd
                csum[1]=csum[0]+10
            else:
                csum[0]+=1
                csum[1]+=1
        else:
            csum[0]=csum[0]+crd
            if csum[1]!=0:
                csum[1]+=crd
    if csum[1]>21:
        csum[1]=0
    return csum

def annoucecard(cards):
    sentence=""
    for c in range (0,len(cards)):
        crd=cards[c]
        if crd==13:
            sentence+=" K,"
        elif crd==12:
            sentence+=" Q,"
        elif crd==11:
            sentence+=" J,"
        elif  crd==1:
            sentence+=" A,"
        elif (crd==0)==False:
            sentence= sentence+" " + str(crd) + ","
    return sentence
def ifquit():
    print("Would you like to restart? Y/N")
    ans=input()
    global game 
    if ans!='y' and ans!='Y':
        game=True
       
def npcdecision(npc):
    npcsum=cardsum(npc)
    if npcsum[1]==0:
        if npcsum[0]>=17:
            return False
        elif npcsum[0]>=12:
            if dealer[0]>=7 or dealer[0]==1:
                return True
            else:
                return False
        else:
            return True
    else:
        if npcsum[1]>=19:
            return False
        elif npcsum[1]>=16:
            if dealer[0]>=7 or dealer[0]==1:
                return True
            else:
                return False
        else:
            return True

while game==False:
    random.shuffle(deck)
    dealer=[]
    player=[]
    npc=[]
    reader=0
    pburst=False
    dburst=False
    nburst=[]
    npcnum=int(input("How many players do you want to play with (Not counting dealer and yourself!)"))
    for i in range (1, npcnum+1):
        npc.append([i])
        for c in range(1,2):
            npc[i-1].append(dealcard())
    print(npc)
    print("Game start")
    
    for i in range (0,2):
        dealer.append(dealcard())
        player.append(dealcard())
    dsum=cardsum(dealer)
    psum=cardsum(player)
    for i in range (0, npcnum):
        print("NPC #" +str(i+1) +" has cards"+annoucecard(npc[i-1]))
        nsum=cardsum(npc[i-1])
        if nsum[1]==21:
            print("NPC #" +str(i+1)+" recieved blackjack and win")
    if dsum[1]==21:
        if psum[1]==21:
            print("Player has cards "+annoucecard(player))
            print("Dealer has cards "+annoucecard(dealer))
            if npcnum>0:
                print("You draw with the dealer")
            else:
                print("Draw, both recieved blackjack")
            ifquit()
        else:
            print("Player has cards "+annoucecard(player))
            print("Dealer has cards "+annoucecard(dealer))
            if npcnum>0:
                print("All lose, Dealer recieved blackjack")
            else:
                print("You lose, Dealer recieved blackjack")
            ifquit()
            
    if game==False:
        d1=[]
        d1.append(dealer[0])
        print("Dealer has cards "+annoucecard(d1)+"and one faced down")
        print("Player has cards "+annoucecard(player))
        pround=True
        while pround:
            print("You have cards "+annoucecard(player))
            sums=cardsum(player)
            if (sums[1]<21 and sums[1]>0) and sums[1]!=sums[0]:
                print("Your sum is "+str(sums[0])+" or "+str(sums[1]))
            else:
                print("You sum is "+str(sums[0]))
            print("Would you like to hit? Y/N")
            ans=input()
            if ans=='Y' or ans=="y":
                player.append(dealcard())
                sums=cardsum(player)
                c1=[]
                c1.append(player[len(player)-1])
                print("You draw a"+annoucecard(c1))
                if sums[0]>21:
                    print("Your sum is "+ str(sums[0]))
                    print("You burst")
                    pburst=True
                    pround=False
                elif sums[1]==21 or sums[0]==21:
                    print("You got 21")
                    pround=False
            else:
                pround=False
                
        for i in range(0,npcnum):
            nround=True
            nburst.append(False)
            sums=cardsum(npc[i])
            while nround:
                print("NPC #" +str(i+1) +" has cards"+annoucecard(npc[i]) )
                if (sums[1]<21 and sums[1]>0) and sums[1]!=sums[0]:
                    print("NPC #" +str(i+1) +"'s sum is " +str(sums[0])+" or "+str(sums[1]))
                else:
                    print("NPC #" +str(i+1) +"'s sum is " +str(sums[0]))
                if npcdecision(npc[i]):
                    print("NPC #" +str(i+1) +" hit")
                    npc[i].append(dealcard())
                    sums=cardsum(npc[i])
                    c1=[]
                    c1.append(npc[i][len(npc[i])-1])
                    print("NPC #" +str(i+1) +" draw a"+annoucecard(c1))
                    if sums[0]>21:
                        print("NPC #" +str(i+1) +" sum is "+ str(sums[0]))
                        print("NPC #" +str(i+1) +" burst")
                        nburst[i]=True
                        nround=False
                    elif sums[1]==21 or sums[0]==21:
                        print("NPC #" +str(i+1) +" got 21")
                        nround=False
                else:
                    print("NPC #" +str(i+1) +" stand")
                    nround=False
        dround=True
        while dround:
            print("Dealer have cards "+annoucecard(dealer))
            sums=cardsum(dealer)
            if sums[1]<21 and sums[1]>0 and sums[1]!=sums[0]:
                print("Dealer's sum is "+str(sums[0])+" or "+str(sums[1]))
            else:
                print("Dealer's sum is "+str(sums[0]))
            if sums[1]==17 or sums[0]<=16:
                dealer.append(dealcard())
                sums=cardsum(dealer)
                c1=[]
                c1.append(dealer[len(dealer)-1])
                print("Dealer draws a"+annoucecard(c1))
                if sums[0]>21:
                    print("Dealer's sum is "+ str(sums[0]))
                    print("Dealer burst")
                    dburst=True
                    dround=False
                elif sums[1]==21 or sums[0]==21:
                    print("Dealer got 21")
                    dround=False
            else:
                dround=False
        #Yay finally summerize start
            dsum=cardsum(dealer)
            if dsum[1]>dsum[0] and dsum[1]<=21:
                dscore=dsum[1]
            else:
                dscore=dsum[0]
        for i in range (0, npcnum):
            if dburst and nburst[i]:
                print("NPC #" +str(i+1) +" and dealer both Burst, DEALER WINS")
            elif dburst:
                print("Dealer Burst, NPC #" +str(i+1) +" WIN")
            elif pburst:
                print("NPC #" +str(i+1) +" Brust, DEALER WINS")
            else:
                nsum=cardsum(npc[i])
                if nsum[1]>nsum[0] and dsum[1]<=21:
                    nscore=psum[1]
                else:
                    nscore=psum[0]
                if nscore>dscore:
                    print("NPC #" +str(i+1) +" score more than dealer, YOU WIN")
                elif nscore<dscore:
                    print("Dealer score more than NPC #" +str(i+1) +", DEALER WINS")
                else:
                    print("NPC #" +str(i+1) +" and dealer got same score, DEALER WINS")

        if dburst and pburst:
            print("You and dealer both burst, DEALER WINS")
        elif dburst:
            print("Dealer Burst, YOU WIN")
        elif pburst:
            print("You Brust, DEALER WINS")
        else:
            psum=cardsum(player)
            if psum[1]>psum[0] and dsum[1]<=21:
                pscore=psum[1]
            else:
                pscore=psum[0]
            if pscore>dscore:
                print("You score more than dealer, YOU WIN")
            elif pscore<dscore:
                print("Dealer score more than you, DEALER WINS")
            else:
                print("You got same score with dealer, DEALER WINS")
        ifquit()

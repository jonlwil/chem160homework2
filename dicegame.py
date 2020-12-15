from random import choices
ntrials=15000
player1wins=0
p2dice=2
p1dice=3
total=0
for i in range(ntrials):
    dice=choices(range(1,7), k=p2dice)
    dice.sort(reverse=True)
    total=total+dice[0]+dice[1]
    if dice[0]==dice[1]:
        continue
    dice2=choices(range(1,7), k=p1dice)
    dice.sort(reverse=True)
    if dice[0]+dice[1]< dice2[1]+dice2[2]:
        player1wins=player1wins+1
print("Fairness ratio=",player1wins/ntrials)
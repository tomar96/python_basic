def game():
    return 5

score= game()
with open('highscore.txt') as f:
    highscore=int(f.read())
if highscore<score:
    with open('highscore.txt','w') as f:
        f.write(str(score))
elif highscore>score:
    with open('highscore.txt','w') as f:
        f.write(str(score))
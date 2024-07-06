PLAYER_1=('A','B','C','D','E','F')
PLAYER_2=('G','H','I','J','K','L')
OPPOSITE_SITE={'A': 'G', 'B': 'H', 'C': 'I', 'D': 'J', 'E': 'K','F': 'L', 'G': 'A', 'H': 'B', 'I': 'C', 'J': 'D','K': 'E', 'L': 'F'}
NEXT_SITE={'A': 'B', 'B': 'C', 'C': 'D', 'D': 'E', 'E': 'F', 'F': '1','1': 'L', 'L': 'K', 'K': 'J', 'J': 'I', 'I': 'H', 'H': 'G','G': '2', '2': 'A'}
PLACE_ALINGMENT='ABCDEF1LKJIHG2'
TOTAL_IN_SITE=4
def sample_total():
    S=TOTAL_IN_SITE
    return {'1':0,'2':0,'A':S,'B':S,'C':S,'D':S,'E':S,'F':S,'G':S}
def playermove(turn,board):
    while True:
        if turn == '1':
            print("choose from (A-G) :")
        elif turn == '2':
            print("choose from (H-N) :")
        res=input("enter here --->").upper().strip()
        if res == 'QUIT':
            print("THANKS FOR PLAYING...!")
            sys.exit()
        if (turn =='1' and res not in PLAYER_1)or(turn =='2' and res not in PLAYER_2):
            print("please pick a letter on your side of the board")
            continue
        if board.get(res)==0:
            print("please pick a non-empty pit")
            continue
        return res
def displayboard(board):
 seedAmounts = []
 for pit in 'GHIJKL21ABCDEF':
     numSeedsInThisPit = str(board[pit]).rjust(2)
     seedAmounts.append(numSeedsInThisPit)

 print("""
 +------+------+--<<<<<-Player 2----+------+------+------+
 2      |G     |H     |I     |J     |K     |L     |      1
        |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |
 S      |      |      |      |      |      |      |      S
 T  {}  +------+------+------+------+------+------+  {}  T
 O      |A     |B     |C     |D     |E     |F     |      O
 R      |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |      R
 E      |      |      |      |      |      |      |      E
 +------+------+------+-Player 1->>>>>-----+------+------+
. """.format(*seedAmounts))
def makemove(board,playerturn,place):
    seedstosow = board[place]
    board[place] = 0
    while seedstosow > 0:
        place = next_place[place]
        if (playertrun == '1' and place == '2') or (playerturn =='2'and place == '1'):
            continue
        board[place]+=1
        seedstosow -=1
    if(place == placeturn == '1')or(place == placeturn == '2'):
        return playerturn
    if playerturn == '1' and place in player_1 and board[place]==1:
        oppositeside = OPPOSITE_SITS[place]
        board['1']+=board[oppositeside]
        board[oppositeside]=0
    elif playerturn == '2' and place in player_2 and board[place]==1:
        oppositeside = OPPOSITE_SITS[PLACE]
        board['2']+=board[oppositeside]
        board[oppositeside]=0
    if playerturn == '1':
        return '2'
    elif playerturn == '2':
        return '1'
def winner_check(board):
    player_total_1=board['A']+board['B']+board['C']+board['D']+board['E']+board['F']
    player_total_2=board['G']+board['H']+board['I']+board['J']+board['K']+board['L']
    if player_total_1 == 0:
        board['2']+=player_total_2
        for place in player_2:
            board[place]=0
    elif player_total_2 == 0:
        board['1']+=player_total_1
        for place in player_1:
            board[place]==0
    else:
        return 'no winner'
    if(board['1'] > board['2']):
        return '1'
    elif(board['2'] > board['1']):
        return '2'
    else:
        return 'tie'        
def p_k():
    playerturn='1'
    gameboard=sample_total()
    player_move=0
    displayboard(gameboard)
    while True:
        displayboard(gameboard)
        player_move==playermove(playerturn,gameboard)
        playerturn=makemove(gameboard,playerturn,player_move)
        winnner=winner_check(gameboard)
        if winner == '1' or winner == '2':
            displayboard(gameboard)
            print("player "+winner+" has won")
            sys.exit()
        elif winner == 'tie':
            displayboard(gameboard)
            print("there is a tie")
            sys.exit()
p_k()            
        

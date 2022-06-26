from Def import *

#---------------VARIABLE-----------------#

#List
lett=["       A","   B","   C","   D","   E","   F","   G","   H","   I","   J ","  K ","  L ","  M ","  N ","  O ","  P ","  Q","   R","   S","   T","   U","   V","   W","   X","   Y","   Z"]
lett2=["        A","   B","   C","   D","   E","   F","   G","   H","   I","   J","   K","   L","   M","   N","   O","   P","   Q","   R","   S","   T","   U","   V","   W","   X","   Y","   Z"]#We Have lett and lett 2, which are nearly the same, just lett is for 6 and 8, and lett2 for 10 to 26 thanks to this method, we have a good presentation, without, points are shifted 
num  =["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26"] #same method here with num and num 2
num2  =[" 1"," 2"," 3"," 4"," 5"," 6"," 7"," 8"," 9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26"]
lettup=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"] 
lettlow=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"] #2 list because it must work when the player enter it's coordinate even if it's lowercase or uppercase
com = ["p","P","a","A"]
com1=["p","P"]
com2=["a","A"]

#Initialisation:
X=2
O=2
turn=0
size=0
Xscore = 2
Oscore = 2
end=0



#------------------------Beginning--------------------#
print("-------------------------------------------------  Welcome to Black&White  !  -------------------------------------------------- \n")

Player1 = input ("Hi, player 1. What's your name ? \n")
Player2 = input ("Hi, Player 2. What's your name ?\n")


while size<6 or size>26 or size%2!=0 : #security
    print("First of all, what size of the game board do you want ?\n")
    size =int(input())  
Table=[]
Table_line=[]
size2 = size*size
for i in range(0,size):
    Table_line=[]
    for j in range(0,size):
        Table_line.append(' .')
    Table.append(Table_line)
    
init(size,lett,num,Table)
Gameboard(Table,size,lett,num,lett2,num2)
resume(turn,X,O,Player1,Player2)
command=""
#Now, the game will begin, we need the while condition which allows us to stop the game.

while Continue(X,O,size,command) == True:
    print(("     Possibles commands:\n     P: place a pawn\n     A: abandon\n"))
    command = input()
    Continue(X,O,size,command)
    while Command(command,com,com1)==False:
        print("Wrong command, Try again")
        command=input()
    if command=="a" or command=="A":
        end=1
    
#-----------------------refusing invalid moves----------------------------------------------#
#-----------------------Propose (on request) the list of valid moves;-----------------------#
#-----------------------Determine the winner---------------------------------------------------#
#-----------------------Provide help on keys to use-------------------------------------------#


#-----------------------Enter the position of a pawn to be placed with its coordinates----------------#
    if end==0:
        placinglett=str(input("Where do you want to place your pawns (letter) ?\n"))
        placingnum=int(input("Where do you want to place your pawns (number) ?\n"))
        if placinglett in lettup:
            pll=lettup.index(placinglett)
        if placinglett in lettlow:
            pll=lettlow.index(placinglett)
        placingnum=placingnum-1
   
        while (movesonboard(pll,placingnum,size,Table)==False) or (invalidmoves (Table,placingnum,pll,turn,size) == False) :
            print("Wrong coordinates, try again")
            placinglett=str(input("Where do you want to place your pawns (letter) ?\n"))
            placingnum=int(input("Where do you want to place your pawns (number) ?\n"))
            if placinglett in lettup:
                pll=lettup.index(placinglett)
            if placinglett in lettlow:
                pll=lettlow.index(placinglett)
            placingnum=placingnum-1
        
        
        flip(turn,Table,placingnum,pll,size)
        placingpawns(size,pll,placingnum,Table,turn)
    
        Gameboard(Table,size,lett,num,lett2,num2)
        turn=turn+1
        score(size,Table,X,O)
        resume(turn,X,O,Player1,Player2)
    else:
        winner (O,X,Player1,Player2,command, turn,com2)


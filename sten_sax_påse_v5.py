import random
import msvcrt
import os
import time
from colors import bcolors
from funktion_v2 import rockcal 
from funktion_v2 import papercal
from funktion_v2 import scissorscal
from funktion_v2 import menu
from funktion_v2 import change

#eteblering av variabler
gamedraw = False
loss = 0
win = 0
draw = 0
game = True
gwin = False
error = False
reset = False
rock = bcolors.BLUE+" \n  _________\n  |   |  |  \__\n  /¨¨¨¨===  |  |\n /    ___/__|__|\n|    /         |\n|              |\n \____ROCK_____/"
paper = bcolors.BLUE+"    __ __ __\n   |  |  |  |__\n   |¨¨|¨¨|¨¨|  |\n__ |¨¨|¨¨|¨¨|¨¨|\n\ \|  |  |  |¨¨|\n|              |\n \____PAPER____/\n"
scissors = bcolors.BLUE+"__       __\n \  \   /  /\n  \  \ /  /\n   \  V  /__ __\n  /¨¨¨¨===  |  |\n /    ___/__|__|\n|    /         |\n \__SCISSORS___/"

menu()
pt = msvcrt.getwch().lower()

#main loop 
while game == True:

    #reset/quit
    if pt == "q":
        os.system("cls")
        exit() 

    elif pt == "m":
        reset = True
    
    #AI  
    gameuse  = random.randint(1,3)
    if gameuse == 1:
        gt = "r"
    elif gameuse == 2:
        gt = "p"
    elif gameuse == 3:
            gt = "s"
   
    #bäsämer vinnst/ förlust/ draw
    if gt == pt:
        gamedraw = True
        error = False
        draw = draw + 1

    elif  pt == "r":
        gwin, loss, win, error, pt = rockcal(pt,gt,loss,win,error)
        
    elif pt == "p":
        gwin, loss, win, error = papercal(gt,loss,win,error)

    elif pt == "s":
        gwin , loss, win, error = scissorscal(gt,loss,win,error)
    
    #ser till att inputen är korect 
    elif pt != "p" or "r" or "s" or "m":
        error = True

    #ändrar från bockstav till händer
    pt,gt = change(pt,gt,paper,scissors,rock)

    menu()

    #skriver utt ressultat 
    if reset == True:
        loss = 0
        win = 0
        draw = 0
        print(bcolors.GREEN+"Game reset")
        time.sleep(1)
        menu()
        reset = False
    
    elif error == True:
        print(bcolors.RED+"give a valid input")
        time.sleep(1)
        menu()

    elif error == False:
        print(bcolors.BOLD+bcolors.DEFAULT+"game:\n",bcolors.BLUE+ gt)
        print(bcolors.BOLD+bcolors.DEFAULT+"player:\n",bcolors.BLUE+ pt)

        if gamedraw == False:
            if gwin == True:
                print(bcolors.BOLD+bcolors.GREEN+"\ndu van")
            elif gwin == False:
                print(bcolors.BOLD+bcolors.YELLOW+"\ndu förlorade")
        elif gamedraw == True:
            print(bcolors.DEFAULT+bcolors.UNDERLINE+"\ndraw")
            gamedraw = False

        print(bcolors.BOLD+bcolors.DEFAULT+"played", int(win) + int(loss) + int(draw),"/wins",int(win),"/losses", int(loss), "/draws", int(draw)  )

    pt = msvcrt.getwch().lower()
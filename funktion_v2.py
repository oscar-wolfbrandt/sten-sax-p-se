import os
from colors import bcolors

#om spelare väljer sten
def rockcal(p,x,y,z,q):
    p = "  _________\n  |   |  |  \__\n  /¨¨¨¨===  |  |\n /    ___/__|__|\n|    /         |\n \____ROCK_____/"
    if x == "p":
        loss = y + 1
        win = z
        q = False
        gwin = False
        return gwin ,loss, win ,q, p
    elif x == "s":
        win = z + 1
        loss = y
        q = False
        gwin = True 
        return gwin,loss,win, q, p
    
#om spelare väljer paper
def papercal(x,y,z,q):
    if x == "s":
        loss = y + 1
        win = z 
        gwin = False
        q = False
        return gwin, loss ,win,q
    elif x ==  "r":
        win = z +1
        loss = y
        q = False
        gwin = True
    return gwin, loss ,win,q

# om spleare väljer sax
def scissorscal(x,y,z,q):
    if x == "r":
        loss = y + 1
        win = z
        q = False
        gwin = False
        return gwin,loss,win,q
    elif x == "p":
        win = z + 1 
        loss = y
        q = False
        gwin = True  
        return gwin,loss,win,q
    
# visar meny 
def menu():
    os.system("cls")
    print(bcolors.CYAN+"--------------------------------------------------------------------------\n\n                               R o c k\n                              P a p e r\n                             S c i s s o r s\n\n================     By : Oscar schmerer wolfbrandt   ====================\n--------------------------------------------------------------------------\nq = quit/m = restet/ r = rock/ p = paper/ s = scissors")

#ändrar till händer
def change(pt,gt,paper,scissors,rock):
    if gt == "p":
        gt = paper
    elif gt == "r":
        gt = rock
    elif gt == "s":
        gt = scissors

    if pt == "p":
        pt = paper
    if pt == "r":
        pt = rock
    if pt == "s":
        pt = scissors
    return pt,gt

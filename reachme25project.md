PYTHON PROJECT USING TKINTER MODULE:

Reach Me 25 is a two-player game where players roll dice to advance on a grid. The first player to reach position 25 wins the game. There are snakes on the board that will send the players back to earlier positions if they land on them.
-----------------   
|| How to Play ||
-----------------
Install Python and Tkinter: Ensure that you have Python and Tkinter installed on your system. You can install Tkinter using the following command:

bash
Copy code
sudo apt-get install python3-tk
Run the Program: Open a terminal or command prompt and navigate to the directory where the game code is saved. Run the game by executing:

bash
Copy code
python your_game_file.py

--------------------
|| Game Interface ||: The game window will open, displaying the game board, player positions, dice values, and control buttons.
--------------------

Player 1's Turn:

Click the "dice for p1" button to roll the dice for Player 1.
The rolled value (1, 2, or 3) will be displayed in the "DICE VALUE" section.
Player 1's position will be updated on the board, and the new position will be displayed below the dice value section.
Player 2's Turn:

Click the "dice for p2" button to roll the dice for Player 2.
The rolled value (1, 2, or 3) will be displayed in the "DICE VALUE" section.
Player 2's position will be updated on the board, and the new position will be displayed below the dice value section.
Snakes: If a player's position lands on a snake, the player will be sent back to a designated earlier position:

Position 7 sends the player back to position 3.
Position 14 sends the player back to position 10.
Position 21 sends the player back to position 17.
Winning the Game: The first player to reach position 25 wins the game. A winning message will be displayed on the board.

Restarting the Game: Click the "restart" button to reset the game and start from the beginning.
Game Code: 
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||REACHME25|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from tkinter import *
import random
global m1,n1,p1,p2,n2,m2,po1,po2,dr,l
l=[" .  \n  "," .  \n .",".  .\n ."]
po2=0
po1=0
n1=0
m1=0
p1=-1
n2=0
m2=0
p2=-1
window= Tk()
window.title("reach me 25")
dr=Label(window,font="gortesque 35",text=" . \n .",padx=30,bg="black",fg="white")
dr.grid(row=0,column=8,columnspan=5)
global lp1,lp2
lp1=Label(window,font="Times 24",text="p1",padx=30,pady=10,borderwidth=10,bg="red",fg="white")
lp1.grid(row=1,column=8)
lp2=Label(window,font="Times 24",text="p2",padx=30,pady=10,borderwidth=10,bg="green",fg="black")
lp2.grid(row=2,column=8)
def restart():
    global m1,n1,p1,p2,n2,m2,po1,po2
    po2=0
    po1=0
    n1=0
    m1=0
    p1=-1
    n2=0
    m2=0
    p2=-1
    global lp1,lp2
    lp1.destroy()
    lp2.destroy()
    e.delete(0,len(e.get()))
    e1.delete(0,len(e1.get()))
    e2.delete(0,len(e2.get()))
def click_button1():
    
    global lp1,n1,m1,p1,po1,dr
    t=p1
    d=0
    n1=random.choice([1,2,3])
    dr.destroy()
    dr=Label(window,font="gortesque 35",text=l[n1-1],padx=30,bg="black",fg="white")
    dr.grid(row=0,column=8,columnspan=5)
    p1=p1+n1
    e.delete(0,len(e.get()))
    e.insert(0,(str(n1)))
    if p1>=5:
        m1=m1+p1//5
        p1=p1%5
    if (m1==1 and p1==1) or (m1==2 and p1==3) or (m1==4 and p1==0) : 
        m1=m1-1 
        d=4
        p1=p1+1
    if m1==4 and p1==4:
        lp1.destroy()
        lp1=Label(window,font="Times 24",text="PLAYER 1 \n WON",padx=100,pady=100,borderwidth=10,bg="red",fg="white")
        lp1.grid(row=1,column=1,columnspan=3,rowspan=3)
    elif m1>=5:
        d=d+n1
        m1=m1-1
        p1=t
    else:
        lp1.destroy()
        lp1=Label(window,font="Times 24",text="p1",padx=30,pady=10,borderwidth=10,bg="red",fg="white")
        lp1.grid(row=m1,column=p1)
    po1+=n1-d
    e1.delete(0,len(e1.get()))
    e1.insert(0,str(po1))
    
def click_button2():
    global lp2,n2,m2,p2,po2,l,dr
    t=p2
    d=0
    n2=random.choice([1,2,3])
    dr.destroy()
    dr=Label(window,font="gortesque 35",text=l[n2-1],padx=30,bg="black",fg="white")
    dr.grid(row=0,column=8,columnspan=5)
    e.delete(0,len(e.get()))
    e.insert(0,(str(n2)))
    p2=p2+n2
    if p2>=5:
        m2=m2+p2//5
        p2=p2%5
    if (m2==1 and p2==1) or (m2==2 and p2==3) or (m2==4 and p2==0) : 
        m2=m2-1 
        p2=p2+1
        d=4
        
    if m2==4 and p2==4:
        lp2.destroy()
        lp2=Label(window,font="Times 24",text="PLAYER 2 \n WON",padx=100,pady=100,borderwidth=10,bg="green",fg="white")
        lp2.grid(row=1,column=1,columnspan=3,rowspan=3)
    elif m2>4:
        p2=t
        m2=m2-1
        d=d+n2
    else:
        lp2.destroy()
        lp2=Label(window,font="Times 24",text="p2",padx=30,pady=10,borderwidth=10,bg="green",fg="white")
        lp2.grid(row=m2,column=p2)
    po2+=n2-d
    e2.delete(0,len(e2.get()))
    e2.insert(0,str(po2))
     
l1=Label(window,font="Times 24",text="01",padx=50,pady=30,borderwidth=10,bg="blue",fg="white")
l1.grid(row=0,column=0)

l2=Label(window,font="Times 24",text="02",padx=50,pady=30,borderwidth=10,bg="blue",fg="white")
l2.grid(row=0,column=1)

l3=Label(window,font="Times 24",text="03",padx=50,pady=30,borderwidth=10,bg="blue",fg="white")
l3.grid(row=0,column=2)

l4=Label(window,font="Times 24",text="04",padx=50,pady=30,borderwidth=10,bg="blue",fg="white")
l4.grid(row=0,column=3)

l5=Label(window,font="Times 24",text="05",padx=50,pady=30,borderwidth=10,bg="blue",fg="white")
l5.grid(row=0,column=4)

l6=Label(window,font="Times 24",text="06",padx=50,pady=30,borderwidth=10,bg="blue",fg="white")
l6.grid(row=1,column=0)

l7=Label(window,font="Times 12",text="down\nto 03",padx=49,pady=29,borderwidth=10,bg="blue",fg="white")
l7.grid(row=1,column=1)

l8=Label(window,font="Times 24",text="08",padx=50,pady=30,borderwidth=10,bg="blue",fg="white")
l8.grid(row=1,column=2)

l9=Label(window,font="Times 24",text="09",padx=50,pady=30,borderwidth=10,bg="blue",fg="white")
l9.grid(row=1,column=3)

l10=Label(window,font="Times 24",text="10",padx=50,pady=30,borderwidth=10,bg="blue",fg="white")
l10.grid(row=1,column=4)

l11=Label(window,font="Times 24",text="11",padx=50,pady=30,borderwidth=10,bg="blue",fg="white")
l11.grid(row=2,column=0)

l12=Label(window,font="Times 24",text="12",padx=50,pady=30,borderwidth=10,bg="blue",fg="white")
l12.grid(row=2,column=1)

l13=Label(window,font="Times 24",text="13",padx=50,pady=30,borderwidth=10,bg="blue",fg="white")
l13.grid(row=2,column=2)

l14=Label(window,font="Times 12",text="down\nto 10",padx=49,pady=29,borderwidth=10,bg="blue",fg="white")
l14.grid(row=2,column=3)

l15=Label(window,font="Times 24",text="15",padx=50,pady=30,borderwidth=10,bg="blue",fg="white")
l15.grid(row=2,column=4)

l16=Label(window,font="Times 24",text="16",padx=50,pady=30,borderwidth=10,bg="blue",fg="white")
l16.grid(row=3,column=0)

l17=Label(window,font="Times 24",text="17",padx=50,pady=30,borderwidth=10,bg="blue",fg="white")
l17.grid(row=3,column=1)

l18=Label(window,font="Times 24",text="18",padx=50,pady=30,borderwidth=10,bg="blue",fg="white")
l18.grid(row=3,column=2)

l19=Label(window,font="Times 24",text="19",padx=50,pady=30,borderwidth=10,bg="blue",fg="white")
l19.grid(row=3,column=3)

l20=Label(window,font="Times 24",text="20",padx=50,pady=30,borderwidth=10,bg="blue",fg="white")
l20.grid(row=3,column=4)

l21=Label(window,font="Times 12",text="down\nto 17",padx=49,pady=29,borderwidth=10,bg="blue",fg="white")
l21.grid(row=4,column=0)

l22=Label(window,font="Times 24",text='22',padx=50,pady=30,borderwidth=10,bg="blue",fg="white")
l22.grid(row=4,column=1)

l23=Label(window,font="Times 24",text="23",padx=50,pady=30,borderwidth=10,bg="blue",fg="white")
l23.grid(row=4,column=2)

l24=Label(window,font="Times 24",text="24",padx=50,pady=30,borderwidth=10,bg="blue",fg="white")
l24.grid(row=4,column=3)

l25=Label(window,font="Times 24",text="25",padx=50,pady=30,borderwidth=10,bg="blue",fg="white")
l25.grid(row=4,column=4)

b1=Button(window,font="Times 24",text="dice\nfor\np1",padx=0,pady=20,command=lambda: click_button1(),borderwidth=10,bg="orange",fg="black")
b1.grid(row=5,column=0)
b1=Button(window,font="Times 24",text="dice\nfor\np2",padx=0,pady=20,command=lambda: click_button2(),borderwidth=10,bg="orange",fg="black")
b1.grid(row=5,column=4)
lll=Label(window,font="Times 24",text="reach 25 to win",padx=30,pady=10,borderwidth=10,bg="white",fg="black")
lll.grid(row=5,column=1,columnspan=3)
e=Entry(window,font="Times 27",fg='black',bg='yellow')
e.grid(row=0,column=7)
ldv=Label(window,font="Times 24",text="DICE VALUE  : ",pady=10,borderwidth=10,bg="yellow",fg="black")
ldv.grid(row=0,column=5)
e1=Entry(window,font="Times 27",fg='black',bg='yellow')
e1.grid(row=1,column=7)
e2=Entry(window,font="Times 27",fg='black',bg='yellow')
e2.grid(row=2,column=7)
lPO2=Label(window,font="Times 24",text="PLAYRE 2 AT : ",pady=10,borderwidth=10,bg="yellow",fg="black")
lPO2.grid(row=2,column=5)
lPO1=Label(window,font="Times 24",text="PLAYRE 1 AT : ",pady=10,borderwidth=10,bg="yellow",fg="black")
lPO1.grid(row=1,column=5)
reset=Button(window,font="Times 24",text="restart",padx=0,pady=20,command=lambda: restart(),borderwidth=10,bg="orange",fg="black")
reset.grid(row=5,column=8)

window.mainloop()
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

output:
![image](https://github.com/user-attachments/assets/0ea0e916-b52a-4362-b3f9-9a2a393ab66a)

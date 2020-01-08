from tkinter import *
import tkinter.messagebox as tkmb
import random

#Window settings
WINDOW_H = "800"

#Box settings
BOX_H = 100
LINE_COLOR = "grey"
BOX = ['' for i in range(8) for j in range(8)]
MINES = [[-1,-1] for i in range(10)]

#Box states
MINE = 'X';
EMPTY = 0;
OPEN = 1
CLOSED = 0

class Box():
    def __init__(self,canvas=None,state=EMPTY,xcord=-1,ycord=-1):
        self.state = state
        self.xcord = xcord
        self.ycord = ycord
        self.cond = CLOSED
        self.canvas = canvas
        self.label = Label(self.canvas,text=str(self.state))
        self.label.config(font=("Courier",40))
        self.label.pack()
        self.canvas.create_window(xcord,ycord,window=self.label)
        
    def Display(self):
        if(self.label.cget("text")==MINE ):
            self.label.config(fg="red")
            self.label['text'] = MINE
        elif(self.cond!=OPEN):
            self.label['text'] = ""
        else:
            self.label['text'] = str(self.state)
        self.label.pack()
        self.canvas.create_window(self.xcord,self.ycord,window=self.label)

class Mines:
    def __init__(self,master):
        self.master = master
        self.flag = 10
        self.canvas = Canvas(self.master,width=WINDOW_H,height=WINDOW_H)
        self.Main_page()
        self.canvas.bind("<Button-1>",self.Play)
        self.count = 64
        self.canvas.bind("<Button-2>",self.Mark_Flag)
        self.canvas.bind("<Button-3>",self.Unmark_Flag)

    def Main_page(self):
        self.New_Game()
        self.Place_Mines()
        self.Box_Assign()

    def New_Game(self):
        self.canvas.delete("all")
        self.count = 64
        self.flag = 10
        self.boxes=[[Box(canvas=self.canvas) for i in range(8)]for j in range(8)]

        #Creating vertical lines
        for i in range(1,8):
            self.canvas.create_line(BOX_H*i,0,BOX_H*i,WINDOW_H,fill=LINE_COLOR)

        #Creating horizontal lines
        for i in range(1,8):
            self.canvas.create_line(0,BOX_H*i,WINDOW_H,BOX_H*i,fill=LINE_COLOR)

        y=0
        for i in range(8):
            x = 0
            for j in range(8):
                self.boxes[i][j].canvas = self.canvas
                self.boxes[i][j].xcord = x+50
                self.boxes[i][j].ycord = y+50
                self.boxes[i][j].cond = CLOSED
                self.boxes[i][j].Display()
                x+=BOX_H
            y+=BOX_H

        self.canvas.pack()

    def Place_Mines(self):
        i = 10
        while(i):
            x = random.randint(0,7)
            y = random.randint(0,7)
            if self.boxes[x][y].state==EMPTY:
                self.boxes[x][y].state=MINE
                i-=1

    def Box_Assign(self):
        n = 7
        for i in range(8):
            for j in range(8):
                if self.boxes[i][j].state==MINE:
                    self.boxes[i][j].Display()
                    continue
                count = 0
                if (i>0):
                    count += 1 if(self.boxes[i-1][j].state==MINE) else 0
                    count += 1 if(j>0 and self.boxes[i-1][j-1].state==MINE) else 0
                    count += 1 if(j<n and self.boxes[i-1][j+1].state==MINE) else 0
                if(i<n):
                    count += 1 if(self.boxes[i+1][j].state==MINE) else 0
                    count += 1 if(j>0 and self.boxes[i+1][j-1].state==MINE) else 0
                    count += 1 if(j<n and self.boxes[i+1][j+1].state==MINE) else 0
                count += 1 if(j>0 and self.boxes[i][j-1].state==MINE) else 0 
                count += 1 if(j<n and self.boxes[i][j+1].state==MINE) else 0
                self.boxes[i][j].state = count
                self.boxes[i][j].label.text = count
                self.boxes[i][j].Display()
    def Mark_Flag(self,event):
        print("for flag: x:",event.x," y:",event.y)
        x = self.Coordinate(event.x)
        y = self.Coordinate(event.y)
        if(self.boxes[y][x].cond==OPEN):
            tkmb.showinfo("Attention!!","This box is already flagged")
            return
        if(self.flag<=0):
            tkmb.showinfo("Attention!!","Max number of flags allowed is 10")
            return
        self.count-=1
        if(self.count==0):
            self.Game_Over("W")
        self.boxes[y][x].label['text']=MINE
        self.boxes[y][x].cond = OPEN
        self.boxes[y][x].Display()
        self.flag-=1
        self.Update_Status()
    
    def Unmark_Flag(self,event):
        x=self.Coordinate(event.x)
        y=self.Coordinate(event.y)
        if(self.boxes[y][x].cond==CLOSED):
            tkmb.showinfo("Attention !!","The Box is already unflagged")
            return
        if(self.flag>=10):
            tkmb.showinfo("Attention!!","Min number of flags - 0")
            return
        self.count += 1
        self.boxes[y][x].label['text'] = ""
        self.boxes[y][x].cond = CLOSED
        self.boxes[y][x].Display()
        self.flag+=1
        self.Update_Status()
        
    def Update_Status(self):
        pass

    def Play(self,event):
        x = self.Coordinate(event.x)
        y = self.Coordinate(event.y)
        self.boxes[y][x].label["text"] = ""
        if(self.boxes[y][x].state==MINE):
            self.Game_Over('L')
        self.Dfs(x,y)
            
    def Dfs(self,x,y):
        if(x<0 or y<0 or x>7 or y>7 or self.boxes[y][x].cond==OPEN or self.boxes[y][x].state=='M'):
            return
        self.boxes[y][x].cond = OPEN
        self.count -= 1
        if(self.count==0):
            self.Game_Over("W")
        print("box:",self.boxes[y][x].state," x:",x," y:",y)
        if(self.boxes[y][x].state!=0):
            self.boxes[y][x].Display()
            return
        self.Dfs(x-1,y-1)
        self.Dfs(x,y-1)
        self.Dfs(x-1,y)
        self.Dfs(x-1,y+1)
        self.Dfs(x,y+1)
        self.Dfs(x+1,y+1)
        self.Dfs(x+1,y-1)
        self.Dfs(x+1,y)
        self.boxes[y][x].Display()

    def Game_Over(self,res):
        if(res=='L'):
            answer = tkmb.askquestion(":(","You Lost !! Want to play again ?")
        else:
            answer = tkmb.askquestion(":)","You Won !! Want to play again ?")
        if answer == 'yes':
            self.Main_page()
            self.Main_page()
        else:
            self.master.destroy()

    def Coordinate(self,x):
        if x>=int(WINDOW_H):
            x = int(WINDOW_H)-1
        return x//BOX_H

def mines_main():
    root = Tk()
    mines= Mines(root)
    root.mainloop()

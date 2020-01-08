from tkinter import *
from tictoe import *
from mines import *
WINDOW_SIZE=600

class Menu(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.canvas = Canvas(
            height=600, width=600,
            bg='white')

        self.canvas.pack()
        self.bind('<x>', self.destroy)
        self.canvas.bind('<Button-1>', self.tic)
        self.canvas.bind('<Button-3>', self.mine)
        self.title_screen()
        
    def title_screen(self):
        # placeholder title screen
            self.canvas.delete('all') #just in case 
    
            self.canvas.create_rectangle(
                0, 0,
                WINDOW_SIZE, WINDOW_SIZE,
                fill='light grey',
                outline='')
            
            self.canvas.create_rectangle(
                int(WINDOW_SIZE/10), int(WINDOW_SIZE/10),
                int(WINDOW_SIZE*9/10), int(WINDOW_SIZE*9/10),
                width=int(WINDOW_SIZE/15),
                outline='violet red')
            self.canvas.create_text(
                WINDOW_SIZE/2,
                WINDOW_SIZE/1.8,
                text='Tic Tac Toe', fill='white',
                font=('Franklin Gothic', int(-WINDOW_SIZE/12), 'bold'))
    
            self.canvas.create_text(
                int(WINDOW_SIZE/2),
                int(WINDOW_SIZE/2),
                text='Left Click for', fill='white',
                font=('Franklin Gothic', int(-WINDOW_SIZE/25)))
            
            self.canvas.create_text(
                WINDOW_SIZE/2,
                WINDOW_SIZE/3,
                text='Minesweeper', fill='white',
                font=('Franklin Gothic', int(-WINDOW_SIZE/12), 'bold'))
    
            self.canvas.create_text(
                int(WINDOW_SIZE/2),
                int(WINDOW_SIZE/3.5),
                text='Right Click for', fill='white',
                font=('Franklin Gothic', int(-WINDOW_SIZE/25)))
            
    def tic(self, event):
        self.destroy()
        main()
    def mine(self, event):
        self.destroy()
        mines_main()
            
def main_menu():
    root=Menu()
    #root.resizable(0,0)
    root.mainloop()    

main_menu()

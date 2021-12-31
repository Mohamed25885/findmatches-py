from tkinter import *
from constants import setLevel, setScore


menu=Tk()
menu.geometry("1050x550+225+150")
menu.title("Matching Game")
menu.config(background="#102025")
def dele():
    menu.destroy()
def open_game(l):
    menu.destroy()
    setLevel(l)
    import findMatches
def score():
    setScore(4)
    menu.destroy()
    import scoreMenu
label1=Label(menu,text="Welcome to EA sports, It's now in the game!",bg='#102020',font=("Times bold",20),height=3,pady=45,padx=45,activeforeground = '#12005e',
            activebackground = "yellow",fg='white')
label1.pack(side='top')
B0 = Button(menu, text = "Start new game (Very EASY)",command=lambda: open_game(2),
                activeforeground = 'white',
                activebackground = "#6746c3", bg = "#12005e",
                fg = "white", width = 50, font = 'summer',bd='5')
B0.place(x=400,y=250)
B1 = Button(menu, text = "Start new game (EASY)",command=lambda: open_game(4),
                activeforeground = 'white',
                activebackground = "#6746c3", bg = "#12005e",
                fg = "white", width = 50, font = 'summer',bd='5')
B1.place(x=400,y=250)
B9 = Button(menu, text = "Start new game (Medium)",command=lambda: open_game(6),
                activeforeground = 'white',
                activebackground = "#6746c3", bg = "#12005e",
                fg = "white", width = 50, font = 'summer',bd='5')
B9.place(x=243,y=230)
B4 = Button(menu, text = "Start new game (HARD)",command=lambda: open_game(8),
                activeforeground = 'white',
                activebackground = "#6746c3", bg = "#12005e",
                fg = "white", width = 50, font = 'summer',bd='5')
B4.place(y=210)
B2 = Button(menu, text = "Score board",command=lambda:score(), activeforeground = 'white',
                activebackground = "#6746c3", bg = "#12005e", fg = "white",
                width = 50, font = 'summer', bd = 5)
B2.place(y=190)
B3 = Button(menu, text = "Exit", command = menu.quit, activeforeground = 'white',
                activebackground = "#6746c3", bg = "#12005e", fg = "white",
                width = 50, font = 'summer', bd = 5)
B3.place(y=240)
B0.pack(side = 'top')
B1.pack(side = 'top')
B9.pack(side = 'top')
B4.pack(side = 'top')
B2.pack(side = 'top')
B3.pack(side = 'top')
menu.mainloop()

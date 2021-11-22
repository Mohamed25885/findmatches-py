from tkinter import*   #call all libraries for tkinter
import random
from PIL import ImageTk, Image

game=Tk()
game.title("Matching-Game!")
game.geometry("1000x500")

my_img1=ImageTk.PhotoImage(Image.open("C:\ziad\python\image/monkey.jpg"))
my_img2=ImageTk.PhotoImage(Image.open("C:\ziad\python\image/ballon.png"))
my_img3=ImageTk.PhotoImage(Image.open("C:\ziad\python\image/ice.png"))
my_img4=ImageTk.PhotoImage(Image.open("C:\ziad\python\image/cangro.png"))
my_img5=ImageTk.PhotoImage(Image.open("C:\ziad\python\image/flower.png"))
my_img6=ImageTk.PhotoImage(Image.open("C:\ziad\python\image/peer.png"))


matches=[my_img1,my_img1,my_img2,my_img2,my_img3,my_img3,my_img4,my_img4,my_img5,my_img5,my_img6,my_img6]


random.shuffle(matches)
my_frame = Frame(game)
my_frame.pack(pady=10)

count=0
answer_list=[]
answer_dict={}
#function to click
def button_click(b,num):
    global count,answer_list,answer_dict
    if b["text"]==' 'and count<2:
        b["image"]=matches[num]
    
def return_menu():
    game.destroy()
    import menu

b0=Button(my_frame,text=' ',font=("Helvetica",20),width=6,height=3,command=lambda:button_click(b0,0))
b1=Button(my_frame,text=' ',font=("Helvetica",20),width=6,height=3,command=lambda:button_click(b1,1))
b2=Button(my_frame,text=' ',font=("Helvetica",20),width=6,height=3,command=lambda:button_click(b2,2))
b3=Button(my_frame,text=' ',font=("Helvetica",20),width=6,height=3,command=lambda:button_click(b3,3))
b4=Button(my_frame,text=' ',font=("Helvetica",20),width=6,height=3,command=lambda:button_click(b4,4))
b5=Button(my_frame,text=' ',font=("Helvetica",20),width=6,height=3,command=lambda:button_click(b5,5))
b6=Button(my_frame,text=' ',font=("Helvetica",20),width=6,height=3,command=lambda:button_click(b6,6))
b7=Button(my_frame,text=' ',font=("Helvetica",20),width=6,height=3,command=lambda:button_click(b7,7))
b8=Button(my_frame,text=' ',font=("Helvetica",20),width=6,height=3,command=lambda:button_click(b8,8))
b9=Button(my_frame,text=' ',font=("Helvetica",20),width=6,height=3,command=lambda:button_click(b9,9))
b10=Button(my_frame,text=' ',font=("Helvetica",20),width=6,height=3,command=lambda:button_click(b10,10))
b11=Button(my_frame,text=' ',font=("Helvetica",20),width=6,height=3,command=lambda:button_click(b11,11))
##############

button_return=Button(game,text='Menu',font=("Helvetica",20),width=15,height=1,command=return_menu,bg="gray",borderwidth=0)
button_return.pack()
#Grid
#row one
b0.grid(row=0,column=0)
b1.grid(row=0,column=1)
b2.grid(row=0,column=2)
b3.grid(row=0,column=3)

#row two

b4.grid(row=1,column=0)
b5.grid(row=1,column=1)
b6.grid(row=1,column=2)
b7.grid(row=1,column=3)

#row three

b8.grid(row=2,column=0)
b9.grid(row=2,column=1)
b10.grid(row=2,column=2)
b11.grid(row=2,column=3)

game.mainloop()
from tkinter import *
from Score import Score
from tkinter import ttk
from constants import  getScore, setScore
import os
levels  = {"Easy": 4, "Medium": 6, "Hard": 8}
choice = {4:0, 6:1, 8:2}
results = Score.getLevel(getScore())
root = Tk()

root.geometry("400x500")

mainFrame = Frame(root)
mainFrame.pack(fill = BOTH, expand=1)

style= ttk.Style()
style.theme_use('clam')
style.configure("TCombobox", fieldbackground= "orange", background= "white")

def retrun2menu():
    root.destroy()
    os.system("python ./menu.py")

def onChange(*args):
    setScore(levels[levelchoosen.get()])
    root.destroy()
    os.system("python ./scoreMenu.py")
    
    

n=StringVar()
#n.trace("w", onChange)
chooselabel=Label(mainFrame,text="choose the level you want?",fg="gray",bg="black").pack()
levelchoosen=ttk.Combobox(mainFrame,width=10,textvar=n)
levelchoosen.bind("<<ComboboxSelected>>", onChange)
levelchoosen.pack()
levelchoosen["values"]=[i for i in levels.keys()]
levelchoosen.current(choice[getScore()])

canvas = Canvas(mainFrame)
canvas.pack(side=LEFT, fill=BOTH, expand=1)

scrollbar = Scrollbar(mainFrame, orient=VERTICAL, command=canvas.yview)
scrollbar.pack(side = RIGHT, fill=Y)

canvas.configure(yscrollcommand=scrollbar.set)

canvas.bind('<Configure>', lambda event: 
    canvas.configure(scrollregion= canvas.bbox(ALL) ))

frame = Frame(canvas)

canvas.create_window((0,0), window=frame, anchor=NW)

texts = [StringVar(frame,"\n".join([str(i[0]).capitalize()+": "+str(i[1]) for i in result.items()]))
         for result in results
         ]

labels = [Label(frame, width=50, height=5, background="red", textvariable=text)
          for text in texts]

for i in range(len(labels)):
    labels[i].grid(row=i, pady=5, padx=5)
    
    
my_menu = Menu(root)
root.config(menu=my_menu)

#create an option dropdown menu
option_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=option_menu)
my_menu.add_separator()
my_menu.add_command(label="Menu",command=retrun2menu)
my_menu.add_command(label="Exit game", command=root.destroy)


root.mainloop()


#print()



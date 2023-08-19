from tkinter import *

foreground = "red4"
foreground_2 = "red4"
Background = "gray8"
Background_2 = "red2"
Background_3 = "red2"
text_1 = "white"
text_2 = "white"
text_3 = "white"
activeBG = "red"
BGAlert = "gray8"
AlertText = "red"


root = Tk()
root.configure(background='black')
root.title("Order Tracker")
# root.geometry('2080x730+0+0')
root.geometry('2080x730')


# Define a function to display the message
def key_press(e):
   key = e.char
   print(key, 'is pressed')
   label.config(text=key)
   label.place(x=100, y=100)
   
def key_pressU(e):
   key = e.char
   print(key, 'is pressed')
   label.config(text='Up')
   label.place(x=100, y=100)
   
def key_pressD(e):
   key = e.char
   print(key, 'is pressed')
   label.config(text='Down')
   label.place(x=100, y=100)
   
def key_pressL(e):
   key = e.char
   print(key, 'is pressed')
   label.config(text='Left')
   label.place(x=100, y=100)
   
def key_pressR(e):
       #todo keysym to identifiy key press
   key = e.keysym
   print(key, 'is pressed')
   label.config(text='Right')
   label.place(x=100, y=100)
   
def key_pressE(e):
   key = e.char
   print(key, 'is pressed')
   label.config(text='Enter')
   label.place(x=100, y=100)

def key_release(e):
   Label.config(text="Press any Key...")
   label.place(x=100, y=100)
# Create a label widget to add some text



root.bind('<KeyPress>',key_press)
root.bind('<Up>',key_pressU)
root.bind('<Down>',key_pressD)
root.bind('<Return>',key_pressE)
root.bind('<Left>',key_pressL)
root.bind('<Right>',key_pressR)
orderFrame = Frame(root, bg=Background)
orderFrame.place(x=10, y=10, width=1500, height=400)

palletL = Label(orderFrame, width=10, text="Pallets")
palletL.place(x=100, y=10)
palletE = Entry(orderFrame, width=10, font=('Arial 24'))
palletE.place(x=100, y=50)

caseL= Label(orderFrame, width=10, text="Case Count")
caseL.place(x=300, y=10)
caseE = Entry(orderFrame, width=10, font=('Arial 24'))
caseE.place(x=300, y=50)

aisleL = Label(orderFrame, width=10, text="Aisle")
aisleL.place(x=500, y=10)
aisleE = Entry(orderFrame, width=10, font=('Arial 24'))
aisleE.place(x=500, y=50)

storeNumL = Label(orderFrame, width=10, text="Store Number")
storeNumL.place(x=700, y=10)
storeNumE = Entry(orderFrame, width=10, font=('Arial 24'))
storeNumE.place(x=700, y=50)

slotNumL = Label(orderFrame, width=10, text="Slot Number")
slotNumL.place(x=900, y=10)
slotNumE = Entry(orderFrame, width=10, font=('Arial 24'))
slotNumE.place(x=900, y=50)


label = Label(orderFrame, width=10, text="Slot Number")
label.place(x=100, y=100)

quit = Button(root, text='Quit', command=root.destroy, takefocus=0)
quit.place(x=1750, y=30)
palletE.focus()
entries = [palletE, caseE, aisleE, storeNumE, slotNumE]
for i in entries:
       i.lift()
root.mainloop()
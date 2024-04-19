from tkinter import *
from records  import create_order
from record_api import get_all_records


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
root.title("Order Tracker New")
# root.geometry('2080x730+0+0')
root.geometry('1200x390')


# Define a function to display the message
def key_press(e):
   key = e.char
   # print(key, 'is pressed')
   label.config(text=key)
   label.place(x=100, y=200)
   
def key_pressU(e):
   key = e.char
   # print(key, 'is pressed')
   
def key_pressD(e):
   key = e.char
   # print(key, 'is pressed')
   
def key_pressL(e):
   key = e.char
   # print(key, 'is pressed')
   
def key_pressR(e):
       #todo keysym to identifiy key press
   key = e.keysym
   # print(key, 'is pressed')
   
def key_pressE():
   print("Sent...")
   key = e.char
   create_order(palletE.get(), caseE.get(),
                aisleE.get(), storeNumE.get(),
                laneNumE.get())


def key_release(e):
   key = e.keysym
   print(key, 'is pressed')
# Create a label widget to add some text

def upload():
   print("Uploaded")
   get_all_records()


root.bind('<KeyPress>',key_press)
root.bind('<Up>',key_pressU)
root.bind('<Down>',key_pressD)
root.bind('<Return>',key_pressE)
root.bind('<Left>',key_pressL)
root.bind('<Right>',key_pressR)

# ################################# UI CONFIG #######################
orderFrame = Frame(root, bg=Background)
orderFrame.place(x=10, y=10, width=1050, height=400)

mainFrame = Frame(root, bg=Background)
# mainFrame.place(x=10, y=10, width=1050, height=400)

quit = Button(root, text='Quit', font=('Arial 20'), command=root.destroy, takefocus=0)
quit.place(x=1100, y=30)

start = Button(root, text='start', font=('Arial 20'), command=key_pressE, takefocus=0)
start.place(x=1100, y=100)

upload = Button(root, text='upload', font=('Arial 20'), command=upload, takefocus=0)
upload.place(x=1100, y=300)


# ###################################   orderFrame #######################################
palletL = Label(orderFrame, width=10, text="Pallets")
palletL.place(x=100, y=10)
palletE = Entry(orderFrame, width=5, font=('Arial 30'))
palletE.place(x=100, y=50)

caseL= Label(orderFrame, width=10, text="Case Count")
caseL.place(x=250, y=10)
caseE = Entry(orderFrame, width=5, font=('Arial 30'))
caseE.place(x=250, y=50)

aisleL = Label(orderFrame, width=10, text="Aisle")
aisleL.place(x=400, y=10)
aisleE = Entry(orderFrame, width=5, font=('Arial 30'))
aisleE.place(x=400, y=50)

storeNumL = Label(orderFrame, width=12, text="Store Number")
storeNumL.place(x=550, y=10)
storeNumE = Entry(orderFrame, width=5, font=('Arial 30'))
storeNumE.place(x=550, y=50)

laneNumL = Label(orderFrame, width=12, text="Lane Number")
laneNumL.place(x=700, y=10)
laneNumE = Entry(orderFrame, width=5, font=('Arial 30'))
laneNumE.place(x=700, y=50)


label = Label(orderFrame, width=25, font=('Arial 25'), text="Curent Order Due - 11:00 AM")
label.place(x=100, y=200)

curTotal = Label(orderFrame, width=12, font=('Arial 25'), text="Total= 1200")
curTotal.place(x=750, y=300)

curRate = Label(orderFrame, width=12, font=('Arial 25'), text="Rate = 160/hr")
curRate.place(x=750, y=200)



palletE.focus()
entries = [palletE, caseE, aisleE, storeNumE, laneNumE]
for i in entries:
       i.lift()
# ########################## END UI ######################################
root.mainloop()
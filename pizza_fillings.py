# my first exercise with tkinter
# GUI program for  ordering pizza`s fillings
# unflexible and hard to scale up 


from  tkinter import *

# scan active checkbuttons and create global tuple with ones and zeros 
# ones and zeros correspond with tuple pizza_fillings 
def scan_filling():
    """
    scan active checkbuttons and create global tuple with ones and zeros 
    ones and zeros correspond with tuple pizza_fillings 
    """
    
    global fill
    fill = var1, var2, var3
    


def apply():
    """
    callback to apply_button
    create new frame with list of ordered fillings for pizza
    show appropriate message 
    """
    
    frame_2 = Frame(relief=RAISED)
    frame_2.pack()
    
    order = []
    for i in range(len(pizza_fillings)):
        if fill[i].get():
            order.append(pizza_fillings[i])
            
    answer = "You ordered pizza with " + str(order).strip("[]")
    msg = Message(frame_2, text=answer)
    msg.pack()
    
    
    
root = Tk()
frame_1 = Frame(relief=RAISED, borderwidth=5)
frame_1.pack()
# initing checkbuttons for fillings 
var1 = IntVar() 
var2 = IntVar()
var3 = IntVar()

pizza_fillings = 'Paperoni', 'Mozarella', 'Cheese'
check_paperoni = Checkbutton(frame_1, text='Paperoni', variable=var1,
                             command=scan_filling)
check_mozarella = Checkbutton(frame_1, text='Mozarella', variable=var2,
                             command=scan_filling)
check_cheese = Checkbutton(frame_1, text='Cheese', variable=var3,
                             command=scan_filling)
# packing buttons to frame
check_paperoni.pack()
check_mozarella.pack()
check_cheese.pack()
# button that save the states of checkbuttons and shows message with ordered
# pizza`s fillings
apply_button = Button(frame_1, text='Apply', command=apply )
apply_button.pack(side=TOP)

mainloop()
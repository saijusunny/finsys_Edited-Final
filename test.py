#Import the tkinter library
from tkinter import *

#Create an instance of the tkinter frame
win = Tk()

#Define the geometry of the frame
win.geometry("600x400")

#Define the text-widget
my_text= Text(win, height = 5, width = 52)

# Create label
lab = Label(win, text ="TutorialsPoint.com")

#Configure it using other properties
lab.config(font =("Helvetica", 20))

#Create a button widget
my_button = Button(text="Hello")

#Define the position of the widget
my_button.place(x=100, y=100)

#Update the coordinates with respect to the tkinter frame
win.update()

#Get the coordinates of both text widget and button widget
widget_x1, widget_y1 = my_button.winfo_rootx(),
my_button.winfo_rooty()
widget_x2, widget_y2 = my_text.winfo_rootx(),
my_button.winfo_rooty()

lab.pack()

print(widget_x1, widget_y1)
print(widget_x2, widget_y2)

#Keep the window running
win.mainloop()
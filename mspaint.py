from tkinter import *
from classes import Tooltip
from tkinter import Scale
from tkinter import colorchooser, filedialog, messagebox
from PIL import ImageGrab as ImageGrab
import os, subprocess

#functions
def canvas_button_b1():
    global eraser_color
    color = colorchooser.askcolor()
    drawing_canvas.configure(bg=color[1])
    eraser_color = color[1]
    
def save_button_b2():
    file_name = filedialog.asksaveasfilename(defaultextension=".jpg", initialfile="Drawing Image", filetypes=(("Image Files", "*.jpg"), ("All files", "*.*")))
    x = window.winfo_rootx() + drawing_canvas.winfo_x()
    y = window.winfo_rooty() + drawing_canvas.winfo_y()
    x1 = x + drawing_canvas.winfo_width()
    y1 = y + drawing_canvas.winfo_height()
    ImageGrab.grab().crop((x,y,x1,y1)).save(file_name)
    messagebox.showinfo("File Saved", message="File Saved As : " + str(file_name))
    subprocess.Popen(f'explorer "{file_name}"')
    print(file_name)
    
def erase_button_b3():
    global pen_color 
    pen_color = eraser_color
    
def clear_button_b4():
    drawing_canvas.delete("all")
    
def paint(event):
    x1 , y1 = (event.x-2),(event.y-2)
    x2 , y2 = (event.x+2), (event.y+2)
    print (pen_color)
    drawing_canvas.create_oval(x1,y1,x2,y2, fill=pen_color,outline=pen_color, width=pen_size.get())
    
def select_color(col):
    global pen_color
    pen_color = str(col)
    print(col)

pen_color = "black"
eraser_color = "white"

#Color Codes
dict_colors = {"White": "#ffffff", "Black":"#000000", "Dark Grey": "#4e4e4e", "Green": "#00ff00", "Blue": "0000ff", "Red": "#ff0000", "Dark Red":"#A93226", "Yellow":"#FFEB3B", "Brown":"#5D4037", "Cyan":"#4FC3F7", "Dark Green": "#023020"}

window = Tk()
window.state("zoomed") #fullscreen
window.title("MS Paint Clone")

#Canvas
drawing_canvas = Canvas(window, bg="white", bd=5, relief=FLAT, height=800, width=1500)
drawing_canvas.place(x=0, y=100)
drawing_canvas.bind("<B1-Motion>", paint)

#Frame
color_frame = LabelFrame(window, text="Color", relief=RIDGE, bg="white", font=("Arial", 13, "bold"), bd=5, width=230)
color_frame.place(x=0, y=0, height=100)

#Tools Frame
tool_frame = LabelFrame(window, text="Tools", relief=RIDGE, bg="white", font=("Arial", 13, "bold"), bd=5, width=230)
print(color_frame.winfo_reqwidth())
tool_frame.place(x=color_frame.winfo_reqwidth(), y=0, height=100)

#Pen size frame
pensize_frame = LabelFrame(window, text="Pensize", relief=RIDGE, bg="white", font=("Arial", 13, "bold"), bd=5, width=250)
pensize_frame.place(x=color_frame.winfo_reqwidth() + tool_frame.winfo_reqwidth(), y=0, height=100)

#Button 
column = row = index = 0
colorkeys = list(dict_colors.keys())

for color in dict_colors.keys():
    color_btn = Button(color_frame,bd=3, relief=RIDGE, width=3, bg=color, command=lambda col = dict_colors[color]:select_color(col))
    color_btn.grid(row=row, column=column, padx=2, pady=2)
    tooltip = Tooltip(color_btn, colorkeys[index])
    
    row += 1
    index += 1
    if row > 1:
        column += 1
        row = 0
   
#Tool Buttons
btn_canvascolor = Button(tool_frame, text="Canvas", command=canvas_button_b1)
btn_canvascolor.grid(row = 0, column= 0, padx=2)
btn_save = Button(tool_frame, text="Save File", command=save_button_b2)
btn_save.grid(row=0, column= 1, padx=2)
btn_eraser = Button(tool_frame, text="Eraser", command=erase_button_b3)
btn_eraser.grid(row=0, column=2, padx=2)
btn_clear = Button(tool_frame, text="Clear", command=clear_button_b4)
btn_clear.grid(row=0, column=3, padx=2)

#Pen and Eraser Size
pen_size = Scale(pensize_frame, orient=HORIZONTAL, from_=1, to=50, length=170)
pen_size.set(5)
pen_size.grid(row=0, column=0)

    
    
window.mainloop()
import cv2
import copy
import numpy as np
import tkinter as tk 
from PIL import Image, ImageTk
from tkinter import filedialog as fd 

# ------------------
# -- FILTERS CODE --
# ------------------

sharp = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
edges = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])

# Basic Filters
def basic_filters(filter):
    global modifiable_image

    if filter == 'blur':
        modifiable_image = cv2.blur(modifiable_image,(5,5))
    else:
        modifiable_image  = cv2.filter2D(modifiable_image, -1, filter)

    canvas.image_tk = ImageTk.PhotoImage(image=Image.fromarray(cv2.resize(modifiable_image , maxsize)))
    # configure the canvas item to use this image
    canvas.itemconfigure(image_id, image=canvas.image_tk)

# --------------
# -- GUI CODE --
# --------------

# Interface and Image Uploading
# -----------------------------

# interface
root = tk.Tk()
root.geometry('400x400')
root.title('Awesome Image Filters')

# canvas creation
canvas = tk.Canvas(root)
canvas.grid(column=0, row=0, columnspan=3)

# image variables
image = None
modifiable_image = None # copy of main image so it can be changed without altering the latter
maxsize = (350, 250)
image_id = canvas.create_image(20, 20, anchor='nw')

# instructions
instructions_text = tk.StringVar()
instructions = tk.Label(root, textvariable=instructions_text, font='Raleway')
instructions_text.set('Select a PNG or a JPEG file')
instructions.grid(column=0, row=2, columnspan=3)

# browse button and image loading
browse_text = tk.StringVar()
browse_image = tk.Button(root, width=12, height=1, command=upload_image, textvariable=browse_text, font='Raleway') # when the button is pressed, it opens the file explorer
browse_text.set('Select Image')
browse_image.grid(column=0, row=3)
root.grid_rowconfigure(1, minsize=10)

# save image button
save_button = tk.Button(root, width=10, height=1, text='Save Image', font='Raleway')
save_button.grid(column=1, row=3)

# exit button 
exit_button = tk.Button(root, command=lambda: exit(), text='Exit', font='Raleway')
exit_button.grid(column=2, row=3)


# Menu and filter application 
# ---------------------------

# main menu
menu = tk.Menu(root) 
root.config(menu=menu) 

# basic filter menu
basic_filters_menu = tk.Menu(menu)
menu.add_cascade(label='Basic Filters', menu=basic_filters_menu) 

basic_filters_menu.add_command(label='Sharpen', command=lambda:basic_filters(sharp)) 
basic_filters_menu.add_command(label='Blur', command=lambda:basic_filters('blur')) 
basic_filters_menu.add_command(label='Show edges', command=lambda:basic_filters(edges))

# color filter menu

colorFilterMenu = tk.Menu(menu)
menu.add_cascade(label='Color Filters', menu=colorFilterMenu) 
colorFilterMenu.add_command(label='Red tint')
colorFilterMenu.add_command(label='Green tint')
colorFilterMenu.add_command(label='Blue tint')
colorFilterMenu.add_command(label='Custom tint...')

root.mainloop() 


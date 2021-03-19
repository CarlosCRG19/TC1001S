import cv2
import tkinter as tk 
from PIL import Image, ImageTk
from tkinter import filedialog as fd 

def upload_image():
    """
    Function called by the Browse button. It opens the file explorer and asks you to select a png or jpeg file 
    (actually, only this type of files are displayed on the file explorer). 
    After that, it reads the file and stores it in the image variable.
    """
    global image # this variable now belongs to the global scope

    select_text.set("Loading...") 
    filepath = fd.askopenfile(filetypes=(('image files', '.png'), ('image files', '.jpg'))) # filedialog function to open a file, it will only accept png or jpg images
    if filepath:
        select_text.set('Loaded')
        print('image successfully loaded')
        image = cv2.imread(filepath.name)

        # create the image object, and save it so that it
        # won't get deleted by the garbage collector
        canvas.image_tk = ImageTk.PhotoImage(image=Image.fromarray(cv2.resize(image, maxsize)))

        # configure the canvas item to use this image
        canvas.itemconfigure(image_id, image=canvas.image_tk)



# image variables
image = None
maxsize = (300, 350)

# interface
root = tk.Tk()
root.geometry('300x350')
root.title('Awesome Image Filters')
root.resizable(True, True)

canvas = tk.Canvas(root)
canvas.pack(side=tk.BOTTOM, padx=15, pady=15)

# instructions 

# browse button and image loading
image_id = canvas.create_image(20, 20, anchor='nw')

select_text = tk.StringVar()
selected_image = tk.Button(root, command=upload_image, textvariable=select_text, font='Raleway') # when the button is pressed, it opens the file explorer
select_text.set('Select Image')
selected_image.pack(side=tk.LEFT, padx=35)

# exit button 
exit_button = tk.Button(root, command=lambda: exit(), text='Exit', font='Raleway')
exit_button.pack(side=tk.LEFT)

menu = tk.Menu(root) 
root.config(menu=menu) 
root.title('Image Lab') 
basicFilterMenu = tk.Menu(menu)
menu.add_cascade(label='Basic Filters', menu=basicFilterMenu) 
basicFilterMenu.add_command(label='Sharpen') 
basicFilterMenu.add_command(label='Blur') 
basicFilterMenu.add_command(label='Show edges')
colorFilterMenu = tk.Menu(menu)
menu.add_cascade(label='Color Filters', menu=colorFilterMenu) 
colorFilterMenu.add_command(label='Red tint')
colorFilterMenu.add_command(label='Green tint')
colorFilterMenu.add_command(label='Blue tint')
colorFilterMenu.add_command(label='Custom tint...')

root.mainloop() 






root.mainloop()
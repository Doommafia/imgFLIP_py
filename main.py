from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog

def open_image():
    global img, img_label
    file_path = filedialog.askopenfilename()
    if file_path:
        img = Image.open(file_path)
        img_label.config(image=ImageTk.PhotoImage(img))

def flip_image(degrees):
    global img, img_label
    if img:
        img = img.rotate(degrees)
        img_label.config(image=ImageTk.PhotoImage(img))

def save_image():
    if img:
        save_path = filedialog.asksaveasfilename(defaultextension=".png")
        if save_path:
            img.save(save_path)

# Create the main window
root = tk.Tk()
root.title("Image Flipping Tool")

# Create buttons for flipping
flip90_button = tk.Button(root, text="Rotate 90°", command=lambda: flip_image(90))
flip90_button.pack(side=tk.LEFT, padx=5, pady=5)

flip180_button = tk.Button(root, text="Rotate 180°", command=lambda: flip_image(180))
flip180_button.pack(side=tk.LEFT, padx=5, pady=5)

flip270_button = tk.Button(root, text="Rotate -90°", command=lambda: flip_image(-90))
flip270_button.pack(side=tk.LEFT, padx=5, pady=5)

# Create button for opening image
open_button = tk.Button(root, text="Open Image", command=open_image)
open_button.pack(side=tk.LEFT, padx=5, pady=5)

# Create button for saving image
save_button = tk.Button(root, text="Save Image", command=save_image)
save_button.pack(side=tk.LEFT, padx=5, pady=5)

# Create label for displaying image
img_label = tk.Label(root)
img_label.pack()

# Variable to hold the loaded image
img = None

# Start the main event loop
root.mainloop()

import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image

import numpy as np
import cv2
from outils import contrast_enhancement, blurring_image, image_thresholding, image_sharpening

root = tk.Tk()
root.title("Image Enhancement")
# root.geometry("720x800")

book_image = Image.open('book.jpg')
image_book = ImageTk.PhotoImage(book_image)
frame = tk.Frame(root)
label = tk.Label(frame, image=image_book)
label.pack(fill='both')
frame.grid(row=1, column=0, columnspan=16)


def show_image(image):
    image_tk = ImageTk.PhotoImage(image)
    # frame = tk.Frame(root)
    # label = tk.Label(frame, image=image_tk)
    label.configure(image=image_tk)
    label.image = image_tk
    label.pack(fill='both')
    frame.grid(row=1, column=0, columnspan=16)

    edit_image(image)
    frame.mainloop()



def edit_image(image):
    enhance_contrast = tk.Button(root, text="Enhance contrast", state='active', command=lambda: contrast(image))
    blurring = tk.Button(root, text="Blurring", state='active', command=lambda: blur(image))
    thresholding = tk.Button(root, text="Change thresholding", state='active', command=lambda: threshold(image))
    sharpening = tk.Button(root, text="Sharpening", state='active', command=lambda: sharpen(image))
    # original = tk.Button(root, text="Show original", state='active', command=)

    enhance_contrast.grid(row=2, column=2,  padx=2)
    blurring.grid(row=2, column=3, padx=2)
    thresholding.grid(row=2, column=4,  padx=2)
    sharpening.grid(row=2, column=5, rowspan=2)
    root.mainloop()


def select_image():

    path = filedialog.askopenfilename(initialdir='', title='Select an image',
                                      filetypes=(('PNG files', ['*.png', '*.PNG']),
                                                  ('JPEG files', ['*.jpg', '*.jpeg'])))
    image = Image.open(path)
    show_image(image)
    root.mainloop()


def contrast(image):
    array = np.array(image)
    image_cv = cv2.cvtColor(array, cv2.COLOR_RGB2BGR)
    image1 = contrast_enhancement(image_cv)
    image1_rgb = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
    image1 = Image.fromarray(image1_rgb)
    show_image(image1)


def blur(image):
    array = np.array(image)
    image_cv = cv2.cvtColor(array, cv2.COLOR_RGB2BGR)
    image1 = blurring_image(image_cv)
    image1_rgb = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
    image1 = Image.fromarray(image1_rgb)
    show_image(image1)


def threshold(image):
    array = np.array(image)
    image_cv = cv2.cvtColor(array, cv2.COLOR_RGB2BGR)
    image1 = image_thresholding(image_cv)
    image1_rgb = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
    image1 = Image.fromarray(image1_rgb)
    show_image(image1)


def sharpen(image):
    array = np.array(image)
    image_cv = cv2.cvtColor(array, cv2.COLOR_RGB2BGR)
    image1 = image_sharpening(image_cv)
    image1_rgb = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
    image1 = Image.fromarray(image1_rgb)
    show_image(image1)


welcoming_text = tk.Label(root, text="For editing an image press the Select an image button bellow")
first_view = tk.Button(root, text="Select an image", state='active', command=select_image)

welcoming_text.grid(row=0, column=0)
first_view.grid(row=2, column=0, columnspan=4)


root.mainloop()


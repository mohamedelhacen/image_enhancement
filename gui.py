import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image

import cv2
from outils import contrast_enhancement, blurring_image, image_thresholding, image_sharpening

root = tk.Tk()
root.title("Image Enhancement")
root.geometry("720x800")


# def process_and_show(image_path):
#
#     image = Image.open(image_path)
#     image = ImageTk.PhotoImage(image)
#     label = tk.Label(root, image=image)
#     label.grid(row=1, column=0, columnspan=4)
#     root.mainloop()


def select_image():

    path = filedialog.askopenfilename(initialdir='', title='Select an image',
                                       filetypes=(('PNG files', ['*.png', '*.PNG']), ('JPEG files', ['*.jpg', '*.jpeg'])))
    # process_and_show(path)
    image = Image.open(path)
    w, h = image.size
    root.geometry(f"{w+20}x{h+70}")
    image = ImageTk.PhotoImage(image)
    label = tk.Label(root, image=image)
    label.grid(row=1, column=0, columnspan=16)

    enhance_contrast = tk.Button(root, text="Enhance contrast", state='active', command=lambda: contrast(path))
    blurring = tk.Button(root, text="Blurring", state='active', command=lambda: blur(path))
    thresholding = tk.Button(root, text="Change thresholding", state='active', command=lambda: threshold(path))
    sharpening = tk.Button(root, text="Sharpening", state='active', command=lambda: sharpen(path))
    # original = tk.Button(root, text="Show original", state='active', command=)

    enhance_contrast.grid(row=2, column=2,  padx=2)
    blurring.grid(row=2, column=3, padx=2)
    thresholding.grid(row=2, column=4,  padx=2)
    sharpening.grid(row=2, column=5, rowspan=2)
    root.mainloop()


def contrast(im_path):
    image = cv2.imread(im_path)
    image1 = contrast_enhancement(image)
    image1_rgb = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
    image1 = Image.fromarray(image1_rgb)
    image1 = ImageTk.PhotoImage(image1)
    label1 = tk.Label(root, image=image1)
    label1.grid(row=1, column=0, columnspan=4)
    root.mainloop()


def blur(im_path):
    image = cv2.imread(im_path)
    image1 = blurring_image(image)
    image1_rgb = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
    image1 = Image.fromarray(image1_rgb)
    image1 = ImageTk.PhotoImage(image1)
    label1 = tk.Label(root, image=image1)
    label1.grid(row=1, column=0, columnspan=4)
    root.mainloop()


def threshold(im_path):
    image = cv2.imread(im_path)
    image1 = image_thresholding(image)
    image1_rgb = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
    image1 = Image.fromarray(image1_rgb)
    image1 = ImageTk.PhotoImage(image1)
    label1 = tk.Label(root, image=image1)
    label1.grid(row=1, column=0, columnspan=4)
    root.mainloop()


def sharpen(im_path):
    image = cv2.imread(im_path)
    image1 = image_sharpening(image)
    image1_rgb = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
    image1 = Image.fromarray(image1_rgb)
    image1 = ImageTk.PhotoImage(image1)
    label1 = tk.Label(root, image=image1)
    label1.grid(row=1, column=0, columnspan=4)
    root.mainloop()


welcoming_text = tk.Label(root, text="For editing an image press the Select an image button bellow")
first_view = tk.Button(root, text="Select an image", state='active', command=select_image)

welcoming_text.grid(row=0, column=0)
first_view.grid(row=2, column=0, columnspan=4)


root.mainloop()


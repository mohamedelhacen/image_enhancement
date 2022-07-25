import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image

import cv2
from outils import contrast_enhancement, blurring_image, image_thresholding, image_sharpening

root = tk.Tk()
root.title("Image Enhancement")
root.geometry("720x800")

image_path = filedialog.askopenfilename(initialdir='', title='Select an image',
                                   filetypes=(('PNG files', ['*.png', '*.PNG']), ('JPEG files', ['*.jpg', '*.jpeg'])))
image_bgr = cv2.imread(image_path)
image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)

image = Image.fromarray(image_rgb)
image = ImageTk.PhotoImage(image)

label = tk.Label(root, image=image)
label.grid(row=0, column=0, columnspan=4)
type(image)

def contrast(image):
    image1 = contrast_enhancement(image)
    image1_rgb = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
    image1 = Image.fromarray(image1_rgb)
    image1 = ImageTk.PhotoImage(image1)
    label1 = tk.Label(root, image=image1)
    label1.grid(row=0, column=0, columnspan=4)

def just_pass():
    pass

enhance_contrast = tk.Button(root, text="Enhance contrast", state='active', command=contrast(image_bgr))
blurring = tk.Button(root, text="Blurring", state='active', command=just_pass)
thresholding = tk.Button(root, text="Change thresholding", state='active', command=just_pass)
sharpening = tk.Button(root, text="Sharpening", state='active', command=just_pass)


enhance_contrast.grid(row=1, column=0, columnspan=4)
blurring.grid(row=1, column=1, columnspan=4)
thresholding.grid(row=1, column=2, columnspan=4)
sharpening.grid(row=1, column=3, columnspan=4)

root.mainloop()


import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageGalleryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Gallery")

        # Dark theme colors
        self.bg_color = "#000000"
        self.button_bg_color = "#800080"
        self.fg_color = "#FFFFFF"

        self.root.configure(bg=self.bg_color)
        self.root.state('zoomed')

        self.images = []
        self.current_image = 0

        self.canvas = tk.Canvas(root, bg=self.bg_color)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Increase button dimensions
        button_width = 12
        button_height = 2

        self.prev_button = tk.Button(root, text="Previous", command=self.show_previous, bg=self.button_bg_color, fg=self.fg_color, borderwidth=0, relief=tk.FLAT, width=button_width, height=button_height)
        self.prev_button.pack(side=tk.LEFT, padx=10, pady=5)

        self.next_button = tk.Button(root, text="Next", command=self.show_next, bg=self.button_bg_color, fg=self.fg_color, borderwidth=0, relief=tk.FLAT, width=button_width, height=button_height)
        self.next_button.pack(side=tk.RIGHT, padx=10, pady=5)

        self.browse_button = tk.Button(root, text="Select Folder", command=self.select_folder, bg=self.button_bg_color, fg=self.fg_color, borderwidth=0, relief=tk.FLAT, width=button_width, height=button_height)
        self.browse_button.pack(padx=10, pady=5)

        self.info_frame = tk.Frame(root, bg=self.bg_color)
        self.info_frame.pack(side=tk.BOTTOM, fill=tk.X)

        self.current_image_label = tk.Label(self.info_frame, text="Images: 0/0", bg=self.bg_color, fg=self.fg_color)
        self.current_image_label.pack(padx=100, pady=5)

    def select_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.load_images_from_folder(folder_path)
            self.current_image = 0
            self.show_current()

    def load_images_from_folder(self, folder_path):
        self.images = []
        image_files = [f for f in os.listdir(folder_path) if f.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))]
        for image_file in image_files:
            image_path = os.path.join(folder_path, image_file)
            image = Image.open(image_path)
            image.thumbnail((700, 700))
            self.images.append(ImageTk.PhotoImage(image))

        self.total_images_label.config(text="Total Images: {}".format(len(self.images)))

    def show_current(self):
        self.canvas.delete("all")
        if self.images:
            image = self.images[self.current_image]
            image_width = image.width()
            image_height = image.height()

            canvas_width = self.canvas.winfo_width()
            canvas_height = self.canvas.winfo_height()

            x_scale = canvas_width / image_width
            y_scale = canvas_height / image_height
            scale = min(x_scale, y_scale)

            new_width = int(image_width * scale)
            new_height = int(image_height * scale)

            self.canvas.create_image(canvas_width / 2, canvas_height / 2, image=image, anchor=tk.CENTER)
            self.current_image_label.config(text="Images: {}/{}".format(self.current_image + 1, len(self.images)))

    def show_previous(self):
        if self.images:
            self.current_image = (self.current_image - 1) % len(self.images)
            self.show_current()

    def show_next(self):
        if self.images:
            self.current_image = (self.current_image + 1) % len(self.images)
            self.show_current()

if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg="#000000")  # Set overall background color to black
    app = ImageGalleryApp(root)
    root.mainloop()

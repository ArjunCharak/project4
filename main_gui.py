import tkinter as tk
from multiprocessing import Process
from gallery_app import ImageGalleryApp

def start_gui():
    root = tk.Tk()
    root.title("Servo Control")
    root.geometry("300x200")

    # Dark theme colors
    bg_color = "#000000"
    fg_color = "#FFFFFF"
    button_bg_color = "#800080"
    

    root.configure(bg=bg_color)

    label_font = ("Helvetica", 16)  # Specify font family and size
    label_servo_1 = tk.Label(root, text="Main Screen", bg=bg_color, fg=fg_color, font=label_font)
    button_fire = tk.Button(root, text="Fire!", bg=button_bg_color, fg=fg_color)
    button_capture = tk.Button(root, text="Capture Image", bg=button_bg_color, fg=fg_color)
    button_gallery = tk.Button(root, text="Open Gallery", command=open_gallery, bg=button_bg_color, fg=fg_color)

    label_servo_1.pack(pady=10)
    button_fire.pack(pady=10)
    button_capture.pack(pady=10)
    button_gallery.pack(pady=10)

    # Create a menu bar
    menu_bar = tk.Menu(root)
    
    
    # Add file menu
    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Exit", command=root.quit)
    menu_bar.add_cascade(label="File", menu=file_menu)
    
    # Add about  menu
    help_menu = tk.Menu(menu_bar, tearoff=0)
    help_menu.add_command(label="About", command=show_about)
    menu_bar.add_cascade(label="About", menu=help_menu)

    # Add help menu
    help_menu = tk.Menu(menu_bar, tearoff=0)
    help_menu.add_command(label="Help", command=show_about)
    menu_bar.add_cascade(label="Help", menu=help_menu)
    
    root.config(menu=menu_bar)

    root.mainloop()

def open_gallery():
    gallery_process = Process(target=start_gallery_app)
    gallery_process.start()

def start_gallery_app():
    gallery_root = tk.Tk()
    gallery_app = ImageGalleryApp(gallery_root)
    gallery_root.mainloop()

def show_about():
    about_window = tk.Toplevel()
    about_window.title("About")
    about_window.geometry("300x150")

    about_label = tk.Label(about_window, text="This is the Servo Control App.\nVersion 1.0", padx=10, pady=10)
    about_label.pack()

if __name__ == "__main__":
    start_gui()

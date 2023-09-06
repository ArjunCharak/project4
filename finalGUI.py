import tkinter as tk
import cv2
from PIL import Image, ImageTk
from tkinter import PhotoImage
import time
from tkinter import ttk
import os





#````````````````````````````Splash Screen```````````````````````````````````````````
# ```````````````````````````````````````````````````````````````````````````````````
# Function to close the splash screen and open the main window
def close_splash_and_open_main():
    splash_screen.destroy()  # Close the splash screen
    main()       # Open the main window

# Create the splash screen window
splash_screen = tk.Tk()
#Set the geometry
width = 400
height = 400
# Calculate the starting X and Y coordinates for the splash screen window
screen_width = splash_screen.winfo_screenwidth()
screen_height = splash_screen.winfo_screenheight()
x = int((screen_width / 2) - (width / 2))
y = int((screen_height / 2) - (height / 2))
# Set the position and size of the splash screen using the formula
splash_screen.geometry(f"{width}x{height}+{x}+{y}")
splash_screen.title("Splash Screen")
splash_screen.configure(bg="#1F1C25")

# Disable resizing and remove maximize, minimize, and close buttons
splash_screen.resizable(False, False)
splash_screen.overrideredirect(True)

# Add a label or any content you want on the splash screen
splash_label = tk.Label(splash_screen, text="\n\nPragyastra", font=("Helvetica", 28),bg="#1F1C25",fg="white")
splash_label.pack(expand=True)
splash_label = tk.Label(splash_screen, text="\n\nv 2.0", font=("Helvetica", 12),bg="#1F1C25",fg="#837C91")
splash_label.pack(expand=True)

# Schedule the opening of the global window after 30 seconds
splash_screen.after(5000, close_splash_and_open_main)  # Removed the parentheses after "open_global_window"

# Run the tkinter main loop for the splash screen
splash_screen.mainloop()



#``````````````````````````````````````````````````````````````````````````````````````````````````````````````

#                                               -----------------Menu-function----------------

def open_image_folder():
    folder_path = r"C:\Users\Aniket\Desktop\defence_project"
    os.system(f'explorer.exe "{folder_path}"')

# Function to restart the application
def restart_app():
    window.destroy()
    main()

# Function to display About information
def show_about():
    about_text = """
    This is a simple webcam viewer app created with tkinter and OpenCV.
    It's designed by Mongo Tom, the one and only!
    """
    about_window = tk.Toplevel(window)
    about_window.title("About")
    about_label = tk.Label(about_window, text=about_text)
    about_label.pack()

    # Function to open the new window and close the main window
def open_new_window_and_close_main():
    window.destroy()  # Close the main window
    open_new_window()  # Open the new window



   




    

#                                   ---------------------------Main------------------------
#````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
# Create the main window
def main():
    global window
    window = tk.Tk()
    window.title("eXPERIMENT")
    # Set the window geometry to 1920x1080
    window.geometry("1920x1080")
    #Set the background color to black
    window.configure(bg="black")
    #--------------------------------------------MENU-----------------

     # Create a menu
    menu = tk.Menu(window)
    window.config(menu=menu)
 
    # Add options to the menu
    file_menu = tk.Menu(menu)
    menu.add_cascade(label="System", menu=file_menu)
    file_menu.add_command(label="Restart", command=restart_app)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=window.quit)
    Go = tk.Menu(menu)
    menu.add_cascade(label="Go", menu=Go)
    Go.add_command(label="Gallery",command=open_image_folder)
    Go.add_command(label="Smart Mode",command=open_new_window_and_close_main)


    View = tk.Menu(menu)
    menu.add_cascade(label="View", menu=View)
    View.add_command(label="Extend Screen", command=None)

    help_menu = tk.Menu(menu)
    menu.add_cascade(label="Help", menu=help_menu)
    help_menu.add_command(label="About", command=show_about)




    #-------------------------------------WEBCAM--------------------------
    # Create a label to display the webcam feed
    webcam = tk.Label(window, bg="black")
    webcam.place(x=40, y=10) 
    # Initialize the webcam using OpenCV
    cap = cv2.VideoCapture(0)
    def update_webcam():
        ret, frame = cap.read()
        if ret:
            # Resize the frame to 861x564
            frame = cv2.resize(frame, (900, 500))
            
            # Convert the frame to RGB format
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            # Convert the frame to a tkinter-compatible format
            img = Image.fromarray(frame_rgb)
            img_tk = ImageTk.PhotoImage(image=img)
            
            # Update the label with the new frame
            webcam.img = img_tk
            webcam.config(image=img_tk)
            
            # Repeat the update every 10 milliseconds
            webcam.after(10, update_webcam)
        else:
            cap.release()
    # Start updating the webcam feed
    update_webcam()

    #--------------------------------------control panel---------------------------
    # Create controller widget
    blue_widget = tk.Frame(window, width=540, height=500, bg="#38353E")
    blue_widget.place(x=950, y=10)  # Set the x and y coordinates for the blue widget
    # Disable automatic resizing of the widget
    blue_widget.pack_propagate(0)


    # Create a text label inside the blue widget
    text_label = tk.Label(blue_widget, text="Controller", font=("Helvetica", 14), fg="#837C91", bg="#38353E")
    text_label.pack(pady=20)  # Add some padding
#----------------------------------------x-slider------------------------------------------
        # Create a ttk Style
    style = ttk.Style()

    # Configure the style to set the background color of the Scale widget to black
    style.configure("TScale", background="#1F1C25")

    # Create a ttk Scale widget (slider)
    slider = ttk.Scale(blue_widget, from_=0, to=100, orient="horizontal", length=300, style="TScale")
    slider.pack()
        # Set the initial position of the slider to 50
    slider.set(50)

    # Create a Label to display the slider value
    label = tk.Label(blue_widget, text="X-Coordinate: 50", fg="white", bg="#1F1C25")
    label.pack(pady=10)

    # Function to update the label with the current slider value
    def update_label(value):
        label.config(text=f"X-Coordinate : {value}")

    # Bind the slider's "command" to the update_label function
    slider.config(command=lambda x: update_label(slider.get()))




    #-----------------y-slider-------------------------

        # Create a ttk Style
    style = ttk.Style()

    # Configure the style to set the background color of the Scale widget to black
    style.configure("TScale", background="#1F1C25")

    # Create a ttk Scale widget (vertical slider)
    vertical_slider = ttk.Scale(blue_widget, from_=0, to=100, orient="vertical", length=200, style="TScale")
    vertical_slider.pack()

    # Set the initial position of the vertical slider to 50
    vertical_slider.set(50)

    # Create a Label to display the vertical slider value
    slider_label1 = tk.Label(blue_widget, text="Y-Coordinate : 50", fg="white", bg="#1F1C25")
    slider_label1.pack(padx=10,pady=30)

    # Function to update the label with the current vertical slider value
    def update_label1(value):
        slider_label1.config(text=f"Y-Coordinate : {value}")

    # Bind the vertical slider's "command" to the update_label function
    vertical_slider.config(command=lambda x: update_label1(vertical_slider.get()))



    # Function to reset the slider to its default value
    def reset_slider():
        slider.set(50)
        vertical_slider.set(50)

    

#

    

    # Create a button to reset the slider
    reset_button = tk.Button(
        blue_widget,
        text="Default Position",
        command=reset_slider,
        bg="blue",    # Set the background color to blue
        fg="white",   # Set the text color to white
        width=23,     # Set the width
        height=2,     # Set the height
        relief="flat" # Set the relief to flat for a flat-style button
)
    reset_button.place(x=180,y=420) 



  


    
    #------------------------------human VIEW---------------------------------
    # Create your widget with the specified size and color
    human = tk.Frame(window, width=192, height=132, bg="#38353E")
    # Pack the widget to make it visible
    human.place(x=40, y=530)
    human.pack_propagate(0)

    # Load an icon image using Pillow
    icon_image = Image.open(r"c:\Users\Aniket\Desktop\defence_project\IconCheck.png")# Replace "your_icon.png" with the path to your icon image
    icon_image = icon_image.resize((32, 32), Image.ANTIALIAS)  # Resize the icon to fit

    # Convert the image to a PhotoImage for tkinter
    icon_photo = ImageTk.PhotoImage(icon_image)

    # Create a label to display the icon at position (10, 10) inside the human widget
    icon_label = tk.Label(human, image=icon_photo, bg="#38353E")
    icon_label.image = icon_photo  # Keep a reference to the image to prevent it from being garbage collected
    icon_label.place(x=10, y=10)

        # Create a label for the "human detected" text at position (20, 10) inside the human widget
    text_label = tk.Label(human, text="Intruder Detected", font=("Helvetica", 12), fg="#837C91", bg="#38353E")
    text_label.place(x=50, y=15)




   
        #------------------------------weapon VIEW---------------------------------
    # Create your widget with the specified size and color
    weapon = tk.Frame(window, width=192, height=132, bg="#38353E")

    # Pack the widget to make it visible
    weapon.place(x=300, y=530)
    weapon.pack_propagate(0)

    # Load an icon image using Pillow
    icon_image = Image.open(r"c:\Users\Aniket\Desktop\defence_project\weapon.png")# Replace "your_icon.png" with the path to your icon image
    icon_image = icon_image.resize((32, 32), Image.ANTIALIAS)  # Resize the icon to fit

    # Convert the image to a PhotoImage for tkinter
    icon_photo = ImageTk.PhotoImage(icon_image)

    # Create a label to display the icon at position (10, 10) inside the human widget
    icon_label = tk.Label(weapon, image=icon_photo, bg="#38353E")
    icon_label.image = icon_photo  # Keep a reference to the image to prevent it from being garbage collected
    icon_label.place(x=10, y=10)

        # Create a label for the "human detected" text at position (20, 10) inside the human widget
    text_label = tk.Label(weapon, text="Weapon Detected", font=("Helvetica", 12), fg="#837C91", bg="#38353E")
    text_label.place(x=50, y=15)


    #------------------------------distance VIEW---------------------------------
    # Create your widget with the specified size and color
    distance = tk.Frame(window, width=192, height=132, bg="#38353E")

    # Pack the widget to make it visible
    distance.place(x=570, y=530)
    distance.pack_propagate(0)

    # Load an icon image using Pillow
    icon_image = Image.open(r"c:\Users\Aniket\Desktop\defence_project\distance.png")# Replace "your_icon.png" with the path to your icon image
    icon_image = icon_image.resize((32, 32), Image.ANTIALIAS)  # Resize the icon to fit

    # Convert the image to a PhotoImage for tkinter
    icon_photo = ImageTk.PhotoImage(icon_image)

    # Create a label to display the icon at position (10, 10) inside the human widget
    icon_label = tk.Label(distance, image=icon_photo, bg="#38353E")
    icon_label.image = icon_photo  # Keep a reference to the image to prevent it from being garbage collected
    icon_label.place(x=10, y=10)

        # Create a label for the "human detected" text at position (20, 10) inside the human widget
    text_label = tk.Label(distance, text="Distance", font=("Helvetica", 12), fg="#837C91", bg="#38353E")
    text_label.place(x=50, y=15)

    #------------------------------------------distance button-------------------------------

# Create the 100m flat-style button with white text
    button = tk.Button(
        window,
        text="100 m",
        width=23,
        height=2,
        bg="blue",  # Background color
        fg="white",    # Text color
        relief="flat"  # Flat style (no border)
    )
    button.place(x=40, y=700)  # Set the x and y coordinates for the button
    #button.config(command=button_click)  # Set the button's click function
#-------------------------------

    #Create the 200m flat-style button with white text
    button1 = tk.Button(
        window,
        text="200 m",
        width=23,
        height=2,
        bg="blue",  # Background color
        fg="white",    # Text color
        relief="flat"  # Flat style (no border)
    )
    button1.place(x=250, y=700)  # Set the x and y coordinates for the button
    #button.config(command=button_click)  # Set the button's click function

#-------------------------------

    #Create the 200m flat-style button with white text
    button2 = tk.Button(
        window,
        text="300 m",
        width=23,
        height=2,
        bg="blue",  # Background color
        fg="white",    # Text color
        relief="flat"  # Flat style (no border)
    )
    button2.place(x=460, y=700)  # Set the x and y coordinates for the button
    #button.config(command=button_click)  # Set the button's click function
#----------------------------

    #Create the Fire flat-style button with white text
    buttonfire = tk.Button(
        window,
        text="Fire",
        width=23,
        height=2,
        bg="#CC1111",  # Background color
        fg="white",    # Text color
        relief="flat"  # Flat style (no border)
    )
    buttonfire.place(x=670, y=700)  # Set the x and y coordinates for the button
    #button.config(command=button_click)  # Set the button's click function

        #--------------------------------------tools panel---------------------------
    # Create tools widget
    blue_widget2 = tk.Frame(window, width=540, height=230, bg="#38353E")
    blue_widget2.place(x=950, y=530)  # Set the x and y coordinates for the blue widget
    # Disable automatic resizing of the widget
    blue_widget2.pack_propagate(0)


    # Create a text label inside the blue widget
    text_label = tk.Label(blue_widget2, text="Tools", font=("Helvetica", 14), fg="#837C91", bg="#38353E")
    text_label.pack(pady=20)  # Add some padding
#-----------------------------intruder checkbox----------------------------------
    # Create an IntVar to control the state of the checkbox (0 for unchecked, 1 for checked)
    checkbox_var = tk.IntVar()

    # Create a modern ttk Style
    style = ttk.Style()

    # Configure the style for the modern checkbox
    style.configure("TCheckbutton", background="#38353E", foreground="white")

    # Create a modern ttk Checkbutton with a default value of 0 (unchecked)
    modern_checkbox = ttk.Checkbutton(
        blue_widget2,
        text="Intruder Box",
        style="TCheckbutton",  # Apply the configured style
        variable=checkbox_var  # Use the IntVar to control the state
    )
    modern_checkbox.place(x=40, y=70)

    # Set the initial state of the checkbox to 0 (unchecked)
    checkbox_var.set(0)
    #------------------------weapon checkbox-----------------------

        # Create an IntVar for the second checkbox (Weapon Box)
    weapon_checkbox_var = tk.IntVar()

    # Create the second modern ttk Checkbutton (Weapon Box)
    weapon_checkbox = ttk.Checkbutton(
        blue_widget2,
        text="Weapon Box",
        style="TCheckbutton",       # Apply the configured style
        variable=weapon_checkbox_var  # Use the IntVar to control the state
    )
    weapon_checkbox.place(x=40, y=110)

    # Set the initial state of the second checkbox to 0 (unchecked)
    weapon_checkbox_var.set(0)
    #-----------------------------auto capture image----------------------------
        # Create a function to capture an image when Auto Capture Image is checked
    auto_capture_var = tk.IntVar()

    def capture_image_auto():
        if auto_capture_var.get() == 1:  # Check if Auto Capture Image is checked (1)
            print("Auto capturing image...")

    # Create the third modern ttk Checkbutton (Auto Capture Image)
    auto_capture_checkbox = ttk.Checkbutton(
        blue_widget2,
        text="Auto Capture Images",
        style="TCheckbutton",          # Apply the configured style
        variable=auto_capture_var,     # Use the IntVar to control the state
        command=capture_image_auto    # Call the capture_image_auto function when checked
    )
    auto_capture_checkbox.place(x=40, y=150)

    #-------------------alarm------------------------
    def trigger_alarm():
        print("Alarm triggered!")

        # Create a function to trigger an alarm when Alarm is checked
    alarm_var = tk.IntVar()

    def trigger_alarm_auto():
        if alarm_var.get() == 1:  # Check if Alarm is checked (1)
            print("Alarm triggered!")

    # Create the fourth modern ttk Checkbutton (Alarm)
    alarm_checkbox = ttk.Checkbutton(
        blue_widget2,
        text="Auto Alarm",
        style="TCheckbutton",       # Apply the configured style
        variable=alarm_var,         # Use the IntVar to control the state
        command=trigger_alarm_auto  # Call the trigger_alarm_auto function when checked
    )
    alarm_checkbox.place(x=40, y=190)

    # Set the initial state of Alarm checkbox to unchecked (0)
    alarm_var.set(0)

    #---------------------nightvision checkbox---------------------------
    # Create an IntVar for the fifth checkbox (Night Vision)
    night_vision_var = tk.IntVar()

    # Create the fifth modern ttk Checkbutton (Night Vision)
    night_vision_checkbox = ttk.Checkbutton(
        blue_widget2,
        text="Night Vision",
        style="TCheckbutton",         # Apply the configured style
        variable=night_vision_var,    # Use the IntVar to control the state
        command=None  # Call the activate_night_vision function when checked
    )
    night_vision_checkbox.place(x=350, y=70)

    # Set the initial state of Night Vision checkbox to unchecked (0)
    night_vision_var.set(0)

    #----------------grey vision---------------------------------------

        # Create an IntVar for the sixth checkbox (Gray Vision)
    gray_vision_var = tk.IntVar()

    # Create the sixth modern ttk Checkbutton (Gray Vision)
    gray_vision_checkbox = ttk.Checkbutton(
        blue_widget2,
        text="Gray Vision",
        style="TCheckbutton",         # Apply the configured style
        variable=gray_vision_var,    # Use the IntVar to control the state
        command=None  # Call the activate_gray_vision function when checked
    )
    gray_vision_checkbox.place(x=350, y=110)

    # Set the initial state of Gray Vision checkbox to unchecked (0)
    gray_vision_var.set(0)

    #-------distance box-----------------
        # Create an IntVar for the seventh checkbox (Distance)
    distance_var = tk.IntVar()

    # Create the seventh modern ttk Checkbutton (Distance)
    distance_checkbox = ttk.Checkbutton(
        blue_widget2,
        text="Distance",
        style="TCheckbutton",        # Apply the configured style
        variable=distance_var,      # Use the IntVar to control the state
        command=None     # Call the check_distance function when checked
    )
    distance_checkbox.place(x=350, y=150)

    # Set the initial state of Distance checkbox to unchecked (0)
    distance_var.set(0)




    


        #`````````````````````MAIN LOOP`````````````````
    # Run the tkinter main loop
    window.mainloop()

# Start the application
main()

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#---------------------------------Ai Mode````````````````````````````````

def open_new_window():
    new_window = tk.Tk()
    new_window.title("Smart Mode")
    new_window.geometry("1920x1080")  # Set the geometry to 1920x1080
    new_window.configure(bg="black")  # Set the background color to #18152C

    #----------header-------------------------------------------------
    # Create your widget with the specified size and color
    header = tk.Frame(new_window, width=1920, height=50, bg="black")
    # Pack the widget to make it visible
    header.place(x=0,y=0)
    header.pack_propagate(0)

    from tkinter import font

    # Create a custom font using Google Fonts
    custom_font = font.Font(family="Google Sans", size=18, weight="normal")

    # Add a label to the header widget
    ai_mode_label = tk.Label(header, text="Smart Mode", bg="black", fg="#00D7ED", font=custom_font)
    ai_mode_label.place(x=20,y=12)
#-------------------------Captured image Button------------------------------
    
    def destroy_and_open_main():
        new_window.destroy()  # Open the new window
        main()  # Close the main window
        

    flat_button1 = tk.Button(new_window, text="Gallery", command=open_image_folder, relief=tk.FLAT, bg="#222327", fg="white")
    flat_button1.place(x=1360, y=17)

#-------------------------Manual Mode Button------------------------------
    
    def destroy_and_open_main():
        new_window.destroy()  # Open the new window
        main()  # Close the main window
        

    flat_button = tk.Button(new_window, text="Manual Mode", command=destroy_and_open_main, relief=tk.FLAT, bg="#222327", fg="#00D7ED")
    flat_button.place(x=1426, y=17)


    #-------------------------------------WEBCAM--------------------------
    # Create a label to display the webcam feed
    webcam = tk.Label(new_window, bg="black")
    webcam.place(x=40, y=60) 
    # Initialize the webcam using OpenCV
    cap = cv2.VideoCapture(0)
    def update_webcam():
        ret, frame = cap.read()
        if ret:
            # Resize the frame to 861x564
            frame = cv2.resize(frame, (900, 500))
            
            # Convert the frame to RGB format
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            # Convert the frame to a tkinter-compatible format
            img = Image.fromarray(frame_rgb)
            img_tk = ImageTk.PhotoImage(image=img)
            
            # Update the label with the new frame
            webcam.img = img_tk
            webcam.config(image=img_tk)
            
            # Repeat the update every 10 milliseconds
            webcam.after(10, update_webcam)
        else:
            cap.release()
    # Start updating the webcam feed
    update_webcam()

#------------------------ai logo---------------
# Load and display the image
    # Load and display the image
    image = Image.open("C:/Users/Aniket/Desktop/defence_project/ai.png")
    image = image.resize((590, 260))  # Adjust the size as needed
    image = ImageTk.PhotoImage(image)

    # Create a label for the image with no border
    image_label = tk.Label(new_window, image=image,  bd=0, relief=tk.FLAT)
    image_label.image = image
    image_label.place(x=945,y=60)
    #------------------------------------control ________________________
 # Create controller widget
    blue_widget = tk.Frame(new_window, width=540, height=160, bg="#38353E")
    blue_widget.place(x=950, y=340)  # Set the x and y coordinates for the blue widget
    # Disable automatic resizing of the widget
    blue_widget.pack_propagate(0)


    # Create a text label inside the blue widget
    text_label = tk.Label(blue_widget, text="Controller", font=("Helvetica", 14), fg="#837C91", bg="#38353E")
    text_label.pack(pady=20)  # Add some padding


    #Create the Fire flat-style button with white text
    buttonfire = tk.Button(
        blue_widget,
        text="Fire",
        width=23,
        height=2,
        bg="#CC1111",  # Background color
        fg="white",    # Text color
        relief="flat"  # Flat style (no border)
    )
    buttonfire.place(x=40, y=70)  # Set the x and y coordinates for the button
    #button.config(command=button_click)  # Set the button's click function


    #button default position

    default = tk.Button(
    blue_widget,
    text="Default Position",  # Modify the button's name here
    width=23,
    height=2,
    bg="#131314",  # Background color
    fg="white",    # Text color
    relief="flat"  # Flat style (no border)
    )
    default.place(x=300, y=70) 


    #-----------------button tracking----------------------

    default = tk.Button(
    blue_widget,
    text="Default Position",  # Modify the button's name here
    width=23,
    height=2,
    bg="#131314",  # Background color
    fg="white",    # Text color
    relief="flat"  # Flat style (no border)
    )
    default.place(x=300, y=70) 

    #-----------auto tracking------------
   

#-------------------------------status data----------------
    def create_status_widget(window, x, y, icon_path, text):
        # Create the widget with the specified size and color
        status_widget = tk.Frame(new_window, width=192, height=132, bg="#38353E")

        # Pack the widget to make it visible
        status_widget.place(x=x, y=y)
        status_widget.pack_propagate(0)

        # Load an icon image using Pillow
        icon_image = Image.open(icon_path)
        icon_image = icon_image.resize((32, 32), Image.ANTIALIAS)  # Resize the icon to fit

        # Convert the image to a PhotoImage for tkinter
        icon_photo = ImageTk.PhotoImage(icon_image)

        # Create a label to display the icon at position (10, 10) inside the status widget
        icon_label = tk.Label(status_widget, image=icon_photo, bg="#38353E")
        icon_label.image = icon_photo  # Keep a reference to the image to prevent it from being garbage collected
        icon_label.place(x=10, y=10)

        # Create a label for the status text at position (50, 15) inside the status widget
        text_label = tk.Label(status_widget, text=text, font=("Helvetica", 12), fg="#837C91", bg="#38353E")
        text_label.place(x=50, y=15)

    # Create the "Human" status widget
    create_status_widget(window, 40, 615, r"c:\Users\Aniket\Desktop\defence_project\IconCheck.png", "Intruder Detected")

    # Create the "Weapon" status widget
    create_status_widget(window, 300, 615, r"c:\Users\Aniket\Desktop\defence_project\weapon.png", "Weapon Detected")

    # Create the "Distance" status widget
    create_status_widget(window, 570, 615, r"c:\Users\Aniket\Desktop\defence_project\distance.png", "Distance")

#-
     #--------------------------------------tools panel---------------------------
    # Create tools widget
    blue_widget2 = tk.Frame(new_window, width=540, height=230, bg="#38353E")
    blue_widget2.place(x=950, y=530)  # Set the x and y coordinates for the blue widget
    # Disable automatic resizing of the widget
    blue_widget2.pack_propagate(0)


    # Create a text label inside the blue widget
    text_label = tk.Label(blue_widget2, text="Tools", font=("Helvetica", 14), fg="#837C91", bg="#38353E")
    text_label.pack(pady=20)  # Add some padding
#-----------------------------intruder checkbox----------------------------------
    # Create an IntVar to control the state of the checkbox (0 for unchecked, 1 for checked)
    checkbox_var = tk.IntVar()

    # Create a modern ttk Style
    style = ttk.Style()

    # Configure the style for the modern checkbox
    style.configure("TCheckbutton", background="#38353E", foreground="white")

    # Create a modern ttk Checkbutton with a default value of 0 (unchecked)
    modern_checkbox = ttk.Checkbutton(
        blue_widget2,
        text="Intruder Box",
        style="TCheckbutton",  # Apply the configured style
        variable=checkbox_var  # Use the IntVar to control the state
    )
    modern_checkbox.place(x=40, y=70)

    # Set the initial state of the checkbox to 0 (unchecked)
    checkbox_var.set(0)
    #------------------------weapon checkbox-----------------------

        # Create an IntVar for the second checkbox (Weapon Box)
    weapon_checkbox_var = tk.IntVar()

    # Create the second modern ttk Checkbutton (Weapon Box)
    weapon_checkbox = ttk.Checkbutton(
        blue_widget2,
        text="Weapon Box",
        style="TCheckbutton",       # Apply the configured style
        variable=weapon_checkbox_var  # Use the IntVar to control the state
    )
    weapon_checkbox.place(x=40, y=110)

    # Set the initial state of the second checkbox to 0 (unchecked)
    weapon_checkbox_var.set(0)
    #-----------------------------auto capture image----------------------------
        # Create a function to capture an image when Auto Capture Image is checked
    auto_capture_var = tk.IntVar()

    def capture_image_auto():
        if auto_capture_var.get() == 1:  # Check if Auto Capture Image is checked (1)
            print("Auto capturing image...")

    # Create the third modern ttk Checkbutton (Auto Capture Image)
    auto_capture_checkbox = ttk.Checkbutton(
        blue_widget2,
        text="Auto Capture Images",
        style="TCheckbutton",          # Apply the configured style
        variable=auto_capture_var,     # Use the IntVar to control the state
        command=capture_image_auto    # Call the capture_image_auto function when checked
    )
    auto_capture_checkbox.place(x=40, y=150)

    #-------------------alarm------------------------
    def trigger_alarm():
        print("Alarm triggered!")

        # Create a function to trigger an alarm when Alarm is checked
    alarm_var = tk.IntVar()

    def trigger_alarm_auto():
        if alarm_var.get() == 1:  # Check if Alarm is checked (1)
            print("Alarm triggered!")

    # Create the fourth modern ttk Checkbutton (Alarm)
    alarm_checkbox = ttk.Checkbutton(
        blue_widget2,
        text="Auto Alarm",
        style="TCheckbutton",       # Apply the configured style
        variable=alarm_var,         # Use the IntVar to control the state
        command=trigger_alarm_auto  # Call the trigger_alarm_auto function when checked
    )
    alarm_checkbox.place(x=40, y=190)

    # Set the initial state of Alarm checkbox to unchecked (0)
    alarm_var.set(0)

    #---------------------nightvision checkbox---------------------------
    # Create an IntVar for the fifth checkbox (Night Vision)
    night_vision_var = tk.IntVar()

    # Create the fifth modern ttk Checkbutton (Night Vision)
    night_vision_checkbox = ttk.Checkbutton(
        blue_widget2,
        text="Night Vision",
        style="TCheckbutton",         # Apply the configured style
        variable=night_vision_var,    # Use the IntVar to control the state
        command=None  # Call the activate_night_vision function when checked
    )
    night_vision_checkbox.place(x=350, y=70)

    # Set the initial state of Night Vision checkbox to unchecked (0)
    night_vision_var.set(0)

    #----------------grey vision---------------------------------------

        # Create an IntVar for the sixth checkbox (Gray Vision)
    gray_vision_var = tk.IntVar()

    # Create the sixth modern ttk Checkbutton (Gray Vision)
    gray_vision_checkbox = ttk.Checkbutton(
        blue_widget2,
        text="Gray Vision",
        style="TCheckbutton",         # Apply the configured style
        variable=gray_vision_var,    # Use the IntVar to control the state
        command=None  # Call the activate_gray_vision function when checked
    )
    gray_vision_checkbox.place(x=350, y=110)

    # Set the initial state of Gray Vision checkbox to unchecked (0)
    gray_vision_var.set(0)

    #-------distance box-----------------
        # Create an IntVar for the seventh checkbox (Distance)
    distance_var = tk.IntVar()

    # Create the seventh modern ttk Checkbutton (Distance)
    distance_checkbox = ttk.Checkbutton(
        blue_widget2,
        text="Distance",
        style="TCheckbutton",        # Apply the configured style
        variable=distance_var,      # Use the IntVar to control the state
        command=None     # Call the check_distance function when checked
    )
    distance_checkbox.place(x=350, y=150)

    # Set the initial state of Distance checkbox to unchecked (0)
    distance_var.set(0)







    new_window.mainloop()
open_new_window()

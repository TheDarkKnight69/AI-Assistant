import tkinter as tk
from tkinter import ttk

# Function to handle button click
def send_message():
    message = input_box.get()
    # You can add code here to process the user's input or trigger voice assistant actions
    # For this example, we will print the message
    print(f"User: {message}")
    input_box.delete(0, tk.END)  # Clear the input box

# Create the main window
root = tk.Tk()
root.title("Voice Assistant")
root.geometry('500x700')

# Load the background image using PhotoImage
bg_image = tk.PhotoImage(file="visualizer.gif")  # Replace "your_image.gif" with your image file

# Create a label to display the background image
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)  # Cover the entire window

# Create a frame for the menu (left side)
menu_frame = tk.Frame(root, background="white")
menu_frame.pack(side=tk.LEFT, fill=tk.BOTH)

# Create menu items with padding to control the width
menu_item_1 = tk.Label(menu_frame, text="File", background="white", padx=50, pady = 10)
menu_item_1.pack(fill=tk.BOTH)
menu_item_2 = tk.Label(menu_frame, text="Exit", background="white", padx=50, pady = 10)
menu_item_2.pack(fill=tk.BOTH)

# Create a frame for communication box and enter button (bottom)
bottom_frame = tk.Frame(root)
bottom_frame.pack(side=tk.BOTTOM, fill=tk.BOTH)

# Create the communication box with rounded tube-like appearance
input_box = ttk.Entry(bottom_frame, width=10)
input_box.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.X, expand=True)
input_box_style = ttk.Style()
input_box_style.configure("Rounded.TEntry", borderwidth=10, relief="sunken", padding=(5, 5))
input_box["style"] = "Rounded.TEntry"

# Create the enter button
enter_button = tk.Button(bottom_frame, text="Enter", command=send_message, background="white")
enter_button.pack(side=tk.LEFT, padx=10, pady=10)

# Start the main event loop
root.mainloop()

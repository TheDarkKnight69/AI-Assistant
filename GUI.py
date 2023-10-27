import tkinter as tk
from tkinter import ttk
import query
import importlib

# Function to handle button click
def takecommand():
    q = input_box.get()
    try:
        q = q.lower()
        # Add any code to process 'q' here
        input_box.delete(0, tk.END)
        return q
    except Exception as e:
        # Handle exceptions if necessary
        input_box.delete(0, tk.END)
        pass
def handle_gui_button_click():
    query = takecommand()
    input_box.delete(0, tk.END)
    mod = importlib.import_module("AI_Structure")
    # Pass 'query' to your ai() function or process it here as needed
    mod.ai(query)

# Create the main window
root = tk.Tk()
root.title("Voice Assistant")
root.geometry('500x700')

# Create a frame for the menu (left side)
menu_frame = tk.Frame(root, background="white")
menu_frame.pack(side=tk.LEFT, fill=tk.BOTH)

# Create menu items with padding to control the width
menu_item_1 = tk.Label(menu_frame, text="File", background="white", padx=50, pady=10)
menu_item_1.pack(fill=tk.BOTH)
menu_item_2 = tk.Label(menu_frame, text="Exit", background="white", padx=50, pady=10)
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
enter_button = tk.Button(bottom_frame, text="Enter", command=handle_gui_button_click, background="white")  # Change 'ai.ai' to 'takecommand'
enter_button.pack(side=tk.LEFT, padx=10, pady=10)

# Start the main event loop
root.mainloop()

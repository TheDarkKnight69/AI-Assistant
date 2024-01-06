import tkinter as tk
from tkinter import ttk
import query
import importlib
from AI_Structure import *
# Function to handle button click
root = tk.Tk()
root.title("Voice Assistant")
root.geometry('500x700')

def value():
    value = input_box.get()
    return value
    input_box.delete('1.0', tk.END)
    
def ask():
    user_val = value()
    bot_val = ai(user_val)
    output_text.insert(tk.END, "You: "+user_val+"\n")
    output_text.insert(tk.END, "Assistant: "+str(bot_val)+"\n")

# Create the main window

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
enter_button = tk.Button(bottom_frame, text="Enter", command=ask, background="white")  # Change 'ai.ai' to 'takecommand'
enter_button.pack(side=tk.LEFT, padx=10, pady=10)

output_text = tk.Text(root, height=41)  # Or use tk.Label if you prefer a single-line display
output_text.pack(side=tk.BOTTOM, fill=tk.X)

# Start the main event loop
root.mainloop()

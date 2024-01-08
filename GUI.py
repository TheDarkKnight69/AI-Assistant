import tkinter as tk
from tkinter import ttk
import query
import importlib
from AI_Structure import *
import json
import sv_ttk



preferences = {}
with open("C:\\Users\\SHAAYEQ\\Desktop\\AI-Assistant\\preferences.json", 'r') as f:
    preferences = json.load(f)

# Function to handle button click
root = tk.Tk()
root.title("Voice Assistant")
root.geometry('500x700')

sv_ttk.set_theme("light")

def change_theme():
    # NOTE: The theme's real name is azure-<mode>
    if sv_ttk.get_theme() == "light":
        # Set light theme
        sv_ttk.set_theme("dark")

    else:
        # Set dark theme
        sv_ttk.set_theme("light")

def save_button():
    with open("C:\\Users\\SHAAYEQ\\Desktop\\AI-Assistant\\preferences.json", 'w') as f:
        json.dump(preferences, f)
    popup.destroy()

def end():
    root.destroy()
    sys.exit()

def value():
    value = input_box.get()
    return value
    
        
def ask():
    if len(value()) > 0:
        user_val = value()
        input_box.delete('0',tk.END)
        bot_val = ai(user_val)
        output_text.config(state = 'normal')
        output_text.insert(tk.END, "You: "+user_val+"\n")
        output_text.insert(tk.END, "Assistant: "+str(bot_val)+"\n")
        output_text.config(state = 'disabled')
    else:
        pass
    
def settings():
    popup = tk.Toplevel()
    popup.grab_set()
    popup.title("Settings")
    popup.geometry("400x300")
    theme = tk.Checkbutton(popup, text = "Toggle the dark or light mode")
    theme.config(command = change_theme)
    theme.pack(side = tk.TOP, anchor = "nw")
    save = tk.Button(popup, text = "Save", command = save_button)
    save.pack(side = tk.BOTTOM, anchor = "se", padx = 15, pady = 15)
# Create the main window

# Create a frame for the menu (left side)
menu_bar = tk.Menu(root)
menu_frame = tk.Frame(root, background="white")
menu_frame.pack(side=tk.LEFT, fill=tk.BOTH)


file = tk.Menu(menu_bar, tearoff = 0) 
menu_bar.add_cascade(label ='Settings', menu = file) 
file.add_command(label ='Preferences', command = settings) 
file.add_separator() 
file.add_command(label ='Exit', command = root.destroy)



# Create menu items with padding to control the width
#menu_item_1 = tk.Label(menu_frame, text="File", background="white", padx=50, pady=10)
#menu_item_1.pack(fill=tk.BOTH)
#menu_item_2 = tk.Button(menu_frame, text="Exit", background="white", padx=50, pady=10, command = end)
#menu_item_2.pack(fill=tk.BOTH)

# Create a frame for communication box and enter button (bottom)
bottom_frame = tk.Frame(root)
bottom_frame.pack(side=tk.BOTTOM, fill=tk.BOTH)
a = tk.PhotoImage(file = "C:\\Users\\SHAAYEQ\\Desktop\\AI-Assistant\\mic.png")
mic_button = tk.Button(bottom_frame, image = a, width = 25, height = 25, command = speech_to_text)
mic_button.pack(side = tk.RIGHT, padx = 10, pady = 10, fill = tk.X)
# Create the communication box with rounded tube-like appearance
input_box = ttk.Entry(bottom_frame, width=10)
input_box.pack(side = tk.LEFT, padx=10, pady=10, fill=tk.X, expand=True)
input_box_style = ttk.Style()
input_box_style.configure("Rounded.TEntry", borderwidth=10, relief="sunken", padding=(5, 5))
input_box["style"] = "Rounded.TEntry"

# Create the enter button

enter_button = tk.Button(bottom_frame, text="Enter", command=ask, background="white")  # Change 'ai.ai' to 'takecommand'
enter_button.pack(side=tk.LEFT, padx=10, pady=10)

output_text = tk.Text(root, height=41, state = 'disabled')  # Or use tk.Label if you prefer a single-line display
output_text.pack(side=tk.BOTTOM, fill=tk.X)

root.config(menu = menu_bar)
# Start the main event loop
root.mainloop()

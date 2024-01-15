import tkinter as tk
from tkinter import ttk
import importlib
from AI_Structure import *
import json
import sv_ttk
from PIL import Image, ImageTk
<<<<<<< HEAD
=======
import customtkinter as ctk
import speech_recognition as speech
global name_input
>>>>>>> b6edd831942d8adb2ce0a3388728a1e0a70d594d

preferences = {}
with open("E:\\Voice assistant code final\\AI-Assistant\\preferences.json", 'r') as f:
    preferences = json.load(f)

# Function to handle button click
root = tk.Tk()
root.title("Voice Assistant")
root.geometry('500x700')

sv_ttk.set_theme(preferences["theme"])

def window_closed(event):
    with open("E:\\Voice assistant code final\\AI-Assistant\\preferences.json", 'w') as f:
        json.dump(preferences, f)    


def change_theme():
    # NOTE: The theme's real name is azure-<mode>
    if sv_ttk.get_theme() == "light":
        # Set light theme
        sv_ttk.set_theme("dark")
        preferences["theme"] = "dark"
    else:
        # Set dark theme
        sv_ttk.set_theme("light")
        preferences["theme"] = "light"

    
    
     

def end():
    root.destroy()
    sys.exit()

def speech_input():
    r=speech.Recognizer()
    with speech.Microphone() as source:   
        speak("Listening")
        r.pause_threshold=0.4
        r.non_speaking_duration=0.4
        r.energy_threshold=300
        audio=r.listen(source)
<<<<<<< HEAD
        try:

=======
        
        try:
>>>>>>> b6edd831942d8adb2ce0a3388728a1e0a70d594d
            query=r.recognize_google(audio, language="en-in")
            bot_val = ai(query.lower())
            output_text.config(state = 'normal')
            output_text.insert(tk.END, "You: "+query+"\n")
            output_text.insert(tk.END, f"{preferences['name']}: {str(bot_val)}\n")
            output_text.config(state = 'disabled')
            
        except Exception as e:
            speak("Couldn't catch what you said")
            output_text.config(state = 'normal')
            output_text.insert(tk.END, "You: "+query+"\n")
            output_text.insert(tk.END, f"{preferences['name']}: {str(e)}\n")
            output_text.config(state = 'disabled')
    

def value():
    value = input_box.get()
    if len(str(value))>0:
        return value

<<<<<<< HEAD
        
=======
>>>>>>> b6edd831942d8adb2ce0a3388728a1e0a70d594d
def ask():
    if len(input_box.get()) > 0:
        user_val = value()
        print(user_val)
        input_box.delete('0',tk.END)
        bot_val = ai(user_val.lower())
        output_text.config(state = 'normal')
        output_text.insert(tk.END, "You: "+user_val+"\n")
        output_text.insert(tk.END, f"{preferences['name']}: {str(bot_val)}\n")
        output_text.config(state = 'disabled')
    else:
        pass

def settings():
    def nameee():
        a = name_input.get()
        preferences['name'] = a

    popup = tk.Toplevel()
    popup.grab_set()
    popup.title("Settings")
    popup.geometry("400x300")   
    tabControl = ttk.Notebook(popup) 
  
    tab1 = ttk.Frame(tabControl) 
    tab2 = ttk.Frame(tabControl) 
  
    tabControl.add(tab1, text ='Appearance') 
    tabControl.pack(expand = 1, fill ="both") 
  
    theme_frame = tk.Label(tab1)
    theme_frame.pack(side = tk.TOP, anchor = "nw")
    theme = tk.Checkbutton(theme_frame)
    theme.config(command = change_theme)
    theme.grid(column = 0, row = 0)
    #theme.pack(padx = 5) #side = tk.LEFT, anchor = "w", 
    theme_text = tk.Label(theme_frame, text = "Toggle the dark or light mode")
    theme_text.grid(column = 1, row = 0)
    #theme_text.pack() #side = tk.RIGHT, anchor = "e"
    name = tk.Label(theme_frame, text = "Name: ")
    name.config(padx = 16, pady = 5)
    name.grid(column = 0, row = 1) 
    #name.pack()
    name_input = tk.Entry(theme_frame, font= ("Arial", 10), width = 18)
    name_input.insert(0, preferences["name"])
    name_input.grid(column = 1, row = 1)

    save = tk.Button(tab1, text = "Save", command=nameee)     
    save.pack(side = tk.BOTTOM, anchor = "se", padx = 15, pady = 15)
# Create the main window

# Create a frame for the menu (left side)
menu_bar = tk.Menu(root)
menu_bar.config(borderwidth = 0)
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
<<<<<<< HEAD
a = ImageTk.PhotoImage(Image.open("C:\\Users\\SHAAYEQ\\Desktop\\AI-Assistant\\mic.png").resize((20,20)))
=======
a = ImageTk.PhotoImage(Image.open("E:\\Voice assistant code final\\AI-Assistant\\mic.png").resize((20,20)))
>>>>>>> b6edd831942d8adb2ce0a3388728a1e0a70d594d
mic_button = tk.Button(bottom_frame, image = a, width = 25, height = 25, command = speech_input)
mic_button.pack(side = tk.RIGHT, padx = 10, pady = 10, fill = tk.X)
# Create the communication box with rounded tube-like appearance
input_box = ttk.Entry(bottom_frame, width=10)
input_box.pack(side = tk.LEFT, padx=10, pady=10, fill=tk.X, expand=True)
input_box_style = ttk.Style()
input_box_style.configure("Rounded.TEntry", borderwidth=10, relief="sunken", padding=(5, 5))
input_box["style"] = "Rounded.TEntry"

# Create the enter button

enter_button = tk.Button(bottom_frame, text="Enter", command=ask)  # Change 'ai.ai' to 'takecommand'
enter_button.pack(side=tk.LEFT, padx=10, pady=10)

output_text = tk.Text(root, height=41, state = 'disabled')  # Or use tk.Label if you prefer a single-line display
output_text.pack(side=tk.BOTTOM,expand = True, fill=tk.BOTH)

root.config(menu = menu_bar)
# Start the main event loop
root.bind("<Destroy>", window_closed)
root.mainloop()

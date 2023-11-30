import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

window = tk.Tk()
window.title("Ghost Notes")
window.geometry("400x400")
window.resizable(False, True)
window.minsize(400, 400)
#window.overrideredirect(True)
window.attributes("-topmost", 1)

opacity_value = tk.DoubleVar()
opacity_value.set(0.9)
def change_opacity(value):
    print(value)
    window.attributes("-alpha", value)
      
#top frame
top_frame = ttk.Frame(window, height= 50, borderwidth= 10, relief= tk.GROOVE)
top_frame.pack(fill= "x", padx=10, pady=10)

#bottom frame 
bottom_frame = ttk.Frame(window, height=50, borderwidth= 10, relief=tk.GROOVE)
bottom_frame.pack(fill= "both", expand= True, padx=10, pady=10)

#opacity slider
slider_opacity = ttk.Scale(top_frame, variable= opacity_value, from_= 0.3, to= 0.9, length= 200, command= change_opacity)
slider_opacity.pack(side= "left", padx= 10)

#quit button
button_quit = ttk.Button(top_frame, text= "Quit", command= lambda: window.quit() )
button_quit.pack(side= "left", padx= 10, fill= "x", expand= True)

#scrolled text
scrolled_text = scrolledtext.ScrolledText(bottom_frame)
scrolled_text.pack(expand= True, fill= "both")








window.mainloop()

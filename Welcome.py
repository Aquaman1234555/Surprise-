import tkinter as tk
import itertools

# Create the main window
window = tk.Tk()
window.title("Welcome Message")
window.geometry("500x300")

# Define colors for a glowing effect
colors = itertools.cycle(["red", "orange", "yellow", "green", "blue", "purple"])

# Define the message and label with larger font size
message = "Hello Neha didi and diya didi We are excited and also ready with horror movies and gossips."
label = tk.Label(window, text=message, wraplength=450, font=("Arial", 18, "bold"))
label.pack(pady=40)

# Function to change the label color for glowing effect
def glow_text():
    label.config(fg=next(colors))
    window.after(300, glow_text)  # Change color every 300 milliseconds

# Start glowing effect
glow_text()

# Run the application
window.mainloop()

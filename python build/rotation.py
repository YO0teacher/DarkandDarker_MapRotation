import tkinter as tk
from datetime import datetime, timedelta

# Create the clock window
root = tk.Tk()
root.geometry("400x200")
root.configure(background='dark gray')
root.title("Map Rotation Tracker")

global delay
delay = timedelta(seconds=1)

def fetch_settings():
    global delay
    with open('settings.txt', 'r') as file:
        file.readline()  # Skip the first line
        second_line = file.readline().strip()  # Read the second line and strip newline characters
        delay_seconds = float(second_line)  # Convert the line to an integer
        delay = timedelta(seconds=delay_seconds)  # Convert seconds to timedelta

def time():
    global delay
    now = datetime.now()
    # Calculate the next 3-minute mark
    target = now.replace(second=0, microsecond=0) + timedelta(minutes=3)
    target -= timedelta(minutes=target.minute % 3)

    # Calculate remaining time (with a slight delay to account for processing time)
    remaining = target - now + delay
    # Format as minutes:seconds
    countdown = "Next rotation in\n" + '{:02d}:{:02d}'.format(remaining.seconds // 60, remaining.seconds % 60)
    
    # Update label
    lbl.config(text=countdown)
    root.after(1000, time)  # Schedule the next tick

# Create countdown label
lbl = tk.Label(root, font=('comic sans', 40, 'bold'), background='gray', foreground='white')
lbl.pack(anchor='center')
time()

# Fetch current maps by the hour and minute
def mapupdate():
    global solomap, duomap, triomap
    now = datetime.now()
    minute = now.minute
    hour = now.hour
    if hour % 3 == 0:
        if minute in {0, 1, 2, 9, 10, 11, 18, 19, 20, 27, 28, 29, 36, 37, 38, 45, 46, 47, 54, 55, 56}:
            solomap = "Frost Mountain ▶ Goblin Caves"
            duomap = "Crypts ▶ Frost Mountain"
            triomap = "Goblin Caves ▶ Crypts"
        elif minute in {3, 4, 5, 12, 13, 14, 21, 22, 23, 30, 31, 32, 39, 40, 41, 48, 49, 50, 57, 58, 59}:
            solomap = "Goblin Caves ▶ Crypts"
            duomap = "Frost Mountain ▶ Goblin Caves"
            triomap = "Crypts ▶ Frost Mountain"
        elif minute in {6, 7, 8, 15, 16, 17, 24, 25, 26, 33, 34, 35, 42, 43, 44, 51, 52, 53}:
            solomap = "Crypts ▶ Frost Mountain"
            duomap = "Goblin Caves ▶ Crypts"
            triomap = "Frost Mountain ▶ Goblin Caves"
    elif (hour - 1) % 3 == 0:
        if minute in {0, 1, 2, 9, 10, 11, 18, 19, 20, 27, 28, 29, 36, 37, 38, 45, 46, 47, 54, 55, 56}:
            solomap = "Crypts ▶ Frost Mountain"
            duomap = "Goblin Caves ▶ Crypts"
            triomap = "Frost Mountain ▶ Goblin Caves"
        elif minute in {3, 4, 5, 12, 13, 14, 21, 22, 23, 30, 31, 32, 39, 40, 41, 48, 49, 50, 57, 58, 59}:
            solomap = "Frost Mountain ▶ Goblin Caves"
            duomap = "Crypts ▶ Frost Mountain"
            triomap = "Goblin Caves ▶ Crypts"
        elif minute in {6, 7, 8, 15, 16, 17, 24, 25, 26, 33, 34, 35, 42, 43, 44, 51, 52, 53}:
            solomap = "Goblin Caves ▶ Crypts"
            duomap = "Frost Mountain ▶ Goblin Caves"
            triomap = "Crypts ▶ Frost Mountain"
    elif (hour - 2) % 3 == 0:
        if minute in {0, 1, 2, 9, 10, 11, 18, 19, 20, 27, 28, 29, 36, 37, 38, 45, 46, 47, 54, 55, 56}:
            solomap = "Goblin Caves ▶ Crypts"
            duomap = "Frost Mountain ▶ Goblin Caves"
            triomap = "Crypts ▶ Frost Mountain"
        elif minute in {3, 4, 5, 12, 13, 14, 21, 22, 23, 30, 31, 32, 39, 40, 41, 48, 49, 50, 57, 58, 59}:
            solomap = "Crypts ▶ Frost Mountain"
            duomap = "Goblin Caves ▶ Crypts"
            triomap = "Frost Mountain ▶ Goblin Caves"
        elif minute in {6, 7, 8, 15, 16, 17, 24, 25, 26, 33, 34, 35, 42, 43, 44, 51, 52, 53}:
            solomap = "Frost Mountain ▶ Goblin Caves"
            duomap = "Crypts ▶ Frost Mountain"
            triomap = "Goblin Caves ▶ Crypts"
    map_label.config(text="Solos: " + solomap + "\nDuos: " + duomap + "\nTrios: " + triomap)
    root.after(1500, mapupdate) # Automatically updates every couple of seconds

# Create label for current maps
map_label = tk.Label(root, font=('comic sans', 10, 'bold'), background='light gray', foreground='black')
map_label.pack(anchor='center')

# Start loops
fetch_settings()
mapupdate()
root.mainloop()

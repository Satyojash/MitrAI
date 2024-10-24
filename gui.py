import tkinter as tk

# Function that will be called when the button is clicked
def start_main_program():
    import phoenix  # This will run your main program
    phoenix.run()   # Assuming you have a function named 'run' in your main program

# Creating the GUI window
def create_gui():
    root = tk.Tk()
    root.title("Start Assistant")
    root.geometry("300x200")

    # Create a start button
    start_button = tk.Button(root, text="Start Assistant", command=start_main_program, font=("Arial", 14), padx=10, pady=5)
    start_button.pack(pady=60)

    root.mainloop()

# Running the GUI window
if __name__ == "__main__":
    create_gui()

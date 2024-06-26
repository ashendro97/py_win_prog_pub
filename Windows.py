import tkinter as tk
from tkinter import filedialog, Tk, Text, Scrollbar, Y, BOTH, LEFT, RIGHT, END, WORD
from tkinter import messagebox
from tkinter import Canvas

#x1
#x2
#x3
def open_file():
    # Create a root window and hide it
    root = Tk()
    root.withdraw()

    # Open file dialog
    file_path = filedialog.askopenfilename(initialdir="./", title="Select File", filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))

    if file_path:
        try:
            with open(file_path, "r") as file:
                content = file.read()

            # Create a new window
            #new_window = Tk()
            #new_window.title("File Content")

            # Create a canvas
            canvas = Canvas(window, width=400, height=300)
            canvas.pack()

            # Display the content of the file in the canvas
            canvas.create_text(200, 150, text=content, font=("Arial", 12), anchor="n")

        except FileNotFoundError:
            print("File not found")

def open_documentation():
    try:
        with open("doc.txt", "r") as file:
            content = file.read()

        # Create a new window
        new_window = tk.Toplevel()
        new_window.title("Documentation")

        # Add a scrollbar
        scrollbar = tk.Scrollbar(new_window)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Add a text widget with the content of the file
        text_widget = tk.Text(new_window, wrap=tk.WORD, yscrollcommand=scrollbar.set)
        text_widget.insert(tk.END, content)
        text_widget.pack(side=tk.LEFT, fill=tk.BOTH)

        # Configure the scrollbar
        scrollbar.config(command=text_widget.yview)

    except FileNotFoundError:
        messagebox.showerror("Error", "Documentation file not found")


# Create a new window
window = tk.Tk()

# Set the window title
window.title("DCAI-DCPAE Release Tool")

# Set the window size
window.geometry("400x300")

# Create a dropdown menu
menu = tk.Menu(window)
window.config(menu=menu)

# Create a File menu
file_menu = tk.Menu(menu, tearoff=False)
menu.add_cascade(label="File", menu=file_menu)

# Add Open option to File menu
file_menu.add_command(label="Open", command=open_file)

# Add a separator in the File menu
file_menu.add_separator()

# Add Exit option to File menu
file_menu.add_command(label="Exit", command=window.quit)

# Add a Help menu
help_menu = tk.Menu(menu, tearoff=False)
menu.add_cascade(label="Help", menu=help_menu)

# Add About option to Help menu
help_menu.add_command(label="About")

# Add a separator in the Help menu
help_menu.add_separator()

# Add Documentation option to Help menu
help_menu.add_command(label="Documentation", command=open_documentation)

# Run the window's event loop
window.mainloop()

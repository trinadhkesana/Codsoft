import tkinter as tk
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_button_click():
    try:
        password_length = int(length_entry.get())
        if password_length <= 0:
            result_label.config(text="Password length must be a positive integer.")
            return
        password = generate_password(password_length)
        result_label.config(text="Generated Password: " + password)
    except ValueError:
        result_label.config(text="Invalid input. Please enter a valid integer.")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create a bold heading for the application
heading_label = tk.Label(root, text="Password Generator", font=("Helvetica", 16, "bold"))
heading_label.pack(pady=10)

# Create a label and entry widget for username
username_label = tk.Label(root, text="Username:")
username_label.pack(anchor='w', padx=10)
username_entry = tk.Entry(root)
username_entry.pack(anchor='w', padx=10)

# Create a label and entry widget for password length
length_label = tk.Label(root, text="Password Length:")
length_label.pack(anchor='w', padx=10)
length_entry = tk.Entry(root)
length_entry.pack(anchor='w', padx=10)

# Create a bordered box for the "Generate Password" button
generate_frame = tk.LabelFrame(root, text="Generate Password", padx=10, pady=10, bd=2, relief=tk.SOLID)
generate_frame.pack(padx=10, pady=10, fill='both', expand='true')

# Create the "Generate Password" button
generate_button = tk.Button(generate_frame, text="Generate", command=generate_button_click)
generate_button.pack()

# Create a label to display the result
result_label = tk.Label(root, text="", pady=10)
result_label.pack()

# Start the GUI event loop
root.mainloop()
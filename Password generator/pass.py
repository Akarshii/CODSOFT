import tkinter as tk
import random
import string

def generate_password():
    password_length = int(length_entry.get())
    if password_length <= 0:
        result_label.config(text="Invalid length")
        return

    complexity = complexity_var.get()
    characters = ""

    if complexity == "Weak":
        characters = string.ascii_lowercase
    elif complexity == "Medium":
        characters = string.ascii_letters + string.digits
    elif complexity == "Strong":
        characters = string.ascii_letters + string.digits + string.punctuation

    if characters:
        password = ''.join(random.choice(characters) for _ in range(password_length))
        result_label.config(text=f"Generated Password: {password}")

# main window
window = tk.Tk()
window.title("Password Generator")
window.geometry("400x250")  
window.configure(bg="lightblue")

# frame for input elements
input_frame = tk.Frame(window, padx=10, pady=10)
input_frame.pack(fill=tk.BOTH, expand=True)


# Create and pack widgets within the input frame
length_label = tk.Label(input_frame, text="Enter password length:")
length_label.grid(row=0, column=0, sticky="w")

length_entry = tk.Entry(input_frame)
length_entry.grid(row=0, column=1, padx=10)

complexity_label = tk.Label(input_frame, text="Select complexity:")
complexity_label.grid(row=1, column=0, sticky="w")

complexity_var = tk.StringVar()
complexity_var.set("Medium")  # Default complexity option
complexity_options = ["Weak", "Medium", "Strong"]
complexity_menu = tk.OptionMenu(input_frame, complexity_var, *complexity_options)
complexity_menu.grid(row=1, column=1, padx=10)

generate_button = tk.Button(input_frame, text="Generate Password", command=generate_password)
generate_button.grid(row=2, columnspan=2, pady=10)

# frame for the result label
result_frame = tk.Frame(window)
result_frame.pack(fill=tk.BOTH, expand=True)

# Create and pack the result label within the result frame
result_label = tk.Label(result_frame, text="", font=("Helvetica", 14))
result_label.pack(padx=10, pady=10)

window.mainloop()

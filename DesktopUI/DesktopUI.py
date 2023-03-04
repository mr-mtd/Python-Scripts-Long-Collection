import tkinter as tk

# Create a new window
window = tk.Tk()
window.title("My GUI")

# Define a function to display a message when the button is clicked
def button_click():
    message_label.config(text="Hello, world!")

# Create a label to display the message
message_label = tk.Label(window, text="Click the button to display a message.")
message_label.pack()

# Create a button to trigger the message display
button = tk.Button(window, text="Click me", command=button_click)
button.pack()

# Run the GUI loop
window.mainloop()


if __name__ == '__main__':
    window.mainloop()
    button_click()
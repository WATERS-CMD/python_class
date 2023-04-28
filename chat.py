import tkinter as tk
from tkinter import scrolledtext, messagebox, simpledialog

class ChatArea:
    def __init__(self, master):
        self.master = master
        self.master.title("AIR CHATS")

        # Create chat box
        self.chat_box = scrolledtext.ScrolledText(self.master, height=20, width=50)
        self.chat_box.pack(padx=10, pady=10)

        # Create input box
        self.input_box = tk.Entry(self.master, width=50)
        self.input_box.pack(padx=10, pady=10)

        # Create send button
        self.send_button = tk.Button(self.master, text="Send", command=self.send_message)
        self.send_button.pack(padx=10, pady=10)

    def send_message(self):
        message = self.input_box.get()
        if not message:
            messagebox.showwarning("Warning", "Please enter a message.")
            return
        self.chat_box.configure(state="normal")
        self.chat_box.insert(tk.END, f"You: {message}\n")
        self.chat_box.configure(state="disabled")
        self.input_box.delete(0, tk.END)
        
       
        # Simulate receiving a response after 1 second
        self.master.after(1000, self.receive_response)

    def receive_response(self):
        response = simpledialog.askstring("Response", "Enter a response:")
        if not response:
            return
        self.chat_box.configure(state="normal")
        self.chat_box.insert(tk.END, f"Bot: {response}\n")
        self.chat_box.configure(state="disabled")
        self.chat_box.align(right)
root = tk.Tk()
app = ChatArea(root)
root.mainloop()

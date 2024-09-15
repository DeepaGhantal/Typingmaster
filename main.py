import tkinter as tk
from tkinter import messagebox
import time

class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.sample_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex."

        self.sample_text_label = tk.Label(root, text=self.sample_text, wraplength=400)
        self.sample_text_label.pack()

        self.entry_field = tk.Text(root, height=10, width=40)
        self.entry_field.pack()

        self.start_time = time.time()
        self.start_button = tk.Button(root, text="Start", command=self.start_test)
        self.start_button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def start_test(self):
        self.start_button.config(state="disabled")
        self.entry_field.focus()
        self.start_time = time.time()

    def check_test(self, event):
        end_time = time.time()
        elapsed_time = end_time - self.start_time
        typed_text = self.entry_field.get("1.0", "end-1c")
        num_words = len(typed_text.split())
        wpm = num_words / (elapsed_time / 60)
        self.result_label.config(text=f"Your typing speed is {wpm:.2f} words per minute.")

    def run(self):
        self.root.bind("<Return>", self.check_test)
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTest(root)
    app.run()
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file(window, text_edit):
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt")])

    if not filepath:
        return

    text_edit.delete(1.0, tk.END)
    with open(filepath, "r") as f:
        content = f.read()
        text_edit.insert(tk.END, content)
    window.title(f"Open File: {filepath}")

def save_file(window, text_edit):
    filepath = asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])

    if not filepath:
        return

    with open(filepath, "w") as f:
        content = text_edit.get(1.0, tk.END)
        f.write(content)
    window.title(f"Saved File: {filepath}")

def main():
    window = tk.Tk()
    window.title("Text Editor")
    window.rowconfigure(0, minsize=400, weight=1)
    window.columnconfigure(1, minsize=500, weight=1)

    text_edit = tk.Text(window, font="Helvetica 18", bg="#F0F8FF", fg="#000080", insertbackground="#FF4500")
    text_edit.grid(row=0, column=1, sticky="nsew")

    frame = tk.Frame(window, relief=tk.RAISED, bd=2, bg="#4682B4")
    save_button = tk.Button(frame, text="Save", command=lambda: save_file(window, text_edit), bg="#B0C4DE", fg="#000080")
    open_button = tk.Button(frame, text="Open", command=lambda: open_file(window, text_edit), bg="#B0C4DE", fg="#000080")

    save_button.grid(row=0, column=0, padx=5, pady=5)
    open_button.grid(row=1, column=0, padx=5, pady=5)
    frame.grid(row=0, column=0, sticky="ns")

    window.bind("<Control-s>", lambda event: save_file(window, text_edit))
    window.bind("<Control-o>", lambda event: open_file(window, text_edit))
    window.mainloop()

main()

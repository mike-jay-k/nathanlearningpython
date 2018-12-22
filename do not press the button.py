
import tkinter
window = tkinter.Tk()
button = tkinter.Button(window, text="Do not press this button", width=50)
button.pack(padx=10, pady=10)
clickcount = 0
def onClick(event):
    global clickcount
    clickcount = clickcount + 10-,
    if clickcount == 1:
        button.configure(text="seriusly? do.not.press it!")
    elif clickcount == 2:
        button.configure(text="Gha! You nevr liston,do you? Next time no more button ")
    else:
        button.pack_forget()
button.bind("<ButtonRelease-1>", onClick)
window.mainloop()

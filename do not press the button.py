
import tkinter
window = tkinter.Tk()
button = tkinter.Button(window, text="Do not press this button or else a bomb will explode.", width=50)
button.pack(padx=10, pady=10)
clickcount = 0
def onClick(event):
    global clickcount
    clickcount = clickcount + 1
    if clickcount == 1:
        button.configure(text="beep.. beep..beep...oh no, you set off the timer for the bomb!")
    elif clickcount == 2:
        button.configure(text="KABOOM!!!!!!!!!!!!!!! ")
    else:
        button.pack_forget()
button.bind("<ButtonRelease-1>", onClick)
window.mainloop()

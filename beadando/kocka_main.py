from tkinter import *
import kocka_fuggv


window = Tk()
window.wm_minsize(500, 465)
window.maxsize(500, 465)
window.title("Kocka dobás")


def kiiras(args):
    lbl2['text']= kocka_fuggv.dobas(args)


# panelok
lbl1 = Label(window, text="Válasszon egy kockát!", foreground="red", font="courier 15 bold")
lbl2 = Label(window, text="", foreground="red", font="courier 15 bold")
lbl1.place(x=120, y=2)
lbl2.place(x=120, y=200)

# gombok
btn4 = Button(window, text="D4", height=3, width=10, borderwidth=3, command=lambda:kiiras(4))
btn6 = Button(window, text="D6", height=3, width=10, borderwidth=3, command=lambda:kiiras(6))
btn8 = Button(window, text="D8", height=3, width=10, borderwidth=3, command=lambda:kiiras(8))
btn10 = Button(window, text="D10", height=3, width=10, borderwidth=3, command=lambda:kiiras(10))
btn12 = Button(window, text="D12", height=3, width=10, borderwidth=3, command=lambda:kiiras(12))
btn20 = Button(window, text="D20", height=3, width=10, borderwidth=3, command=lambda:kiiras(20))
btn100 = Button(window, text="D100", height=3, width=10, borderwidth=3, command=lambda:kiiras(100))

btn4.place(x=5, y=40)
btn6.place(x=100, y=40)
btn8.place(x=200, y=40)
btn10.place(x=300, y=40)
btn12.place(x=400, y=40)
btn20.place(x=150, y=110)
btn100.place(x=250, y=110)

window.mainloop()
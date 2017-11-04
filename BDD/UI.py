"""
User Interface to edit PCN data and generate COBDD, ROBDD and ITE.

"""

import tkinter as Tkinter
from COBDD import cobdd
from ROBDD import robdd
from ITE import ite_master
import webbrowser


def opentxtfile():
    url = "file:///Users/arvindkumar/Documents/My%20Documents/Academics/5th%20Sem/SDC/Project/PCN_data.txt"
    path = 'open -a /Applications/TextEdit.app %s'
    webbrowser.get(path).open(url)

if __name__ == "__main__":

    top = Tkinter.Tk()

    top.title("Binary Decision Diagrams")

    w = 300  # width for the Tk root
    h = 300  # height for the Tk root
    ws = top.winfo_screenwidth()  # width of the screen
    hs = top.winfo_screenheight()  # height of the screen
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    top.geometry('%dx%d+%d+%d' % (w, h, x, y))

    # Creating Buttons
    A = Tkinter.Button(top, text="Change Input File Contents", command=lambda: opentxtfile)
    B = Tkinter.Button(top, text="Complete Order B.D.D", command=lambda: cobdd)
    C = Tkinter.Button(top, text="Reduced Order B.D.D", command=lambda: robdd)
    D = Tkinter.Button(top, text="Recursive ITE", command=lambda: ite_master)
    w = Tkinter.Label(top, text="\n\n\n\n\nMade By\nArvind .S. Kumar\nShantanu Vijay\nSripathi M")

    A.pack()
    B.pack()
    C.pack()
    D.pack()
    w.pack()

    top.mainloop()

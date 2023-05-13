from Remote_GUI import *
from tkinter import *


def main():
    """
    - Change the window title to 'Lab 10'.
    - Set its length to 250 and height to 200.
    - Make the window non-resizable.
    """
    window = Tk()
    window.title("Remote")
    window.geometry("250x400")
    window.resizable(False, False)
    GUI(window)
    window.mainloop()

if __name__ == '__main__':
    main()

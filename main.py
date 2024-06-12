from tkinter import Tk
from MainPage import MainPage


class Main:
    @staticmethod
    def main():
        root = Tk()
        root.title('SIS v0.0.5')
        MainPage(master=root)
        root.mainloop()


if __name__ == '__main__':
    Main.main()

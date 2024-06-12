import tkinter as tk
from views import AboutFrame, InsertFrame, SearchFrame, DeleteFrame, UpdateFrame


class MainPage:
    def __init__(self, master: tk.Tk):
        self.root = master
        self.root.geometry('600x400')
        self.create_page()

        self.insert_frame = InsertFrame(self.root)
        self.search_frame = SearchFrame(self.root)
        self.delete_frame = DeleteFrame(self.root)
        self.update_frame = UpdateFrame(self.root)
        self.about_frame = AboutFrame(self.root)

        self.show_about_frame()

    def create_page(self):
        menu_bar = tk.Menu(self.root)
        menu_bar.add_command(label='Add', command=self.show_insert_frame)
        menu_bar.add_command(label='Search', command=self.show_search_frame)
        menu_bar.add_command(label='Delete', command=self.show_delete_frame)
        menu_bar.add_command(label='Update', command=self.show_update_frame)
        menu_bar.add_command(label='About', command=self.show_about_frame)
        self.root['menu'] = menu_bar

    def show_insert_frame(self):
        self.insert_frame.pack()
        self.search_frame.forget()
        self.delete_frame.forget()
        self.update_frame.forget()
        self.about_frame.forget()

    def show_search_frame(self):
        self.insert_frame.forget()
        self.search_frame.pack()
        self.delete_frame.forget()
        self.update_frame.forget()
        self.about_frame.forget()

    def show_delete_frame(self):
        self.insert_frame.forget()
        self.search_frame.forget()
        self.delete_frame.pack()
        self.update_frame.forget()
        self.about_frame.forget()

    def show_update_frame(self):
        self.insert_frame.forget()
        self.search_frame.forget()
        self.delete_frame.forget()
        self.update_frame.pack()
        self.about_frame.forget()

    def show_about_frame(self):
        self.insert_frame.forget()
        self.search_frame.forget()
        self.delete_frame.forget()
        self.update_frame.forget()
        self.about_frame.pack()


if __name__ == '__main__':
    root = tk.Tk()
    root.title('SIS v0.0.5')

    MainPage(master=root)

    root.mainloop()

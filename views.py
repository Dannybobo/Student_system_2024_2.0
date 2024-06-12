import tkinter as tk
from tkinter import ttk
from db import db


class InsertFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(master=root)

        self.name = tk.StringVar()
        self.math = tk.StringVar()
        self.chinese = tk.StringVar()
        self.english = tk.StringVar()
        self.status = tk.StringVar()

        self.create_page()

    def create_page(self):
        tk.Label(self).grid(row=0, pady=10)

        tk.Label(self, text='Name').grid(row=1, column=1, pady=10, sticky=tk.E)
        tk.Entry(self, textvariable=self.name).grid(
            row=1, column=2, pady=10)

        tk.Label(self, text='Math').grid(row=2, column=1, pady=10, sticky=tk.E)
        tk.Entry(self, textvariable=self.math).grid(
            row=2, column=2, pady=10)

        tk.Label(self, text='Chinese').grid(
            row=3, column=1, pady=10, sticky=tk.E)
        tk.Entry(self, textvariable=self.chinese).grid(
            row=3, column=2, pady=10)

        tk.Label(self, text='English').grid(
            row=4, column=1, pady=10, sticky=tk.E)
        tk.Entry(self, textvariable=self.english).grid(
            row=4, column=2, pady=10)

        tk.Button(self, text='Add', command=self.add).grid(
            row=5, column=2, sticky=tk.E)
        tk.Label(self, textvariable=self.status).grid(
            row=6, column=2, sticky=tk.E)

    def add(self):
        record = {'name': self.name.get(),
                  'math': self.math.get(),
                  'chinese': self.chinese.get(),
                  'english': self.english.get()}

        self.name.set('')
        self.math.set('')
        self.chinese.set('')
        self.english.set('')

        print(record)
        message = db.insert(record)
        self.status.set(message)


class SearchFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(master=root)

        self.table_view = tk.Frame()
        self.table_view.pack()

        self.create_page()

    def create_page(self):
        columns = ('name', 'chinese', 'math', 'english')
        columns_values = ('Name', 'Chinese', 'Math', 'English')

        self.tree_view = ttk.Treeview(self, show='headings', columns=columns)
        self.tree_view.column('name', width=100, anchor='center')
        self.tree_view.column('chinese', width=100, anchor='center')
        self.tree_view.column('math', width=100, anchor='center')
        self.tree_view.column('english', width=100, anchor='center')
        self.tree_view.heading('name', text='Name')
        self.tree_view.heading('chinese', text='Chinese')
        self.tree_view.heading('math', text='Math')
        self.tree_view.heading('english', text='English')
        self.tree_view.pack(fill=tk.BOTH, expand=True)

        self.show_data_frame()
        tk.Button(self, text='Refresh', command=self.show_data_frame).pack(
            anchor=tk.E, pady=10)

    def show_data_frame(self):
        for _ in map(self.tree_view.delete, self.tree_view.get_children('')):
            pass

        students = db.get_all()

        index = 0
        for stu in students:
            self.tree_view.insert(
                '', index+1, values=(stu['name'], stu['math'], stu['chinese'], stu['english']))


class DeleteFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(master=root)

        self.name = tk.StringVar()
        self.status = tk.StringVar()

        tk.Label(self, text='Use name to delete a data').pack()
        tk.Entry(self, textvariable=self.name).pack()
        tk.Button(self, text='Delete', command=self.delete).pack()
        tk.Label(self, textvariable=self.status).pack()

    def delete(self):
        flag, message = db.delete_by_name(self.name.get())
        self.status.set(message)


class UpdateFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(master=root)

        self.name = tk.StringVar()
        self.math = tk.StringVar()
        self.chinese = tk.StringVar()
        self.english = tk.StringVar()
        self.status = tk.StringVar()

        self.create_page()

    def create_page(self):
        tk.Label(self).grid(row=0, pady=10)

        tk.Label(self, text='Name').grid(row=1, column=1, pady=10, sticky=tk.E)
        tk.Entry(self, textvariable=self.name).grid(
            row=1, column=2, pady=10)

        tk.Label(self, text='Math').grid(row=2, column=1, pady=10, sticky=tk.E)
        tk.Entry(self, textvariable=self.math).grid(
            row=2, column=2, pady=10)

        tk.Label(self, text='Chinese').grid(
            row=3, column=1, pady=10, sticky=tk.E)
        tk.Entry(self, textvariable=self.chinese).grid(
            row=3, column=2, pady=10)

        tk.Label(self, text='English').grid(
            row=4, column=1, pady=10, sticky=tk.E)
        tk.Entry(self, textvariable=self.english).grid(
            row=4, column=2, pady=10)

        tk.Button(self, text='Search', command=self.search_record).grid(
            row=5, column=1, sticky=tk.E)
        tk.Button(self, text='Update', command=self.update_record).grid(
            row=5, column=2, sticky=tk.E)

        tk.Label(self, textvariable=self.status).grid(
            row=6, column=2, sticky=tk.E)

    def search_record(self):
        flag, record = db.search_by_name(self.name.get())
        if flag:
            self.name.set(record['name'])
            self.math.set(record['math'])
            self.chinese.set(record['chinese'])
            self.english.set(record['english'])

            self.status.set('Data found')
        else:
            self.status.set(record)

    def update_record(self):
        record = {'name': self.name.get(),
                  'math': self.math.get(),
                  'chinese': self.chinese.get(),
                  'english': self.english.get()}

        self.name.set('')
        self.math.set('')
        self.chinese.set('')
        self.english.set('')

        db.update_data(record)
        self.status.set('Update success')


class AboutFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(master=root)

        tk.Label(self, text='Copyright©2024 DannyBOBO').pack()

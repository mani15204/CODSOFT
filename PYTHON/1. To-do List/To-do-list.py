import tkinter as tk
from tkinter import *
from tkinter.constants import *

def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        # nothing to add
        pass


def delete_task():
    try:
        index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(index)
    except IndexError:
        # Nothing to delete
        pass

root = Tk()
root.geometry("500x500")


lbl_title = Label(root, text="To-do-List", font=('Times',25))
lbl_title.grid(row=0, column=0, columnspan=4, padx=190,pady=5)

lbl_enter = Label(root, text="Enter new task: ", font=('Times',15))
lbl_enter.grid(row=1, column=0, columnspan=2, padx=100, pady=50)

entry_task = Entry(root, width=25)
entry_task.grid(row=1, column=1, columnspan=3, padx=100,pady=50)

btn_add = Button(root, text='Add Task', command=add_task)
btn_add.grid(row=2, column=0, columnspan=2, padx=100)

btn_delete = Button(root, text='Delete Task', command=delete_task)
btn_delete.grid(row=2, column=1, columnspan=2, padx=100)

listbox_tasks = Listbox(root, height=10, width=50, border=0)
listbox_tasks.grid(row=3, column=0, columnspan=3, padx=100, pady=40)
root.mainloop()
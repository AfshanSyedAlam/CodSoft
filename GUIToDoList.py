import tkinter
import tkinter.messagebox
import pickle


root = tkinter.Tk()
root.title("To-Do List")


def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tkinter.END, task)
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="You must enter a task.")


def completed_task():
    try:
        marked = listbox_tasks.curselection()
        temp = marked[0]
        temp_marked = listbox_tasks.get(marked)
        temp_marked = temp_marked + " ✔"
        listbox_tasks.delete(temp)
        listbox_tasks.insert(temp, temp_marked)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task.")


def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task.")


def load_tasks():
    try:
        tasks = pickle.load(open("tasks.dat", "rb"))
        listbox_tasks.delete(0, tkinter.END)
        for task in tasks:
            listbox_tasks.insert(tkinter.END, task)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="Cannot find tasks.dat")


def save_tasks():
    tasks = listbox_tasks.get(0, listbox_tasks.size())

    pickle.dump(tasks, open("tasks.dat", "wb"))


frame_tasks = tkinter.Frame(master=root, width=5, height=5)
frame_tasks.pack()


listbox_tasks = tkinter.Listbox(frame_tasks, height=15, width=50)
listbox_tasks.pack(side=tkinter.LEFT, fill=tkinter.Y)

entry_task = tkinter.Entry(root, width=50)
entry_task.pack()

button_add_task = tkinter.Button(root, text="Add task", cursor="hand2", width=48, command=add_task)
button_add_task.pack()

button_completed_task= tkinter.Button(root, text="Completed ", cursor="hand2", width=48, command=completed_task)
button_completed_task.pack()

button_delete_task = tkinter.Button(root, text="Delete task", cursor="hand2", width=48, command=delete_task)
button_delete_task.pack()

button_load_task = tkinter.Button(root, text="Load task", width=48, command=load_tasks)
button_load_task.pack()

button_save_task = tkinter.Button(root, text="Save task", width=48, command=save_tasks)
button_save_task.pack()

root.mainloop()

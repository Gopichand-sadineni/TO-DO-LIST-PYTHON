from tkinter import *
from tkinter import messagebox
no_of_tasks = 0
def add_task():
    global no_of_tasks
    no_of_tasks+= 1
    task=new_task.get()
    tasks.insert(no_of_tasks,task)
def delete_task():
    if tasks.curselection():
        tasks.delete(tasks.curselection())
    else:
        messagebox.showwarning(title='WARNING!', message='select the task to delete')
window = Tk()
window.geometry("900x500")
window.title("TO-DO LIST")
window.config(background='white')
heading=Label(window,
              text='enter the task',
              font=('Times New Roman',25,'bold'),
              bd=2,
              relief=RAISED,
              padx=10,
              pady=10)

new_task=Entry(window,
        font=('Cambria',25),
        bd=2,
        relief='solid')
new_task.place(x=0,y=60)
heading.place(x=0,y=0)
add = Button(window,
           font=('Arial',15),
           text="ADD",
           command=add_task,
           bd=2,
           relief='solid')
add.place(x=370,y=60)
delete = Button(window,
                font=('Arial',15),
                bd=2,
                text='COMPLETED',
                relief='solid',
                command=delete_task)
delete.place(x=430,y=60)
tasks = Listbox(window,
                bg='#b7f7f1',
                font = ('Lucida Sans',20),
                width=45,
                height=0)
tasks.config(height=tasks.size())
tasks.place(x=0,y=110)

window.mainloop()

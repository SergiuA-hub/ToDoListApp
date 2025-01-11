from tkinter import*
import tkinter.messagebox

#Main app settings
window = Tk()
window.title("To do list App")
window.geometry('600x500')


#Frame for the items to stay
items_frame = Frame(window)
items_frame.pack()


#Listbox Hold the items
listbox_hold = Listbox(items_frame,bg="grey",height=25,width=90, )
listbox_hold.pack(side=tkinter.LEFT)

#Scrollbar for the task in case of multiple tasks at once 
scrollbar_frame = Scrollbar(items_frame)
scrollbar_frame.pack(side=tkinter.RIGHT,fill=tkinter.Y)
listbox_hold.config(yscrollcommand=scrollbar_frame.set)
scrollbar_frame.config(command=listbox_hold.yview)

# Adding selected item function
def addtask():
    def add():
        input_text = add_task.get(1.0, "end-1c")
        if input_text == "":
            tkinter.messagebox.showwarning(title="Warning!", message="Please Enter some Text")
        else:
            listbox_hold.insert(END, input_text)
            root1.destroy()

    root1 = Tk()
    root1.title("Add task")
    add_task = Text(root1, width=40, height=3)
    add_task.pack()
    button_temp = Button(root1, text="Add task", command=add)
    button_temp.pack()
    root1.mainloop()

# Button for ADD TASK
add_button = Button(window, text="Add Task", width=50, command=addtask)
add_button.pack()

#Deleting selected item function

def deletetask():
    selected =listbox_hold.curselection()
    listbox_hold.delete(selected[0])

#Button for deleting tasks

delete_button = Button(window,text="Delete Task",width=50,command=deletetask)
delete_button.pack()

#Marking done tasks function

def marktasks():
    marked =listbox_hold.curselection()
    temp = marked[0]

    temp_marked = listbox_hold.get(marked)
    temp_marked =temp_marked+"✔"
    listbox_hold.delete(temp)
    listbox_hold.insert(temp,temp_marked)

    

#Button for mark task as done 
mark_task = Button(window,text="Mark Tast Done",width=50,command=marktasks)
mark_task.pack()




window.mainloop()






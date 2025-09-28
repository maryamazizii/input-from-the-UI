from tkinter import *
from tkinter import messagebox
win = Tk()
win.geometry('340x270')
win.resizable(0,0)
win.title('Input Data')

def add():
    name = ent_name.get()
    code = ent_code.get()
    score = ent_score.get()
    if not name or not code or not score:
        messagebox.showerror('Error','fill all of the fields!')
    elif len(code) != 10:
        messagebox.showerror('Error','Personality code must equal 10 numbers!')
    elif not code.isdigit():
        messagebox.showerror('Error','Personality code must be number ; not srtring!')
    elif  not score.isdigit():
        messagebox.showerror('Error','score must be number ; not srtring!')
    elif int(score) >= 0 and int(score) <= 20:
        lst_data.insert(END,f'{name},{code},{score}')
    else:
        messagebox.showerror('Error','Score must between 0 to 20!')
        clear()

def select():
    index = lst_data.curselection()
    datas = lst_data.get(index)
    lst = datas.split(',')
    ent_name.insert(END,lst[0])
    ent_code.insert(END,lst[1])
    ent_score.insert(END,lst[2])

def clear():
    ent_name.delete(0,END)    
    ent_code.delete(0,END)    
    ent_score.delete(0,END)    

def exit():
    q = messagebox.askquestion('U sure?','Are U sure to exit?')
    if q == 'yes':
        win.destroy()       

def delete():
    index = lst_data.curselection()
    if index:
        q = messagebox.askquestion('U sure?','Are U sure to delet this item?')
        if q == 'yes':
            lst_data.delete(index)
    

lbl_name = Label(win,text='Name:',font='arial 13')
lbl_name.place(x=10 , y=5 )

lbl_code = Label(win,text='Personality Code:',font='arial 13')
lbl_code.place(x=10 , y=40 )

lbl_score = Label(win,text='Score:',font='arial 13')
lbl_score.place(x=10 , y=75 )

ent_name = Entry(win,font='arial 13')
ent_name.place(x=150 , y=8)

ent_code = Entry(win,font='arial 13')
ent_code.place(x=150 , y=39)

ent_score = Entry(win,font='arial 13')
ent_score.place(x=150 , y=74)

lst_data = Listbox(win,width=30,height=9)
lst_data.place(x=150 , y=105)

btn_add = Button(win,text='Add',width=15,command=add)
btn_add.place(x=10 , y=110)

btn_select = Button(win,text='Select',width=15,command=select)
btn_select.place(x=10 , y=140)

btn_del = Button(win,text='Delete',width=15,command=delete)
btn_del.place(x=10 , y=170)

btn_clear = Button(win,text='Clear',width=15,command=clear)
btn_clear.place(x=10 , y=200)

btn_exit = Button(win,text='Exit',width=15,command=exit)
btn_exit.place(x=10 , y=230)



win.mainloop()
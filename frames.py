import tkinter as tk
import tkinter.ttk as ttk
from db import Product

def create_login_window(master):
    frm_login_window = ttk.Frame(
        master=master,
        name="frm_login_window",
        width=350,
        height=350,
    )

    frm_lgn = ttk.Frame(
        master=frm_login_window,
        name="frm_login"
    )

    lbl_lgn = ttk.Label(
        master=frm_lgn,
        name="lbl_login",
        anchor=tk.E,
        width=8,
        text="Логин:",
        font=("Arial", 14),
    )

    ent_lgn = ttk.Entry(
        master=frm_lgn,
        name="ent_login",
        font=("Arial", 14)
    )

    frm_pwd = ttk.Frame(
        master=frm_login_window,
        name="frm_password"
    )

    lbl_pwd = ttk.Label(
        master=frm_pwd,
        anchor=tk.E,
        width=8,
        text="Пароль:",
        font=("Arial", 14),
    )

    ent_pwd = ttk.Entry(
        master=frm_pwd,
        name="ent_password",
        font=("Arial", 14),
        show="*",
    )

    btn_lgn = ttk.Button(
        master=frm_login_window,
        name="btn_login",
        text="Войти",
    )

    frm_lgn.pack(side=tk.TOP, fill=tk.X, pady=(60, 40))
    frm_lgn.columnconfigure(0, weight=1)
    frm_lgn.columnconfigure(0, weight=1)
    lbl_lgn.grid(column=0, row=0, sticky=tk.W)
    ent_lgn.grid(column=1, row=0, sticky=tk.E, ipady=5)

    frm_pwd.pack(side=tk.TOP, fill=tk.X, pady=(0, 80))
    frm_pwd.columnconfigure(0, weight=1)
    frm_pwd.columnconfigure(0, weight=1)
    lbl_pwd.grid(column=0, row=0, sticky=tk.W)
    ent_pwd.grid(column=1, row=0, sticky=tk.E, ipady=5)

    btn_lgn.pack(side=tk.TOP, ipady=5, ipadx=5)

    return frm_login_window


def create_admin_window(master):
    frm_admin_window = ttk.Frame(
        master=master,
        width=960,
        height=540,
    )

    trv_users = ttk.Treeview(
        master=frm_admin_window,
        columns=("#1", "#2", "#3"),
        yscrollcommand=ttk.Scrollbar()
    )

    trv_users.heading("#0", text="Имя пользователя")
    trv_users.heading("#1", text="Логин")
    trv_users.heading("#2", text="Пароль")
    trv_users.heading("#3", text="Роль")


    trv_users.pack(expand=True)

    return frm_admin_window


def Cntrea(tree,name):
    tree.column(name, anchor="center")
    

def create_director_window(master):
    frm_dir= ttk.Frame(master=master,
                        width = 960,
                        height = 540)


    columns = ("num", "name", "product","quantity","time")
    tree = ttk.Treeview(master=frm_dir,columns=columns, show="headings")
    for col in columns: Cntrea(tree,col)

    tree.heading("num", text="Номер заказа")
    tree.heading("name", text="Имя клиента")
    tree.heading("product", text="Название товара")
    tree.heading("quantity", text="Количество")
    tree.heading("time", text="Оставшийся срок")


    for string in Product.All(): 
        tree.insert("", tk.END, values=string)

    scrollbar = ttk.Scrollbar(orient=tk.VERTICAL, command=tree.yview, master = tree)
    tree.config(yscrollcommand=scrollbar.set)

    add_bt = ttk.Button(master =frm_dir,text ="Добавить", name = "btn_open_add")
    edit_bt = ttk.Button(master =frm_dir,text ="Изменить", name = "btn_edit"  ) 
    del_bt = ttk.Button(master =frm_dir,text = "Удалить", name = "btn_del")


    tree.pack(fill=tk.Y, expand=True)
    add_bt.pack(side=tk.LEFT)
    edit_bt.pack(side=tk.LEFT)
    del_bt.pack(side=tk.LEFT)
    # scrollbar.pack(side=tk.RIGHT, fill=tk.Y, in_=frm_dir)
    

    return frm_dir

def NewBlock(master: tk.Tk, text: str, name: str) -> tuple[ttk.Frame, ttk.Label, ttk.Entry]:
    new_frm=ttk.Frame(
        master=master,
        name=f"frm_{name}",
    )
    new_lab = ttk.Label(
        master=new_frm,
        justify=tk.CENTER,
        width=20,
        text=text,
        font=("Arial", 14),
    )
    new_ent = ttk.Entry(
        master=new_frm,
        name=f"ent_{name}",
        font=("Arial", 14),
    )
    new_frm.pack()
    new_lab.pack()
    new_ent.pack()
    return new_frm, new_lab, new_ent

#catmeme top

def create_add_window(master):
    frm_add= ttk.Frame(master=master,
                       name="frm_add_window",
                        width = 640,
                        height = 320)
    
    NewBlock(frm_add,"Номер заказа", "num")
    NewBlock(frm_add,"Название товара", "prod")
    NewBlock(frm_add,"Количество", "quantity")
    NewBlock(frm_add,"Дата отгрузки", "time")
    NewBlock(frm_add,"Заказчик", "name")

    ok_bt = ttk.Button(master =frm_add,text ="Принять", name="btn_add")
    ok_bt.pack()

    return frm_add
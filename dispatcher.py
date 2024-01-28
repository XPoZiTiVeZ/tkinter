import tkinter as tk
import tkinter.ttk as ttk
from frames import *
from functions import *

dev=True

def clear_all(root):
    for widget in root.winfo_children():
        widget.destroy()


def dispatcher(root: tk.Tk, path: str):
    page = path.split("/")[1:]
    
    print(page)
    
    lbl_message = ttk.Label(
        master=root,
        name="lbl_message",
    )
    lbl_message.place(relx=0.5, y="60", anchor="center")
    
    if page[0].split("?")[0] == "login":
        args = page[-1].split("?")
        if len(args) > 1:
            messages = args[1:]
            
            for message in messages:
                code = message.split("=")[0]
                value = message.split("=")[1]
                lbl_message: ttk.Label = root.nametowidget("lbl_message")
                
                if value == "UserNotFound":
                    clear_all(root)
                    lbl_message.config(text="Пользователь не найден")
                    
                    frm_login_window = create_login_window(root)
                    frm_login_window.nametowidget("btn_login").bind("<Button-1>", lambda _: dispatcher(root, login(frm_login_window)))
                    frm_login_window.pack(expand=True)
                    frm_login_window.pack_propagate(False)
                
                elif code == "IncorrectRole":
                    clear_all(root)
                    lbl_message.config(text="Неправильная роль полльзователя")
                    
                    frm_login_window = create_login_window(root)
                    frm_login_window.nametowidget("btn_login").bind("<Button-1>", lambda _: dispatcher(root, login(frm_login_window)))
                    frm_login_window.pack(expand=True)
                    frm_login_window.pack_propagate(False)

        else:
            clear_all(root)
            frm_login_window = create_login_window(root)
            frm_login_window.nametowidget("btn_login").bind("<Button-1>", lambda _: dispatcher(root, login(frm_login_window)))
            frm_login_window.pack(expand=True)
            frm_login_window.pack_propagate(False)
        
        btn_exit = ttk.Button(
            master=root,
            text="Выйти",
        )
        
        btn_log_as_admin = ttk.Button(
            master=root,
            text="Войти как администратор",
        )
        
        btn_log_as_director = ttk.Button(
            master=root,
            text="Войти как директор",
        )
        
        btn_log_as_worker = ttk.Button(
            master=root,
            text="Войти как работник",
        )
        global dev
        if dev:
            btn_exit.pack(side=tk.LEFT, anchor=tk.SW, ipady=5, ipadx=5, padx=10, pady=10)
            btn_exit.bind("<Button-1>", lambda _: root.destroy())
            
            btn_log_as_admin.pack(side=tk.LEFT, anchor=tk.SW, ipady=5, ipadx=5, padx=10, pady=10)
            btn_log_as_admin.bind("<Button-1>", lambda _: dispatcher(root, "/administrator"))
            
            btn_log_as_director.pack(side=tk.LEFT, anchor=tk.SW, ipady=5, ipadx=5, padx=10, pady=10)
            btn_log_as_director.bind("<Button-1>", lambda _: dispatcher(root, "/director"))
            
            btn_log_as_worker.pack(side=tk.LEFT, anchor=tk.SW, ipady=5, ipadx=5, padx=10, pady=10)
            btn_log_as_worker.bind("<Button-1>", lambda _: dispatcher(root, "/worker"))
    
    if page[0].split("?")[0] == "administrator":
        args = page[-1].split("?")
        
        if len(args) > 1:
            pass
        
        else:
            clear_all(root)
            frm_admin_window = create_admin_window(root)
            frm_admin_window.pack(expand=True)
            frm_admin_window.pack_propagate(False)
        
        btn_exit = ttk.Button(
            master=root,
            text="Назад",
        )
        
        btn_exit.pack(side=tk.LEFT, anchor=tk.SW, ipady=5, ipadx=5, padx=10, pady=10)
        btn_exit.bind("<Button-1>", lambda _: dispatcher(root, Back()))
        
    if page[0].split("?")[0] == "director":
        if len(page) > 1 and page[1].split("?")[0] == "add_product":
            args = page[-1].split("?")
            
            if len(args) > 1:
                frm_add_window = root.nametowidget("frm_add_window")
                
                num=frm_add_window.nametowidget("frm_num").nametowidget("ent_num").get()
                name=frm_add_window.nametowidget("frm_name").nametowidget("ent_name").get()
                product=frm_add_window.nametowidget("frm_prod").nametowidget("ent_prod").get()
                quantity=frm_add_window.nametowidget("frm_quantity").nametowidget("ent_quantity").get()
                time=frm_add_window.nametowidget("frm_time").nametowidget("ent_time").get()
                
                clear_all(root)
                lbl_message: ttk.Label = root.nametowidget("lbl_message")
                lbl_message.config(text="Не все поля заполнены")
                
                frm_director_window = create_director_window(root)
                
                frm_add_window.nametowidget("frm_num").nametowidget("ent_num").config(text=num)
                frm_add_window.nametowidget("frm_name").nametowidget("ent_name").config(text=name)
                frm_add_window.nametowidget("frm_prod").nametowidget("ent_prod").config(text=product)
                frm_add_window.nametowidget("frm_quantity").nametowidget("ent_quantity").config(text=quantity)
                frm_add_window.nametowidget("frm_time").nametowidget("ent_time").config(text=time)
                
                frm_director_window.nametowidget("btn_open_add").bind("<Button-1>", lambda _: dispatcher(root, add_product()))
                frm_director_window.nametowidget("btn_edit").bind("<Button-1>", lambda _: dispatcher(root, "/director"))
                frm_director_window.nametowidget("btn_del").bind("<Button-1>", lambda _: dispatcher(root, Del()))
                frm_director_window.pack(expand=True)
                frm_director_window.pack_propagate(False)
            
            else:
                clear_all(root)
                frm_add_window = create_add_window(root)
                frm_add_window.nametowidget("btn_add").bind("<Button-1>", lambda _: dispatcher(root, add_product_confirm(frm_add_window)))
                frm_add_window.pack(expand=True)
                frm_add_window.pack_propagate(False)

            btn_exit = ttk.Button(
                master=root,
                text="Назад",
            )
            
            btn_exit.pack(side=tk.LEFT, anchor=tk.SW, ipady=5, ipadx=5, padx=10, pady=10)
            btn_exit.bind("<Button-1>", lambda _: dispatcher(root, Back_to_dir()))
            
        else:
            args = page[-1].split("?")
            
            if len(args) > 1:
                pass
            
            else:
                clear_all(root)
                frm_director_window = create_director_window(root)
                frm_director_window.nametowidget("btn_open_add").bind("<Button-1>", lambda _: dispatcher(root, add_product()))
                frm_director_window.nametowidget("btn_edit").bind("<Button-1>", lambda _: dispatcher(root, "/director"))
                frm_director_window.nametowidget("btn_del").bind("<Button-1>", lambda _: dispatcher(root, Del()))
                frm_director_window.pack(expand=True)
                frm_director_window.pack_propagate(False)
            
            btn_exit = ttk.Button(
                master=root,
                text="Назад",
            )
            
            btn_exit.pack(side=tk.LEFT, anchor=tk.SW, ipady=5, ipadx=5, padx=10, pady=10)
            btn_exit.bind("<Button-1>", lambda _: dispatcher(root, Back()))

    

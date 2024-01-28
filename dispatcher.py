import tkinter as tk
import tkinter.ttk as ttk
from frames import *
from functions import *


def clear_all(root):
    for widget in root.winfo_children():
        widget.destroy()


def dispatcher(root: tk.Tk, path: str, dev:bool=True):
    page = path.split("/")[1:]
    
    if page[0].split("?")[0] == "login":
        args = page[-1].split("?")
        if len(args) > 1:
            clear_all(root)
            messages = args[1:]
            
            lbl_message = ttk.Label(
                master=root,
                name="lbl_message",
            )
            lbl_message.place(relx=0.5, y="60", anchor="center")
            
            for message in messages:
                code = message.split("=")[0]
                value = message.split("=")[1]
                
                if value == "UserNotFound":
                    lbl_message.config(text="Пользователь не найден")
                    
                    frm_login_window = create_login_window(root)
                    frm_login_window.nametowidget("btn_login").bind("<Button-1>", lambda _: dispatcher(root, login(frm_login_window)))
                    frm_login_window.pack(expand=True)
                    frm_login_window.pack_propagate(False)
                
                elif code == "IncorrectRole":
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
                
        btn_exit.pack(side=tk.LEFT, anchor=tk.SW, ipady=5, ipadx=5, padx=10, pady=10)
        btn_exit.bind("<Button-1>", lambda _: root.destroy())

        if dev:
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
        btn_exit.bind("<Button-1>", lambda _: dispatcher(root, back()))
        
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
                messages = args[1:]
                    
                lbl_message = ttk.Label(
                    master=root,
                    name="lbl_message",
                )
                lbl_message.place(relx=0.5, y="60", anchor="center")
                
                for message in messages:
                    type = message.split("=")[0]
                    code = message.split("=")[1]
                    
                    if code == "EmptyFields":
                        lbl_message.config(text="Не все поля заполнены")
                        
                        frm_add_window = create_add_window(root)
                        frm_add_window.nametowidget("frm_num").nametowidget("ent_num").insert(0, num)
                        frm_add_window.nametowidget("frm_name").nametowidget("ent_name").insert(0, name)
                        frm_add_window.nametowidget("frm_prod").nametowidget("ent_prod").insert(0, product)
                        frm_add_window.nametowidget("frm_quantity").nametowidget("ent_quantity").insert(0, quantity)
                        frm_add_window.nametowidget("frm_time").nametowidget("ent_time").insert(0, time)
                        
                        frm_add_window.nametowidget("btn_add").bind("<Button-1>", lambda _: dispatcher(root, add_product(frm_add_window)))
                        frm_add_window.pack(expand=True)
                        frm_add_window.pack_propagate(False)
                            
            else:
                clear_all(root)
                frm_add_window = create_add_window(root)
                frm_add_window.nametowidget("btn_add").bind("<Button-1>", lambda _: dispatcher(root, add_product(frm_add_window)))
                frm_add_window.pack(expand=True)
                frm_add_window.pack_propagate(False)

            btn_exit = ttk.Button(
                master=root,
                text="Выйти",
            )
                    
            btn_exit.pack(side=tk.LEFT, anchor=tk.SW, ipady=5, ipadx=5, padx=10, pady=10)
            btn_exit.bind("<Button-1>", lambda _: root.destroy())

            btn_exit = ttk.Button(
                master=root,
                text="Назад",
            )
            
            btn_exit.pack(side=tk.LEFT, anchor=tk.SW, ipady=5, ipadx=5, padx=10, pady=10)
            btn_exit.bind("<Button-1>", lambda _: dispatcher(root, back_to_director()))
        
        elif len(page) > 1 and page[1].split("?")[0] == "edit_product":
            args = page[-1].split("?")
            
            if len(args) > 1:
                clear_all(root)
                messages = args[1:]
                    
                lbl_message = ttk.Label(
                    master=root,
                    name="lbl_message",
                )
                lbl_message.place(relx=0.5, y="60", anchor="center")
                
                for message in messages:
                    type = message.split("=")[0]
                    code = message.split("=")[1]
                    
                    if code == "NotSelected":
                        lbl_message.config(text="Изменяемый элемент не выбран")
                        
                        dispatcher(root, "/director")
                    elif code == "MultipleSelected":
                        lbl_message.config(text="Изменяемый элемент не выбран")
                        
                        dispatcher(root, "/director")
                            
            else:
                frm_director_window = root.nametowidget("frm_director_window")
                trv_product = frm_director_window.nametowidget("frm_treeview").nametowidget("trv_product")
                selected_products = trv_product.selection()
                
                if len(selected_products) == 0:
                    dispatcher(root, "/director/edit_product?error=NotSelected")

                elif len(selected_products) > 1:
                    dispatcher(root, "/director/edit_product?error=MulipleSelected")
                
                else:
                    values = trv_product.item(selected_products[0])["values"]
                    clear_all(root)
                    frm_edit_window = create_edit_window(root)
                    frm_edit_window.nametowidget("frm_num").nametowidget("ent_num").insert(0, values[1])
                    frm_edit_window.nametowidget("frm_name").nametowidget("ent_name").insert(0, values[2])
                    frm_edit_window.nametowidget("frm_prod").nametowidget("ent_prod").insert(0, values[3])
                    frm_edit_window.nametowidget("frm_quantity").nametowidget("ent_quantity").insert(0, values[4])
                    frm_edit_window.nametowidget("frm_time").nametowidget("ent_time").insert(0, values[5])
                    frm_edit_window.nametowidget("btn_edit").bind("<Button-1>", lambda _: dispatcher(root, edit_product(frm_edit_window, values[0])))
                    frm_edit_window.pack(expand=True)
                    frm_edit_window.pack_propagate(False)
                    
        elif len(page) > 1 and page[1].split("?")[0] == "delete_product":
            lbl_message = ttk.Label(
                master=root,
                name="lbl_message",
            )
            lbl_message.place(relx=0.5, y="60", anchor="center")
            
            frm_director_window = root.nametowidget("frm_director_window")
            trv_product = frm_director_window.nametowidget("frm_treeview").nametowidget("trv_product")
            selected_products = trv_product.selection()
            
            if len(selected_products) == 0:
                lbl_message.config(text="Выберите хотя бы один элемент, чтобы удалить")
            else:
                for product in selected_products:
                    selected_product = trv_product.item(product)
                    Product.Delete(selected_product["values"][0])
                    dispatcher(root, "/director")
        else:
            args = page[-1].split("?")
            
            if len(args) > 1:
                pass
            
            else:
                clear_all(root)
                frm_director_window = create_director_window(root)
                frm_director_window.nametowidget("btn_open_add").bind("<Button-1>", lambda _: dispatcher(root, show_product_add_window()))
                frm_director_window.nametowidget("btn_edit").bind("<Button-1>", lambda _: dispatcher(root, "/director/edit_product"))
                frm_director_window.nametowidget("btn_del").bind("<Button-1>", lambda _: dispatcher(root, delete_product()))
                frm_director_window.pack(expand=True)
                frm_director_window.pack_propagate(False)
            
            btn_exit = ttk.Button(
                master=root,
                text="Выйти",
            )
                    
            btn_exit.pack(side=tk.LEFT, anchor=tk.SW, ipady=5, ipadx=5, padx=10, pady=10)
            btn_exit.bind("<Button-1>", lambda _: root.destroy())

            
            btn_exit = ttk.Button(
                master=root,
                text="Назад",
            )
            
            btn_exit.pack(side=tk.LEFT, anchor=tk.SW, ipady=5, ipadx=5, padx=10, pady=10)
            btn_exit.bind("<Button-1>", lambda _: dispatcher(root, back()))
    

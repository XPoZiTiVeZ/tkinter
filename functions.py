import tkinter as tk
import tkinter.ttk as ttk
from db import User, Product


def login(frame: tk.Tk):
    ent_lgn = frame.nametowidget("frm_login").nametowidget("ent_login")
    ent_pwd = frame.nametowidget("frm_password").nametowidget("ent_password")
    user = User.authenticate(ent_lgn.get(), ent_pwd.get())
    if user != None:
        if user.role == "администратор":
            return "/administrator"
        elif user.role == "директор":
            return "/director"
        elif user.role == "работник":
            return "/login"
        else:
            print("Неправильная роль")
            return "/login?error=IncorrectRole"
    else:
        print("Неправильный логин или пароль")
        return "/login?error=UserNotFound"


def show_product_add_window():
    return "/director/add_product"

def add_product(frm_add_window: tk.Tk):
    num=frm_add_window.nametowidget("frm_num").nametowidget("ent_num").get()
    name=frm_add_window.nametowidget("frm_name").nametowidget("ent_name").get()
    product=frm_add_window.nametowidget("frm_prod").nametowidget("ent_prod").get()
    quantity=frm_add_window.nametowidget("frm_quantity").nametowidget("ent_quantity").get()
    time=frm_add_window.nametowidget("frm_time").nametowidget("ent_time").get()
    
    if not all([num, name, product, quantity, time]):
        return "/director/add_product?error=EmptyFields"

    Product.Add(
        num=num,
        name=name,
        product=product,
        quantity=quantity,
        time=time,
    )
    return "/director"

def show_product_edit_window():
    return "/director/add_product"

def edit_product(frm_edit_window: tk.Tk, id):
    num=frm_edit_window.nametowidget("frm_num").nametowidget("ent_num").get()
    name=frm_edit_window.nametowidget("frm_name").nametowidget("ent_name").get()
    product=frm_edit_window.nametowidget("frm_prod").nametowidget("ent_prod").get()
    quantity=frm_edit_window.nametowidget("frm_quantity").nametowidget("ent_quantity").get()
    time=frm_edit_window.nametowidget("frm_time").nametowidget("ent_time").get()
    
    if not all([num, name, product, quantity, time]):
        return "/director/edit_product?error=EmptyFields"

    Product.Edit(id, num, name, product, quantity, time)
    return "/director"

def delete_product():
    return "/director/delete_product"
    
def back():
    return "/login"


def back_to_director(): 
    return "/director"

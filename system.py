import tkinter as tk
from _init_ import *

root = tk.Tk()
root.title("Menu com Interface Gráfica")

menu = tk.Menu(root)
root.config(menu=menu)

submenu = tk.Menu(menu)

menu.add_cascade(label="Opções", menu=submenu)
submenu.add_command(label="Cadastro", command=opcao1)
submenu.add_command(label="Opção 2", command=opcao2)
submenu.add_command(label="Opção 3", command=opcao3)
submenu.add_command(label="Opção 4", command=opcao4)
submenu.add_command(label="Opção 5", command=opcao5)
submenu.add_separator()
submenu.add_command(label="Sair", command=sair)

submenu1 = tk.Menu(menu)
menu.add_cascade(label="Situação", menu=submenu1)

root.mainloop()
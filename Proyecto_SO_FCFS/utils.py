import tkinter as tk


def escribir_log(area_log, texto):

    area_log.insert(tk.END, texto + "\n")

    area_log.see(tk.END)
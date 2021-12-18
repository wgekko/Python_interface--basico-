#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 23:43:49 2021

@author: walter
"""

from tkinter import *

from tkinter import messagebox

from tkinter.filedialog import askopenfile, asksaveasfile



def acopiar():

    editor.clipboard_clear()

    editor.clipboard_append(editor.selection_get())

def apegar():

    editor.insert(INSERT, editor.clipboard_get())

def acortar():

    editor.clipboard_clear()

    editor.clipboard_append(editor.selection_get())

    editor.delete("sel.first", "sel.last")

def adeshacer():

    editor.edit_undo()

def arehacer():

    editor.edit_redo()

def anuevo():

    editor.delete(1.0,END)

def aabrir():

    documento = askopenfile(filetypes=[("Archivo de texto","*.txt")])

    if documento != None:

        editor.insert(1.0, documento.read())

def aguardar():

    documento = asksaveasfile(filetypes=[("Archivo de texto","*.txt")])

    print(documento.write(editor.get(1.0, END)))

def aacerca():

    messagebox.showinfo("En relación al Bloc de notas de Python", "Bloc de notas  en Python  es un lector de archivos de texto plano,"
                        
                                                         " donde el formato o extensión del archivo es de tipo txt, "

                                                         " la idea es realizar una aplicación orientada a la practica "

                                                         " el uso de interfaces gráficas, la manipulación de archivos de texto"

                                                         " y algunas funciones extra."

                                                         "\n\n"
                                                         
                                                         "un dato no menor esta aplicacion se ha agregado y a pesar de ser"

                                                         " se tiene dos funcionalidades que no tiene el hasta el momento"

                                                         " el bloc de notas tradicional de Windows, la 1ra. es la opción de rehacer,"

                                                         " la 2da. es que se puede deshacer o rehacer tantas veces"

                                                         " la intención es marcar una diferencia del bloc denotas de Windows que solo permite"

                                                         " deshacer 2 veces y la segunda cuenta como un rehacer.")





if __name__ == "__main__":



    ventana = Tk()



    menubar = Menu(ventana)

    archivo = Menu(menubar, tearoff=0)

    archivo.add_command(label="Nuevo     ", command=anuevo)

    archivo.add_command(label="Abrir     ", command=aabrir)

    archivo.add_command(label="Guardar     ", command=aguardar)

    archivo.add_command(label="Salir     ", command=ventana.quit)

    menubar.add_cascade(label="Archivo", menu=archivo)



    editar = Menu(menubar, tearoff=0)

    editar.add_command(label="Deshacer     ", command=adeshacer)

    editar.add_command(label="Rehacer     ", command=arehacer)

    editar.add_separator()

    editar.add_command(label="Copiar     ", command=acopiar)

    editar.add_command(label="Pegar     ", command=apegar)

    editar.add_command(label="Cortar     ", command=acortar)

    menubar.add_cascade(label="Edición", menu=editar)



    ayuda = Menu(menubar, tearoff=0)

    ayuda.add_command(label="Acerca de Bloc de notas ", command=aacerca)

    menubar.add_cascade(label="Ayuda", menu=ayuda)



    editor = Text(ventana, undo="true")

    editor.pack(side=TOP, fill=BOTH, expand=1)



    ventana.title(" *** Bloc de notas *** ")

    ventana.geometry("695x424")

    ventana.config(menu=menubar)

    ventana.mainloop()
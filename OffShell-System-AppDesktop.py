#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
import webbrowser
from subprocess import call
import subprocess
import commands
import os
import subprocess as sub
import Tkinter as tk

# Defino funciones

def advertencia():
	boton_Aviso=Frame(root, width=30, height=10)
	boton_Aviso.place(x=15, y=49)
	Button(boton_Aviso, command=lambda:[boton_Aviso.destroy(), instalacion()], text="Si no eres ROOT... \nUn SUDO en la consola te ayudará...\n-Clickame para Continuar-", cursor="heart", justify="center", bd=1, relief="raised", overrelief="sunken", background="black", activebackground='DarkRed', activeforeground='white', foreground='White', font=("URW Chancery L", 26)).pack()

	pass


def instalacion():

	win_instalacion = tk.Tk()
	win_instalacion.title("Luka Vision. Version Test")
	win_instalacion.geometry("600x420+330+190")
	win_instalacion.resizable(width=False, height=False)
	win_instalacion.config(width=300, height=300, cursor="heart", bg="black")

	lb1=Label(win_instalacion, width=0, anchor="e", text="La instalación ha teminado.\nDisfruta de OffSHell System Software.", font=("URW Chancery L", 18), bg="black", fg="White").pack()

	boton_volver=Frame(win_instalacion, width=50, height=60)
	boton_volver.place(x=250, y=100)
	Button(boton_volver, command=lambda:[win_instalacion.destroy()], text="Volver", cursor="heart", justify="center", bd=1, relief="raised", overrelief="sunken", background="black", activebackground='orange', activeforeground='white', foreground='orange', font=("URW Chancery L", 20)).pack()


	call('sudo apt-get install speedtest-cli', shell=True)
	call('sudo apt-get install vlc', shell=True)
	call('sudo apt-get install info', shell=True)
	call('sudo apt-get install hostname', shell=True)
	call('sudo apt-get install lshw', shell=True)
	pass


def software(): # Definición de la pantalla de Tienda de Software.
	
	boton1=tk.Frame(root, cursor="heart", background="black")
	boton1.pack()
	boton1.place(x=410, y=100)

	Button(boton1, cursor="heart", text="Software Comunidad", justify="center", bd=5, relief="raised", overrelief="sunken", background="black", activebackground='DarkRed', activeforeground='white', foreground='White', font=("URW Chancery L", 16)).pack()

	boton2=tk.Frame(root, cursor="heart", background="black")
	boton2.pack(side='top', fill=BOTH, expand=YES)
	boton2.place(x=410, y=140)

	Button(boton2, cursor="heart", text="Software OffShell System", justify="center", bd=5, relief="raised", overrelief="sunken", background="black", activebackground='DarkRed', activeforeground='white', foreground='White', font=("URW Chancery L", 16)).pack()

	boton3=tk.Frame(root, cursor="heart", background="black")
	boton3.pack(side='top', fill=BOTH, expand=YES)
	boton3.place(x=410, y=180)

	Button(boton3, cursor="heart", text="Publicar Software", justify="center", bd=5, relief="raised", overrelief="sunken", background="black", activebackground='DarkRed', activeforeground='white', foreground='White', font=("URW Chancery L", 16)).pack()

	boton4=tk.Frame(root, cursor="heart", background="black")
	boton4.pack(side='top', fill=BOTH, expand=YES)
	boton4.place(x=410, y=220)

	Button(boton4, command=lambda:[boton1.destroy(), boton2.destroy(), boton3.destroy(), boton4.destroy()], text="Salir",cursor="heart", justify="center", bd=5, relief="raised", overrelief="sunken", background="black", activebackground='DarkRed', activeforeground='white', foreground='White', font=("URW Chancery L", 16)).pack()


	pass


# Definiciones de los objetos de interacción del menu principal.

def sobreNosotros():
	botonSobre=Frame(root, width=50, height=100)
	botonSobre.pack(fill=BOTH, expand=YES)
	botonSobre.place(x=5, y=60)
	Button(botonSobre, command=lambda:[botonSobre.destroy()], cursor="heart", text="Mi nombre es Alexandre Varela Sixto.\nOffShell System Application es un proyecto pequeño de Software Libre.\nUn sueño que he cumplido programando en Python.\nUna contribución a los sistemas que respetan nuestras libertades como usuari@s,\nuna forma de agradecer a la comunidad y a la filosofía de un vínculo humano - máquina éticamente correcto...\n-- Pulsa sobre mí para continuar --", justify="center", bd=5, relief="raised", overrelief="sunken", background="black", activebackground='DarkRed', activeforeground='white', foreground='White', font=("URW Chancery L", 14)).pack()

	pass

def comunidad():

	# /Imagen de fondo.
	botonComunidad=Frame(root, width=50, height=100)
	botonComunidad.pack(fill=BOTH, expand=YES)
	botonComunidad.place(x=5, y=231)

	Button(botonComunidad, command=lambda:[botonComunidad.destroy()], cursor="heart", text="Descubre la Comunidad Underground.\nOffShell System es un proyecto destinado a los usuari@s con ganas de un cambio.\nPersonas que adoran la libertad y desarrollo constructivo.\n-- Soy un recuadro interactivo. --\n-- Pulsa sobre mí y desapareceré. -- ", justify="center", bd=5, relief="raised", overrelief="sunken", background="black", activebackground='DarkRed', activeforeground='white', foreground='White', font=("URW Chancery L", 14)).pack()

	pass

def unete():
	botonContacto=Frame(root, width=50, height=100)
	botonContacto.pack(fill=X, expand=YES)
	botonContacto.place(x=5, y=377)

	Button(botonContacto, command=lambda:[botonContacto.destroy()], cursor="heart", text="Únete a OffShell System enviando tu Nick de Usuari@ y tus proyectos a nuestro correo\n| offshell00@gmail.com |", justify="center", bd=5, relief="raised", overrelief="sunken", background="black", activebackground='DarkRed', activeforeground='white', foreground='White', font=("URW Chancery L", 15)).pack(side=TOP)

	pass


def openWeb():
	webbrowser.open_new_tab("https://www.offshellsystem.tk/p/offshell-system.html")

	botonWeb1=Frame(root, width=50, height=50)
	botonWeb1.pack(fill=BOTH, expand=YES)
	botonWeb1.place(x=5, y=570)

	Button(botonWeb1, command=botonWeb1.destroy, cursor="heart", text="Se acaba de abrir una pestaña nueva\nen tu navegador predefinido.", justify="center", bd=5, relief="raised", overrelief="sunken", background="black", activebackground='DarkRed', activeforeground='white', foreground='White', font=("URW Chancery L", 16)).pack()
	

def openWeb2():
	webbrowser.open_new_tab("https://offshellsystemconnection.blogspot.com/p/bienvenido.html")

	botonWeb2=Frame(root, width=50, height=50)
	botonWeb2.pack(fill=BOTH, expand=YES)
	botonWeb2.place(x=25, y=600)

	Button(botonWeb2, command=botonWeb2.destroy, cursor="heart", text="Se acaba de abrir una pestaña nueva\nen tu navegador predefinido.", justify="center", bd=5, relief="raised", overrelief="sunken", background="black", activebackground='DarkRed', activeforeground='white', foreground='White', font=("URW Chancery L", 16)).pack()
	
def openWeb3():
	webbrowser.open_new_tab("https://github.com/OffShellSystem")

	botonWeb3=Frame(root, width=50, height=50)
	botonWeb3.pack(fill=BOTH, expand=YES)
	botonWeb3.place(x=45, y=630)


	Button(botonWeb3, command=botonWeb3.destroy, cursor="heart", text="Se acaba de abrir una pestaña nueva\nen tu navegador predefinido.", justify="center", bd=5, relief="raised", overrelief="sunken", background="black", activebackground='DarkRed', activeforeground='white', foreground='White', font=("URW Chancery L", 16)).pack()
	

def perfilOffshell():
	webbrowser.open_new_tab("https://github.com/OffShellSystem")
	pass

def usuarios():

	root = Toplevel()
	root.title("OffShell System - Versión 'Luka' - Modo Testeo")
	root.geometry("1120x682+80+130")
	root.resizable(width=False, height=False)
	root.config(width=300, height=300, cursor="heart", bg="White")

	imagen_primate = PhotoImage(file="puertas5.gif")


	img_boton_menu=Frame(root)
	img_boton_menu.pack(fill=BOTH, expand=YES)
	img_boton_menu.place(x=0, y=0)
	Button(img_boton_menu, image=imagen_primate, cursor="heart", justify="center", bd=0, relief="flat", overrelief="flat", background="black", activebackground='darkblue', activeforeground='white', foreground='White').pack()

	botonMenu1=Frame(root, width=50, height=100)
	botonMenu1.place(x=232, y=120)
	Button(botonMenu1, text="Vacante", cursor="heart", justify="center", bd=1, relief="raised", overrelief="sunken", background="black", activebackground='DarkRed', activeforeground='orange', foreground='orange', font=("URW Chancery L", 14)).pack()

	botonMenu2=Frame(root, width=50, height=100)
	botonMenu2.place(x=415, y=120)
	Button(botonMenu2, text="Vacante", cursor="heart", justify="center", bd=1, relief="raised", overrelief="sunken", background="black", activebackground='DarkRed', activeforeground='orange', foreground='orange', font=("URW Chancery L", 14)).pack()
	botonMenu3=Frame(root, width=50, height=100)
	botonMenu3.place(x=10, y=120)
	Button(botonMenu3, command=lambda:[offShell()], text="OffShell-(Fundador)", cursor="heart", justify="center", bd=1, relief="raised", overrelief="sunken", background="black", activebackground='DarkRed', activeforeground='orange', foreground='orange', font=("URW Chancery L", 14)).pack()

	botonMenu4=Frame(root, width=50, height=100)
	botonMenu4.place(x=967, y=120)
	Button(botonMenu4, text="Vacante", cursor="heart", justify="center", bd=1, relief="raised", overrelief="sunken", background="black", activebackground='DarkRed', activeforeground='orange', foreground='orange', font=("URW Chancery L", 14)).pack()

	botonMenu5=Frame(root, width=50, height=100)
	botonMenu5.place(x=601, y=120)
	Button(botonMenu5, text="Vacante", cursor="heart", justify="center", bd=1, relief="raised", overrelief="sunken", background="black", activebackground='DarkRed', activeforeground='orange', foreground='orange', font=("URW Chancery L", 14)).pack()

	botonMenu7=Frame(root, width=50, height=100)
	botonMenu7.place(x=782, y=120)
	Button(botonMenu7, text="Vacante", cursor="heart", justify="center", bd=1, relief="raised", overrelief="sunken", background="black", activebackground='DarkRed', activeforeground='orange', foreground='orange', font=("URW Chancery L", 14)).pack()




	botonSalir=Frame(root, width=50, height=100)
	botonSalir.place(x=790, y=568)
	Button(botonSalir, command=lambda:[root.destroy()], text="Salir", cursor="heart", justify="center", bd=1, relief="raised", overrelief="sunken", background="gray", activebackground='black', activeforeground='orange', foreground='DarkRed', font=("URW Chancery L", 14)).pack()

	botonMenu_Web=Frame(root, width=50, height=100)
	botonMenu_Web.place(x=530, y=440)
	Button(botonMenu_Web, command=lambda:[openWeb2()], text="Visita la Tienda de Software\nOffShellSystem.tk", cursor="heart", justify="center", bd=1, relief="flat", overrelief="flat", background="gray", activebackground='black', activeforeground='white', foreground='black', font=("URW Chancery L", 14)).pack()

	root.mainloop()

	
	pass

def offShell():

	win_offshell = Toplevel()
	win_offshell.title("Tienda de Software OffSehll System")
	win_offshell.config(cursor="heart", bg="black")
	win_offshell.resizable(width=False, height=False)
	win_offshell.geometry("950x250+170+300")


	Label(win_offshell, width=0, anchor="n", text="Off-Shell significa una partícula sin movimiento en física cuántica.\nEscogí este alias porque estuve sin movimiento durante muchos años en el ámbito tecnológico,\nhasta que por motivos personales descubrí un mundo increíble en las comunidades de Usuari@s.\nPersonas apasionadas y colaborativas que no dudan en fomentar\nun lugar mejor donde interactuar y aprender unos de otros.\nPor tod@s y cada un@ de ell@s me encuentro aquí con vosotr@s, usuari@s del cambio.", bg="black", font=("URW Chancery L", 18), fg="Red").pack(fill=BOTH, expand=YES)

	
	botonOffGit=Frame(win_offshell, width=50, height=50)
	botonOffGit.pack()
	botonOffGit.place(x=200, y=200)

	Button(botonOffGit, command=lambda:[perfilOffshell()], cursor="heart", text="Ir a su Git Hub", justify="center", bd=5, relief="raised", overrelief="sunken", background="black", activebackground='DarkRed', activeforeground='white', foreground='White', font=("URW Chancery L", 16)).pack()

	botonOffWeb=Frame(win_offshell, width=50, height=50)
	botonOffWeb.pack()
	botonOffWeb.place(x=400, y=200)

	Button(botonOffWeb, command=lambda:[offwebperfil()], cursor="heart", text="Ir a su Web Oficial", justify="center", bd=5, relief="raised", overrelief="sunken", background="black", activebackground='DarkRed', activeforeground='white', foreground='White', font=("URW Chancery L", 16)).pack()

	botonOffSalir=Frame(win_offshell, width=50, height=50)
	botonOffSalir.pack()
	botonOffSalir.place(x=630, y=200)

	Button(botonOffSalir, command=lambda:[win_offshell.destroy()], cursor="heart", text="Volver", justify="center", bd=5, relief="raised", overrelief="sunken", background="black", activebackground='DarkRed', activeforeground='white', foreground='White', font=("URW Chancery L", 16)).pack()

	pass

def offwebperfil():
	webbrowser.open_new_tab("https://offshellsystemconnection.blogspot.com/p/bienvenido.html")

	pass


def Ram_Metricas():

	p = sub.Popen(["free"],stdout=sub.PIPE,stderr=sub.PIPE)
	output, errors = p.communicate()
	

	text = tk.Text(root, width=130, height=30)
	text.pack()
	text.place(x=55, y=20)
	text.insert(tk.END, output)




	botonVolver=Frame(root, width=50, height=100)
	botonVolver.place(x=890, y=410)
	Button(botonVolver, command=lambda:[text.destroy(), botonVolver.destroy()], text="Cerrar", cursor="heart", justify="center", bd=1, relief="raised", overrelief="sunken", background="black", activebackground='DarkRed', activeforeground='white', foreground='White', font=("URW Chancery L", 20)).pack()


	pass


def speedtest():

	p = sub.Popen(["speedtest"],stdout=sub.PIPE,stderr=sub.PIPE)
	output, errors = p.communicate()
	
	text = tk.Text(root, width=130, height=30)
	text.pack()
	text.place(x=55, y=20)
	text.insert(tk.END, output)

	botonVolver=Frame(root, width=50, height=100)
	botonVolver.place(x=890, y=410)
	Button(botonVolver, command=lambda:[text.destroy(), botonVolver.destroy()], text="Cerrar", cursor="heart", justify="center", bd=1, relief="raised", overrelief="sunken", background="black", activebackground='DarkRed', activeforeground='white', foreground='White', font=("URW Chancery L", 20)).pack()


	pass

def comandos_gnu():
	p = sub.Popen(["info"],stdout=sub.PIPE,stderr=sub.PIPE)
	output, errors = p.communicate()
	
	text = tk.Text(root, width=130, height=30)
	text.pack()
	text.place(x=55, y=20)
	text.insert(tk.END, output)

	botonVolver=Frame(root, width=50, height=100)
	botonVolver.place(x=890, y=410)
	Button(botonVolver, command=lambda:[text.destroy(), botonVolver.destroy()], text="Cerrar", cursor="heart", justify="center", bd=1, relief="raised", overrelief="sunken", background="black", activebackground='DarkRed', activeforeground='white', foreground='White', font=("URW Chancery L", 20)).pack()

	pass


def hardware_metricas():
	p = sub.Popen(["lshw"],stdout=sub.PIPE,stderr=sub.PIPE)
	output, errors = p.communicate()
	
	text = tk.Text(root, width=130, height=30)
	text.pack()
	text.place(x=55, y=20)
	text.insert(tk.END, output)

	botonVolver=Frame(root, width=50, height=100)
	botonVolver.place(x=890, y=410)
	Button(botonVolver, command=lambda:[text.destroy(), botonVolver.destroy()], text="Cerrar", cursor="heart", justify="center", bd=1, relief="raised", overrelief="sunken", background="black", activebackground='DarkRed', activeforeground='white', foreground='White', font=("URW Chancery L", 20)).pack()

	pass


def procesador():
	p = sub.Popen(["lscpu"],stdout=sub.PIPE,stderr=sub.PIPE)
	output, errors = p.communicate()
	
	text = tk.Text(root, width=130, height=30)
	text.pack()
	text.place(x=55, y=20)
	text.insert(tk.END, output)

	botonVolver=Frame(root, width=50, height=100)
	botonVolver.place(x=890, y=410)
	Button(botonVolver, command=lambda:[text.destroy(), botonVolver.destroy()], text="Cerrar", cursor="heart", justify="center", bd=1, relief="raised", overrelief="sunken", background="black", activebackground='DarkRed', activeforeground='white', foreground='White', font=("URW Chancery L", 20)).pack()

	pass



def actividad_procesador():
	p = sub.Popen(['who', '-a'],stdout=sub.PIPE,stderr=sub.PIPE)
	output, errors = p.communicate()
	
	text = tk.Text(root, width=130, height=30)
	text.pack()
	text.place(x=55, y=20)
	text.insert(tk.END, output)

	botonVolver=Frame(root, width=50, height=100)
	botonVolver.place(x=890, y=410)
	Button(botonVolver, command=lambda:[text.destroy(), botonVolver.destroy()], text="Cerrar", cursor="heart", justify="center", bd=1, relief="raised", overrelief="sunken", background="black", activebackground='DarkRed', activeforeground='white', foreground='White', font=("URW Chancery L", 20)).pack()

	pass

def listado_pip_librerias():
	p = sub.Popen(['pip', 'list'],stdout=sub.PIPE,stderr=sub.PIPE,)
	output, errors = p.communicate()
	
	text = tk.Text(root, width=130, height=30)
	text.pack()
	text.place(x=55, y=20)
	text.insert(tk.END, output)

	botonVolver=Frame(root, width=50, height=100)
	botonVolver.place(x=890, y=410)
	Button(botonVolver, command=lambda:[text.destroy(), botonVolver.destroy()], text="Cerrar", cursor="heart", justify="center", bd=1, relief="raised", overrelief="sunken", background="black", activebackground='DarkRed', activeforeground='white', foreground='White', font=("URW Chancery L", 20)).pack()

	pass


def consola1():

	termf = Frame(root, height=750, width=250) 

	termf.pack(fill=BOTH, expand=0)
	termf.place(x=100, y=110)
	termf.config(width=830, height=405)
	wid = termf.winfo_id() 
	os.system('xterm -into %d -geometry 600x300 -sb &' % wid)

	botonMenu2=Frame(root, width=50, height=100)
	botonMenu2.pack(fill=BOTH, expand=YES)
	botonMenu2.place(x=820, y=495)
	Button(botonMenu2, command=lambda:[botonMenu2.destroy(), termf.destroy()], text="Cerrar Consola", cursor="heart", justify="center", bd=1, relief="raised", overrelief="sunken", background="black", activebackground='DarkRed', activeforeground='white', foreground='White', font=("URW Chancery L", 14)).pack()


	pass



# /Ventana principal con menu_bar.

root = Tk()

root.title("··· OffShell System Aplication -- Luka Version (0.1) -- for Gnu/Linux···")
root.geometry("1024x720+130+50")
root.resizable(width=False, height=False)

root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='primate.gif'))

barramenu=Menu(root, relief=RAISED, cursor="heart", activebackground='Black', foreground='white', activeforeground='Red', activeborderwidth=3, bg='Black', bd=5)

root.config(menu=barramenu, width=300, height=300, cursor="heart")


archMenu=Menu(barramenu, tearoff=0)

archMenu.add_command(label="Instalación.(Recomendada)", command=advertencia, font=("URW Chancery L", 14), background='DarkRed', activebackground='black', foreground='white', activeforeground='white')

archMenu.add_separator(background='DarkRed')

archMenu.add_command(label="Métrica Memoria Ram", command=Ram_Metricas, font=("URW Chancery L", 14), background='DarkRed', activebackground='Black', foreground='white', activeforeground='white')

archMenu.add_separator(background='DarkRed')

archMenu.add_command(label="Speed Test Internet", command=speedtest, font=("URW Chancery L", 14), background='DarkRed', activebackground='Black', foreground='white', activeforeground='white')

archMenu.add_separator(background='DarkRed')

archMenu.add_command(label="Gía Comandos Gnu", command=comandos_gnu, font=("URW Chancery L", 14), background='DarkRed', activebackground='black', foreground='white', activeforeground='white')

archMenu.add_separator(background='DarkRed')

archMenu.add_command(label="Especificaciones Hardware", command=hardware_metricas, font=("URW Chancery L", 14), background='DarkRed', activebackground='black', foreground='white', activeforeground='white')

archMenu.add_separator(background='DarkRed')

archMenu.add_command(label="Especificaciones Procesador", command=procesador, font=("URW Chancery L", 14), background='DarkRed', activebackground='black', foreground='white', activeforeground='white')

archMenu.add_separator(background='DarkRed')

archMenu.add_command(label="Actividad Procesos Procesador", command=actividad_procesador, font=("URW Chancery L", 14), background='DarkRed', activebackground='black', foreground='white', activeforeground='white')

archMenu.add_separator(background='DarkRed')

archMenu.add_command(label="Listado Librerías PIP", command=listado_pip_librerias, font=("URW Chancery L", 14), background='DarkRed', activebackground='black', foreground='white', activeforeground='white')


archConsola=Menu(barramenu, tearoff=0)

archConsola.add_command(label="Abrir Consola de Comandos", command=consola1, font=("URW Chancery L", 14), background='DarkRed', activebackground='Black', foreground='white', activeforeground='white')


archPlataformasWeb=Menu(barramenu, tearoff=0)

archPlataformasWeb.add_command(label="Ver OffShell System Classic", command=openWeb, font=("URW Chancery L", 14), background='DarkRed', activebackground='Black', foreground='white', activeforeground='white')

archPlataformasWeb.add_separator(background='DarkRed')

archPlataformasWeb.add_command(label="Ver Blog OffShell System Connection", command=openWeb2, font=("URW Chancery L", 14), background='DarkRed', activebackground='Black', foreground='white', activeforeground='white')

archPlataformasWeb.add_separator(background='DarkRed')

archPlataformasWeb.add_command(label="Ver Git Hub", command=openWeb3, font=("URW Chancery L", 14), background='DarkRed', activebackground='black', foreground='white', activeforeground='white')


archMultimedia=Menu(barramenu, tearoff=0)

archMultimedia.add_command(label="Tienda de Software", command=software, font=("URW Chancery L", 14), background='DarkRed', activebackground='black', foreground='white', activeforeground='white')


archMiembros=Menu(barramenu, tearoff=0)

archMiembros.add_command(label="Ver Usuari@s OffShell System", command=usuarios, font=("URW Chancery L", 14), background='DarkRed', activebackground='black', foreground='white', activeforeground='white')


archsobreNosotros=Menu(barramenu, tearoff=0)

archsobreNosotros.add_command(label="Proyecto OffShell System", command=sobreNosotros, font=("URW Chancery L", 14), background='DarkRed', activebackground='black', foreground='white', activeforeground='white')

archsobreNosotros.add_separator(background='DarkRed')

archsobreNosotros.add_command(label="Únete como Usuari@", command=unete, font=("URW Chancery L", 14), background='DarkRed', activebackground='black', foreground='white', activeforeground='white')


archSalir=Menu(barramenu, tearoff=0,)

archSalir.add_command(label="Salir de la aplicación.", font=("URW Chancery L", 14), command=root.destroy, background='DarkRed', activebackground='Black', foreground='white', activeforeground='white')


barramenu.add_cascade(label="OffShell System Tools", menu=archMenu, font=("URW Chancery L", 15))

barramenu.add_cascade(label="Consola de Comandos", menu=archConsola, font=("URW Chancery L", 15))

barramenu.add_cascade(label="Plataformas Web", menu=archPlataformasWeb, font=("URW Chancery L", 15))

barramenu.add_cascade(label="Software", menu=archMultimedia, font=("URW Chancery L", 15))

barramenu.add_cascade(label="Miembros", menu=archMiembros, font=("URW Chancery L", 15))

barramenu.add_cascade(label="Sobre Nosotros", menu=archsobreNosotros, font=("URW Chancery L", 15))

barramenu.add_cascade(label="Salir", menu=archSalir, font=("URW Chancery L", 15))

# /vENTANA INICIO APLCACIÓN.
wmenu=Frame(root, width=2000, height=1024)
wmenu.place(x=0, y=0, relwidth=1, relheight=1)
wmenu.pack(fill=BOTH, expand=YES)

# /Imagen de fondo.

imagen_off = PhotoImage(file="mandala.gif")

imgicono = PhotoImage(file="fondo_inicio.gif")
imagen_primate = PhotoImage(file="puertas5.gif")
# /Botones de pantalla de inicio

botonBienvenido=Frame(root, width=1024, height=1024)
botonBienvenido.pack(fill=BOTH, expand=YES)
botonBienvenido.place(x=0, y=0)
Button(botonBienvenido, image=imgicono, cursor="heart", justify="center", bd=1, relief="raised", overrelief="sunken", background="DarkRed", activebackground='DarkRed', activeforeground='white', foreground='White', font=("URW Chancery L", 15)).pack()

root.mainloop()

#OffShell System es una Marca Registrada con la siguiente Licencia. Este programa sin embargo es Software Libre con licencia GPL 3.
#Licencia de Creative Commons
#OffShell System by Alexandre Varela Sixto is licensed under a Creative Commons Reconocimiento-NoComercial-SinObraDerivada 4.0 Internacional License.
#Creado a partir de la obra en https://offshellsystemconnection.blogspot.com/p/software.html.


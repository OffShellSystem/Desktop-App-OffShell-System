#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
import webbrowser
import os

# /Defino funciones

def software(): # Definición de la pantalla de Tienda de Software.
	ventanasoft = Tk()
	ventanasoft.title("Tienda de Software OffSehll System")
	ventanasoft.config(cursor="heart", background='black')
	ventanasoft.resizable(width=False, height=False)
	ventanasoft.geometry("400x400+450+200")

	Label(ventanasoft, width=0, anchor="s", text="Bienvenido Usuari@\n-- Aplicación Versión {Luka} --\n-- Licencia GPL Versión 3 --", font=("URW Chancery L", 18), bg="black", fg="White").pack(fill=BOTH, expand=YES)

	boton1=Frame(ventanasoft, cursor="heart", background="black")
	boton1.pack(side='top', fill=BOTH, expand=YES)

	Button(boton1, cursor="heart", text="Software Comunidad", justify="center", bd=5, relief="raised", overrelief="sunken", background="black", activebackground='DarkRed', activeforeground='white', foreground='White', font=("URW Chancery L", 16)).pack()

	boton1=Frame(ventanasoft, cursor="heart", background="black")
	boton1.pack(side='top', fill=BOTH, expand=YES)

	Button(boton1, cursor="heart", text="Software OffShell System", justify="center", bd=5, relief="raised", overrelief="sunken", background="black", activebackground='DarkRed', activeforeground='white', foreground='White', font=("URW Chancery L", 16)).pack()

	boton1=Frame(ventanasoft, cursor="heart", background="black")
	boton1.pack(side='top', fill=BOTH, expand=YES)

	Button(boton1, cursor="heart", text="Publicar Software", justify="center", bd=5, relief="raised", overrelief="sunken", background="black", activebackground='DarkRed', activeforeground='white', foreground='White', font=("URW Chancery L", 16)).pack()

	boton1=Frame(ventanasoft, cursor="heart", background="black")
	boton1.pack(side='top', fill=BOTH, expand=YES)

	Button(boton1, command=ventanasoft.destroy, text="Salir",cursor="heart", justify="center", bd=5, relief="raised", overrelief="sunken", background="black", activebackground='DarkRed', activeforeground='white', foreground='White', font=("URW Chancery L", 16)).pack()

	boton1=Frame(ventanasoft, cursor="heart", background="black")
	boton1.pack(side='top', fill=BOTH, expand=YES)

	ventanasoft.mainloop()

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

	win_usuarios = Tk()
	win_usuarios.title("Miembros de OffShell System")
	win_usuarios.config(cursor="heart", background='White')
	win_usuarios.geometry("1024x720+130+50")
	win_usuarios.resizable(width=False, height=False)

	Label(win_usuarios, width=0, anchor="n", text="Miembros de la comunidad de offShell System\nUsuari@s pasionales y desarrolladores de Software independiente", font=("URW Chancery L", 18), bg="black", fg="Red").pack(fill=BOTH, expand=YES)

	botonOffshell=Frame(win_usuarios, width=50, height=50)
	botonOffshell.pack()
	botonOffshell.place(x=10, y=100)

	Button(botonOffshell, command=lambda:[offShell()], cursor="heart", text="OffShell (Fundador)", justify="center", bd=5, relief="raised", overrelief="sunken", background="black", activebackground='DarkRed', activeforeground='white', foreground='White', font=("URW Chancery L", 16)).pack()

	botonSalir=Frame(win_usuarios, width=50, height=50, background='White')
	botonSalir.pack()
	botonSalir.place()

	Button(win_usuarios, command=win_usuarios.destroy, cursor="heart", text="Volver al Menu", justify="center", bd=5, relief="raised", overrelief="sunken", background="black", activebackground='DarkRed', activeforeground='white', foreground='White', font=("URW Chancery L", 16)).pack()

	pass

def offShell():

	win_offshell = Tk()
	win_offshell.title("Tienda de Software OffSehll System")
	win_offshell.config(cursor="heart", background='black')
	win_offshell.resizable(width=False, height=False)
	win_offshell.geometry("950x250+170+300")
	
	Label(win_offshell, width=0, anchor="n", text="Off-Shell significa una partícula sin movimiento en física cuántica.\nEscogí este alias porque estuve sin movimiento durante muchos años en el ámbito tecnológico,\nhasta que por motivos personales descubrí un mundo increíble en las comunidades de Usuari@s.\nPersonas apasionadas y colaborativas que no dudan en fomentar\nun lugar mejor donde interactuar y aprender unos de otros.\nPor tod@s y cada un@ de ell@s me encuentro aquí con vosotr@s, usuari@s del cambio.", font=("URW Chancery L", 18), bg="black", fg="Red").pack(fill=BOTH, expand=YES)

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


# /Ventana principal con menu_bar.

root = Tk()

root.title("··· OffShell System Aplication -- Luka Version (0.1) -- for Gnu/Linux···")
root.geometry("1024x720+130+50")
root.resizable(width=False, height=False)

barramenu=Menu(root, relief=RAISED, cursor="heart", activebackground='Black', foreground='white', activeforeground='Red', activeborderwidth=3, bg='Black', bd=3)

root.config(menu=barramenu, width=300, height=300, cursor="heart")


archMenu=Menu(barramenu, tearoff=0)

archMenu.add_command(label="Proyecto", command=sobreNosotros, font=("URW Chancery L", 14), background='DarkRed', activebackground='Black', foreground='white', activeforeground='white')

archMenu.add_command(label="Comunidad", command=comunidad, font=("URW Chancery L", 14), background='DarkRed', activebackground='Black', foreground='white', activeforeground='white')

archMenu.add_command(label="Únete como Usuari@", command=unete, font=("URW Chancery L", 14), background='DarkRed', activebackground='black', foreground='white', activeforeground='white')


archPlataformasWeb=Menu(barramenu, tearoff=0)

archPlataformasWeb.add_command(label="Ver OffShell System Classic", command=openWeb, font=("URW Chancery L", 14), background='DarkRed', activebackground='Black', foreground='white', activeforeground='white')

archPlataformasWeb.add_command(label="Ver Blog OffShell System Connection", command=openWeb2, font=("URW Chancery L", 14), background='DarkRed', activebackground='Black', foreground='white', activeforeground='white')

archPlataformasWeb.add_command(label="Ver Git Hub", command=openWeb3, font=("URW Chancery L", 14), background='DarkRed', activebackground='black', foreground='white', activeforeground='white')


archMultimedia=Menu(barramenu, tearoff=0)

archMultimedia.add_command(label="Tienda de Software", command=software, font=("URW Chancery L", 14), background='DarkRed', activebackground='black', foreground='white', activeforeground='white')


archMiembros=Menu(barramenu, tearoff=0)

archMiembros.add_command(label="Ver Usuari@s OffShell System", command=usuarios, font=("URW Chancery L", 14), background='DarkRed', activebackground='black', foreground='white', activeforeground='white')


archsobreNosotros=Menu(barramenu, tearoff=0)

archsobreNosotros.add_command(label="Proyecto OffShell System", command=sobreNosotros, font=("URW Chancery L", 14), background='DarkRed', activebackground='black', foreground='white', activeforeground='white')


archSalir=Menu(barramenu, tearoff=0,)

archSalir.add_command(label="Salir de la aplicación.", font=("URW Chancery L", 14), command=root.destroy, background='DarkRed', activebackground='Black', foreground='white', activeforeground='white')


barramenu.add_cascade(label="OffShell System", menu=archMenu, font=("URW Chancery L", 15))

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

imgicono = PhotoImage(file="world.gif")

# /Botones de pantalla de inicio

botonBienvenido=Frame(root, width=1024, height=1024)
botonBienvenido.pack(fill=BOTH, expand=YES)
botonBienvenido.place(x=0, y=0, relwidth=1, relheight=1)
Button(botonBienvenido, image=imgicono, cursor="heart", justify="center", bd=5, relief="raised", overrelief="sunken", background="DarkRed", activebackground='DarkRed', activeforeground='white', foreground='White', font=("URW Chancery L", 15)).pack()

root.mainloop()


Licencia de Creative Commons
OffShell System by Alexandre Varela Sixto is licensed under a Creative Commons Reconocimiento-NoComercial-SinObraDerivada 4.0 Internacional License.
Creado a partir de la obra en https://offshellsystemconnection.blogspot.com/p/software.html.


from sense_emu import SenseHat
import tkinter as tk
from tkinter import ttk
import time 
import matplotlib.pyplot as plt 
from datetime import datetime


class Aplicacion():
    def __init__(self):
        
        self.ventana1=tk.Tk()
        self.ventana1.title("Práctica GUI SenseHat")
        
        self.comienzo=False
        self.datos_insertados=1

        #Creamos el diálogo Opciones
        self.menubar1 = tk.Menu(self.ventana1) #Creamos el diálogo
        self.ventana1.config(menu=self.menubar1)#Hacemos que aparezca en nuestra ventana
        self.menubar1.add_cascade(label="Opciones")#Le ponemos el nombre de Opciones

        #Creamos un cuaderno con las páginas Monitorización y Gráfica
        self.cuaderno1 = ttk.Notebook(self.ventana1) #Creamos el cuaderno

        self.pagina1 = ttk.Frame(self.cuaderno1)#Creamos la página
        self.cuaderno1.add(self.pagina1, text="Monitorización")#Ponemos el nombre Monitorización a la página 1
        
        self.labelframe1=ttk.LabelFrame(self.pagina1, text="Control") #Creamos el frame Control       
        self.labelframe1.grid(column=0, row=0) #Lo colocamos     
        self.control() #Llamamos a una función donde añadiremos todo lo que va en este labelframe

        self.labelframe2=ttk.LabelFrame(self.pagina1, text="Medidas") #Creamos el frame Medidas       
        self.labelframe2.grid(column=0, row=1)  #Lo colocamos      
        self.medidas() #Llamamos a una función donde añadiremos todo lo que va en este labelframe

        self.labelframe3=ttk.LabelFrame(self.pagina1, text="Historico") #Creamos el frame Historico    
        self.labelframe3.grid(column=0, row=2)  #Lo colocamos 
        self.historico() #Llamamos a una función donde añadiremos todo lo que va en este labelframe

        self.pagina2 = ttk.Frame(self.cuaderno1)#Creamos otra página
        self.cuaderno1.add(self.pagina2, text="Gráfica")#Ponemos el nombre Gráfica a la página 2

        self.cuaderno1.grid(column=0, row=0) #Colocamos el cuaderno en nuestra ventana

        self.ventana1.mainloop()

        
    def control(self): #Función donde añadiremos todo lo que va en labelframe1
        

        self.boton1=tk.Button(self.labelframe1, text="Comenzar", command=self.comenzar)
        self.boton1.pack()

    def medidas(self): #Función donde añadiremos todo lo que va en labelframe2
        

        self.entry1=tk.Entry(self.labelframe2, width=20, text='hola')
        self.entry1.grid(column=1, row=0)

        self.seleccion1=tk.IntVar()
        self.seleccion1.set(3)
        
        self.radio1=tk.Radiobutton(self.labelframe2,text="Temperatura", variable=self.seleccion1, value=1)
        self.radio1.grid(column=0, row=1)
        self.radio2=tk.Radiobutton(self.labelframe2,text="Presion", variable=self.seleccion1, value=2)
        self.radio2.grid(column=1, row=1)
        self.radio3=tk.Radiobutton(self.labelframe2,text="Humedad", variable=self.seleccion1, value=3)
        self.radio3.grid(column=2, row=1)

        
    def historico(self): #Función donde añadiremos todo lo que va en labelframe3
        self.scroll1 = tk.Scrollbar(self.labelframe3, orient=tk.VERTICAL)
        self.tree = ttk.Treeview(self.labelframe3, yscrollcommand=self.scroll1.set)
        self.tree.grid(column=1, row=0)
        
        self.scroll1.configure(command=self.tree.yview)         
        self.scroll1.grid(column=2, row=0, sticky='NS')    # NS de norte a sur
        
        self.tree['columns'] = ('valor', 'data', 'tipo')

        # self.tree.column('size', width=100, anchor='center')
        self.tree.heading('#0', text='#Num')
        self.tree.heading('valor', text='Valor')
        self.tree.heading('data', text='Fecha/Hora')
        self.tree.heading('tipo', text='Tipo')


        self.boton2=tk.Button(self.labelframe3, text="Limpiar")
        self.boton2.grid(column=0, row=1)
        self.boton3=tk.Button(self.labelframe3, text="Calcular Media")
        self.boton3.grid(column=1, row=1)
        self.boton4=tk.Button(self.labelframe3, text="Exportar")
        self.boton4.grid(column=2, row=1)

        self.seleccion2=tk.IntVar()
        self.check1=tk.Checkbutton(self.labelframe3,text="Añadir a lista", variable=self.seleccion2)
        self.check1.grid(column=1, row=2)

    def comenzar(self):
        if(self.comienzo==False):
            
            self.comienzo=True
            self.boton1.configure(text="Parar")
            periodo=10
            i=0
            sense=SenseHat()
            while(i<periodo):
                self.medir(sense)
                i+=1
        
        else:
            self.comienzo=False
            self.boton1.configure(text="Comenzar")

    def medir(self,sense):
        date=datetime.now()
        if(self.seleccion1.get()==1):
            dato=sense.temperature
            tipo='Temperatura'
        elif(self.seleccion1.get()==2):
            dato=sense.pressure
            tipo='Presión'
        elif(self.seleccion1.get()==3):
            dato=sense.humidity
            tipo='Humedad'
        time.sleep(1)
        self.entry1.delete(0,tk.END)
        self.entry1.insert(0,str(dato))
        fecha_y_hora=date.strftime("%d/%m/%Y %H:%M:%S")
        self.tree.insert('', 'end', text=str(self.datos_insertados), values=(str(dato),fecha_y_hora, tipo))
        self.datos_insertados+=1
        print(dato)
        


aplicacion=Aplicacion()


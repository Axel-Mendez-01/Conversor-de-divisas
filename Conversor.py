from tkinter import *
from tkinter import ttk
import requests

#Creación de la ventana.
ventana = Tk()
ventana.minsize(500,500)
ventana.title("Convertidor en python")
ventana.resizable(0,0)
ventana.configure(bg="silver")

#Creación del titulo de la aplicación.
titulo_label = Label(ventana, text= "Convertidor de monedas")
titulo_label.config(
        fg="black",
        bg="silver",
        font=("Arial", 28),
        padx=210,
        pady=20
    )
titulo_label.grid(row=0, column=0)

#Creación del titulo y la ventana para introducir la cantidad.
numero_label = Label(ventana, text="Introduzca la cantidad (solo números) y después seleccione la moneda correspondiente")
numero_entry = Entry(ventana)
numero_label.grid(row=1, column=0, padx=5, pady=5)
numero_entry.grid(row=2, column=0, padx=5, pady=5)

#Creación del primer seleccionador de moneda.
combo = ttk.Combobox()
combo = ttk.Combobox(state="readonly")
combo["values"] = ['MXN', 'USD', 'EUR', 'GBP', 'CAD', 'BRL', 'ARS']
combo.grid(row=3, column=0, padx=5, pady=5)

#Creación del tercer titulo.
second_moneda = Label(ventana, text="¿A que moneda desea convertir?")
second_moneda.grid(row=4, column=0, padx=5, pady=5)

#Creación del segundo seleccionador de moneda.
combo2 = ttk.Combobox()
combo2 = ttk.Combobox(state="readonly")
combo2["values"] = ['MXN', 'USD', 'EUR', 'GBP', 'CAD', 'BRL', 'ARS']
combo2.grid(row=5, column=0, padx=5, pady=5)

#Creación de la función para la propiedad 'command' correspondiente al boton 'convertir' y una variable para obtener la URL de la API.
def conversion():
    try: 
        URL = 'https://v6.exchangerate-api.com/v6/14929aae3893be27a34511f1/latest/'+combo.get() 
        response= requests.get(URL)
        data = response.json()
        numero1 = float(numero_entry.get())
        resultado = round((numero1 * data['conversion_rates'][combo2.get()]), 2)
        espacio = Label(ventana, text="")
        espacio.grid(row=7, column=0)
        resultado_label = Label(ventana, text=resultado)
        resultado_label.grid(row=8, column=0)
        resultado_label.config(
            fg="black",
            bg="silver",
            font=("Arial", 21),
            padx=386,
            pady=20
        )
    except:
        espacio = Label(ventana, text="")
        espacio.grid(row=7, column=0)
        resultado_label = Label(ventana, text="¡Ocurrió un error! Recuerda que solo puedes agregar números.")
        resultado_label.grid(row=8, column=0)
        resultado_label.config(
            fg="red",
            bg="black",
            font=("Arial", 19),
            padx=56,
            pady=15
        )

#Creación del boton 'convertir'.
boton = Button(ventana, text="convertir", command=conversion)
boton.grid(row=6, column=0)
#Creación del ´mainloop' para que se pueda ejecutar el programa.
ventana.mainloop()
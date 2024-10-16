import customtkinter as ctk
from tkinter import messagebox
from typing import List, Dict
import time
import threading as th
class Ventana():
    """ This class creates a window for the current program
    Atributes
    ----------
    :title:`str` -> The title of the window
    :dim: `str` -> The dimension of the window 
    
    Example
    ---------
    >>> Window:object = Ventana(title:str="Window", dim:str = "500x500")
    """
    def __init__(self,title:str="File organizer",dim:str="500x600") -> object:
        self.ventana:object|ctk.CTk = ctk.CTk()
        self.dimensiones = self.ventana.geometry(dim)
        self.titulo = self.ventana.title(title)
        self.protocolo = self.ventana.protocol("WM_DELETE_WINDOW",self.close_window)
        self.comboboxes:Dict[str,object] = {}
        self.boton_org:object = ctk.CTkButton(master = self.ventana, text = "Organizar Archivos", command = self.organize_files_create_files, font = ("Sans Seriff", 16) )
        self.boton_crf:object = ctk.CTkButton(master = self.ventana, text = "Crear Carpetas", command = self.organize_files_create_files, font = ("Sans Seriff", 16) )
        self.frame:object = ctk.CTkFrame(master= self.ventana)
        self.labels:Dict[int,object] = {}

    def close_window(self) -> None:
        """This method stops the window and "breaks the code"
        Parameters
        ----------
        `None`

        Example
        ----------
        >>> window.close_window() -> messagebox -> "Seguro de que quieres cerrar la ventana"
        
        """
    
        try:
            if messagebox.askyesno(message="Estas seguro de que quieres cerrar la ventana"):
                self.ventana.destroy()
                
        except Exception as e:
            print("Hubo un error al cerrar la ventana, el error es el siguiente",e)
            raise e
    
    def open_window(self) -> None:
        """ This method opens the window
        Atributes
        -----------
        `None`

        Example
        -----------
        >>> window.open_window() -> Opens the window
        """
        
        try:
            
            #Funktion, die den Comboboxen Werte zuweist # | #Funcion para asignar valores a los comboxes#
            self.Comboboxes(num_comb=3)

            #Funktion, die die beschriftungen zuweist # | Funcion que asigna los valores a los labels
            self.die_beschriftungen(3,["Introduzca el numero del semestre","Seleccione el periodo escolar","Acción"])
            
            #Funktion, die schaltflächen, die comboboxen und beschriftungen zeigt # | # Funcion que muestra los botones, los comboboxes y los labels#
            self.labels[1].pack(pady = 10 )
            self.comboboxes["1"].pack(pady = 10 )
            self.labels[2].pack(pady = 10)
            self.comboboxes["2"].pack(pady = 12, padx = 18)
            self.boton_org.pack(pady= 12, padx = 18)
            self.labels[3].pack(pady = 10)
            self.comboboxes["3"].pack(pady = 10)
            self.boton_crf.pack(pady= 12, padx = 18)

            #Funktion, die die Hauptshleife startet# | #Funcion que inicia el bucle principal#
            self.ventana.mainloop() #Die funktion  muss am Ende plarziert werden# | #Esta funcion debe de estar colocada siempre al final#
        
        except Exception as e:
            print("Hubo un error al iniciar la ventana, el error es el siguiente", e)
            raise e
    
    def Comboboxes(self,num_comb:int,comb_values:List[List[str]] = [[f"Semestre {x+1}" for x in range(12)],["Enero - Junio","Agosto - Noviembre"], ["Organizar Archivos","Crear Carpetas"]]) -> None:
        """ This method creates the necesary comboboxes for the window
        Parameters
        -----------
        :num_comb: `int` -> The number of comboboxes that will be created
        :comb_values: `List[List[str]]` -> The default text displayed on the comboboxes
        
        """
        
        try:
            if not num_comb == len(comb_values):
                raise ValueError("La cantidad de numeros y texto no es igual")
            else:
                for i,opciones in zip(range(num_comb),comb_values):
                    comb = ctk.CTkComboBox(master = self.ventana, values = opciones) 
                    self.comboboxes[f'{i+1}'] = comb
                    self.comboboxes[f"{i+1}"].set("Selecciona una opción")
                    
        except Exception as e:
            print("Hubo un error al crear los botones en el metodo buttons, el error es el siguiente", e)
    
    def combo_value(self,combobox:int) -> str:
        """Returns the combobox value with the correspondent   
        Parameters
        ----------
        :combobox: `int` -> The # of the combobox
        
        Return
        ----------
        `str` -> The value of the combobox at the moment

        Example
        ----------
        >>> combobox.combo_value(combobox:int = 1)
        {f"combobox.get()"}
        """
        try:
            return self.comboboxes[combobox].get()
        except Exception as e:
            print("Hubo un error al obtener el valor el combobox, el error es el siguiente", e)

    def organize_files_create_files(self,ordenar_archivos:object,create_folders:object,calc_sem:object)-> None:
        """It uses as a parameter an object to use it's methods, specifically the organize method for the files in the folders
        Parameters
        -----------
        :ordenar_archivos: `object` -> The object with the correspondent files
        
        Return
        -----------
        `None`

        Example
        -----------
        >>> Ventana.organize_files(object_1():object)
        {None}
        """
        try:
            semanas = calc_sem(self.combo_value(2) if type(self.combo_value(2)) == int else None)
            semestre = self.combo_value(1) if type(self.combo_value) == int else None
            period = self.combo_value(2) if type(self.combo_value(2)) == int else None
            if semanas and semestre and period:
                #Si son los datos correctos, se evalua los siguientes condicionales#
                if self.combo_value(3) == "Organizar Archivos":
                    organize_F:object = ordenar_archivos(semester = semestre, periodo = period)
                    directories:dict = organize_F.organize() #Contiene el directorio de la siguiente manera, dict  = {archivo: [directorio archivo, carpeta correspondiente]}#
                    #-- Aqui colocar la clase que muestra la barra de carga --#
                elif self.combo_value(3) == "Crear Carpetas":
                    create_F:object = create_folders("")
            
                else: 
                    raise ValueError("Uno de los valores es incorrecto")
            # -- Agregar un condicional para verificar que se ejecuta, de lo contrario mostrar una caja de texto --#
            organize_F.organize()
            create_F.create_folders()
        
        except Exception as e:
            print("Hubo un error al organizar los archivos",e)
            messagebox.askokcancel("Uno de los valores es incorrecto")


    def die_beschriftungen(self, labels:int, text:List[str]) -> None:
        """ This method creates the necesary labels for the current program
        Parameters
        -----------
        :labels: `int` -> The quantity of labels that will be created
        :text: `List[str]` -> The content of each label

        Return
        -----------
        `None`

        Example 
        ----------
        window:object = Ventana()
        window.die_beschriftungen(labels:int = 2, text:List[str]  = ["Inicio", "Fin"])
        {None} -> It creates the value of the labels
        """
        try:
            if not labels == len(text):
                raise ValueError("El valor no es el correcto")
            else:
                for x in range(labels):
                    self.labels[x+1] = ctk.CTkLabel(master = self.ventana, text= text[x], font= ("Sans Seriff",20)) 
        except Exception as e:
            print("Hubo un error en la funcion die beschriftungen para definir el label, el error es el siguiente", e )
            raise e 


class Barra_de_Progreso():
    def __init__(self) -> None:
        self.ventana = ctk.CTk()
        self.withdraw = self.ventana.withdraw()
        self.geometry = self.ventana.geometry('200x200')
        self.title = self.ventana.title("Barra de progreso")
        self.protocolo = self.ventana.protocol("WM_DELETE_WINDOW", lambda : None)
        self.items:List[object] = []
    
    def mostrar(self) -> None:
        """ This method shows the window with the progressbar
        Parameters
        ----------
        `None`
        
        Return 
        ----------
        `None`
        
        Example
        ----------
        >>> progress_bar:object = Barra_de_Progreso.mostrar()
        {None} -> Shows the progressbar
        """    
        self.ventana.deiconify()
    
    def ocultar(self) -> None:
        """ This method hides the window with the progressbar
        Parameters
        ----------
        `None`

        Return
        ----------
        `None`

        Example
        ----------
        >>> progress_bar:object = Barra_de_Progreso.ocultar()
        {None} -> Hides the progress bar
        """
        self.ventana.withdraw()
    
    def progress_bar(self) -> None:
        self.items.append(ctk.CTkProgressBar(master= self.ventana,width=400, progress_color="Green"))

    def progress_in_bar(self,value) -> None:
        
        self.items[1].set(value)


if __name__ == "__main__":
    Fenster:object = Ventana()
    Fenster.open_window()

#Me falta agregar la barra de carga#
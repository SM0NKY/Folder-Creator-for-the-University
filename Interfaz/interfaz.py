import customtkinter as ctk
from tkinter import messagebox
from typing import List, Dict, Any
import time
import threading as th
import re


class Ventana():
    """ This class creates a window for the current program
    Atributes
    ----------
    :lista_objetos: `List[object]` -> Object used in specific functions to organize the files
    :title:`str` -> The title of the window
    :dim: `str` -> The dimension of the window 
    
    Example
    ---------
    >>> Window:object = Ventana(title:str="Window", dim:str = "500x500")
    """
    
    def __init__(self,lista_objetos:List[object],title:str="File organizer",dim:str="500x600") -> object:
        self.ventana:object|ctk.CTk = ctk.CTk()
        self.dimensiones = self.ventana.geometry(dim)
        self.titulo = self.ventana.title(title)
        self.protocolo = self.ventana.protocol("WM_DELETE_WINDOW",self.close_window)
        self.comboboxes:Dict[str,object] = {}
        self.objects:List[object] = lista_objetos
        self.boton_org:object = ctk.CTkButton(master = self.ventana, text = "Ejecutar", command = self.organize_files_create_files , font = ("Sans Seriff", 16) ) #Recordar en los botones no llamar a la funcion solo definirla ahi
        self.frame:object = ctk.CTkFrame(master= self.ventana)
        self.labels:Dict[int,object] = {}
        self.pattern:str = r'(\d{1}){1}'
    
    def close_window(self) -> None:
        """This method stops the window and "breaks the code"
        
        Parameters
        ----------
        `None`

        Example
        ----------
        >>> window.close_window()
        {None} -> messagebox ->  "Seguro de que quieres cerrar la ventana"
        """
    
        try:
            if messagebox.askyesno(message="Estas seguro de que quieres cerrar la ventana"):
                self.ventana.destroy()
                
        except Exception as e:
            print("Hubo un error al cerrar la ventana, el error es el siguiente",e)
            raise e
    
    def open_window(self) -> None:
        """ This method opens the window, and shows the items in the window
        Atributes
        -----------
        `None`

        Example
        -----------
        >>> window.open_window() -> Opens the window and shows items
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
            self.labels[3].pack(pady = 10)
            self.comboboxes["3"].pack(pady = 10)
            self.boton_org.pack(pady= 12, padx = 18)

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
        
        Return
        -----------
        `None`

        Example
        -----------
        >>> comboboxes = Ventana(atributes)
        >>> comboboxes.Comboboxes(num_comb:int = 2, comb_values:List[List[str]] = [[Value_1...Value_n][Value_1...Value_n]]) 
        {None} -> Creates the comboboxes that are going to be used
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
        {f"combobox.get()"} -> Returns the value of the combox #1
        """
        try:
            return self.comboboxes[f'{combobox}'].get()
        except Exception as e:
            print("Hubo un error al obtener el valor el combobox, el error es el siguiente", e)
            raise e

    def organize_files_create_files(self)-> None:
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
        {None} -> It organizes the files and shows the progress in a progressbar
        """
        
        try:
            Weeks:List[str] = self.objects[2](self.combo_value(2) if type(self.combo_value(2)) == int else None)
            Weeks.calcular_semanas()
            semestre = self.combo_value(1) if self.combo_value(1) in [f"Semestre {x+1}" for x in range(12)] else None
            period = 1 if self.combo_value(2) == "Enero - Junio" else 2

            if Weeks and semestre and period:
                
                print(Weeks,semestre,period)
                #Wenn die daten korrekt sind,die folgenden bedingungen werden ausgewertet # | #Si son los datos correctos, se evalua los siguientes condicionales#
                
                if self.combo_value(3) == "Organizar Archivos":
                    # Hier wird das semester im string gesucht# | #Aqui se busca el semestre en el string #
                    
                    organize_F:object = self.objects[0](semester = re.search(self.pattern,semestre).group(1), periodo = period)
                    directories:dict = organize_F.organize() #Contiene el directorio de la siguiente manera, dict  = {archivo: [directorio archivo, carpeta correspondiente]}#
                    
                    progress:object = Barra_de_Progreso(0,len(list(directories.keys())))
                    progress.progress_bar()
                    progress.mostrar()
                    
                    for dir in list(directories.keys()):    
                        
                        time.sleep(0.5)
                        print(dir,directories[dir][0],directories[dir][1])
                        progress.progress_in_bar(list(directories.keys()).index(dir) + 1,len(list(directories.items())))
                        organize_F.move_files(directories[dir][0],directories[dir][1])
                    
                    time.sleep(0.5)
                    progress.ocultar()
                    messagebox.askokcancel(message="Los archivos han sido ordenados correctamente")
                
                elif self.combo_value(3) == "Crear Carpetas":
                    
                    create_F:object = self.objects[3](Weeks.semanas,period)
                    create_f:object = self.objects[1](create_F.folder_names())
                    create_f.c_foleders()
                    messagebox.askokcancel(message="Las carpetas han sido creado correctamente")
                
                else: 
                    raise ValueError("Uno de los valores es incorrecto")
            
        
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
    """ This class creates a new window and displays the progressbar and a counter
    Atributes
    ----------
    :file_num: `int` -> The file position of the total files => 1 of 23
    :file_quant: `int` -> The total quantity of files

    Example
    ----------
    >>> progress_bar:object = Barra_de_Progreso(file_num:int = 1, file_quant:int = 10)
    """
    def __init__(self,file_num:int, file_quant:int) -> None:
        self.ventana = ctk.CTk()
        self.withdraw = self.ventana.withdraw()
        self.geometry = self.ventana.geometry('400x200')
        self.title = self.ventana.title("Barra de progreso")
        self.protocolo = self.ventana.protocol("WM_DELETE_WINDOW", lambda : None)
        self.items:List[Any] = []
        self.label:object = ctk.CTkLabel(master= self.ventana,text = f"Archivo {file_num} de {file_quant}", font=("Sans Seriff", 20) )
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
        self.label.pack(pady = 12, padx = 18)
    
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
    
    def progress_bar(self, number:int = 1) -> None:
        """ This method creates and configures the progress bar
        Parameters
        ----------
        :number: `int` -> The number of progress_bars that will be created
        
        Return
        ----------
        `None`

        Example
        ----------
        >>> progress_barr:object = Barra_de_Progreso(Atributes)
        >>> progress_bar.progress_bar(number:int = 1)
        {None} -> It creates 1 progress_bar to display 
        """
        try:
            for x in range(number):
                self.items.append(ctk.CTkProgressBar(master= self.ventana,width=400, progress_color="Green"))
                self.items[x].place(x=20, y =20)
                self.items[x].pack(pady = 10)
        except Exception as e:
            print("Hubo un error al mostrar la barra de progreso, en el metodo progress_bar en la clase Barra_de_Progresom el error es el siguiente",e)
            raise ValueError("Error al definir barra/s de progreso")
        

    def progress_in_bar(self,number:int,quantity:int,progressbar_pos:int = 0) -> None:
        """ It changes the progress in the progressbar
        Parameters
        ----------
        :number: `int` -> The number of the position of the file on the total file quantity
        :quantity: `int` -> The total files that will be transfered
        :progressbar_pos: `int` -> The number of the list of the progress_bar that was created before

        Return
        ---------
        `None`

        Example
        >>> progressbar:object = Barra_de_Progreso(Atributes)
        >>> progressbar.progress_bar(Parameters)
        >>> progressbar.progress_in_bar(number:int = 1, quantity = 3)
        {None} -> Displays the progress in the progressbar
        """
        try:
            self.items[progressbar_pos].set(number/quantity)
            self.items[progressbar_pos].update_idletasks()
            self.label.configure(text = f"Archivo {number} de {quantity}")#Cambia el texto del label en lugar de crear nuevos labels#
        except Exception as e:
            raise e

if __name__ == "__main__":
    Zeigt_der_Fenster:object = Barra_de_Progreso(1,3) 
    Zeigt_der_Fenster.progress_bar(1)
    Zeigt_der_Fenster.mostrar()
    
    #Fenster:object = Ventana()
    #Fenster.open_window()

#Me falta agregar la barra de carga#
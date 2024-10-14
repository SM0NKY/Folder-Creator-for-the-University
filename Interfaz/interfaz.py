import customtkinter as ctk
from tkinter import messagebox
from typing import List, Dict

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
        self.botones = []
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
            self.ventana.mainloop()
        except Exception as e:
            print("Hubo un error al iniciar la ventana, el error es el siguiente", e)
            raise e
    
    def Comboboxes(self,num_comb:int,comb_values:List[List[str]] = [[f"Semestre {x+1}" for x in range(12)],["Organizar Archivos","Crear Carpetas"]]) -> None:
        """ This method creates the necesary comboboxes for the window
        Parameters
        -----------
        :num_comb: `int` -> The number of comboboxes that will be created
        :comb_values: `List[List[str]]` -> The default text displayed on the comboboxes
        
        """
        
        try:
            if not num_comb == len(comb_values):
                raise "La cantidad de numeros y texto no es igual"
            else:
                for i,opciones in zip(range(num_comb),comb_values):
                    self.comboboxes[f'{i+1}'] = ctk.CTkComboBox(master = self.ventana, values=opciones)
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

    def organize_files(self,ordenar_archivos:object)-> None:
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
            #Aqui agregar el el get, con el numero de semestre, para el objeto#
            organize_F:object = ordenar_archivos("") # -- Agregar los atributos de la clase --# 
            organize_F.organize()
        except Exception as e:
            print("Hubo un error al organizar los archivos",e)

    def create_folders(self,create_folders:object) -> None:
        """ It create the correspondent folder using the class to create folders, it creates and uses the correspondend data
        Parameters
        -----------
        :create_folders: `object`

        Return
        -----------
        `None`

        Example
        -----------
        >>> Ventana.create_folders(object_1():object)
        {None}
        """
        try:
            pass
        except Exception as e:
            print("Hubo un error al crear los archivos, ")



if __name__ == "__main__":
    pass
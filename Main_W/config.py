import customtkinter as ctk
from typing import Any, List, Literal, Dict,Callable, Optional
import os
from pathlib import Path
import json

class Einstellungen(ctk.CTkToplevel):
    """ This method is in charge of the settings of the main window

    Parameters
    ----------
    `master` : Optional[object] 
        This method utilizes herence to build up the windows layout, it is recomended to use self
    
    ``    
    """
    
    def __init__(self,master:Optional[object] = None):
        super().__init__(master)
        self.geometry("400x500")
        self.title("Configuration")
        self.protocol("WM_DELETE_WINDOW",lambda:None)
        #Variable de parametro
        self.showed:bool = False

        #Directorio .json
        self.directorio:str = os.path.join(Path(__file__).parent,"config.json")

        #Agregar los botones y el boton para seleccionar el directorio
        self.label1:object|ctk.CTkLabel = ctk.CTkLabel(master = self,text="El directorio seleccionado es:", font=("Sans Seriff", 16))
        self.label2:object|ctk.CTkLabel = ctk.CTkLabel(master= self, text= "", font= ("Sans Seriff", 16))
        self.button1:object|ctk.CTkButton = ctk.CTkButton(master= self, text="Cambiar directorio directorio", font=("Sans Seriff", 16), command= self.directory)
        self.button2:object|ctk.CTkButton = ctk.CTkButton(master= self, text=" Regresar", font=("Sans Seriff",16), command= self.abholen)

    def exceptions(message:Literal["Error al inicializar la ventana","Error al buscar el directorio","Error al minimizar la ventana"]) -> Any:
        def deco(func:Callable[...,Any]) -> Any:
            def wr(*args,**kwargs) -> Callable[...,Any]:
                try:
                    return func(*args,**kwargs)
                except Exception as e:
                    print(f"{message}:{e}, en la función {func.__name__}")
                    raise e
            return wr
        return deco

    @exceptions("Error al inicializar la ventana")
    def show_w(self) -> None:
        """ This method displays the window with the correspondent objects

        Parameters
        ----------
        `showed` :bool
            This pointer/parameter helps the mainwindow avoid errors with another window 
        """
        #Cambia la variable correspondiente para indicar si esta abierta la ventana
        self.showed:bool = True
        
        #Muestra los objetos creados de la ventana
        self.button2.pack(padx =10, pady = 10,anchor = "nw")
        self.label1.pack(padx = 10, pady = 10)
        self.label2.pack(padx = 10, pady = 10)
        self.button1.pack(padx = 10, pady = 10)
        self.load_dir()
        
        self.deiconify()
        
    @exceptions("Error al buscar el directorio")
    def directory(self) -> None:
        """ This method shows the current selected directory

        Parameters
        ----------
        `None`
        """
        selected_dir:str = os.path.abspath(ctk.filedialog.askdirectory())
        self.label2.configure(text = selected_dir)
        #Se revisa si el directorio existe, en caso de que exista
        with open(self.directorio, 'r+') as directorio:
            json.load(directorio)

        with open(self.directorio,'w') as directory:
            
            if directory:
                json.dump({"directory":selected_dir}, directory, indent=4)

    @exceptions("Error al inicializar la ventana")            
    def load_dir(self) -> None:
        """ Loads the current directory into the label of the window

        Parameters
        ----------
        `None`
        """
        #Carga el nuevo directorio y lo muestra en la ventana
        with open(self.directorio, 'r') as dir:
            directory:Dict[str,str] = json.load(dir)
            print(directory)
            self.label2.configure(text = directory.get("directory"))

    @exceptions("Error al minimizar la ventana")
    def abholen(self) -> None:
        """ This method withdraws the window from the screen

        Parameters
        ----------
        `showed` : bool
            Uses a variable to indicate if there's another window that is in use to avoid errorss
        """
        self.showed:bool = False
        self.withdraw()
        
if  __name__ == "__main__":

    settings:object|Einstellungen = Einstellungen()
    settings.show_w()
    settings.mainloop()

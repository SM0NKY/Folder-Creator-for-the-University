import os, shutil
from tkinter import messagebox
import customtkinter as ctk
from typing import Literal, Any,Dict 
from collections.abc import Callable
from pathlib import Path
import json

directory:str = ""

class Folders(ctk.CTkToplevel):
    """ This method creates the corresponden folders depending on the files in the directory

    Parameters
    ----------
    `master`: object 
        Uses an heredated atribute to avoid errors, it corresponds to the main window
    
    """
    def __init__(self, master = None):
        super().__init__(master)
        self.geometry("400x300")
        self.title("Progress Bar")
        self.protocol("WM_DELETE_WINDOW", lambda:None)
        self.showed:bool = False


        #Aqui agregar la barra de progreso
        self.items:int = 0
        self.counter:object|ctk.CTkLabel =  ctk.CTkLabel(master= self,text="")
        self.progressb:object|ctk.CTkProgressBar = ctk.CTkProgressBar(master= self,progress_color=("Green"), width = 400)
    
        #Directorio
        self.directorio:str = ""
        self.main_dir()

    def exceptions(message:str|Literal["Error al mostrar la ventana","Error al cargar la barra de progreso", "Error al mover los archivos","Error al encontrar el directorio"]) -> Callable[[None],None]:
        def deco(func:Callable[[Any], None]) -> Callable[[Any], None]:
            def wr(self,*args,**kwargs) -> None:
                try:
                    return func(self,*args, **kwargs)
                except Exception as e:
                    print(f"{message}:{e} en el metodo {func.__name__}")
                    raise e
            return wr
        return deco
    
    @exceptions("Error al mostrar la ventana")
    def show(self) -> None:
        self.counter.pack(padx = 10, pady = 10)
        self.progressb.pack(padx = 10, pady = 10)
        self.deiconify()

    @exceptions("Error al mover los archivos")
    def archivos(self) -> None:
        print(os.listdir(path= self.directorio))

    

    @exceptions("Error al encontrar el directorio")
    def main_dir(self) -> None:
        with open(os.path.join(Path(__file__).parent.parent,"Main_W","config.json"),'r') as settings:
            directorio:Dict[str,str] = json.load(settings)
            self.directorio = directorio.get("directory")
    
if __name__ == "__main__":
    folders:object|Folders = Folders(master=None)
    folders.archivos()
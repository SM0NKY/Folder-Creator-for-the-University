import customtkinter as ctk
from typing import Any, List, Literal, Dict,Callable, Optional
import os

class Einstellungen(ctk.CTkToplevel):
    """ This method is in charge of the settings of the main window

    Parameters
    ----------
    `master` : Optional[object] 
        This method utilizes herence to build up the windows layout, it is recomended to use self
    """
    
    def __init__(self, master:Optional[object] = None):
        super().__init__(master)
        self.geometry("400x500")
        self.title("Configuration")
        self.protocol("WM_DELETE_WINDOW",lambda:None)
        

        #Agregar los botones y el boton para seleccionar el directorio
        self.label1:object|ctk.CTkLabel = ctk.CTkLabel(master = self,text="El directorio seleccionado es:", font=("Sans Seriff", 16))
        self.label2:object|ctk.CTkLabel = ctk.CTkLabel(master= self, text= "", font= ("Sans Seriff", 16))
        self.button1:object|ctk.CTkButton = ctk.CTkButton(master= self, text="Cambiar directorio directorio", font=("Sans Seriff", 16), command= self.directory)
    
    def exceptions(message:Literal["Error al inicializar la ventana","Error al buscar el directorio"]) -> Any:
        def deco(func:Callable[...,Any]) -> Any:
            def wr(*args,**kwargs) -> Callable[...,Any]:
                try:
                    return func(*args,**kwargs)
                except Exception as e:
                    print(f"{message}:{e}, en la función {func.__name__}")
            return wr
        return deco

    @exceptions("Error al inicializar la ventana")
    def show_w(self) -> None:
        """ This method displays the window with the correspondent objects

        Parameters
        ----------
        `None`
        """

        self.label1.pack(padx = 10, pady = 10)
        self.label2.pack(padx = 10, pady = 10)
        self.button1.pack(padx = 10, pady = 10)
        
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


if  __name__ == "__main__":
    settings:object|Einstellungen = Einstellungen()
    settings.show_w()
    settings.mainloop()

import customtkinter as ctk
from typing import Any, List, Literal, Dict,Callable


class Einstellungen(ctk.CTkToplevel):
    """
    """
    def __init__(self, master = None):
        super().__init__(master)
        self.geometry("300x500")
        self.title("Configuration")

        #Agregar los botones y el boton para seleccionar el directorio
        self.label1:object|ctk.CTkLabel = ctk.CTkLabel(master = self,text="El directorio seleccionado es:", font=("Sans Seriff", 16))
        self.label2:object|ctk.CTkLabel = ctk.CTkLabel(master= self, text= "", font= ("Sans Seriff", 16))
        self.button1:object|ctk.CTkButton = ctk.CTkButton(master= self, text="Seleccionar directorio", font=("Sans Seriff", 16), command= lambda:None)
    
    def exceptions(message:Literal["Error al inicializar la ventana"]) -> Any:
        def deco(func:Callable[...,Any]) -> Any:
            def wr(*args,**kwargs) -> Callable[...,Any]:
                try:
                    return func(*args,**kwargs)
                except Exception as e:
                    print(f"{message}:{e}, en la función {func.__name__}")
            return wr
        return deco

    def show_w(self) -> None:
        #Agregar aqui los .packs de los botones

        self.deiconify()
        
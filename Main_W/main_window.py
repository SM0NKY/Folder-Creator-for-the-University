from tkinter import messagebox
import customtkinter as ctk 
from typing import Literal,Any, Callable, List,Dict

#Definir la ventana principal
from config import Einstellungen
class Main_Window(ctk.CTk):
    """ This class starts the main window
    
    
    Parameters
    ----------

    Atributes
    ---------

    """
    def __init__(self):
        super().__init__()
        self.title("Organizar")
        self.geometry("400x400")

        self.settings = Einstellungen(master= self)
        self.settings.abholen()

        #Aqui se agregan los objetos correspondientes a la ventana
        self.label1:object|ctk.CTkLabel = ctk.CTkLabel(master= self, text= "Para organizar los archivos, confirma tu directorio en la configuración",font= ("Sans Seriff", 16))
        self.button1:object|ctk.CTkButton = ctk.CTkButton(master= self, text="Configuración", font=("Sans Seriff", 16), command= self.open_s)

    def exceptions(message:Literal["Error al mostrar la ventana",""]) -> None:
        def deco(func:Callable[...,Any]) -> Any:
            def wr(*args,**kwargs) -> Any:
                try: 
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"{message}: {e}, en la funcion {func.__name__}")
                    raise e
            return wr
        return deco

    def exceptandwind(message:Literal["Se tiene otra ventana abierta"]) -> None:
        def deco(func:Callable[...,Any]) -> Callable[...,Any]:
            def wr(self,*args,**kwargs) -> Any:
                try:
                    if not self.settings.showed:
                        return func(self,*args,**kwargs)
                    else:
                        pass
                        messagebox.askokcancel(title= "Ventana Abierta", message = "Porfavor cierra la ventana secundaria")

                except Exception as e:
                    print(f"{message}:{e}, en la funcion {func.__name__}")
                    raise e
            return wr
        return deco

    @exceptions("Error al mostrar la ventana")
    def show_w(self) -> None:

        self.button1.pack(padx = 10, pady = 10, anchor = "nw")
        self.mainloop()


    @exceptandwind("Se tiene otra ventana abierta")
    def open_s(self) -> None:
        self.settings.show_w()


if __name__ == "__main__":
    window:Main_Window = Main_Window()
    window.show_w()
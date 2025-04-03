import customtkinter as ctk 
from typing import Literal,Any, Callable, List,Dict

#Definir la ventana principal

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
        self.geometry("300x300")
        self.second_window = True


        #Aqui se agregan los objetos correspondientes a la ventana
        self.label1:object|ctk.CTkLabel = ctk.CTkLabel(master= self, text= "Para organizar los archivos, confirma tu directorio en la configuración")


    def exceptions(message:Literal["Error al mostrar la ventana",""]) -> None:
        def deco(func:Callable[...,Any]) -> Any:
            def wr(*args,**kwargs) -> Any:
                try: 
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"{message}: {e}, en la funcion {func.__name__}")
            return wr
        return deco


    @exceptions("Error al mostrar la ventana")
    def show_w(self) -> None:
        # Aqui agregar los demas botones correspondientes

        self.mainloop()




if __name__ == "__main__":
    pass
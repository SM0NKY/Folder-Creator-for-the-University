from Verificador_fecha import Carpeta,dir_name
from Creador_python import Crear_Carpetas
from Interfaz import Ventana
from Ordenar_Archivos import organize_files



def iniciar_interfaz() -> None:
    """ This function starts the aplication and it allows it to appear in the screen
    Parameters
    -----------
    `None`

    Return
    ----------
    `None`

    Example
    >>> iniciar_interfaz()
    {None} -> Shows the interface in a window
    """
    
    try:
        interfaz:object = Ventana(lista_objetos=[organize_files,Crear_Carpetas,Carpeta,dir_name])
        interfaz.open_window()
    except Exception as e:
        print("Hubo un error al ejecutar la interfaz, el error es el siguiente",e)
        raise e

#Esta condición inicia la interfaz llamando a la función#
if __name__== "__main__":
    iniciar_interfaz()



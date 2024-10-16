from Verificador_fecha import Carpeta,dir_name
from Creador_python import Crear_Carpetas
from Interfaz import Ventana
from Ordenar_Archivos import organize_files

def iniciar_interfaz() -> None:
    try:
        interfaz:object = Ventana(lista_objetos=[organize_files,Crear_Carpetas,Carpeta,dir_name])
        interfaz.open_window()
    except Exception as e:
        print("Hubo un error al ejecutar la interfaz, el error es el siguiente",e)
        raise e


#File_names:object|Carpeta = Carpeta(2)
#File_names.calcular_semanas()

#dir_names:object|dir_name = dir_name(File_names.semanas,1)
#crear_folders:object|Crear_Carpetas = Crear_Carpetas(dir_names.folder_names())

#crear_folders.c_folders()

if __name__== "__main__":
    iniciar_interfaz()


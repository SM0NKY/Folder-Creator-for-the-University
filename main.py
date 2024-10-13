from Verificador_fecha import Carpeta,dir_name
from Creador_python import Crear_Carpetas

File_names:object|Carpeta = Carpeta(2)
File_names.calcular_semanas()

dir_names:object|dir_name = dir_name(File_names.semanas,1)
crear_folders:object|Crear_Carpetas = Crear_Carpetas(dir_names.folder_names())

crear_folders.c_folders()


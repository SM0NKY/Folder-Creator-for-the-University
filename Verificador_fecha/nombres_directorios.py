import time as tm
from typing import List
import os
import re

class dir_name():
    """ It creates the directories paths and checks in the folders if there is not any repeated folder
    Atributes
    ----------
    :file_names: `list`
    :semester: `int`
    :dir_uabc: `str`
    """
    def __init__(paths, file_names:List[str],semester:int,dir_uabc:str = "C:\\UABC"):
        
        paths.lista_folders:List[str] = file_names ; paths.path_uabc:str = os.path.join(dir_uabc,f"{semester}"); paths.directories:List[str] = [] 

    def folder_names(paths) -> List[str]:
        """ It creates the correspondent folder names for each subject and week
        Parameters
        ----------
        `None`

        :return List[str]:

        Example
        ----------
        >>> directory_names:object = dir_name(Atributes)
        >>> directory_names.folder_names()
        {["C\\Folder x\\Semestre 1\\Materia\\Semana 1",...,"C\\Folder x\\Semestre n\\Materia\\Semana n"]} -> It returns the missing week folders for each class topic
        """    
        try:
            print(paths.path_uabc)
            nombre_de_carpetas:List[str] = [x for x in os.listdir(paths.path_uabc)]

            for n in nombre_de_carpetas:
                for i in paths.lista_folders:
                    new_dict:str = os.path.join(paths.path_uabc,n,i)
                    if not os.path.exists(new_dict):
                        paths.directories.append(new_dict) #-- Crea la carpeta con el siguiente formato C://UABC//Semestre x//Materia//Semana x --#
            return paths.directories
        except Exception as e:
            print("Hubo un error, en la dir_name del archivo, en el archivo nombres_directorios")
            return []
            

if __name__ == "__main__":
    objeto:object = dir_name()
    objeto.folder_names()
    



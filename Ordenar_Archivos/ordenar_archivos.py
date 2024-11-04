import os 
import datetime as dt
import re
import time
from typing import List, Dict
import shutil

class organize_files():
    """ It organizes the files that aren't on a week folder
    Atributes
    ----------
    :semester: `int` -> The semester you're on
    :dir: `str` -> The directory of the school
    """

    def __init__(org,semester:int, periodo:int, dir = "C:\\UABC",):
        org.directory = os.path.join(dir,f"{semester}")
        org.pattern = r'(\d{4}){1}-(\d{2}){1}-(\d{2}){1}' #Patron para buscar el mes en el siguiente texto "2024-09-09 15:21:58.208346" , en este caso seria el 09#
        org.periodo = periodo
    
    def week(org,date:List[int]) -> str:
        """ This method calculates the correspondent week between the school period
        Parameters
        ----------
        :date: `List[int]` -> [year, month, date] 
        
        Return
        ----------
        `str` -> The week of the school period
        
        Example
        ----------
        >>> orgfiles:object = organize_files(Atributes)
        >>> orgfiles.week(date = [2024,12,25]) -> Format Year/Month/Day
        {None} -> Returns the week of the school year of the date introduced
        """        
        # --Calcular primero el dia del año --#
        try:
            dia_del_año:int = time.strptime(f"{date[0]}-{date[1]}-{date[2]}","%Y-%m-%d").tm_yday 
            fecha_inicio:List[int] = [time.localtime().tm_yday,1,27] if org.periodo == 1 else [time.localtime().tm_year,8,12]  
            faño_inicio:int = time.strptime(f"{fecha_inicio[0]}-{fecha_inicio[1]}-{fecha_inicio[2]}","%Y-%m-%d").tm_yday
            n_sem:int = (dia_del_año - faño_inicio)//7
            return f"Semana {n_sem}"
        except Exception as e:
            print(f"Error en el metodo week en la clase organize files, del archivo ordenar archivos.py, el error es el siguiente {e}")
            raise e

    def move_files(org,ruta_i,ruta_f) -> None:
        """ It moves the files from a place to another
        Parameters
        ----------
        :ruta_i: `str` -> The current path of the file
        :ruta_f: `str` -> The final or the path which the document is going to be transfered

        Return
        ----------
        `None`

        Example
        ----------
        >>> orgfiles:object = organize_files(Atributes)
        >>> orgfiles.move_files(ruta_i = "C:\\documen.docx",ruta_f = "C\\folder\\document.docx")
        {None} -> It moves the file from one path to another
        """
        
        try:
            if shutil.move(ruta_i,ruta_f):
                print(f"Se ha movido el archivo el archivo de la ruta {ruta_i} a la ruta {ruta_f}")
                pass
        except Exception as e:
            print("Hubo un error moviendo el archivo en el metodo move_files, de la clase organize_files, del archivo ordenar_archivos, el error es el siguiente",e)
            raise e
        pass 

    def organize(org) -> Dict[str,List[str]]:
        """ This method searchs for a pattern in the creation date of the file and returns the input and output location of the files
        Parameters
        ----------
        `None`
        
        Return
        ----------
        `Dict[str,List[str]]`    
        
        Example
        ----------
        >>> orgfiles:object = organize_files(Atributes)
        >>> orgfiles.organize()
        {document.docx: ["C\\document.docx","C:\\Semana 1\\document.docx"]} -> Returns the value of the dictionary with the files, their current path and their correspondent week path -> 
        """
        
        directorios:Dict[str,List[str]] = {}
        try:
            for materia in os.listdir(org.directory): #Busca en el directorio del # del semestre las materias#
                for x in os.listdir(os.path.join(org.directory,materia)): # Busca en cada materia los archivos que contiene carpetas y archivos#
                    directorio:str = os.path.join(org.directory,materia,x) 
                    
                    if os.path.isfile(directorio): #Realiza una accion si el archivo que busca es diferente de una carpeta#
                        fecha:str = f'{dt.datetime.fromtimestamp(os.path.getctime(directorio))}'
                        year:int = int(re.search(org.pattern,fecha).group(1))
                        month:int = int(re.search(org.pattern,fecha).group(2))
                        date:int = int(re.search(org.pattern,fecha).group(3))
                        semana:str = org.week(date = [year, month, date])
                        #print(f"El archivo es {x},\n su directorio es {directorio} ,\n creado en la semana {semana} ,\n le corresponde a {os.path.join(org.directory,materia,semana)}")
                        if not semana == "Semana 0":
                            directorios[x] = [directorio,os.path.join(org.directory,materia,semana,x)] # Formato del diccionario {documento: directorio_i, directorio_f}
            return directorios
                        
                    
        except Exception as e:
            print("Hubo un error en la clase organize_files del archivo ordenar achivos, el erroe es el siguiente",e)
            raise e
            


if __name__ == "__main__":
    organizador:object = organize_files(1,2)
    organizador.organize()
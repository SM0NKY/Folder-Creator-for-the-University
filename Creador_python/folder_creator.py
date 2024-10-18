import os 
from typing import List, Dict, Any
import ctypes as ct 
import re



class Crear_Carpetas():
    """ This class allows to create folders using the following atributes
    Atributes
    ---------
    path: `str` -> It is the place that the folders are going to be created
    Folders: `List` -> They're the names for the folders that are going to be used to create the folders
    """
    def __init__(self,Folders_wP:List[str]) -> None:
        
        self.FolderWPaths:List[str] = Folders_wP
        
    def c_folders(self) -> None:
        """ This functon creates the correspondent folders in case they don't exist
        
        Parameters
        ----------
        `None`
        
        Return 
        ----------
        `None`
        
        Example
        ----------
        >>> create:object = Crear_Carpetas(Atributes)
        >>> create.c_folders()
        {None} -> It makes new directories in case they don't exist
        
        """
        try:
            print(self.FolderWPaths)
            for i in self.FolderWPaths:
                os.mkdir(i)
                
        except Exception as e:
            raise e    
     

if __name__ == "__main__":
    None
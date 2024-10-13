import time
from typing import Any,Dict,List,Tuple

class Carpeta():
    """ It corroborates if there is any folder with the correspondent week name;
    if not, it creates one

    Attributes
    ----------
    inicio_ciclo: `list` -> kwarg | It indicates the start or the year cicle
    [0] -> Year: `int`
    [1] -> Month: `int`
    [2] -> Date: `int`
    """
    
    def __init__(self,periodo_año:str = 1) -> None:
        self.semanas:List = []
        self.fecha_final_ciclo:List[int] = [time.localtime().tm_year, 5, 31] if periodo_año == 1 else [time.localtime().tm_year, 11, 30]
        self.inicio_del_ciclo:List[int] = [time.localtime().tm_year, 1, 27] if periodo_año == 1 else [time.localtime().tm_year, 8, 12]
       
    def calcular_semanas(self) -> str|List[str]:
        """ It calculates the quantity of weeks that passed since the start of the year cicle
        
        Parameters
        ---------
        self : `Carpeta` -> Attributes

        :returns `List[str]`|`str`:
        
        """
        try:
            dia_del_año:int = time.strptime(f"{self.inicio_del_ciclo[0]}-{self.inicio_del_ciclo[1]}-{self.inicio_del_ciclo[2]}","%Y-%m-%d").tm_yday
            ultimo_dia:int = time.strptime(f"{self.fecha_final_ciclo[0]}-{self.fecha_final_ciclo[1]}-{self.fecha_final_ciclo[2]}","%Y-%m-%d").tm_yday
            sem_clases:int = (ultimo_dia - dia_del_año)//7 # In this line I utilized the `//` double slash to divide and round down to the nearest integer
            #print(f"Las semanas de clase son las siguientes: \n{sem_clases} Semanas")
            self.semanas = [f"Semana {x+1}" for x in range(sem_clases)]
            return self.semanas
        except Exception as e:
            raise e 
    #-- Con la lista resultante de self.semanas , utilizar folder creator, importar este paquete a main --#

        

# The structure of the tuple of the localtime
# [0] -> tm_year
# [1] -> tm_month
# [2] -> tm_mday
# [3] -> tm_hour
# [4] -> tm_min
# [5] -> tm_sec
# [6] -> tm_weekday
# [7] -> tm_yearday
# [8] -> tm_isdst

#-- Inicio del ciclo escolar --#
# 27 de enero al 31 de mayo 
# 12 de agosto al 30 de noviembre

# Pruebas para corroborar los metodos de la clase
if __name__ == "__main__":
    objeto:object = Carpeta(1)
    objeto.calcular_semanas()
    
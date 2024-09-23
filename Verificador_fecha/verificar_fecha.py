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
    def __init__(self,*inicio_ciclo:List[int]) -> None:
        self.fecha_actual_año:Tuple[vars] = time.localtime().tm_yday
        self.inicio_del_ciclo:Tuple[int] = [x for x in inicio_ciclo]
    
    def calcular_semanas(self) -> int:
        """ It calculates the quantity of weeks that passed since the start of the year cicle
        
        Parameters
        ---------
        self : `Carpeta` -> Attributes

        :returns `None`:
        
        """

        dia_del_año:int = time.strptime(f"{self.inicio_del_ciclo[0]}-{self.inicio_del_ciclo[1]}-{self.inicio_del_ciclo[2]}","%Y-%m-%d").tm_yday
        sem_clases:int = (self.fecha_actual_año - dia_del_año)//7 # In this line I utilized the `//` double slash to divide and round down to the nearest integer
        print(f"Las semanas de clase son las siguientes: \n{sem_clases} Semanas")
        return sem_clases
    
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

# Pruebas para corroborar los metodos de la clase
if __name__ == "__main__":
    
    objeto:object = Carpeta(2024,7,1)
    objeto.calcular_semanas()
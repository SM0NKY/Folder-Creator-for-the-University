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
        self.fecha_actual:Tuple[vars] = time.localtime()
        self.inicio_del_ciclo:Tuple[int] = [x for x in inicio_ciclo]
    
    def calcular_semanas(self) -> None:
        """ It calculates the quantity of weeks that passed since the start of the year cicle
        
        Parameters
        ---------
        self : `Carpeta` -> Attributes

        :returns `None`:
        
        """
        print(self.fecha_actual[0:3])
        print(self.inicio_del_ciclo)
    
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
    
    objeto:object = Carpeta(2024,3,21)
    objeto.calcular_semanas()
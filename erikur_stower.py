from math import prod
from typing import Type

class ErikurStower:
    """Klass för riktig stuveriarbetare"""

    def __init__(self, game_info: dict) -> None:
        if not isinstance(game_info, dict):   # Kontrollera att det är en dict
            raise ValueError("Ogiltig 'game_info.")

        try: # Testa om rätt keys finns
            self._truck = CyberTruck(game_info["vehicle"])
            self._not_loaded_packages = game_info["dimensions"]
        except KeyError:
                raise ValueError("Ogiltig 'game_info.")



    def stow_truck(self) -> list:
        """Stuva bilen riktig bra"""
        #self._truck
        #self._not_loaded_packages
        return "Asgrymt packat"




class CyberTruck:
    
    def __init__(self,vehicle: dict) -> None:
        return None




class Package:
    """Klass för paketen"""

    def __init__(self,package_data: dict) -> None:
        if not isinstance(package_data, dict):
            raise TypeError("package_data måste vara av typen dict")

        self._id = package_data["id"]
        self._order_class = package_data["orderClass"]
        self._weight_class = package_data["weightClass"]
        
        # Sorterad lista med paketets dimensioner
        self._dimensions = [package_data["width"], package_data["length"], package_data["height"]]      
        self._dimensions.sort()   
        self._volume = prod(self.dimensions)

        self.loaded_on_truck = False
        # Listor med koordinaterna på lastbilen
        self.x18 = [0 for _ in range(8)]
        self.y18, self.z18 = self.x18, self.x18

    @property 
    def id(self) -> str:
        return self._id

    @property 
    def order_class(self) -> int:
        return self._order_class

    @property 
    def weight_class(self) -> int:
        return self._weight_class
    
    @property 
    def dimensions(self) -> list:
        return self._dimensions
    
    @property 
    def volume(self) -> int:
        return self._volume

    @property 
    def loaded_on_truck(self) -> bool:
        return self._loaded_on_truck

    @loaded_on_truck.setter
    def loaded_on_truck(self, val: bool) -> None:
        if not isinstance(val, bool):
            raise TypeError("loaded_on_truck måste vara en boolean")
        self._loaded_on_truck = val

    @property
    def x18(self) -> list:
        return self._x18

    @x18.setter
    def x18(self, val: list) -> None:
        self.check_coordinates(val)
        self._x18 = val     

    @property
    def y18(self) -> list:
        return self._y18

    @y18.setter
    def y18(self, val: list) -> None:
        self.check_coordinates(val)
        self._y18 = val 

    @property
    def z18(self) -> list:
        return self._z18

    @z18.setter
    def z18(self, val: list) -> None:
        self.check_coordinates(val)
        self._z18 = val 

    @staticmethod
    def check_coordinates(val: list) -> None:
        """Felcheckar koordinatlistorna"""
        if not isinstance(val, list):
            raise TypeError("Lista koordinater ska vara av typen list")
        for v in val:
            if not isinstance(v, int):
                raise TypeError("Kooerdinaterna måste vara int")
            if v < 0:
                raise ValueError("Koordinare kan inte vara negativa")    

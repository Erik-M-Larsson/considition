#from math import prod
import numpy as np
from typing import Type
from itertools import permutations

class ErikurStower:
    """Klass för riktiga stuveriarbetare"""

    def __init__(self, game_info: dict) -> None:
        if not isinstance(game_info, dict):   # Kontrollera att det är en dict
            raise ValueError("Ogiltig 'game_info.")

        try: # Testa om rätt keys finns
            self._truck = CyberTruck(game_info["vehicle"])
            self._not_loaded_packages =  [Package(p) for p in game_info["dimensions"]]
        except KeyError:
                raise ValueError("Ogiltig 'game_info.")  

        self._not_loaded_packages = sorted(self._not_loaded_packages, key = lambda p: (p.volume), reverse = True)
        self._not_loaded_packages = sorted(self._not_loaded_packages, key = lambda p: (p.heavy), reverse = True)
        self._not_loaded_packages = sorted(self._not_loaded_packages, key = lambda p: (p.order_class), reverse = True)
    
        



    def stow_truck(self) -> list:
        """Stuva bilen riktig bra"""
        tr = self._truck
        packing_list = self._not_loaded_packages
        #print([packing_list[i].id for i in range(0,len(packing_list))])
        #tr.occu_space[199, 0, 130] = 1
        for p in packing_list:
            
            print("\npaket", p.id, "order_class", p.order_class, "vikt", p.weight_class, "volym", p.volume)
            # Lägg in paketet på flaket
            placements = []

            for x_dim, y_dim, z_dim in permutations([0, 1, 2], 3):  # För alla vridningar på paketet
                placement_ok = True

                y1 = tr.width - p.dimensions[y_dim]
                y2 = tr.width
                if p.heavy: 
                    z1 = 0
                    z2 = p.dimensions[z_dim]
                else: 
                    z1 = tr.height - p.dimensions[z_dim]
                    z2 = tr.height

                # x-led
                for i in range(tr.length, 0, -1): 
                    x1 = i-1
                    x2 = i
                
                    if not tr.is_space_empty(x1, y1, z1, x2, y2, z2):
                        i += 1
                        break

                x1, x2 = i-1, i -1 + p.dimensions[x_dim] 

                if x2 > tr.length:
                    placement_ok = False
                    print("Paketet är helt eller delvis utanför lastutrymmet")

                # y-led
                for i in range(tr.width, 0, -1):
                    y1 = i-1
                    y2 = i
                    if not tr.is_space_empty(x1, y1, z1, x2, y2, z2):
                        i += 1
                        break

                y1, y2 = i - 1, i - 1 + p.dimensions[y_dim]

                # z-led
                for i in range(tr.length, 0, -1):
                    z1 = i-1
                    z2 = i
                    if not tr.is_space_empty(x1, y1, z1, x2, y2, z2):
                        i += 1
                        break

                z1, z2 = i - 1, i - 1 + p.dimensions[z_dim]
                
                placements.append([x1, y1, z1, x2, y2, z2])
                
                

            # TODO välj vilken placering som är bäst
            
            tr.place_package(p, x1, y1, z1, x2, y2, z2)
            print(tr.occu_volume) 
            #print(tr.free_length) 
            #self._not_loaded_packages.pop(0) # TODO fungerar inte i en forloop
            #packing_list.pop(0)
            #print([packing_list[i].id for i in range(0,len(packing_list))])
        #print([packing_list[i].id for i in range(0,len(packing_list))])
        print(tr.free_length) 
        return "Asgrymt packat"




class CyberTruck:
    """Klass för lastbilen sm paketen lastas på"""
    
    def __init__(self,vehicle: dict) -> None:
        if not isinstance(vehicle, dict):   # Kontrollera att det är en dict
            raise ValueError("Ogiltig 'game_info'")
        
        try: # Testa om rätt keys finns
            self._length = vehicle["length"]
            self._width = vehicle["width"]
            self._height =vehicle["height"]
        except KeyError:
                raise ValueError("Ogiltig 'vehicle'")

        self.occu_space = np.ones((self.length, self.width, self.height), np.int8) * -1  # -1 -> ledigt
        self.loaded_packages =[]
        


        
    @property
    def length(self) -> int:
        return self._length

    @property
    def width(self) -> int:
        return self._width
           
    @property
    def height(self) -> int:
        return self._height

    @property
    def volume(self) -> int:
        return self.length * self.width * self.height

    @property
    def occu_space(self) -> np.ndarray:
        return self._occu_space

    @occu_space.setter
    def occu_space(self, val) -> None:
        if isinstance(val, np.ndarray):
            self._occu_space = val
        else:
            raise TypeError(f"Förväntade en ndarray fick '{type(val)}'")

    @property
    def occu_volume(self) -> int:
        if not np.count_nonzero(self.occu_space +1): # Räknar alla platser skillda från noll. +1  sätter alla lediga platser till 0.
            return 0
        return ((np.max(np.nonzero(np.count_nonzero(self.occu_space +1, axis=(0,1)))) + 1) *
                (np.max(np.nonzero(np.count_nonzero(self.occu_space +1, axis=(0,2)))) + 1) *
                (np.max(np.nonzero(np.count_nonzero(self.occu_space +1, axis=(1,2)))) + 1))

    @property
    def free_length(self) -> int:
        if not np.count_nonzero(self.occu_space +1): # Räknar alla platser skillda från noll. +1  sätter alla lediga platser till 0.
            return 0
        return self.occu_space.shape[0] - np.max(np.nonzero(np.count_nonzero(self.occu_space +1, axis=(1,2)))) - 1

    @property
    def loaded_packages(self) -> list:
        return self._loaded_packages

    @loaded_packages.setter
    def loaded_packages(self, val: list) -> None:
        if not isinstance(val, list):
            raise TypeError(f"Förväntad packing_list inte '{type(val)}'")
        self._loaded_packages = val

    def is_space_empty(self, x1: int, y1: int, z1: int, x2: int, y2:int, z2: int) -> bool:
        """Kontrollerar om den angivna volymen är ledig. Volymen utgörs av ett rätblock mellan de två punkterna"""
        return np.count_nonzero(self.occu_space[x1:x2, y1:y2, z1:z2] +1) == 0
    
    def place_package(self, package: "Package", x1: int, y1: int, z1: int, x2: int, y2: int, z2: int) -> None:
        """Placerar paketet på lastbilen och sätter paketets koordinater"""
        self.occu_space[x1:x2, y1:y2, z1:z2] = package.id # Reservera utrymme i lastutrymmet
        self.loaded_packages.append(package)

        # paketet
        package.x18 = [x1 for _ in range(0, 4)] + [x2 for _ in range(4, 8)]
        package.y18 = [y1 for _ in range(0, 4)] + [y2 for _ in range(4, 8)]
        package.z18 = [z1 for _ in range(0, 4)] + [z2 for _ in range(4, 8)]
        package.loaded_on_truck = True





class Package:
    """Klass för paketen"""

    def __init__(self,package_data: dict) -> None:
        if not isinstance(package_data, dict):
            raise TypeError("package_data måste vara av typen dict")

        self._id = package_data["id"]
        self._order_class = package_data["orderClass"]
        self._weight_class = package_data["weightClass"]
        
        # Sorterad packing_list med paketets dimensioner # TODO felcheck dim? 
        self._dimensions = [package_data["width"], package_data["length"], package_data["height"]]      
        self._dimensions.sort()   

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
    def heavy(self) -> bool:
        return self.weight_class == 2    
    
    @property 
    def dimensions(self) -> list:
        return self._dimensions
    
    @property 
    def volume(self) -> int:
        return np.prod(self.dimensions)

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

    
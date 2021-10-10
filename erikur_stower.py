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
            
            #print("\npaket", p.id, "order_class", p.order_class, "vikt", p.weight_class, "volym", p.volume)
            # Lägg in paketet på flaket
                        
            # TODO Försök pussla in paket i luckor
            
            placements = []
            for x_dim, y_dim, z_dim in permutations([0, 1, 2], 3):  # För alla vridningar på paketet
                
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
                x1, x2 = i - 1, i - 1 + p.dimensions[x_dim] 
 
                
                if x2 <= tr.length: # Kontollera om bakgaveln går att stänga
                    placement_ok = True
                else:
                    placement_ok = False
                    #print("Paketet är helt eller delvis utanför lastutrymmet")
    

                # y-led
                for i in range(y1, 0, -1):
                    y1 = i-1
                    y2 = i
                    if not tr.is_space_empty(x1, y1, z1, x2, y2, z2):
                        i += 1
                        break
                y1, y2 = i - 1, i - 1 + p.dimensions[y_dim]


                # z-led
                if not p.heavy:
                    for i in range(z1, 0, -1):
                        z1 = i-1
                        z2 = i
                        if not tr.is_space_empty(x1, y1, z1, x2, y2, z2):
                            i += 1
                            break
                    z1, z2 = i - 1, i - 1 + p.dimensions[z_dim]

                # Prova att placera paket
                tr.place_package(p, x1, y1, z1, x2, y2, z2)
                if placement_ok:    # Spara alternativ i lista om okej
                    placements.append({ "occupied volume" : tr.occu_volume,
                                        "coordinates" : (x1, y1, z1, x2, y2, z2)})
                tr.remomve_package(p) # Avlägsna paket igen

           
                  

            # TODO välj vilken placering som är bäst
            if not placements: #Kontrollera att det finns en giltig placering
                print("\npaket", p.id, "order_class", p.order_class, "vikt", p.weight_class, "volym", p.volume)
                print("Paketet får ej i lastbilen.")
                exit()
            
            placements = sorted(placements, key=lambda pa: pa["occupied volume"], reverse = False)
            #print(placements) 
            x1, y1, z1, x2, y2, z2 = placements[0]["coordinates"]
            tr.place_package(p, x1, y1, z1, x2, y2, z2)
            #print(tr.occu_volume) 

            print("\npaket", p.id, "order_class", p.order_class, "vikt", p.weight_class, "volym", p.volume, f" ({x1}, {y1}, {z1}) ", f"({x2}, {y2}, {z2}) ")

            #self._not_loaded_packages.pop(0) # TODO fungerar inte i en forloop
            #packing_list.pop(0)
            #print([packing_list[i].id for i in range(0,len(packing_list))])
        #print([packing_list[i].id for i in range(0,len(packing_list))])
        print("Packat o klart!") 
        
        # Formatera solution
        #print[(tr.loaded_packages)]
        solution =[]
        for p in tr.loaded_packages:
            solution.append({   'id': p.id,   
                                'x1': p.x18[0], 'x2': p.x18[1], 'x3': p.x18[2], 'x4': p.x18[3], 'x5': p.x18[4], 'x6': p.x18[5], 'x7': p.x18[6], 'x8': p.x18[7], 
                                'y1': p.y18[0], 'y2': p.y18[1], 'y3': p.y18[2], 'y4': p.y18[3], 'y5': p.y18[4], 'y6': p.y18[5], 'y7': p.y18[6], 'y8': p.y18[7],
                                'z1': p.z18[0], 'z2': p.z18[1], 'z3': p.z18[2], 'z4': p.z18[3], 'z5': p.z18[4], 'z6': p.z18[5], 'z7': p.z18[6], 'z8': p.z18[7],
                                'weightClass': p.weight_class, 'orderClass': p.order_class})
        
        
        return solution


 


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
        return ((np.max(np.nonzero(np.count_nonzero(self.occu_space +1, axis=(0,1)))) + 1) * # + 1 för att få längden inte index 
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

    def remomve_package(self, package: "Package") -> tuple:
        """Avlägnar redan placerat paket"""
        
        #print(el._truck.occu_space[np.where(el._truck == p.id)])
        self.occu_space[np.where(self.occu_space == package.id)] = -1 # Reservera utrymme i lastutrymmet
        self.loaded_packages.pop(self.loaded_packages.index(package)) # <--------------------------------------------rätt nu?

        # paketet   
        package.x18 = [0 for _ in range(0, 8)]
        package.y18 = [0 for _ in range(0, 8)]
        package.z18 = [0 for _ in range(0, 8)]
        package.loaded_on_truck = False

        return(package.x18[0] , package.y18[0] , package.z18[0], package.x18[-1], package.y18[-1], package.z18[-1])     





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

    
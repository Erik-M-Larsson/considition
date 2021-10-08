from math import prod

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

        self.id = package_data["id"]
        self.order_class = package_data["orderClass"]
        self.weight_class = package_data["weightClass"]
        
        # Sorterad lista med paketets dimensioner
        self.dimensions = [package_data["width"], package_data["length"], package_data["height"]]      
        self.dimensions.sort()   
        self.volume = prod(self.dimensions)

        self.loaded_on_truck = False
        # Listor med koordinaterna på lastbilen
        self.x18 = [0 for _ in range(8)]
        self.y18, self.z18 = self.x18, self.x18

                




class ErikurStower:
    """Klass för riktig stuveriarbetare"""

    def __init__(self, game_info: dict) -> None:
        self.check_game_info(game_info)
        self._truck = CyberTruck(game_info["vehicle"])
        self._not_loaded_packages = game_info["dimensions"]


    def check_game_info(self, val: any) -> None:
        """Kontrollerar så att det är en game_info som kommer in"""
        if isinstance(val, dict):   # Kontrollera att det är en dict
            try:
                val["mapName"]      # Kontrollera att rätt keys finns
                val["vehicle"]
                val["dimensions"]
            except KeyError:
                raise ValueError("Ogiltig 'game_info.")
        else:
            raise ValueError("Ogiltig 'game_info.")



    def stow_truck(self) -> list:
        """Stuva bilen riktig bra"""
        #self._truck
        #self._not_loaded_packages
        return "Asgrymt packat"




class CyberTruck:
    
    def __init__(self,vehicle) -> None:
        return None
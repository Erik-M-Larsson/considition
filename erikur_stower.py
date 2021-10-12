#from math import prod
import numpy as np
from typing import Type
from itertools import permutations
from itertools import islice
import timeit

from numpy.core.fromnumeric import nonzero



class ErikurStower():
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

    def push_package(self, direction: str, start: int, dim: int, x1: int=0, x2: int=0, y1: int=0, y2: int=0, z1: int=0, z2: int=0) -> tuple:   
        """Puttar paketet i riktning längs dim"""
        i = 1 # initera i ifall start = 0
        for i in range(start, 0, -1): # Kör tills paketet når väggen
            # Sätt startvärden
            if direction == 'x':
                x1 = i-1
                x2 = i 
            elif direction == 'y':
                y1 = i-1
                y2 = i
            elif direction == 'z':
                z1 = i-1
                z2 = i
            else:
                print("Ogiltig direction!")
                exit()    

            # Kolla om paketet stöter i annat paket och
            if not self._truck.is_space_empty(x1, y1, z1, x2, y2, z2):
                i += 1
                break
        return (i-1 , i-1 + dim )

    def format_solution(self) -> list:
        solution =[]
        for p in self._truck.loaded_packages:
            solution.append({   'id': p.id,   
                                'x1': p.x18[0], 'x2': p.x18[1], 'x3': p.x18[2], 'x4': p.x18[3], 'x5': p.x18[4], 'x6': p.x18[5], 'x7': p.x18[6], 'x8': p.x18[7], 
                                'y1': p.y18[0], 'y2': p.y18[1], 'y3': p.y18[2], 'y4': p.y18[3], 'y5': p.y18[4], 'y6': p.y18[5], 'y7': p.y18[6], 'y8': p.y18[7],
                                'z1': p.z18[0], 'z2': p.z18[1], 'z3': p.z18[2], 'z4': p.z18[3], 'z5': p.z18[4], 'z6': p.z18[5], 'z7': p.z18[6], 'z8': p.z18[7],
                                'weightClass': p.weight_class, 'orderClass': p.order_class})
        return solution

    def package_behind(self, p: "Package", x1: int , y1: int , z1: int, x2: int, y2: int, z2: int) -> bool:
        """Kontrollera om det finns paket framför med högre order"""
        o_space = self._truck.occu_space[x2:self._truck.length, y1:y2, z1:z2] # Volym från paket till bakgavel
        p_behind =set(self._truck.occu_space[x2:self._truck.length, y1:y2, z1:z2][np.nonzero(o_space+1)]) # Hitta alla unika värden på paket bakom
        
        order_class_loaded_p = { l_p.id : l_p.order_class for l_p in self._truck.loaded_packages}   # För snabbhet borde detta inte ligga i metoden

        for p_b in p_behind:
            if  order_class_loaded_p[p_b] > p.order_class:
                return True

        return False
        




# ****************************** Lösare ******************************

    def stow_truck(self) -> list:
        """Stuva bilen riktig bra"""
        tr = self._truck
        packing_list = self._not_loaded_packages
        
        for p in packing_list:
          
            # Lägg in paketet på flaket

            if len(tr.loaded_packages):  # Kolla om det redan finns paket på flaket annars lägg direkt på (0, 0, 0)
               
                # TODO Försök pussla in paket i luckor här
                
                placements = []
                for x_dim, y_dim, z_dim in permutations([0, 1, 2], 3):  # Prova alla vridningar på paketet
                    
                    
                    # startvärden 
                    x1 = tr.length
                    y1 = tr.width - p.dimensions[y_dim] # Längst till vänster
                    y2 = tr.width   
                    if p.heavy: # kontrollera om tungt paket välj startvärde z. På golvet
                        z1 = 0                      
                        z2 = p.dimensions[z_dim]
                    else: # högst upp vid taket
                        z1 = tr.height - p.dimensions[z_dim]
                        z2 = tr.height

                    xo, yo, zo = -1, -1, -1
                    while  (x1, y1, z1) != (xo, yo, zo):
                        xo, yo, zo = x1, y1, z1 # spara värden fån föregående iterration
                    
                        # Flytta in i x-led
                        x1, x2 = self.push_package(direction='x', start=x1, dim=p.dimensions[x_dim], y1=y1, y2=y2, z1=z1, z2=z2)

                        if x2 <= tr.length: # Kontollera om bakgaveln går att stänga
                            placement_ok = True
                        else:
                            placement_ok = False
                            #print("Paketet är helt eller delvis utanför lastutrymmet")
        
                        # Flytta i y-led
                        y1, y2 = self.push_package(direction='y', start=y1, dim=p.dimensions[y_dim], x1=x1, x2=x2, z1=z1, z2=z2)
                    
                        # Flytta i z-led
                        if not p.heavy:
                            z1, z2 = self.push_package(direction='z', start=z1, dim=p.dimensions[z_dim], x1=x1, x2=x2, y1=y1, y2=y2)

                    # Prova att placera paket
                    tr.place_package(p, x1, y1, z1, x2, y2, z2)
                    if placement_ok:    # Spara alternativ i lista om okej
                        placements.append({ "occupied volume" : tr.occu_volume,
                                            "coordinates" : (x1, y1, z1, x2, y2, z2)})
                    tr.remomve_package(p) # Avlägsna paket igen

            
                # TODO bättre urval av bästa plats

                if not placements: #Kontrollera att det finns en giltig placering
                    print("\npaket", p.id, "order_class", p.order_class, "vikt", p.weight_class, "volym", p.volume)
                    print("Paketet får ej i lastbilen.")
                    exit()
                
                placements = sorted(placements, key=lambda pa: pa["occupied volume"], reverse = False)
                #print(placements) 
            else: # lägg direkt på (0, 0, 0) längsta längden i x-led
                placements = [{ "occupied volume" : None, "coordinates" : (0, 0, 0, p.dimensions[2], p.dimensions[1], p.dimensions[0])}]

            # placera paket på vald bästa placering
            x1, y1, z1, x2, y2, z2 = placements[0]["coordinates"]
            tr.place_package(p, x1, y1, z1, x2, y2, z2)
            

            print("\n", len(tr.loaded_packages), "paket", p.id, "order_class", p.order_class, "vikt", p.weight_class, "volym", p.volume, f" ({x1}, {y1}, {z1}) ", f"({x2}, {y2}, {z2}) ")

            #self._not_loaded_packages.pop(0) # TODO fungerar inte i en forloop
            #packing_list.pop(0)
            #print([packing_list[i].id for i in range(0,len(packing_list))])
        #print([packing_list[i].id for i in range(0,len(packing_list))])
        
        print("Packat o klart!") 
        
        # Formatera solution
        solution = self.format_solution()
        
        return solution



    def stow_truck2(self) -> list:
        """Stuva bilen riktig bra"""
        start = timeit.default_timer()
        tr = self._truck
        packing_list = self._not_loaded_packages
        n_iter = 0
        for p in packing_list: # För varje paket
            
            # Lägg in paketet på flaket
            if len(tr.loaded_packages):  # Kolla om det redan finns paket   på flaket annars lägg direkt på (0, 0, 0)
                
                placements = []
                for x_dim, y_dim, z_dim in permutations([p.dimensions[0], p.dimensions[1], p.dimensions[2]], 3):  # Prova alla vridningar på paketet
                    if x_dim <= 0 or y_dim < 0 or z_dim < 0: 
                            raise ValueError(f"x1, y1, z1 kan inte vara < 0 1'({x1}, {y1}, {z1})'")
                    
                    # Hitta första tomma positionen där paketet passar

                    x_1, y_1, z_1 =  np.where(tr.occu_space[0 : tr.length-x_dim, 0 : tr.width-y_dim, 0 : tr.height-z_dim if not p.heavy else 1] == -1)
                    x_2, y_2, z_2 =np.array([x_1 + x_dim, y_1 + y_dim, z_1 + z_dim])
                    #x_2, y_2, z_2 =x_1 +  np.array([x_dim]), y_1 + np.array([y_dim]), z1 + np.array([z_dim]) #x_1, y_1, z_1 
                
                    for x1 , y1 , z1, x2, y2, z2 in  zip(x_1, y_1, z_1, x_2, y_2, z_2): 
                                           
                        x1, y1, z1, x2, y2, z2 = int(x1), int(y1), int(z1), int(x2), int(y2), int(z2)

                        n_iter += 1    
                        placement_ok = tr.is_space_empty(x1 , y1 , z1, x2, y2, z2)
                        if placement_ok:
                            break
                        elif np.nonzero(tr.occu_space[x1:x1+1 , y1:y1+1 , z1:tr.height] +1): # Kolla z-led om tomt uppåt skippa
                            n = tr.height - z1
                            next(islice(x_1, n, n), None)    
                            next(islice(y_1, n, n), None)    
                            next(islice(z_1, n, n), None)    
                            next(islice(x_2, n, n), None)    
                            next(islice(y_2, n, n), None)    
                            next(islice(z_2, n, n), None)  

                        
                    
                    #if x_dim <= 0 or y_dim < 0 or z_dim < 0: 
                    #        raise ValueError(f"x1, y1, z1 kan inte vara < 0 2'({x1}, {y1}, {z1})'")
                    #if x2-x1 <= 0 or y2-y1 <= 0 or z2-z1 <= 0:
                     #   raise ValueError(f"Paketet kan inte ha negativa sidlängder 2'({x2-x1}, {y2-y1}, {z2-z1})'")

                    # Prova att placera paket
                    if placement_ok:
                        tr.place_package(p, x1, y1, z1, x2, y2, z2)
                        placements.append({ "occupied volume" : tr.occu_volume, "coordinates" : (x1, y1, z1, x2, y2, z2)})
                        tr.remomve_package(p) # Avlägsna paket igen
            
                # TODO bättre urval av bästa plats

                if not placements: #Kontrollera att det finns en giltig placering
                    print("\npaket", p.id, "order_class", p.order_class, "vikt", p.weight_class, "volym", p.volume)
                    print("Paketet får ej plats i fordonet.")
                    exit()
                
                placements = sorted(placements, key=lambda pa: pa["occupied volume"], reverse = False)
                #print(placements)
            else: # lägg första paketet direkt på (0, 0, 0) längsta längden i x-led
                placements = [{ "occupied volume" : None, "coordinates" : (0, 0, 0, p.dimensions[2], p.dimensions[1], p.dimensions[0])}]

            # placera paket på vald bästa placering
            x1, y1, z1, x2, y2, z2 = placements[0]["coordinates"]
            tr.place_package(p, x1, y1, z1, x2, y2, z2)
            
            mid_time = timeit.default_timer()
            print("\n", len(tr.loaded_packages), "paket", p.id, "order_class", p.order_class, "vikt", p.weight_class, "volym", p.volume, f" ({x1}, {y1}, {z1}) ", f"({x2}, {y2}, {z2}) ", "n =", n_iter, "time:", mid_time-start)

            #self._not_loaded_packages.pop(0) # TODO fungerar inte i en forloop
            #packing_list.pop(0)
      
        print("Packat o klart!") 
        print(n_iter)
        # Formatera solution
        solution = self.format_solution()
        
        stop = timeit.default_timer()
        print((stop-start)//60, (stop-start)%60) 
        return solution    



    def load_truck(self) -> list:
        """Lasta bilen"""
        start = timeit.default_timer()
        tr = self._truck
        packing_list = self._not_loaded_packages
        n_iter = 0
        
        for p in packing_list: # För varje paket
           
            # Lägg in paketet på flaket
            if len(tr.loaded_packages):  # Kolla om det redan finns paket   på flaket annars lägg direkt på (0, 0, 0)
                
                placements = []
                for x_dim, y_dim, z_dim in permutations([p.dimensions[0], p.dimensions[1], p.dimensions[2]], 3):  # Prova alla vridningar på paketet
                    #if x_dim <= 0 or y_dim < 0 or z_dim < 0:                                            
                    #     raise ValueError(f"x1, y1, z1 kan inte vara < 0 1'({x1}, {y1}, {z1})'")
                     
                    # Hitta första tomma positionen där paketet passar
                    print(np.nonzero(tr.top_surface[0 : tr.length, 0 : tr.width, 0 : tr.height if not p.heavy else 1] ))
                    x_1, y_1, z_1 = np.nonzero(tr.top_surface[0 : tr.length-x_dim, 0 : tr.width-y_dim, 0 : tr.height-z_dim if not p.heavy else 1] )
                    x_2, y_2, z_2 = np.array([x_1 + x_dim, y_1 + y_dim, z_1 + z_dim])       # Få rätt typ för annars får Python spatt
                    #x_2, y_2, z_2 =x_1 +  np.array([x_dim]), y_1 + np.array([y_dim]), z1 + np.array([z_dim]) #x_1, y_1, z_1 
                    print(x_1, y1, z_1)
                    #print(x_1, y_1, z_1)
                    #print(x_2, y_2, z_2)
                    for x1 , y1 , z1, x2, y2, z2 in  zip(x_1, y_1, z_1, x_2, y_2, z_2): 
                        x1, y1, z1, x2, y2, z2 = int(x1), int(y1), int(z1), int(x2), int(y2), int(z2) # Få rätt typ för annars får Python spatt
                        n_iter += 1    
                        #print('T2')
                        placement_ok = tr.is_space_empty(x1 , y1 , z1, x2, y2, z2)
                        if placement_ok:
                            break
                       
                            
                    
                    #if x_dim <= 0 or y_dim < 0 or z_dim < 0: 
                    #        raise ValueError(f"x1, y1, z1 kan inte vara < 0 2'({x1}, {y1}, {z1})'")
                    #if x2-x1 <= 0 or y2-y1 <= 0 or z2-z1 <= 0:
                    #   raise ValueError(f"Paketet kan inte ha negativa sidlängder 2'({x2-x1}, {y2-y1}, {z2-z1})'")
                    #print("T3")
                    # Prova att placera paket
                    if placement_ok:
                        tr.place_package(p, x1, y1, z1, x2, y2, z2) # TODO snyggare lösning på det här
                        placements.append({ "occupied volume" : tr.occu_volume, "coordinates" : (x1, y1, z1, x2, y2, z2)})
                        tr.remomve_package(p) # Avlägsna paket igen
            
                # TODO bättre urval av bästa plats

                if not placements: #Kontrollera att det finns en giltig placering
                    print("\npaket", p.id, "order_class", p.order_class, "vikt", p.weight_class, "volym", p.volume)
                    print("Paketet får ej plats i fordonet.")
                    exit()
                
                placements = sorted(placements, key=lambda pa: pa["occupied volume"], reverse = False)
               
            else: # lägg första paketet direkt på (0, 0, 0) längsta längden i x-led
                placements = [{ "occupied volume" : None, "coordinates" : (0, 0, 0, p.dimensions[2], p.dimensions[1], p.dimensions[0])}]

            # placera paket på vald bästa placering
            x1, y1, z1, x2, y2, z2 = placements[0]["coordinates"]
            tr.place_package(p, x1, y1, z1, x2, y2, z2)
            
            mid_time = timeit.default_timer()
            print("\n", len(tr.loaded_packages), "paket", p.id, "order_class", p.order_class, "vikt", p.weight_class, "volym", p.volume, f" ({x1}, {y1}, {z1}) ", f"({x2}, {y2}, {z2}) ", "n =", n_iter, "time:", mid_time-start)


        print("Packat o klart!") 
        print(n_iter)
        # Formatera solution 
        solution = self.format_solution()
        stop = timeit.default_timer()
        print((stop-start)//60, (stop-start)%60) 
        return solution           
    


    def load_faster(self) -> list:
        """Lasta bilen"""
        start = timeit.default_timer()
        tr = self._truck
        packing_list = self._not_loaded_packages
        n_iter = 0
        
        for p in packing_list: # För varje paket
           
            # Lägg in paketet på flaket
            if len(tr.loaded_packages):  # Kolla om det redan finns paket   på flaket annars lägg direkt på (0, 0, 0)
                
                placements = []
                for x_dim, y_dim, z_dim in permutations([p.dimensions[0], p.dimensions[1], p.dimensions[2]], 3):  # Prova alla vridningar på paketet
                  
                    x_1, y_1, z_1 = np.nonzero(tr.free_corners[0 : tr.length, 0 : tr.width, 0 : tr.height if not p.heavy else 1] )
                    x_2, y_2, z_2 = np.array([x_1 + x_dim, y_1 + y_dim, z_1 + z_dim])       # Få rätt typ för annars får Python spatt
                    
                    for x1 , y1 , z1, x2, y2, z2 in  zip(x_1, y_1, z_1, x_2, y_2, z_2): 
                        x1, y1, z1, x2, y2, z2 = int(x1), int(y1), int(z1), int(x2), int(y2), int(z2) # Få rätt typ för annars får Python spatt
                        n_iter += 1    
                    
                        xo, yo, zo, = -1, -1, -1
                        while  (x1, y1, z1) != (xo, yo, zo):
                            xo, yo, zo = x1, y1, z1 # spara värden fån föregående iterration
                            z1, z2 = self.push_package('z', start=z1, dim=z_dim, x1=x1, x2=x2, y1=y1, y2=y2)
                            x1, x2 = self.push_package('x', start=x1, dim=x_dim, y1=y1, y2=y2, z1=z1, z2=z2)
                            y1, y2 = self.push_package('y', start=y1, dim=y_dim, x1=x1, x2=x2, z1=z1, z2=z2) # Funkar inte, varför?
                            
                        if not ((x2 <= tr.length) and (y2 <= tr.width) and (z2 < tr.height)): # Kolla så paketet inte är utanför
                            continue
                        
                        placement_ok = tr.is_space_empty(x1 , y1 , z1, x2, y2, z2) # Kolla att det är tomt

                        # Kontrollera om paket med högre order framför
                        p_b = self.package_behind(p,x1 , y1 , z1, x2, y2, z2)

                        if placement_ok and not p_b:
                            break
                        #else:
                            #print("ej ok")
                       
                    # Prova att placera paket
                    if placement_ok: # TODO metod
                        tr.occu_space[x1:x2, y1:y2, z1:z2] = -7 # Reservera ytrymmet 
                        placements.append({ "occupied volume" : tr.occu_volume, "coordinates" : (x1, y1, z1, x2, y2, z2)})
                        tr.occu_space[x1:x2, y1:y2, z1:z2] = -1 # Avboka ytrymmet 
            
                # TODO bättre urval av bästa plats <------------------------------------------------------------------------------------- OBS

                if not placements: #Kontrollera att det finns en giltig placering
                    print("\npaket", p.id, "order_class", p.order_class, "vikt", p.weight_class, "volym", p.volume)
                    print("Paketet får ej plats i fordonet.")
                    exit()
                placements = sorted(placements, key=lambda pa: pa["coordinates"][5]-pa["coordinates"][2], reverse = True)
                placements = sorted(placements, key=lambda pa: pa["occupied volume"], reverse = False)
               
            else: # lägg första paketet direkt på (0, 0, 0) längsta längden i x-led
                placements = [{ "occupied volume" : None, "coordinates" : (0, 0, 0, p.dimensions[2], p.dimensions[0], p.dimensions[1])}]

            # placera paket på vald bästa placering
            x1, y1, z1, x2, y2, z2 = placements[0]["coordinates"]
            tr.place_package(p, x1, y1, z1, x2, y2, z2)
            
            mid_time = timeit.default_timer()
            print("\n", len(tr.loaded_packages), "paket", p.id, "order_class", p.order_class, "vikt", p.weight_class, "volym", p.volume, f" ({x1}, {y1}, {z1}) ", f"({x2}, {y2}, {z2}) ", "n =", n_iter, "time:", mid_time-start)
           
          
        print("Packat o klart!") 
        print("Iteration: ", n_iter)
        # Formatera solution 
        solution = self.format_solution()
        stop = timeit.default_timer()
        print(f"Time {(stop-start)//60:f0}:{(stop-start)%60:f0}" )

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
        self.top_surface = np.zeros((self.length, self.width, self.height), bool)
        self.top_surface[:, :, 0] += True
        
        self.free_corners = np.zeros((self.length, self.width, self.height), bool)
        self.free_corners[0, 0, 0] = np.True_ 

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
    def top_surface(self) -> np.ndarray:
        return self._top_surface   
    
    @top_surface.setter
    def top_surface(self, val: np.ndarray) -> None:
        if isinstance(val, np.ndarray): 
            self._top_surface = val
        else:
            raise TypeError(f"Förväntade en ndarray fick '{type(val)}'")

    @property
    def free_corners(self) -> np.ndarray:
        return self._free_corners
    
    @free_corners.setter
    def free_corners(self, val: np.ndarray) -> None:
        if isinstance(val, np.ndarray): 
            self._free_corners = val
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
        #print(np.count_nonzero(self.occu_space[x1:x2, y1:y2, z1:z2] +1))
        return np.count_nonzero(self.occu_space[x1:x2, y1:y2, z1:z2] +1) == 0
    
    def place_package(self, package: "Package", x1: int, y1: int, z1: int, x2: int, y2: int, z2: int) -> None:
        """Placerar paketet på lastbilen och sätter paketets koordinater"""
        self.occu_space[x1:x2, y1:y2, z1:z2] = package.id # Reservera utrymme i lastutrymmet
        self.top_surface[x1:x2, y1:y2, z1] = 0
        self.top_surface[x1:x2, y1:y2, z2-1] = 1
        self.free_corners[x1, y1, z1] = np.False_
        self.free_corners[x1, y1, z2] = np.True_
        self.free_corners[x2, y1, z1] = np.True_
        self.free_corners[x1, y2, z1] = np.True_
        self.loaded_packages.append(package)

        # paketet
        package.x18 = [x1 for _ in range(0, 4)] + [x2 for _ in range(4, 8)]
        package.y18 = [y1 for _ in range(0, 4)] + [y2 for _ in range(4, 8)]
        package.z18 = [z1 for _ in range(0, 4)] + [z2 for _ in range(4, 8)]
        package.loaded_on_truck = True

    def remomve_package(self, package: "Package") -> tuple:
        """Avlägnar redan placerat paket"""
        
        #print(el._truck.occu_space[np.where(el._truck == p.id)])
        self.occu_space[np.where(self.occu_space == package.id)] = -1 # Avboka utrymme i lastutrymmet
        if package.z18[0]:     # Kolla om paketet inte ligger på golver och lägg till bottenarean
            x, y = nonzero(self.occu_space[package.x18[0]:package.x18[-1], package.y18[0]:package.y18[-1], package.z18[0]-1] + 1)
            self.top_surface[x, y, package.z18[0]]     # Sätt yta till tillgänglig på den dela av ytan med paket under
        else: # Om paketet ligger på golvet
            self.top_surface[package.x18[0]:package.x18[-1], package.y18[0]:package.y18[-1], package.z18[0]] = 1  
        
        self.top_surface[package.x18[0]:package.x18[-1], package.y18[0]:package.y18[-1], package.z18[-1]-1] = 0  # Tabort ovansida
        self.free_corners[package.x18[0], package.y18[0], package.z18[0]] = np.True_
        self.free_corners[package.x18[0], package.y18[0], package.z18[-1]] = np.False_
        #self.free_corners[x2, y1, z1] = np.False_ Behöver jag ta bort dessa? Det borde inte väljas ändå?
        #self.free_corners[x1, y2, z1] = np.False_
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
                raise TypeError(f"Kooerdinaterna måste vara int inte {type(val)}")
            if v < 0:
                raise ValueError("Koordinare kan inte vara negativa")    

    
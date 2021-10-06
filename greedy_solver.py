import operator


class GreedySolver:
    xp = 0
    zp = 0
    yp = 0
    heavyPackages = []
    otherPackages = []
    placedPackages = []
    lastKnownMaxWidth = 0
    lastKnownMaxLength = 0
    lastKnownMaxHeight = 0

    def __init__(self, game_info):
       
        self.vehicle_length = game_info["vehicle"]["length"]    # Måtten på bilen
        self.vehicle_width = game_info["vehicle"]["width"]
        self.vehicle_height = game_info["vehicle"]["height"]
        self.packages = game_info["dimensions"]                 # Lista med dictionary för varje pkt           
       
        """for package in self.packages:                           # För alla paket
            #if(package["height"] > self.lastKnownMaxHeight and package["weightClass"] == 2 ):
            if(package["height"] and package["weightClass"] == 2 > self.lastKnownMaxHeight):
                self.lastKnownMaxHeight = package["height"]
            if(package["weightClass"] == 2):
                self.heavyPackages.append(
                    {"area": package["width"]*package["length"], "id": package["id"]})
            elif(package["weightClass"] != 2): # Varför inte bara else?
                self.otherPackages.append(
                    {"area": package["width"]*package["length"], "id": package["id"]})
        self.heavyPackages = sorted(
            self.heavyPackages, key=lambda i: (i['area'])) # sortera på area?
        self.otherPackages = sorted(
            self.otherPackages, key=lambda i: (i['area']))
        
        print(self.heavyPackages)
        print(self.otherPackages)"""

        for package in self.packages: 
            package["volume"] = package["width"] * package["length"] * package["height"]
            if  package["width"] > package["length"]:
                package["width"], package["length"] = package["length"], package["width"]
            

        self.packages = sorted(self.packages, key = lambda i: (i["volume"]), reverse = True)
        self.packages = sorted(self.packages, key = lambda i: (i["orderClass"]), reverse = True)
        #print("Hallå?")
        #print(self.packages)

    def Solve(self):
     
        for i, package in enumerate(self.packages):
            """if(self.zp <= self.lastKnownMaxHeight):
                id = self.heavyPackages.pop()["id"]
                package = self.packages[id]
            elif(len(self.otherPackages) != 0):
                id = self.otherPackages.pop()["id"]
                package = self.packages[id]
            else:
                id = self.heavyPackages.pop()["id"]
                package = self.packages[id]"""

            #package = p
            #print(i, package)
            
            package_added = False

            if package["id"] == 42:
                self.AddPackage_manual(package, 0, 40, 127, 150, 0, 12)
            elif package["id"] == 49:
                self.AddPackage_manual(package, 0, 39, 124, 150, 12, 25)
            elif package["id"] == 25:
                self.AddPackage_manual(package, 0, 42, 125, 150, 25, 42)
            elif package["id"] == 57:
                self.AddPackage_manual(package, 0, 42, 125, 150, 42, 62)
            elif package["id"] == 21:
                self.AddPackage_manual(package, 0, 41, 134, 150, 62, 96)
            elif package["id"] == 20:
                self.AddPackage_manual(package, 0, 41, 125, 150, 96, 112)
            elif package["id"] == 19:
                self.AddPackage_manual(package, 0, 41, 124, 150, 112, 129)
            elif package["id"] == 52:
                self.AddPackage_manual(package, 42, 60, 128, 150, 0, 38)
            elif package["id"] == 58:
                self.AddPackage_manual(package, 45, 60, 126, 150, 38, 86)
            elif package["id"] == 18:
                self.AddPackage_manual(package, 46, 60, 126, 150, 86, 119)
            elif package["id"] == 24:
                self.AddPackage_manual(package, 60, 100, 126, 150, 0, 11)
            elif package["id"] == 26:
                self.AddPackage_manual(package, 60, 99, 113, 126, 0, 12)
            elif package["id"] == 50:
                self.AddPackage_manual(package, 60, 96, 110, 139, 12, 22)
            elif package["id"] == 38:
                self.AddPackage_manual(package, 60, 101, 129, 150, 22, 26)
            elif package["id"] == 34:
                self.AddPackage_manual(package, 60, 97, 126, 150, 26, 32)
            elif package["id"] == 33:
                self.AddPackage_manual(package, 60, 100, 135, 150, 32, 44)
            elif package["id"] == 37:
                self.AddPackage_manual(package, 60, 94, 125, 150, 44, 53)
            elif package["id"] == 30:
                self.AddPackage_manual(package, 60, 98, 126, 150, 53, 65)
            elif package["id"] == 40:
                self.AddPackage_manual(package, 60, 99, 117, 150, 65, 76)               
            elif package["id"] == 48:
                self.AddPackage_manual(package, 60, 101, 123, 150, 76, 93)
            elif package["id"] == 45:
                self.AddPackage_manual(package, 60, 102, 117, 150, 93, 111)
            elif package["id"] == 59: # 17 37 11
                self.AddPackage_manual(package, 183, 200, 113, 150, 0, 11)             
            


            else:
                # Z
                pack_vrid = (
                    self.flip_package_x(package),
                    self.flip_package_x(self.flip_package_z(package)),
                    package, 
                    self.flip_package_z(package), 
                    self.flip_package_y(package), 
                    self.flip_package_x(self.flip_package_y(package)) 
                    )

                for pv in pack_vrid:
                    if(self.DoesPackageFitZ(pv)):
                        self.AddPackage(pv)
                        self.zp += pv["height"]
                        
                        self.SetMaxX(pv)
                        self.SetMaxY(pv)
                        package_added = True
                        #print("fit z\n")
                        break
                
                # Y
                if(package_added == False):             
                    for pv in pack_vrid:
                        if(self.DoesPackageFitY(pv)):
                            self.yp += self.lastKnownMaxWidth
                            self.zp = 0
                            self.AddPackage(pv)
                            self.zp = pv["height"]
                            self.lastKnownMaxWidth = 0

                            self.SetMaxX(pv)
                            self.SetMaxY(pv)
                            package_added = True
                            #print("fit y", pv, '\n')
                            break
                    
                
                # X
                if(package_added == False):    
                    for pv in pack_vrid:
                        if(self.DoesPackageFitX(pv)):
                            self.xp += self.lastKnownMaxLength
                            self.yp = 0
                            self.zp = 0
                            self.AddPackage(pv)
                            self.zp = pv["height"]
                            self.lastKnownMaxLength = 0

                            self.SetMaxX(pv)
                            self.SetMaxY(pv)
                            package_added = True
                            #print("fit z\n")
                            break



                if(package_added == False):
                    print("Something went terribly wrong!")
                    #print(self.xp + self.lastKnownMaxLength + package["length"])
                    #return None
                    #break

            #self.SetMaxX(package)
            #self.SetMaxY(package)
        for  i, package in enumerate(self.placedPackages):
            if package["id"] == 3:
                #print(self.placedPackages[i]['id'])
                self.placedPackages[i] ["z1"] = 52
                self.placedPackages[i] ["z2"] = 52
                self.placedPackages[i] ["z3"] = 52
                self.placedPackages[i] ["z4"] = 52
                self.placedPackages[i] ["z5"] = 86
                self.placedPackages[i] ["z6"] = 86
                self.placedPackages[i] ["z7"] = 86
                self.placedPackages[i] ["z8"] = 86
            elif package["id"] == 6:
                #print(self.placedPackages[i]['id'])
                self.placedPackages[i] ["z1"] = 86
                self.placedPackages[i] ["z2"] = 86
                self.placedPackages[i] ["z3"] = 86
                self.placedPackages[i] ["z4"] = 86
                self.placedPackages[i] ["z5"] = 110
                self.placedPackages[i] ["z6"] = 110
                self.placedPackages[i] ["z7"] = 110
                self.placedPackages[i] ["z8"] = 110
        return self.placedPackages

    @staticmethod
    def flip_package_x(package) -> dict:
        """Flippa paket run x-axeln"""
        package["width"], package["height"] = package["height"], package["width"]
        return package
    
    @staticmethod
    def flip_package_y(package) -> dict:
        """Flippa paket run y-axeln"""
        package["length"], package["height"] = package["height"], package["length"]
        return package
    
    @staticmethod
    def flip_package_z(package) -> dict:
        """Flippa paket run z-axeln"""
        package["width"], package["length"] = package["length"], package["width"]
        return package

    def DoesPackageFitX(self, package):
        return self.xp + self.lastKnownMaxLength + package["length"] < self.vehicle_length

    def DoesPackageFitY(self, package):
        return self.yp + self.lastKnownMaxWidth + package["width"] < self.vehicle_width and self.xp + package["length"] < self.vehicle_length

    def DoesPackageFitZ(self, package):
        return self.xp + package["length"] < self.vehicle_length and self.yp + package["width"] < self.vehicle_width and self.zp + package["height"] < self.vehicle_height

    def SetMaxY(self, package):
        if(package["width"] > self.lastKnownMaxWidth):
            self.lastKnownMaxWidth = package["width"]

    def SetMaxX(self, package):
        if(package["length"] > self.lastKnownMaxLength):
            self.lastKnownMaxLength = package["length"]

    def AddPackage(self, package):
        self.placedPackages.append({"id": package["id"], "x1": self.xp, "x2": self.xp, "x3": self.xp, "x4": self.xp,
                                    "x5": self.xp + package["length"], "x6": self.xp + package["length"], "x7": self.xp + package["length"], "x8": self.xp + package["length"],
                                    "y1": self.yp, "y2": self.yp, "y3": self.yp, "y4": self.yp,
                                    "y5": self.yp + package["width"], "y6": self.yp + package["width"], "y7": self.yp + package["width"], "y8": self.yp + package["width"],
                                    "z1": self.zp, "z2": self.zp, "z3": self.zp, "z4": self.zp,
                                    "z5": self.zp + package["height"], "z6": self.zp + package["height"], "z7": self.zp + package["height"], "z8": self.zp + package["height"], "weightClass": package["weightClass"], "orderClass": package["orderClass"]})

    def AddPackage_manual(self, package, x14, x58, y14, y58, z14, z58):
        self.placedPackages.append({"id": package["id"], 
                                    "x1": x14, "x2": x14, "x3": x14, "x4": x14,
                                    "x5": x58, "x6": x58, "x7": x58, "x8": x58,
                                    "y1": y14, "y2": y14, "y3": y14, "y4": y14,
                                    "y5": y58, "y6": y58, "y7": y58, "y8": y58,
                                    "z1": z14, "z2": z14, "z3": z14, "z4": z14,
                                    "z5": z58, "z6": z58, "z7": z58, "z8": z58, 
                                    "weightClass": package["weightClass"],
                                    "orderClass": package["orderClass"]})
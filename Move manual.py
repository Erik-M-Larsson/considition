import api
from erikur_stower import CyberTruck, Package

api_key = "3b9a5199-9d80-4178-b658-3b216564d0b4"   
map_name = "training1" # TODO fyll i rätt karta

def flytta(cb, p_id, x_dim, y_dim, z_dim, x1=None, y1=None, z1=None, x2=None, y2=None, z2=None):
    package = None
    for p in cb.loaded_packages: # gör metod
        if p.id == p_id:
            package = p

  
    if type(x1) == int:
        x2 = x1 + package.dimensions[x_dim]
    elif type(x2) == int:
        x1 = x2 - package.dimensions[x_dim]
    else:
        x1 = cb.length - package.dimensions[x_dim]
        x2 = cb.length
        x1, x2 = cb.push_package(direction='x', start= x1, dim=package.dimensions[x_dim], y1=y1, y2=y2, z1=z1, z2=z2)
    
    if type(y1) == int:
        y2 = y1 + package.dimensions[y_dim]
    elif type(y2) == int:
        y1 = y2 - package.dimensions[y_dim]
    else:
        y1 = cb.width - package.dimensions[y_dim]
        y2 = cb.width
        y1, y2 = cb.push_package(direction='y', start= y1, dim=package.dimensions[y_dim], x1=x1, x2=x2, z1=z1, z2=z2)

    if type(z1) == int:
        z2 = z1 + package.dimensions[z_dim]
    elif type(z2) == int:
        z1 = z2 - package.dimensions[z_dim]
    else:
        z1 = cb.height - package.dimensions[z_dim]
        z2 = cb.height
        z1, z2 = cb.push_package(direction='z', start= z1, dim=package.dimensions[z_dim], x1=x1, x2=x2, y1=y1, y2=y2)

    print('(', x1, y1, z1, ') (', x2, y2, z2, ')')

    cb.move_package(package, x1, y1, z1, x2, y2, z2)


#***************************************************
'''
# Filnamn 
path = "prol_tr2_s.txt"	
path = r"C:/Users/ErikLarsson-AIU21GBG/Documents/GitHub/considition/files/" + path


# TODO fixa inläsning från fil. Läs in solution
with open(path, 'r') as f:
    f.read
		f_ut.write("solution = \n")
		f_ut.write(str(solution) + '\n'*2)
		f_ut.write("**************************" + '\n'*2)
			
		for i, p in enumerate(solution):
			f_ut.write(f"{i}\n")
			for k, v in p.items():
				#print(f"\t{k} : {v}")
				f_ut.write(f"\t{k} : {v}\n")
			#print('')	
			f_ut.write('\n')
    solution = 1'''

#***************************************************




vehicle ={  'length' : 200,
            'width' : 150,
            'height' : 136}

cb = CyberTruck(vehicle)

# TODO klipp in den solution du vill ändra nedan
solution = [{'id': 3, 'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 68, 'x6': 68, 'x7': 68, 'x8': 68, 'y1': 0, 'y2': 0, 'y3': 0, 'y4': 0, 'y5': 34, 'y6': 34, 'y7': 34, 'y8': 34, 'z1': 0, 'z2': 0, 'z3': 0, 'z4': 0, 'z5': 47, 'z6': 47, 'z7': 47, 'z8': 47, 'weightClass': 0, 'orderClass': 0}, {'id': 1, 'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 73, 'x6': 73, 'x7': 73, 'x8': 73, 'y1': 0, 'y2': 0, 'y3': 0, 'y4': 0, 'y5': 25, 'y6': 25, 'y7': 25, 'y8': 25, 'z1': 47, 'z2': 47, 'z3': 47, 'z4': 47, 'z5': 93, 'z6': 93, 'z7': 93, 'z8': 93, 'weightClass': 1, 'orderClass': 0}, {'id': 8, 'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 64, 'x6': 64, 'x7': 64, 'x8': 64, 'y1': 34, 'y2': 34, 'y3': 34, 'y4': 34, 'y5': 51, 'y6': 51, 'y7': 51, 'y8': 51, 'z1': 0, 'z2': 0, 'z3': 0, 'z4': 0, 'z5': 68, 'z6': 68, 'z7': 68, 'z8': 68, 'weightClass': 0, 'orderClass': 0}, {'id': 15, 'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 37, 'x6': 37, 'x7': 37, 'x8': 37, 'y1': 51, 'y2': 51, 'y3': 51, 'y4': 51, 'y5': 67, 'y6': 67, 'y7': 67, 'y8': 67, 'z1': 0, 'z2': 0, 'z3': 0, 'z4': 0, 'z5': 73, 'z6': 73, 'z7': 73, 'z8': 73, 'weightClass': 0, 'orderClass': 0}, {'id': 29, 'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 31, 'x6': 31, 'x7': 31, 'x8': 31, 'y1': 0, 'y2': 0, 'y3': 0, 'y4': 0, 'y5': 43, 'y6': 43, 'y7': 43, 'y8': 43, 'z1': 93, 'z2': 93, 'z3': 93, 'z4': 93, 'z5': 105, 'z6': 105, 'z7': 105, 'z8': 105, 'weightClass': 1, 'orderClass': 0}, {'id': 53, 'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 27, 'x6': 27, 'x7': 27, 'x8': 27, 'y1': 43, 'y2': 43, 'y3': 43, 'y4': 43, 'y5': 57, 'y6': 57, 'y7': 57, 'y8': 57, 'z1': 73, 'z2': 73, 'z3': 73, 'z4': 73, 'z5': 112, 'z6': 112, 'z7': 112, 'z8': 112, 'weightClass': 1, 'orderClass': 0}, {'id': 27, 'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 29, 'x6': 29, 'x7': 29, 'x8': 29, 'y1': 0, 'y2': 0, 'y3': 0, 'y4': 0, 'y5': 29, 'y6': 29, 'y7': 29, 'y8': 29, 'z1': 105, 'z2': 105, 'z3': 105, 'z4': 105, 'z5': 119, 'z6': 119, 'z7': 119, 'z8': 119, 'weightClass': 1, 'orderClass': 0}, {'id': 51, 'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 25, 'x6': 25, 'x7': 25, 'x8': 25, 'y1': 25, 'y2': 25, 'y3': 25, 'y4': 25, 'y5': 33, 'y6': 33, 'y7': 33, 'y8': 33, 'z1': 47, 'z2': 47, 'z3': 47, 'z4': 47, 'z5': 85, 'z6': 85, 'z7': 85, 'z8': 85, 'weightClass': 1, 'orderClass': 0}, {'id': 59, 'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 17, 'x6': 17, 'x7': 17, 'x8': 17, 'y1': 57, 'y2': 57, 'y3': 57, 'y4': 57, 'y5': 68, 'y6': 68, 'y7': 68, 'y8': 68, 'z1': 73, 'z2': 73, 'z3': 73, 'z4': 73, 'z5': 110, 'z6': 110, 'z7': 110, 'z8': 110, 'weightClass': 1, 'orderClass': 0}, {'id': 17, 'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 47, 'x6': 47, 'x7': 47, 'x8': 47, 'y1': 67, 'y2': 67, 'y3': 67, 'y4': 67, 'y5': 91, 'y6': 91, 'y7': 91, 'y8': 91, 'z1': 0, 'z2': 0, 'z3': 0, 'z4': 0, 'z5': 72, 'z6': 72, 'z7': 72, 'z8': 72, 'weightClass': 2, 'orderClass': 0}, {'id': 16, 'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 74, 'x6': 74, 'x7': 74, 'x8': 74, 'y1': 68, 'y2': 68, 'y3': 68, 'y4': 68, 'y5': 95, 'y6': 95, 'y7': 95, 'y8': 95, 'z1': 72, 'z2': 72, 'z3': 72, 'z4': 72, 'z5': 135, 'z6': 135, 'z7': 135, 'z8': 135, 'weightClass': 1, 'orderClass': 1}, {'id': 6, 'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 54, 'x6': 54, 'x7': 54, 'x8': 54, 'y1': 91, 'y2': 91, 'y3': 91, 'y4': 91, 'y5': 115, 'y6': 115, 'y7': 115, 'y8': 115, 'z1': 0, 'z2': 0, 'z3': 0, 'z4': 0, 'z5': 58, 'z6': 58, 'z7': 58, 'z8': 58, 'weightClass': 1, 'orderClass': 1}, {'id': 45, 'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 33, 'x6': 33, 'x7': 33, 'x8': 33, 'y1': 95, 'y2': 95, 'y3': 95, 'y4': 95, 'y5': 113, 'y6': 113, 'y7': 113, 'y8': 113, 'z1': 58, 'z2': 58, 'z3': 58, 'z4': 58, 'z5': 100, 'z6': 100, 'z7': 100, 'z8': 100, 'weightClass': 1, 'orderClass': 1}, {'id': 30, 'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 38, 'x6': 38, 'x7': 38, 'x8': 38, 'y1': 29, 'y2': 29, 'y3': 29, 'y4': 29, 'y5': 41, 'y6': 41, 'y7': 41, 'y8': 41, 'z1': 105, 'z2': 105, 'z3': 105, 'z4': 105, 'z5': 129, 'z6': 129, 'z7': 129, 'z8': 129, 'weightClass': 1, 'orderClass': 1}, {'id': 33, 'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 40, 'x6': 40, 'x7': 40, 'x8': 40, 'y1': 0, 'y2': 0, 'y3': 0, 'y4': 0, 'y5': 12, 'y6': 12, 'y7': 12, 'y8': 12, 'z1': 119, 'z2': 119, 'z3': 119, 'z4': 119, 'z5': 134, 'z6': 134, 'z7': 134, 'z8': 134, 'weightClass': 1, 'orderClass': 1}, {'id': 0, 'x1': 38, 'x2': 38, 'x3': 38, 'x4': 38, 'x5': 96, 'x6': 96, 'x7': 96, 'x8': 96, 'y1': 25, 'y2': 25, 'y3': 25, 'y4': 25, 'y5': 50, 'y6': 50, 'y7': 50, 'y8': 50, 'z1': 68, 'z2': 68, 'z3': 68, 'z4': 68, 'z5': 127, 'z6': 127, 'z7': 127, 'z8': 127, 'weightClass': 2, 'orderClass': 1}, {'id': 48, 'x1': 68, 'x2': 68, 'x3': 68, 'x4': 68, 'x5': 85, 'x6': 85, 'x7': 85, 'x8': 85, 'y1': 0, 'y2': 0, 'y3': 0, 'y4': 0, 'y5': 27, 'y6': 27, 'y7': 27, 'y8': 27, 'z1': 0, 'z2': 0, 'z3': 0, 'z4': 0, 'z5': 41, 'z6': 41, 'z7': 41, 'z8': 41, 'weightClass': 2, 'orderClass': 1}, {'id': 40, 'x1': 47, 'x2': 47, 'x3': 47, 'x4': 47, 'x5': 58, 'x6': 58, 'x7': 58, 'x8': 58, 'y1': 51, 'y2': 51, 'y3': 51, 'y4': 51, 'y5': 84, 'y6': 84, 'y7': 84, 'y8': 84, 'z1': 0, 'z2': 0, 'z3': 0, 'z4': 0, 'z5': 39, 'z6': 39, 'z7': 39, 'z8': 39, 'weightClass': 2, 'orderClass': 1}, {'id': 37, 'x1': 40, 'x2': 40, 'x3': 40, 'x4': 40, 'x5': 49, 'x6': 49, 'x7': 49, 'x8': 49, 'y1': 0, 'y2': 0, 'y3': 0, 'y4': 0, 'y5': 25, 'y6': 25, 'y7': 25, 'y8': 25, 'z1': 93, 'z2': 93, 'z3': 93, 'z4': 93, 'z5': 127, 'z6': 127, 'z7': 127, 'z8': 127, 'weightClass': 2, 'orderClass': 1}, {'id': 34, 'x1': 73, 'x2': 73, 'x3': 73, 'x4': 73, 'x5': 79, 'x6': 79, 'x7': 79, 'x8': 79, 'y1': 0, 'y2': 0, 'y3': 0, 'y4': 0, 'y5': 24, 'y6': 24, 'y7': 24, 'y8': 24, 'z1': 41, 'z2': 41, 'z3': 41, 'z4': 41, 'z5': 78, 'z6': 78, 'z7': 78, 'z8': 78, 'weightClass': 2, 'orderClass': 1}, {'id': 38, 'x1': 58, 'x2': 58, 'x3': 58, 'x4': 58, 'x5': 62, 'x6': 62, 'x7': 62, 'x8': 62, 'y1': 51, 'y2': 51, 'y3': 51, 'y4': 51, 'y5': 72, 'y6': 72, 'y7': 72, 'y8': 72, 'z1': 0, 'z2': 0, 'z3': 0, 'z4': 0, 'z5': 41, 'z6': 41, 'z7': 41, 'z8': 41, 'weightClass': 2, 'orderClass': 1}, {'id': 13, 'x1': 54, 'x2': 54, 'x3': 54, 'x4': 54, 'x5': 74, 'x6': 74, 'x7': 74, 'x8': 74, 'y1': 84, 'y2': 84, 'y3': 84, 'y4': 84, 'y5': 128, 'y6': 128, 'y7': 128, 'y8': 128, 'z1': 0, 'z2': 0, 'z3': 0, 'z4': 0, 'z5': 64, 'z6': 64, 'z7': 64, 'z8': 64, 'weightClass': 0, 'orderClass': 2}, {'id': 22, 'x1': 64, 'x2': 64, 'x3': 64, 'x4': 64, 'x5': 82, 'x6': 82, 'x7': 82, 'x8': 82, 'y1': 34, 'y2': 34, 'y3': 34, 'y4': 34, 'y5': 84, 'y6': 84, 'y7': 84, 'y8': 84, 'z1': 0, 'z2': 0, 'z3': 0, 'z4': 0, 'z5': 27, 'z6': 27, 'z7': 27, 'z8': 27, 'weightClass': 0, 'orderClass': 2}, {'id': 47, 'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 45, 'x6': 45, 'x7': 45, 'x8': 45, 'y1': 95, 'y2': 95, 'y3': 95, 'y4': 95, 'y5': 116, 'y6': 116, 'y7': 116, 'y8': 116, 'z1': 100, 'z2': 100, 'z3': 100, 'z4': 100, 'z5': 124, 'z6': 124, 'z7': 124, 'z8': 124, 'weightClass': 1, 'orderClass': 2}, {'id': 56, 'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 23, 'x6': 23, 'x7': 23, 'x8': 23, 'y1': 113, 'y2': 113, 'y3': 113, 'y4': 113, 'y5': 132, 'y6': 132, 'y7': 132, 'y8': 132, 'z1': 58, 'z2': 58, 'z3': 58, 'z4': 58, 'z5': 99, 'z6': 99, 'z7': 99, 'z8': 99, 'weightClass': 1, 'orderClass': 2}, {'id': 43, 'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 31, 'x6': 31, 'x7': 31, 'x8': 31, 'y1': 115, 'y2': 115, 'y3': 115, 'y4': 115, 'y5': 127, 'y6': 127, 'y7': 127, 'y8': 127, 'z1': 0, 'z2': 0, 'z3': 0, 'z4': 0, 'z5': 45, 'z6': 45, 'z7': 45, 'z8': 45, 'weightClass': 1, 'orderClass': 2}, {'id': 46, 'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 42, 'x6': 42, 'x7': 42, 'x8': 42, 'y1': 116, 'y2': 116, 'y3': 116, 'y4': 116, 'y5': 132, 'y6': 132, 'y7': 132, 'y8': 132, 'z1': 99, 'z2': 99, 'z3': 99, 'z4': 99, 'z5': 122, 'z6': 122, 'z7': 122, 'z8': 122, 'weightClass': 1, 'orderClass': 2}, {'id': 32, 'x1': 33, 'x2': 33, 'x3': 33, 'x4': 33, 'x5': 45, 'x6': 45, 'x7': 45, 'x8': 45, 'y1': 95, 'y2': 95, 'y3': 95, 'y4': 95, 'y5': 135, 'y6': 135, 'y7': 135, 'y8': 135, 'z1': 58, 'z2': 58, 'z3': 58, 'z4': 58, 'z5': 90, 'z6': 90, 'z7': 90, 'z8': 90, 'weightClass': 1, 'orderClass': 2}, {'id': 31, 'x1': 45, 'x2': 45, 'x3': 45, 'x4': 45, 'x5': 58, 'x6': 58, 'x7': 58, 'x8': 58, 'y1': 95, 'y2': 95, 'y3': 95, 'y4': 95, 'y5': 133, 'y6': 133, 'y7': 133, 'y8': 133, 'z1': 64, 'z2': 64, 'z3': 64, 'z4': 64, 'z5': 90, 'z6': 90, 'z7': 90, 'z8': 90, 'weightClass': 1, 'orderClass': 2}, {'id': 50, 'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 29, 'x6': 29, 'x7': 29, 'x8': 29, 'y1': 95, 'y2': 95, 'y3': 95, 'y4': 95, 'y5': 131, 'y6': 131, 'y7': 131, 'y8': 131, 'z1': 124, 'z2': 124, 'z3': 124, 'z4': 124, 'z5': 134, 'z6': 134, 'z7': 134, 'z8': 134, 'weightClass': 1, 'orderClass': 2}, {'id': 26, 'x1': 74, 'x2': 74, 'x3': 74, 'x4': 74, 'x5': 86, 'x6': 86, 'x7': 86, 'x8': 86, 'y1': 84, 'y2': 84, 'y3': 84, 'y4': 84, 'y5': 123, 'y6': 123, 'y7': 123, 'y8': 123, 'z1': 0, 'z2': 0, 'z3': 0, 'z4': 0, 'z5': 13, 'z6': 13, 'z7': 13, 'z8': 13, 'weightClass': 0, 'orderClass': 2}, {'id': 28, 'x1': 45, 'x2': 45, 'x3': 45, 'x4': 45, 'x5': 61, 'x6': 61, 'x7': 61, 'x8': 61, 'y1': 95, 'y2': 95, 'y3': 95, 'y4': 95, 'y5': 139, 'y6': 139, 'y7': 139, 'y8': 139, 'z1': 90, 'z2': 90, 'z3': 90, 'z4': 90, 'z5': 121, 'z6': 121, 'z7': 121, 'z8': 121, 'weightClass': 2, 'orderClass': 2}, {'id': 39, 'x1': 58, 'x2': 58, 'x3': 58, 'x4': 58, 'x5': 73, 'x6': 73, 'x7': 73, 'x8': 73, 'y1': 95, 'y2': 95, 'y3': 95, 'y4': 95, 'y5': 133, 'y6': 133, 'y7': 133, 'y8': 133, 'z1': 64, 'z2': 64, 'z3': 64, 'z4': 64, 'z5': 86, 'z6': 86, 'z7': 86, 'z8': 86, 'weightClass': 2, 'orderClass': 2}, {'id': 54, 'x1': 61, 'x2': 61, 'x3': 61, 'x4': 61, 'x5': 73, 'x6': 73, 'x7': 73, 'x8': 73, 'y1': 95, 'y2': 95, 'y3': 95, 'y4': 95, 'y5': 122, 'y6': 122, 'y7': 122, 'y8': 122, 'z1': 86, 'z2': 86, 'z3': 86, 'z4': 86, 'z5': 124, 'z6': 124, 'z7': 124, 'z8': 124, 'weightClass': 2, 'orderClass': 2}, {'id': 55, 'x1': 73, 'x2': 73, 'x3': 73, 'x4': 73, 'x5': 83, 'x6': 83, 'x7': 83, 'x8': 83, 'y1': 95, 'y2': 95, 'y3': 95, 'y4': 95, 'y5': 123, 'y6': 123, 'y7': 123, 'y8': 123, 'z1': 64, 'z2': 64, 'z3': 64, 'z4': 64, 'z5': 104, 'z6': 104, 'z7': 104, 'z8': 104, 'weightClass': 2, 'orderClass': 2}, {'id': 24, 'x1': 68, 'x2': 68, 'x3': 68, 'x4': 68, 'x5': 79, 'x6': 79, 'x7': 79, 'x8': 79, 'y1': 27, 'y2': 27, 'y3': 27, 'y4': 27, 'y5': 51, 'y6': 51, 'y7': 51, 'y8': 51, 'z1': 27, 'z2': 27, 'z3': 27, 'z4': 27, 'z5': 67, 'z6': 67, 'z7': 67, 'z8': 67, 'weightClass': 2, 'orderClass': 2}, {'id': 14, 'x1': 82, 'x2': 82, 'x3': 82, 'x4': 82, 'x5': 113, 'x6': 113, 'x7': 113, 'x8': 113, 'y1': 27, 'y2': 27, 'y3': 27, 'y4': 27, 'y5': 79, 'y6': 79, 'y7': 79, 'y8': 79, 'z1': 0, 'z2': 0, 'z3': 0, 'z4': 0, 'z5': 56, 'z6': 56, 'z7': 56, 'z8': 56, 'weightClass': 0, 'orderClass': 3}, {'id': 21, 'x1': 74, 'x2': 74, 'x3': 74, 'x4': 74, 'x5': 90, 'x6': 90, 'x7': 90, 'x8': 90, 'y1': 50, 'y2': 50, 'y3': 50, 'y4': 50, 'y5': 91, 'y6': 91, 'y7': 91, 'y8': 91, 'z1': 67, 'z2': 67, 'z3': 67, 'z4': 67, 'z5': 101, 'z6': 101, 'z7': 101, 'z8': 101, 'weightClass': 1, 'orderClass': 3}, {'id': 57, 'x1': 86, 'x2': 86, 'x3': 86, 'x4': 86, 'x5': 106, 'x6': 106, 'x7': 106, 'x8': 106, 'y1': 79, 'y2': 79, 'y3': 79, 'y4': 79, 'y5': 121, 'y6': 121, 'y7': 121, 'y8': 121, 'z1': 0, 'z2': 0, 'z3': 0, 'z4': 0, 'z5': 25, 'z6': 25, 'z7': 25, 'z8': 25, 'weightClass': 0, 'orderClass': 3}, {'id': 19, 'x1': 31, 'x2': 31, 'x3': 31, 'x4': 31, 'x5': 48, 'x6': 48, 'x7': 48, 'x8': 48, 'y1': 115, 'y2': 115, 'y3': 115, 'y4': 115, 'y5': 141, 'y6': 141, 'y7': 141, 'y8': 141, 'z1': 0, 'z2': 0, 'z3': 0, 'z4': 0, 'z5': 41, 'z6': 41, 'z7': 41, 'z8': 41, 'weightClass': 0, 'orderClass': 3}, {'id': 25, 'x1': 49, 'x2': 49, 'x3': 49, 'x4': 49, 'x5': 66, 'x6': 66, 'x7': 66, 'x8': 66, 'y1': 0, 'y2': 0, 'y3': 0, 'y4': 0, 'y5': 25, 'y6': 25, 'y7': 25, 'y8': 25, 'z1': 93, 'z2': 93, 'z3': 93, 'z4': 93, 'z5': 135, 'z6': 135, 'z7': 135, 'z8': 135, 'weightClass': 1, 'orderClass': 3}, {'id': 58, 'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 24, 'x6': 24, 'x7': 24, 'x8': 24, 'y1': 127, 'y2': 127, 'y3': 127, 'y4': 127, 'y5': 142, 'y6': 142, 'y7': 142, 'y8': 142, 'z1': 0, 'z2': 0, 'z3': 0, 'z4': 0, 'z5': 48, 'z6': 48, 'z7': 48, 'z8': 48, 'weightClass': 0, 'orderClass': 3}, {'id': 52, 'x1': 73, 'x2': 73, 'x3': 73, 'x4': 73, 'x5': 91, 'x6': 91, 'x7': 91, 'x8': 91, 'y1': 95, 'y2': 95, 'y3': 95, 'y4': 95, 'y5': 133, 'y6': 133, 'y7': 133, 'y8': 133, 'z1': 104, 'z2': 104, 'z3': 104, 'z4': 104, 'z5': 126, 'z6': 126, 'z7': 126, 'z8': 126, 'weightClass': 1, 'orderClass': 3}, {'id': 18, 'x1': 66, 'x2': 66, 'x3': 66, 'x4': 66, 'x5': 80, 'x6': 80, 'x7': 80, 'x8': 80, 'y1': 0, 'y2': 0, 'y3': 0, 'y4': 0, 'y5': 24, 'y6': 24, 'y7': 24, 'y8': 24, 'z1': 93, 'z2': 93, 'z3': 93, 'z4': 93, 'z5': 126, 'z6': 126, 'z7': 126, 'z8': 126, 'weightClass': 1, 'orderClass': 3}, {'id': 42, 'x1': 48, 'x2': 48, 'x3': 48, 'x4': 48, 'x5': 71, 'x6': 71, 'x7': 71, 'x8': 71, 'y1': 128, 'y2': 128, 'y3': 128, 'y4': 128, 'y5': 140, 'y6': 140, 'y7': 140, 'y8': 140, 'z1': 0, 'z2': 0, 'z3': 0, 'z4': 0, 'z5': 40, 'z6': 40, 'z7': 40, 'z8': 40, 'weightClass': 0, 'orderClass': 3}, {'id': 7, 'x1': 83, 'x2': 83, 'x3': 83, 'x4': 83, 'x5': 109, 'x6': 109, 'x7': 109, 'x8': 109, 'y1': 91, 'y2': 91, 'y3': 91, 'y4': 91, 'y5': 134, 'y6': 134, 'y7': 134, 'y8': 134, 'z1': 25, 'z2': 25, 'z3': 25, 'z4': 25, 'z5': 90, 'z6': 90, 'z7': 90, 'z8': 90, 'weightClass': 2, 'orderClass': 3}, {'id': 2, 'x1': 90, 'x2': 90, 'x3': 90, 'x4': 90, 'x5': 114, 'x6': 114, 'x7': 114, 'x8': 114, 'y1': 50, 'y2': 50, 'y3': 50, 'y4': 50, 'y5': 86, 'y6': 86, 'y7': 86, 'y8': 86, 'z1': 56, 'z2': 56, 'z3': 56, 'z4': 56, 'z5': 101, 'z6': 101, 'z7': 101, 'z8': 101, 'weightClass': 2, 'orderClass': 3}, {'id': 20, 'x1': 79, 'x2': 79, 'x3': 79, 'x4': 79, 'x5': 95, 'x6': 95, 'x7': 95, 'x8': 95, 'y1': 0, 'y2': 0, 'y3': 0, 'y4': 0, 'y5': 25, 'y6': 25, 'y7': 25, 'y8': 25, 'z1': 41, 'z2': 41, 'z3': 41, 'z4': 41, 'z5': 82, 'z6': 82, 'z7': 82, 'z8': 82, 'weightClass': 2, 'orderClass': 3}, {'id': 49, 'x1': 91, 'x2': 91, 'x3': 91, 'x4': 91, 'x5': 104, 'x6': 104, 'x7': 104, 'x8': 104, 'y1': 86, 'y2': 86, 'y3': 86, 'y4': 86, 'y5': 112, 'y6': 112, 'y7': 112, 'y8': 112, 'z1': 90, 'z2': 90, 'z3': 90, 'z4': 90, 'z5': 129, 'z6': 129, 'z7': 129, 'z8': 129, 'weightClass': 2, 'orderClass': 3}, {'id': 5, 'x1': 96, 'x2': 96, 'x3': 96, 'x4': 96, 'x5': 124, 'x6': 124, 'x7': 124, 'x8': 124, 'y1': 0, 'y2': 0, 'y3': 0, 'y4': 0, 'y5': 47, 'y6': 47, 'y7': 47, 'y8': 47, 'z1': 56, 'z2': 56, 'z3': 56, 'z4': 56, 'z5': 121, 'z6': 121, 'z7': 121, 'z8': 121, 'weightClass': 1, 'orderClass': 4}, {'id': 12, 'x1': 109, 'x2': 109, 'x3': 109, 'x4': 109, 'x5': 130, 'x6': 130, 'x7': 130, 'x8': 130, 'y1': 86, 'y2': 86, 'y3': 86, 'y4': 86, 'y5': 145, 'y6': 145, 'y7': 145, 'y8': 145, 'z1': 0, 'z2': 0, 'z3': 0, 'z4': 0, 'z5': 67, 'z6': 67, 'z7': 67, 'z8': 67, 'weightClass': 1, 'orderClass': 4}, {'id': 4, 'x1': 109, 'x2': 109, 'x3': 109, 'x4': 109, 'x5': 131, 'x6': 131, 'x7': 131, 'x8': 131, 'y1': 86, 'y2': 86, 'y3': 86, 'y4': 86, 'y5': 146, 'y6': 146, 'y7': 146, 'y8': 146, 'z1': 67, 'z2': 67, 'z3': 67, 'z4': 67, 'z5': 129, 'z6': 129, 'z7': 129, 'z8': 129, 'weightClass': 1, 'orderClass': 4}, {'id': 11, 'x1': 113, 'x2': 113, 'x3': 113, 'x4': 113, 'x5': 136, 'x6': 136, 'x7': 136, 'x8': 136, 'y1': 0, 'y2': 0, 'y3': 0, 'y4': 0, 'y5': 65, 'y6': 65, 'y7': 65, 'y8': 65, 'z1': 0, 'z2': 0, 'z3': 0, 'z4': 0, 'z5': 47, 'z6': 47, 'z7': 47, 'z8': 47, 'weightClass': 1, 'orderClass': 4}, {'id': 10, 'x1': 130, 'x2': 130, 'x3': 130, 'x4': 130, 'x5': 155, 'x6': 155, 'x7': 155, 'x8': 155, 'y1': 65, 'y2': 65, 'y3': 65, 'y4': 65, 'y5': 133, 'y6': 133, 'y7': 133, 'y8': 133, 'z1': 0, 'z2': 0, 'z3': 0, 'z4': 0, 'z5': 35, 'z6': 35, 'z7': 35, 'z8': 35, 'weightClass': 0, 'orderClass': 4}, {'id': 9, 'x1': 136, 'x2': 136, 'x3': 136, 'x4': 136, 'x5': 162, 'x6': 162, 'x7': 162, 'x8': 162, 'y1': 0, 'y2': 0, 'y3': 0, 'y4': 0, 'y5': 35, 'y6': 35, 'y7': 35, 'y8': 35, 'z1': 0, 'z2': 0, 'z3': 0, 'z4': 0, 'z5': 50, 'z6': 50, 'z7': 50, 'z8': 50, 'weightClass': 0, 'orderClass': 4}, {'id': 41, 'x1': 136, 'x2': 136, 'x3': 136, 'x4': 136, 'x5': 152, 'x6': 152, 'x7': 152, 'x8': 152, 'y1': 35, 'y2': 35, 'y3': 35, 'y4': 35, 'y5': 61, 'y6': 61, 'y7': 61, 'y8': 61, 'z1': 0, 'z2': 0, 'z3': 0, 'z4': 0, 'z5': 43, 'z6': 43, 'z7': 43, 'z8': 43, 'weightClass': 0, 'orderClass': 4}, {'id': 44, 'x1': 62, 'x2': 62, 'x3': 62, 'x4': 62, 'x5': 82, 'x6': 82, 'x7': 82, 'x8': 82, 'y1': 51, 'y2': 51, 'y3': 51, 'y4': 51, 'y5': 74, 'y6': 74, 'y7': 74, 'y8': 74, 'z1': 27, 'z2': 27, 'z3': 27, 'z4': 27, 'z5': 65, 'z6': 65, 'z7': 65, 'z8': 65, 'weightClass': 1, 'orderClass': 4}, {'id': 35, 'x1': 80, 'x2': 80, 'x3': 80, 'x4': 80, 'x5': 96, 'x6': 96, 'x7': 96, 'x8': 96, 'y1': 0, 'y2': 0, 'y3': 0, 'y4': 0, 'y5': 25, 'y6': 25, 'y7': 25, 'y8': 25, 'z1': 82, 'z2': 82, 'z3': 82, 'z4': 82, 'z5': 129, 'z6': 129, 'z7': 129, 'z8': 129, 'weightClass': 2, 'orderClass': 4}, {'id': 23, 'x1': 85, 'x2': 85, 'x3': 85, 'x4': 85, 'x5': 98, 'x6': 98, 'x7': 98, 'x8': 98, 'y1': 0, 'y2': 0, 'y3': 0, 'y4': 0, 'y5': 20, 'y6': 20, 'y7': 20, 'y8': 20, 'z1': 0, 'z2': 0, 'z3': 0, 'z4': 0, 'z5': 37, 'z6': 37, 'z7': 37, 'z8': 37, 'weightClass': 2, 'orderClass': 4}, {'id': 36, 'x1': 114, 'x2': 114, 'x3': 114, 'x4': 114, 'x5': 123, 'x6': 123, 'x7': 123, 'x8': 123, 'y1': 47, 'y2': 47, 'y3': 47, 'y4': 47, 'y5': 71, 'y6': 71, 'y7': 71, 'y8': 71, 'z1': 47, 'z2': 47, 'z3': 47, 'z4': 47, 'z5': 86, 'z6': 86, 'z7': 86, 'z8': 86, 'weightClass': 2, 'orderClass': 4}]

# Läs in ocha skapa alla paker och lasta på cb
for p in solution:
    p_data= {  'id' : p['id'],
	        'width' : p['y8'] - p['y1'],
	        'length' : p['x8'] - p['x1'],
	        'height' : p['z8'] - p['z1'],
	        'weightClass' : p['weightClass'],
	        'orderClass' : p['orderClass']}
    
    cb.place_package(package=Package(p_data), x1=p['x1'], y1=p['y1'], z1=p['z1'], x2=p['x8'], y2=p['y8'], z2=p['z8'])


# Längdder på paketet
kort, mellan, lång = 0, 1, 2 

# ******************************************************************************

# Flytta paketen
# Fyll endast i anting x1 eller x2   
# Fyll endast i anting y1 eller y2
# Fyll endast i anting z1 eller z2. 
# Det går även att utelämna någon men endast en av x, y, z helt. Då hamnar den på första ytan från max.
# Fyll i kort, mellan, lång beroende på hur du vill orientera paketet



id = 53
x1 = None
x2 = None
y1 = None
y2 = 150
z1 = None
z2 = None
flytta(cb, id, mellan, lång, kort, x1, y1, z1, x2, y2, z2)

id = 3
x1 = 136-5
x2 = None
y1 = 0
y2 = None
z1 = None
z2 = None
flytta(cb, id, kort, lång, mellan, x1, y1, z1, x2, y2, z2)


'''
id = 41
x2 = cb.length 
y2 = cb.width
z1 = 0
flytta(cb, id, lång, mellan, kort, x2=x2, y2=y2, z1=z1)


id = 9
x2 = cb.length 
y2 = cb.width
z1 = 16
flytta(cb, id, mellan, lång, kort, x2=x2, y2=y2, z1=z1)


id = 10
x2 = cb.length 
y2 = cb.width
z1 = 42
flytta(cb, id, mellan, lång, kort, x2=x2, y2=y2, z1=z1)


id = 11
x2 = cb.length 
y2 = cb.width
z1 = 67
flytta(cb, id, mellan, lång, kort, x2=x2, y2=y2, z1=z1)


id = 5
x2 = cb.length 
y2 = cb.width
z1 = 90
flytta(cb, id, mellan, lång, kort, x2=x2, y2=y2, z1=z1)


id = 36
x1 = cb.length  
y2 = cb.width
z1 = 118
#flytta(cb, id, mellan, lång, kort, x2=x2, y2=y2, z1=z1)

deltax = 25

id = 4
x2 = cb.length - deltax
y1 = 0
z1 = 0
#flytta(cb, id, mellan, lång, kort, x2=x2, y1=y1, z1=z1)


id = 12
x1 = None
x2 = cb.length - deltax
y1 = 0
y2 = None
z1 = 22
z2 = None
#flytta(cb, id, mellan, lång, kort, x1, y1, z1, x2, y2, z2)

id = 58
x1 = None
x2 = cb.length - deltax
y1 = 0
y2 = None
z1 = 43
z2 = None
#flytta(cb, id, mellan, lång, kort, x1, y1, z1, x2, y2, z2)

id = 19
x1 = None
x2 = cb.length - deltax
y1 = 0
y2 = None
z1 = 58
z2 = None
#flytta(cb, id, mellan, lång, kort, x1, y1, z1, x2, y2, z2)

id = 57
x1 = None
x2 = cb.length - deltax 
y1 = 0
y2 = None
z1 = 75
z2 = None
#flytta(cb, id, mellan, lång, kort, x1, y1, z1, x2, y2, z2)

id = 42
x1 = None
x2 = cb.length - deltax 
y1 = 0
y2 = None
z1 = 95
z2 = None
#flytta(cb, id, mellan, lång, kort, x1, y1, z1, x2, y2, z2)

id = 23
x1 = None
x2 = cb.length - deltax
y1 = 0
y2 = None
z1 = 107
z2 = None
#flytta(cb, id, mellan, lång, kort, x1, y1, z1, x2, y2, z2)
'''
#**********************************************************************

# skapa den nya lösningen
new_solution = cb.format_solution()

# Skriv till fil
path_ut = f"manual_{map_name}_sol.txt"	
path_ut = r"C:/Users/ErikLarsson-AIU21GBG/Documents/GitHub/considition/files/" + path_ut

with open(path_ut, 'w')	as f_ut:
    f_ut.write("solution = \n")
    f_ut.write(str(new_solution) + '\n'*2)
    f_ut.write("**************************" + '\n'*2)
        
    for i, p in enumerate(new_solution):
        f_ut.write(f"{i}\n")
        for k, v in p.items():
            #print(f"\t{k} : {v}")
            f_ut.write(f"\t{k} : {v}\n")
        #print('')	
        f_ut.write('\n')


#Skicka in lösning för bedömning
submit_game_response = api.submit_game(api_key, map_name, new_solution)
print(submit_game_response, 1)
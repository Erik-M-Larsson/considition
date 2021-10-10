
from erikur_stower import Package, ErikurStower, CyberTruck
import numpy as np
#
# 
r = {'mapName': 'training1', 'vehicle': {'length': 200, 'width': 150, 'height': 136}, 'dimensions': [{'id': 0, 'width': 59, 'length': 58, 'height': 25, 'weightClass': 2, 'orderClass': 1, 'volume': 85550}, {'id': 1, 'width': 73, 'length': 46, 'height': 25, 'weightClass': 1, 'orderClass': 0, 'volume': 83950}, {'id': 2, 'width': 45, 'length': 36, 'height': 24, 'weightClass': 2, 'orderClass': 3, 'volume': 38880}, {'id': 3, 'width': 68, 'length': 47, 'height': 34, 'weightClass': 0, 'orderClass': 0, 'volume': 108664}, {'id': 4, 'width': 62, 'length': 60, 'height': 22, 'weightClass': 1, 'orderClass': 4, 'volume': 81840}, {'id': 5, 'width': 65, 'length': 47, 'height': 28, 'weightClass': 1, 'orderClass': 4, 'volume': 85540}, {'id': 6, 'width': 58, 'length': 54, 'height': 24, 'weightClass': 1, 'orderClass': 1, 'volume': 75168}, {'id': 7, 'width': 65, 'length': 43, 'height': 26, 'weightClass': 2, 'orderClass': 3, 'volume': 72670}, {'id': 8, 'width': 68, 'length': 64, 'height': 17, 'weightClass': 0, 'orderClass': 0, 'volume': 73984}, {'id': 9, 'width': 50, 'length': 35, 'height': 26, 'weightClass': 0, 'orderClass': 4, 'volume': 45500}, {'id': 10, 'width': 68, 'length': 35, 'height': 25, 'weightClass': 0, 'orderClass': 4, 'volume': 59500}, {'id': 11, 'width': 65, 'length': 47, 'height': 23, 'weightClass': 1, 'orderClass': 4, 'volume': 70265}, {'id': 12, 'width': 67, 'length': 59, 'height': 21, 'weightClass': 1, 'orderClass': 4, 'volume': 83013}, {'id': 13, 'width': 64, 'length': 44, 'height': 20, 'weightClass': 0, 'orderClass': 2, 'volume': 56320}, {'id': 14, 'width': 56, 'length': 52, 'height': 31, 'weightClass': 0, 'orderClass': 3, 'volume': 90272}, {'id': 15, 'width': 73, 'length': 37, 'height': 16, 'weightClass': 0, 'orderClass': 0, 'volume': 43216}, {'id': 16, 'width': 74, 'length': 63, 'height': 27, 'weightClass': 1, 'orderClass': 1, 'volume': 125874}, {'id': 17, 'width': 72, 'length': 47, 'height': 24, 'weightClass': 2, 'orderClass': 0, 'volume': 81216}, {'id': 18, 'width': 24, 'length': 33, 'height': 14, 'weightClass': 1, 'orderClass': 3, 'volume': 11088}, {'id': 19, 'width': 26, 'length': 41, 'height': 17, 'weightClass': 0, 'orderClass': 3, 'volume': 18122}, {'id': 20, 'width': 25, 'length': 41, 'height': 16, 'weightClass': 2, 'orderClass': 3, 'volume': 16400}, {'id': 21, 'width': 34, 'length': 41, 'height': 16, 'weightClass': 1, 'orderClass': 3, 'volume': 22304}, {'id': 22, 'width': 50, 'length': 27, 'height': 18, 'weightClass': 0, 'orderClass': 2, 'volume': 24300}, {'id': 23, 'width': 37, 'length': 20, 'height': 13, 'weightClass': 2, 'orderClass': 4, 'volume': 9620}, {'id': 24, 'width': 24, 'length': 40, 'height': 11, 'weightClass': 2, 'orderClass': 2, 'volume': 10560}, {'id': 25, 'width': 25, 'length': 42, 'height': 17, 'weightClass': 1, 'orderClass': 3, 'volume': 17850}, {'id': 26, 'width': 12, 'length': 39, 'height': 13, 'weightClass': 0, 'orderClass': 2, 'volume': 6084}, {'id': 27, 'width': 29, 'length': 29, 'height': 14, 'weightClass': 1, 'orderClass': 0, 'volume': 11774}, {'id': 28, 'width': 44, 'length': 31, 'height': 16, 'weightClass': 2, 'orderClass': 2, 'volume': 21824}, {'id': 29, 'width': 43, 'length': 31, 'height': 12, 'weightClass': 1, 'orderClass': 0, 'volume': 15996}, {'id': 30, 'width': 24, 'length': 38, 'height': 12, 'weightClass': 1, 'orderClass': 1, 'volume': 10944}, {'id': 31, 'width': 38, 'length': 26, 'height': 13, 'weightClass': 1, 'orderClass': 2, 'volume': 12844}, {'id': 32, 'width': 40, 'length': 32, 'height': 12, 'weightClass': 1, 'orderClass': 2, 'volume': 15360}, {'id': 33, 'width': 12, 'length': 40, 'height': 15, 'weightClass': 1, 'orderClass': 1, 'volume': 7200}, {'id': 34, 'width': 24, 'length': 37, 'height': 6, 'weightClass': 2, 'orderClass': 1, 'volume': 5328}, {'id': 35, 'width': 47, 'length': 25, 'height': 16, 'weightClass': 2, 'orderClass': 4, 'volume': 18800}, {'id': 36, 'width': 39, 'length': 24, 'height': 9, 'weightClass': 2, 'orderClass': 4, 'volume': 8424}, {'id': 37, 'width': 25, 'length': 34, 'height': 9, 'weightClass': 2, 'orderClass': 1, 'volume': 7650}, {'id': 38, 'width': 21, 'length': 41, 'height': 4, 'weightClass': 2, 'orderClass': 1, 'volume': 3444}, {'id': 39, 'width': 38, 'length': 22, 'height': 15, 'weightClass': 2, 'orderClass': 2, 'volume': 12540}, {'id': 40, 'width': 33, 'length': 39, 'height': 11, 'weightClass': 2, 'orderClass': 1, 'volume': 14157}, {'id': 41, 'width': 43, 'length': 26, 'height': 16, 'weightClass': 0, 'orderClass': 4, 'volume': 17888}, {'id': 42, 'width': 23, 'length': 40, 'height': 12, 'weightClass': 0, 'orderClass': 3, 'volume': 11040}, {'id': 43, 'width': 45, 'length': 31, 'height': 12, 'weightClass': 1, 'orderClass': 2, 'volume': 16740}, {'id': 44, 'width': 38, 'length': 20, 'height': 23, 'weightClass': 1, 'orderClass': 4, 'volume': 17480}, {'id': 45, 'width': 33, 'length': 42, 'height': 18, 'weightClass': 1, 'orderClass': 1, 'volume': 24948}, {'id': 46, 'width': 42, 'length': 23, 'height': 16, 'weightClass': 1, 'orderClass': 2, 'volume': 15456}, {'id': 47, 'width': 45, 'length': 24, 'height': 21, 'weightClass': 1, 'orderClass': 2, 'volume': 22680}, {'id': 48, 'width': 27, 'length': 41, 'height': 17, 'weightClass': 2, 'orderClass': 1, 'volume': 18819}, {'id': 49, 'width': 26, 'length': 39, 'height': 13, 'weightClass': 2, 'orderClass': 3, 'volume': 13182}, {'id': 50, 'width': 29, 'length': 36, 'height': 10, 'weightClass': 1, 'orderClass': 2, 'volume': 10440}, {'id': 51, 'width': 38, 'length': 25, 'height': 8, 'weightClass': 1, 'orderClass': 0, 'volume': 7600}, {'id': 52, 'width': 22, 'length': 38, 'height': 18, 'weightClass': 1, 'orderClass': 3, 'volume': 15048}, {'id': 53, 'width': 39, 'length': 27, 'height': 14, 'weightClass': 1, 'orderClass': 0, 'volume': 14742}, {'id': 54, 'width': 38, 'length': 27, 'height': 12, 'weightClass': 2, 'orderClass': 2, 'volume': 12312}, {'id': 55, 'width': 40, 'length': 28, 'height': 10, 'weightClass': 2, 'orderClass': 2, 'volume': 11200}, {'id': 56, 'width': 41, 'length': 23, 'height': 19, 'weightClass': 1, 'orderClass': 2, 'volume': 17917}, {'id': 57, 'width': 25, 'length': 42, 'height': 20, 'weightClass': 0, 'orderClass': 3, 'volume': 21000}, {'id': 58, 'width': 24, 'length': 48, 'height': 15, 'weightClass': 0, 'orderClass': 3, 'volume': 17280}, {'id': 59, 'width': 17, 'length': 37, 'height': 11, 'weightClass': 1, 'orderClass': 0, 'volume': 6919}]}

el = ErikurStower(r)

s = el.stow_truck()
#print("paket kvar", len(el._not_loaded_packages))
#print("occu_volume", el._truck.occu_volume)
#print(el._truck.occu_space[0:10, 0:10, 0:10])
#print(el._truck.occu_space[10:20, 0:10, 0:10])
#print(el._truck.occu_space[20:30, 0:10, 0:10])
#print(el._truck.occu_space[30:40, 0:10, 0:10])
#print(el._truck.occu_space[40:50, 0:10, 0:10])
print("***")
#print(el._truck.occu_space[0:10, 10:20, 0:10])
#print(el._truck.occu_space[0:10, 20:30, 0:10])
#print("\npaket x", el._truck.loaded_packages[-3].x18)
#print("paket y", el._truck.loaded_packages[-3].y18)
#print("paket z", el._truck.loaded_packages[-3].z18)
print(el._truck.loaded_packages[25].weight_class)
print(el._truck.loaded_packages[25].heavy)
#print('\n', s[40])



#p = el._truck.loaded_packages[0]
#print(el._truck.free_length)
#print(el._truck.occu_space[np.where(el._truck.occu_space == p.id)])
#print(el._truck.remomve_package(p)) 
#print(el._truck.occu_space[0:10, 0:10, 0:10])
#print(np.where(el._truck.occu_space == p.id))
#exit()
#p = Package({'id': 0, 'width': 59, 'length': 58, 'height': 25, 'weightClass': 2, 'orderClass': 1})
#print(p.order_class)
#print(p.dimensions)
#print(p.volume)

#cb = CyberTruck({'length': 200, 'width': 150, 'height': 136})
#cb.occu_space[25, 25, -3] = 1
#cb.occu_space[0:10, 0:1,  0:1] = 5
#cb.free_length

#print(cb.occu_space.shape, cb.occu_space.ndim, cb.occu_space.size)
#print(np.sum(cb.occu_space), cb.volume)
#print('1', cb.occu_volume)

#print('2', np.count_nonzero(cb.occu_space +1))
#print('3', np.nonzero(np.count_nonzero(cb.occu_space +1)))
#print('4', np.max(np.nonzero(np.count_nonzero(cb.occu_space +1))))
#print(cb.occu_space.shape[0] - np.max(np.nonzero(np.count_nonzero(cb.occu_space +1, axis=(1,2)))) - 1)
#print( cb.free_length)

#print(np.count_nonzero(cb.occu_space[0:100, 0:50, -2:-1] +1) == 0)
#print(cb.is_space_empty(0, 0, -2, 100, 50, -1))
#print(cb.occu_space[0:11, 0:3, 0:3])

#np.where()
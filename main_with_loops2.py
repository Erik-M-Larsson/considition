
import api
import json
import sys
sys.path.append("../considition")
from FredrikH2 import ErikurStower, Package, CyberTruck
#greedy =     GreedySolver(game_info=response)   
#solution = greedy.Solve()           



api_key = "3b9a5199-9d80-4178-b658-3b216564d0b4"   # TODO: Your api key here
# The different map names can be found on considition.com/rules
# TODO: You map choice here. Unless changed, the map "training1" will be selected.
map_name = "christmas"

yloop = 100 # Antal generationer
iloop = 40 # Eftersom loopen bryts när den får bättre score så kan man ha ett högt värde om man vill få ett värde på varej generation





def main():
	print("Starting game...")
	response = api.new_game(api_key, map_name)
	print(response["vehicle"])
	packing_list =  [Package(p) for p in response["dimensions"]]
	#shuffle(packing_list)
	packing_list = sorted(packing_list, key = lambda p: (p.volume), reverse = True)
	#packing_list = sorted(packing_list, key = lambda p: (p.volume), reverse = True)
	packing_list = sorted(packing_list, key = lambda p: (p.heavy), reverse = True)
	packing_list = sorted(packing_list, key = lambda p: (p.order_class), reverse = True)
	print (packing_list[0].dimensions)
	max_score = 0
	p_l = packing_list
	for j in range(yloop): 
		
		solution =[]
		submit_game_response = []
		#packing_lists =[]
		
		for i in range(iloop):
			print("yttre loop", j,  "inre loop", i)
			
			erikur =  ErikurStower(packing_list, response["vehicle"])
			try:
				so, p_l, svar = erikur.stow_truck()
				solution.append(so)
				#packing_lists.append(p_l)

				su = api.submit_game(api_key, map_name, so)
				print(su)
				submit_game_response.append(su)
				if su['score'] > max_score:
					max_score = su['score'] 
					print(su['score'])
					print(svar)
					packing_list = p_l # spara till nästa generation. Beroende på placering kan man få in en störnings
					break
			
			except:
				pass
		
		# packing_list = p_l #alternativ placering 
		print ("Max score: ", max_score)
		
	print("Loopen tog slut!")	   

	
	

	

	#avg_score = 0
	#for sus in submit_game_response:
		#avg_score += sus['score']
	
	#print(avg_score/80)


if __name__ == "__main__":
    main()


import api
import json
import sys
sys.path.append("../considition")
from FredrikH import ErikurStower
#greedy =     GreedySolver(game_info=response)   
#solution = greedy.Solve()           



api_key = "3b9a5199-9d80-4178-b658-3b216564d0b4"   # TODO: Your api key here
# The different map names can be found on considition.com/rules
# TODO: You map choice here. Unless changed, the map "training1" will be selected.
map_name = "training2"


latest = 3200

def main():
	print("Starting game...")
	response = api.new_game(api_key, map_name)
	solution =[]
	submit_game_response = []
	for i in range(40):
		
		erikur =  ErikurStower(response)
		try:
			so, svar = erikur.stow_truck()
			solution.append(so)

			su = api.submit_game(api_key, map_name, so)
			print(su)
			submit_game_response.append(su)
			if su['score'] > latest:
				print(su['score'])
				print(svar)
				break
		
		except:
			pass
		
		
	print("Loopen tog slut!")	   

	
	

	

	#avg_score = 0
	#for sus in submit_game_response:
		#avg_score += sus['score']
	
	#print(avg_score/80)


if __name__ == "__main__":
    main()

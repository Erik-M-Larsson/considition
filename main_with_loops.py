
import api
import json
import sys
sys.path.append("../considition")
from Training2_max import ErikurStower
#greedy =     GreedySolver(game_info=response)   
#solution = greedy.Solve()           



api_key = "3b9a5199-9d80-4178-b658-3b216564d0b4"   # TODO: Your api key here
# The different map names can be found on considition.com/rules
# TODO: You map choice here. Unless changed, the map "training1" will be selected.
map_name = "training2"



def main():
	print("Starting game...")
	response = api.new_game(api_key, map_name)
	solution =[]

	for i in range(50):
		
		erikur=  ErikurStower(response)
		try:
			solution.append(erikur.stow_truck())
		except:
			pass
	
		

	'''path_ut = "solution.txt"
	# Skriv utdata till fil # TODO metod
	with open(path_ut, 'w')	as f_ut:
		f_ut.write("solution = \n")
		f_ut.write(str(solution) + '\n'*2)
		f_ut.write("**************************" + '\n'*2)
			
		for p in solution:
			for k, v in p.items():
				#print(f"\t{k} : {v}")
				f_ut.write(f"\t{k} : {v}\n")
			#print('')	
			f_ut.write('\n')
	'''
	submit_game_response = []
	for s in solution:
		su = api.submit_game(api_key, map_name, s)
		print(su)
		submit_game_response.append(su)

	
	max_score = max([su['score'] for su in submit_game_response])
	print(max_score)
	print(su)

	

	#avg_score = 0
	#for sus in submit_game_response:
		#avg_score += sus['score']
	
	#print(avg_score/80)


if __name__ == "__main__":
    main()

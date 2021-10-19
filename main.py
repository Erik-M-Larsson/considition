from erikur_stower import ErikurStower
#from erikur_stower import ErikurStower
from greedy_solver import GreedySolver
import api
import json
from random import shuffle 
from math import sqrt, tau, sin, cos
import os

api_key = "3b9a5199-9d80-4178-b658-3b216564d0b4"   # TODO: Your api key here
# The different map names can be found on considition.com/rules
# TODO: You map choice here. Unless changed, the map "training1" will be selected.
map_name = "christmas"

def response_to_file(response, path): 
	"""Skriv response till fil"""
	with open(path, 'w') as f_in:
		#print("Response\n")
		f_in.write("response =\n")
		f_in.write(str(response) + '\n'*2)
		f_in.write("**************************" + '\n'*2)

		#print(f"mapName : {response['mapName']}")
		f_in.write(f"mapName : {response['mapName']}\n\n")
		#print(f"vehicle :")
		f_in.write(f"vehicle :\n")	
		
		for k, v in response["vehicle"].items():
			#print(f"\t{k} : {v}")
			f_in.write(f"\t{k} : {v}\n")
		
		#print(f"dimensions :")
		f_in.write(f"\ndimensions :\n")
		for d in response["dimensions"]:
			for k, v in d.items():
				#print(f"\t{k} : {v}")
				f_in.write(f"\t{k} : {v}\n")
			#print('')	
			f_in.write('\n')
	
def solution_to_file(solution, path):
	"""Skriv solution till fil"""
	with open(path, 'w')	as f_ut:
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

	
def packages_total_volume(response):
	"Beräknar nettovolym av paketen"
	paket_volym = []
	tot_paket_volym = 0
	for p in response["dimensions"]:
		v = p["width"] * p["length"] * p["height"]
		paket_volym.append(v)
		tot_paket_volym += v
	return tot_paket_volym




def main():
	print("Starting game...")
	
	# Filnamn
	#path_in = "files/indata_training1.txt"
	#path_ut = "files/utdata_training1_og.txt"
	path_in = f"load_faster_{map_name}_resp.txt"
	path_ut = f"load_faster_{map_name}_sol.txt"	

	path_in = r"C:/Users/ErikLarsson-AIU21GBG/Documents/GitHub/considition/files/" + path_in  #"files/indata_training2.txt"
	path_ut = r"C:/Users/ErikLarsson-AIU21GBG/Documents/GitHub/considition/files/" + path_ut #"files/utdata_training2_og.txt"
	
	response = api.new_game(api_key, map_name)  # Indata från api
	
	# Skriv ut response i en textfil
	#response_to_file(response, path_in)

	solution =[] # Lösningslista
	submit_game_response = [] # resultatlista


	#for i in range(6000): # TODO välj antal
	#	print("\n************\n Körning: ", i+1)

	# TODO välj solver här
	#greedy = GreedySolver(game_info=response)   
	erikur = ErikurStower(response)		
	
	try:
		#so = greedy.Solve()	
		#so = erikur.stow_truck()
		so = erikur.load_faster()

		solution.append(so)
		# Skriv data till fil
		solution_to_file(so, path_ut)

		#Skicka in lösning för bedömning
		su = api.submit_game(api_key, map_name, so)
		print(su)

		submit_game_response.append(su)
	except ValueError as err:
		print(err)
	except:
		print("Något gick galet!")



	print("\n******\n")		
	
	if submit_game_response:
		#nr_valid = sum([su['valid'] for su in submit_game_response])
		#print(f"Antal godkända lönsningar {nr_valid}/{i+1}")

		max_score = max([su['score'] for su in submit_game_response])
		print("Max poäng", max_score)
	else:
		print("submit_game_response är tom")
	print("")





if __name__ == "__main__":
    main()




import api

api_key = "3b9a5199-9d80-4178-b658-3b216564d0b4"   
map_name = "training2"


# Filnamn
path = "prol_tr2_s.txt"	
path = r"C:/Users/ErikLarsson-AIU21GBG/Documents/GitHub/considition/files/" + path


# TODO fixa inläsning från fil. Läs in solution
with open(path, 'r') as f:
    f.read
		'''f_ut.write("solution = \n")
		f_ut.write(str(solution) + '\n'*2)
		f_ut.write("**************************" + '\n'*2)
			
		for i, p in enumerate(solution):
			f_ut.write(f"{i}\n")
			for k, v in p.items():
				#print(f"\t{k} : {v}")
				f_ut.write(f"\t{k} : {v}\n")
			#print('')	
			f_ut.write('\n')'''

#Skicka in lösning för bedömning
submit_game_response = api.submit_game(api_key, map_name, solution)
print(submit_game_response, 1)
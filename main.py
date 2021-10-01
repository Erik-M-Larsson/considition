from greedy_solver import GreedySolver
import api
import json

api_key = "3b9a5199-9d80-4178-b658-3b216564d0b4"   # TODO: Your api key here
# The different map names can be found on considition.com/rules
# TODO: You map choice here. Unless changed, the map "training1" will be selected.
map_name = "training1"


def main():
	print("Starting game...")
	response = api.new_game(api_key, map_name) 
	greedy = GreedySolver(game_info=response)   # <----- Dessa två rader räcker för att testa
	solution = greedy.Solve()					# <-----
	submit_game_response = api.submit_game(api_key, map_name, solution)
	print(submit_game_response)
if __name__ == "__main__":
    main()

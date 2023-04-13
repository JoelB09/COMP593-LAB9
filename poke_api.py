import requests

def fetch_pokemon_info(pokemon_name_or_id):
    
    pokemon_name_or_id = str(pokemon_name_or_id).strip().lower()
    
    print(f"Fetching information for {pokemon_name_or_id} from the PokéAPI...")
    
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name_or_id}")
    
    if response.status_code == 200:
        pokemon_info = response.json()
        
        
        statistics = {}
        for stat in pokemon_info['stats']:
            statistics_name = statistics['stats']['name']
            statistics_value = statistics['base_stat']
            statistics[stat_name] = statistics_value
        pokemon_info['statistics'] = statistics
        
        return pokemon_info
    
    else:
        print(f"Error: Unable to fetch information for {pokemon_name_or_id}.")
        return None


   
     
    
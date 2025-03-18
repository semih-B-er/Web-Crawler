import requests
def get_pokemon_info(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/ {pokemon_name.lower()} "
    response = requests.get(url)


def get_pokemon_info(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/ {pokemon_name.lower()} "
    response = requests.get(url)


    if response.status_code == 200:
        pokemon_data = response.json()
        pokemon_info = {
            "name": pokemon_data["name"],
            "height": pokemon_data["height"],
            "weight": pokemon_data["weight"],
            "abilities": [ability["ability"]["name"] for ability in pokemon_data["abilities"]],
            "types": [type_data["type"]["name"] for type_data in pokemon_data["types"]]
        }
        return pokemon_info
    else:
        return None


pokemon_name = input ( "Pokemon adını girin: " )
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print ( f"Ad: {pokemon_info[ 'ad' ]} " )
    print ( f"Boy: {pokemon_info[ 'yükseklik' ]} " )
    print ( f"Kilo: {pokemon_info[ 'ağırlık' ]} " )
    print ( f"Yetenekler: { ', ' .join(pokemon_info[ 'yetenekler' ])} " )
    print ( f"Türler: { ', ' .join(pokemon_info[ 'türler' ])} " )
else :
    print ( "Pokémon bulunamadı!" )
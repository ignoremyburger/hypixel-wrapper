import urllib.request
import json

class HypixelWrapper:
    username = ""
    inside_key = ""
    #Initialize by providing In-game name and API Key from Hypixel
    def __init__(self, key, ign):
        #Assigning
        global inside_key
        global username
        self.ign = ign
        self.key = key
        inside_key = key
        username = ign
    #Contact the Mojang API to get the UUID of the user.
    def get_uuid(self):
        global uuid
        global username
        with urllib.request.urlopen(f"https://api.mojang.com/users/profiles/minecraft/{username}") as res:
            uuid = json.loads(res.read().decode())['id']
        return uuid
    def get_player_data(self):
        global inside_key
        uuid = self.get_uuid()
        #Contact the Hypixel API with the privided key
        with urllib.request.urlopen(f"https://api.hypixel.net/player?key={inside_key}&uuid={uuid}") as res:
            player_data = json.loads(res.read().decode())['player']
        return player_data
    def bedwars_stat(self):
        data = self.get_player_data()['achievements']
        json_string = {
            "level": data['bedwars_level'],
            "beds": data['bedwars_beds'],
            "wins": data['bedwars_wins']
        }
        return json_string


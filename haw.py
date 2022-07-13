from urllib.request import Request, urlopen
import json
import sys
from datetime import datetime as dt

class HypixelWrapper:
    uuid = ""
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
        try:
            global uuid
            global username
            with urlopen(f"https://api.mojang.com/users/profiles/minecraft/{username}") as res:
                uuid = json.loads(res.read().decode())['id']
        except Exception as e:
            sys.exit("Error occured while fetching UUID, did you put in the correct username?")
        return uuid
    def get_player_data(self):
        try:
            global inside_key
            uuid = self.get_uuid()
            #Contact the Hypixel API with the privided key
            with urlopen(f"https://api.hypixel.net/player?key={inside_key}&uuid={uuid}") as res:
                player_data = json.loads(res.read().decode())['player']
        except Exception as e:
            sys.exit("Error occured while fetching player data, did you put in the correct username?")
        return player_data
    def general_stat(self):
        rank = ""
        level = 0
        data = self.get_player_data()
        #Preprocessing
        try:
            rank = data['monthlyPackageRank']
            if rank == "VIP_PLUS":
                rank = "VIP+"
            elif rank == "MVP_PLUS":
                rank = "MVP+"
            elif rank == "SUPERSTAR":
                rank = "MVP++"
        except KeyError:
            rank = "Unranked"
        for i in data:
            try:
                if "levelingReward" in i:
                    level = level + 1
                else: 
                    continue
            except Exception as e:
                break
        
        json_string = {
            "name": data['displayname'],
            "rank": rank,
            "level": level,
            "all_wins": data['achievements']['general_wins']
        }
        return json_string
    def bedwars_stat(self):
        try:
            data = self.get_player_data()['achievements']
            detailed = self.get_player_data()['stats']['Bedwars']
            json_string = {
                "status": "success",
                "game_mode": "Bedwars",
                "level": data['bedwars_level'],
                "total_games_played": detailed['games_played_bedwars_1'],
                "details": [
                    {
                        "mode": "solo",
                        "winstreak": detailed['eight_one_winstreak'],
                        "losses": detailed['eight_one_losses_bedwars'],
                        #Hypixel doesn't count solo wins in the API
                        "wins": detailed['eight_one_games_played_bedwars'] - detailed['eight_one_losses_bedwars'],
                        "beds_broken": detailed['eight_one_beds_broken_bedwars'],
                        "total_kills": detailed['eight_one_kills_bedwars']
                    },
                    {
                        "mode": "doubles",
                        "winstreak": detailed['eight_two_winstreak'],
                        "losses": detailed['eight_two_losses_bedwars'],
                        "wins": detailed['eight_two_wins_bedwars'],
                        "beds_broken": detailed['eight_two_beds_broken_bedwars'],
                        "total_kills": detailed['eight_two_kills_bedwars']
                    },
                    {
                        "mode": "3v3v3v3",
                        "winstreak": detailed['four_three_winstreak'],
                        "losses": detailed['four_three_losses_bedwars'],
                        "wins": detailed['four_three_wins_bedwars'],
                        "beds_broken": detailed['four_three_beds_broken_bedwars'],
                        "total_kills": detailed['four_three_kills_bedwars']
                    },
                    {
                        "mode": "4v4v4v4",
                        "winstreak": detailed['four_four_winstreak'],
                        "losses": detailed['four_four_losses_bedwars'],
                        "wins": detailed['four_four_wins_bedwars'],
                        "beds_broken": detailed['four_four_beds_broken_bedwars'],
                        "total_kills": detailed['four_four_kills_bedwars']
                    }
                ],
                "beds_destroyed": data['bedwars_beds'],
                "wins": data['bedwars_wins']
            }
        except Exception as e:
            json_string = {
                "status": "error",
                "detail": str(e)
            }
        return json_string
    def skywars_stat(self):
        try:
            data = self.get_player_data()['achievements']
            json_string = {
                "status": "success",
                "game_mode": "Skywars",
                "level": data['skywars_you_re_a_star'],
                "cages_owned": data['skywars_cages'],
                "skywars_wins_solo": data['skywars_wins_solo'],
                "skywars_kills_solo": data['skywars_kills_solo'],
                "skywars_kits_solo": data['skywars_kits_solo'],
                "skywars_wins_team": data['skywars_wins_team'],
                "skywars_kills_team": data['skywars_kills_team'],
                "skywars_kits_team": data['skywars_kits_team']
            }
            return json_string
        except Exception as e:
            json_string = {
                "status": "error",
                "detail": str(e)
            }
    def duels_stat(self):
        try:
            data = self.get_player_data()['achievements']
            detailed = self.get_player_data()['stats']['Duels']
            json_string = {
                "status": "success",
                "game_mode": "Duels",
                "total_games_played": detailed['games_played_duels'],
                "highest_winstreak": data['duels_duels_win_streak'],
                "wins": detailed['wins'],
                "losses": detailed['losses'],
                "current_winstreak": detailed['current_winstreak'],
                "total_kills": detailed['kills'],
                "coins": detailed['coins']
            }
        except Exception as e:
            json_string = {
                "status": "error",
                "detail": str(e)
            }
        return json_string
    def skyblock_stat(self):
        complete = 0
        active = 0
        global inside_key
        uuid = self.get_uuid()
        with urlopen(f"https://api.hypixel.net/skyblock/profile?key={inside_key}&profile={uuid}") as res:
            data = json.loads(res.read().decode())['profile']['members'][uuid]
        #Convert time
        converted_time = dt.utcfromtimestamp(int(data['first_join']) / 1000).strftime('%Y-%m-%d %H:%M:%S')
        #Counting objectives completed and still active
        for i in range(0, len(data['objectives']) - 1):
            try:
                if data['objectives'][i]['status'] == "COMPLETE":
                    complete = complete + 1
                elif data['objectives'][i]['status'] == "ACTIVE":
                    active = active + 1
            except KeyError:
                break
        json_string = {
            "first_join": converted_time,
            "deaths": data['stats']['deaths'],
            "death_by_void": data['stats']['deaths_void'],
            "kills": data['stats']['kills'],
            "kills_cow": data['stats']['kills_cow'],
            "deaths_unburried_zombie": data['stats']['deaths_unburried_zombie'],
            "objectives_completed": complete,
            "objectives_active": active
        }
        return json_string
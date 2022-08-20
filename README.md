# Hypixel API Wrapper (HAW)
HAW is writen to simplify the process of gathering data from Hypixel

<h2>Installation</h2>
<b>Step 1</b>: Clone the repository. <b>[<i> git clone https://github.com/buibaohoang06/hypixel-wrapper </i>]</b><br><br>
<b>Step 2</b>: Move <b>haw.py</b> to your project folder.<br><br>
<b>Step 3</b>: Go on to Hypixel to get your API Key by using command <b>/api</b><br><br>
<b>Step 4: Import HypixelWrapper into your code and initialize it.</b><br><br>

```python
from haw import HypixelWrapper

haw = HypixelWrapper(key="your Hypixel API Key", ign="your in-game name")
```

<h2>Modules</h2>
<h3>General Information | general_stat()</h3>
The General Information module returns a JSON string that contains the player's display name, rank, Hypixel level and total wins.
<br><br>
Example: 

```python
from haw import HypixelWrapper

hw = HypixelWrapper("My API Key", "_Heartbr0ken_")
general_stat = hw.general_stat()
print(general_stat)
```
returns

```
{'name': '_Heartbr0ken_', 'rank': 'MVP++', 'level': 96, 'all_wins': 1136}
```

<h3>Bedwars | bedwars_stat()</h3>
The Bedwars module returns a JSON string that contains winstreak, losses, wins, beds_broken, total_kills.
<br><br>
Example: 

```python
from haw import HypixelWrapper

hw = HypixelWrapper("My API Key", "_Heartbr0ken_")
bw_stat = hw.bedwars_stat()
print(bw_stat)
```

returns

```
{'status': 'success', 'game_mode': 'Bedwars', 'level': 145, 'total_games_played': 4100, 'details': [{'mode': 'solo', 'winstreak': 0, 'loses': 1160, 'wins': 176, 'beds_broken': 1509, 'total_kills': 2143}, {'mode': 'doubles', 'winstreak': 0, 'loses': 619, 'wins': 33, 'beds_broken': 254, 'total_kills': 1222}, {'mode': '3v3v3v3', 'winstreak': 0, 'loses': 232, 'wins': 27, 'beds_broken': 53, 'total_kills': 631}, {'mode': '4v4v4v4', 'winstreak': 0, 'loses': 1291, 'wins': 218, 'beds_broken': 375, 'total_kills': 4003}], 'beds_destroyed': 2218, 'wins': 486}
```

<h3>Skywars | skywars_stat()</h3>
The Skywars module returns a JSON string that contains the player's skywars level, number of cages owned, wins (solo and doubles), kits available (solo and doubles) and kills (solo and doubles)
<br><br>
Example: 

```python
from haw import HypixelWrapper

hw = HypixelWrapper("My API Key", "_Heartbr0ken_")
sw_stat = hw.skywars_stat()
print(sw_stat)
```

returns

```
{'status': 'success', 'game_mode': 'Skywars', 'level': 9, 'cages_owned': 12, 'skywars_wins_solo': 135, 'skywars_kills_solo': 2493, 'skywars_kits_solo': 37, 'skywars_wins_team': 38, 'skywars_kills_team': 435, 'skywars_kits_team': 37}
```


<h3>Duels | duels_stat()</h3>
The Duels module returns a JSON string that contains the player's total games played, highest winstreak, wins, losses, current winstreak, total kills and coins.

Example: 

```python
from haw import HypixelWrapper

hw = HypixelWrapper("My API Key", "_Heartbr0ken_")
duels_stat = hw.duels_stat()
print(duels_stat)
```

returns

```
{'status': 'success', 'game_mode': 'Duels', 'total_games_played': 2616, 'highest_winstreak': 10, 'wins': 834, 'loses': 1213, 'current_winstreak': 1, 'total_kills': 708, 'coins': 32242}
```

<h2>Further remarks</h2>
This project is still being developed, more modules will be added in the future. Feel free to contribute.

<h3>Contact Info</h3>
<ul>
<li>Discord: affogato#2605</li>
<li>E-Mail: heartbroken.89@protonmail.ch</li>
</ul>

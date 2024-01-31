#! /usr/bin/env python3


def game_dict():
    return {
        "home": {
            "team_name": "Cleveland Cavaliers",
            "colors": ["Wine", "Gold"],
            "players": [
                {
                    "name": "Jarrett Allen",
                    "number": 31,
                    "position": "Center",
                    "points_per_game": 16.1,
                    "rebounds_per_game": 10.8,
                    "assists_per_game": 1.6,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.3,
                    "career_points": 3945,
                    "age": 24,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Darius Garland",
                    "number": 10,
                    "position": "Point Guard",
                    "points_per_game": 21.7,
                    "rebounds_per_game": 3.3,
                    "assists_per_game": 8.6,
                    "steals_per_game": 1.3,
                    "blocks_per_game": 0.1,
                    "career_points": 3142,
                    "age": 22,
                    "height_inches": 73,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Evan Mobley",
                    "number": 4,
                    "position": "Center",
                    "points_per_game": 15.0,
                    "rebounds_per_game": 8.3,
                    "assists_per_game": 2.5,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.7,
                    "career_points": 1034,
                    "age": 21,
                    "height_inches": 83,
                    "shoe_brand": "Adidas",
                },
                {
                    "name": "Kevin Love",
                    "number": 0,
                    "position": "Power Forward",
                    "points_per_game": 13.6,
                    "rebounds_per_game": 7.2,
                    "assists_per_game": 2.2,
                    "steals_per_game": 0.4,
                    "blocks_per_game": 0.2,
                    "career_points": 14305,
                    "age": 34,
                    "height_inches": 80,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Isaac Okoro",
                    "number": 35,
                    "position": "Small Forward",
                    "points_per_game": 8.8,
                    "rebounds_per_game": 3.0,
                    "assists_per_game": 1.8,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 0.3,
                    "career_points": 1234,
                    "age": 21,
                    "height_inches": 77,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Ricky Rubio",
                    "number": 99,
                    "position": "Point Guard",
                    "points_per_game": 13.1,
                    "rebounds_per_game": 4.1,
                    "assists_per_game": 6.6,
                    "steals_per_game": 1.4,
                    "blocks_per_game": 0.2,
                    "career_points": 7399,
                    "age": 31,
                    "height_inches": 74,
                    "shoe_brand": "Adidas",
                },
            ],
        },
            
        "away": {
            "team_name": "Washington Wizards",
            "colors": ["Red", "White", "Navy Blue"],
            "players": [   
                {
                    "name": "Bradley Beal",
                    "number": 3,
                    "position": "Shooting Guard",
                    "points_per_game": 23.2,
                    "rebounds_per_game": 4.7,
                    "assists_per_game": 6.6,
                    "steals_per_game": 0.9,
                    "blocks_per_game": 0.4,
                    "career_points": 14231,
                    "age": 29,
                    "height_inches": 76,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kyle Kuzma",
                    "number": 33,
                    "position": "Power Forward",
                    "points_per_game": 17.1,
                    "rebounds_per_game": 8.5,
                    "assists_per_game": 3.5,
                    "steals_per_game": 0.6,
                    "blocks_per_game": 0.9,
                    "career_points": 5336,
                    "age": 27,
                    "height_inches": 81,
                    "shoe_brand": "Puma",
                },
                {
                    "name": "Kentavious Caldwell-Pope",
                    "number": 1,
                    "position": "Shooting Guard",
                    "points_per_game": 13.2,
                    "rebounds_per_game": 3.4,
                    "assists_per_game": 1.9,
                    "steals_per_game": 1.1,
                    "blocks_per_game": 0.3,
                    "career_points": 7911,
                    "age": 29,
                    "height_inches": 77,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Davis Bertans",
                    "number": 42,
                    "position": "Power Forward",
                    "points_per_game": 5.6,
                    "rebounds_per_game": 2.1,
                    "assists_per_game": 0.6,
                    "steals_per_game": 0.3,
                    "blocks_per_game": 0.3,
                    "career_points": 3165,
                    "age": 29,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kristaps Porzingis",
                    "number": 6,
                    "position": "Power Forward",
                    "points_per_game": 22.1,
                    "rebounds_per_game": 8.8,
                    "assists_per_game": 2.9,
                    "steals_per_game": 0.7,
                    "blocks_per_game": 1.5,
                    "career_points": 6371,
                    "age": 27,
                    "height_inches": 87,
                    "shoe_brand": "Adidas",
                },
                {
                    "name": "Rui Hachimura",
                    "number": 8,
                    "position": "Power Forward",
                    "points_per_game": 11.3,
                    "rebounds_per_game": 3.8,
                    "assists_per_game": 1.1,
                    "steals_per_game": 0.5,
                    "blocks_per_game": 0.2,
                    "career_points": 1913,
                    "age": 24,
                    "height_inches": 80,
                    "shoe_brand": "Jordan",
                },
            ]
        }
    }

# num_points_per_game()
# Build a function, num_points_per_game() that takes in an argument of a player's name and returns the number of points per game for that player.

def num_points_per_game(player_name):
    for game in game_dict().values():
        for player in game["players"]:
            if player["name"] == player_name:
                print(player['points_per_game'])

num_points_per_game("Jarrett Allen")

# player_age()
# Build a function, player_age(), that takes in an argument of a player's name and returns that player's age.

def player_age(player_name):
    for game in game_dict().values():
        for player in game["players"]:
            if player["name"] == player_name:
                print(player['age'])

player_age("Jarrett Allen")

# team_colors()
# Build a function, team_colors(), that takes in an argument of the team name and returns a list of that team's colors.

def team_colors(team_name):
    for game in game_dict().values():
        if game["team_name"] == team_name:
            return game["colors"]
    return "Team not found"

print(team_colors("Cleveland Cavaliers"))
# team_names()
# Build a function, team_names(), that operates on the dictionary to return a list of the team names.

def team_names():
    teams = []
    for game in game_dict().values():
        teams.append(game["team_name"])
    print(teams)

team_names()

# player_numbers()
# Build a function, player_numbers(), that takes in an argument of a team name and returns a list of the jersey numbers for that team.

def player_numbers(team_name):
    numbers = []
    for game in game_dict().values():
        if game["team_name"] == team_name:
            for player in game["players"]:
                numbers.append(player["number"])
    print(numbers)


player_numbers("Cleveland Cavaliers")


# player_stats()
# Build a function, player_stats(), that takes in an argument of a player's name and returns a dictionary of that player's stats.

def player_stats(player_name):
    for game in game_dict().values():
        for player in game["players"]:
            if player["name"] == player_name:
                return player
    return "Player not found"

print(player_stats("Jarrett Allen"))

# CHALLENGE: average_rebounds_by_shoe_brand()
# Objective: Calculate the average number of rebounds for each shoe brand.
# Approach:
# Create a dictionary to track shoe brands and rebounds.
# Iterate over players, updating the dictionary.
# Calculate averages for each brand.
# Print the results.

def average_rebounds_by_shoe_brand():
    shoe_brand_rebounds = {}
    shoe_brand_players = {}
    for game in game_dict().values():
        for player in game["players"]:
            if player["shoe_brand"] not in shoe_brand_rebounds:
                shoe_brand_rebounds[player["shoe_brand"]] = player["rebounds_per_game"]
                shoe_brand_players[player["shoe_brand"]] = 1
            else:
                shoe_brand_rebounds[player["shoe_brand"]] += player["rebounds_per_game"]
                shoe_brand_players[player["shoe_brand"]] += 1
    for brand, rebounds in shoe_brand_rebounds.items():
        average_rebounds = rebounds / shoe_brand_players[brand]
        print(f"{brand}: {average_rebounds}")

average_rebounds_by_shoe_brand()

# Additional Challenges
# Find the player with the most career points.
# Check for common jersey numbers across teams.
# Identify the player with the longest name.

def most_career_points():
    most_points = 0
    player_name = ""
    for game in game_dict().values():
        for player in game["players"]:
            if player["career_points"] > most_points:
                most_points = player["career_points"]
                player_name = player["name"]
    print(f"{player_name} has the most career points with {most_points}.")

most_career_points()

def common_jersey_numbers():
    jersey_numbers = []
    for game in game_dict().values():
        for player in game["players"]:
            jersey_numbers.append(player["number"])
    common_numbers = [number for number in set(jersey_numbers) if jersey_numbers.count(number) > 1]
    print(common_numbers)

common_jersey_numbers()

def longest_name():
    longest_name = ""
    for game in game_dict().values():
        for player in game["players"]:
            if len(player["name"]) > len(longest_name):
                longest_name = player["name"]
    print(longest_name)

longest_name()
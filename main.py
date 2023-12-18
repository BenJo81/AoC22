with open("input.txt") as f:
    games = f.read().split('\n')

grand_total = 0
game_dict = {}
red_cubes = 12
green_cubes = 13
blue_cubes = 14
game_over = False

for game in games:
    which_game = game.split(":")
    game_dict[which_game[0]] = which_game[1]

for x in range(len(game_dict)):
    game_over = False
    game_results = game_dict[f"Game {x+1}"].split(";")
    for game in game_results:
        colors = game.split(",")
        for color in colors:
            if "blue" in color and int(color[1:3]) > blue_cubes:
                game_over = True
            elif "green" in color and int(color[1:3]) > green_cubes:
                game_over = True
            elif "red" in color and int(color[1:3]) > red_cubes:
                game_over = True
    print(game_over)
    if not game_over:
        grand_total += x+1

print(grand_total)

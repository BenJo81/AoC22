with open("input.txt") as f:
    games = f.read().split('\n')

grand_total = 0
game_dict = {}

for game in games:
    which_game = game.split(":")
    game_dict[which_game[0]] = which_game[1]

for x in range(len(game_dict)):
    largest_blue = 0
    largest_red = 0
    largest_green = 0
    game_results = game_dict[f"Game {x+1}"].split(";")
    for game in game_results:
        colors = game.split(",")
        for color in colors:
            if "blue" in color and int(color[1:3]) > largest_blue:
                largest_blue = int(color[1:3])
            elif "green" in color and int(color[1:3]) > largest_green:
                largest_green = int(color[1:3])
            elif "red" in color and int(color[1:3]) > largest_red:
                largest_red = int(color[1:3])
        print(largest_green, largest_red, largest_blue)
    semi_total = (largest_red * largest_green * largest_blue)
    print(semi_total)
    grand_total += semi_total

print(grand_total)

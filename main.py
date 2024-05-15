from emoji import emojize

level = 0
emojis = [emojize(":person_running:"), emojize(":pizza:" + ":soft_ice_cream:" + ":hamburger:"), emojize(":fire:" + ":boy:" + ":water_wave:" + ":girl:"), emojize(":motorcycle:"),emojize(":penguin:" + ":right_arrow:"), emojize(":yellow_circle:" + ":red_square:" + ":yellow_circle:"), emojize(":pick:" + ":place_of_worship:" + ":hut:" + ":farmer:"), emojize(":prohibited:" + ":video_game:"), emojize(":duck:" + ":1st_place_medal:"), emojize(":snake:" + ":red_apple:")]
games = ["run", "papa", "fireboy and watergirl", "moto x3m", "learn to fly", "worlds hardest game", "pre-civilization bronze age", "there is no game", "duck life", "snake"]

while level != 10:
    print("Guess the Coolmath Game: \n" + emojis[level])
    guess = input(">> ")
    if guess.lower() == games[level]:
        level += 1
    else:
        level = 0
print("You win!")
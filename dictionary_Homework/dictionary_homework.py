def dicioGuesser(keyname, valuename):
    for key in songParameter:
        if keyname == key and valuename == prefSong[key]:
            print("You guess it write :), your current score is\n")
            return True
    print("You guess it wrong, try again later ! Your score was\n")
    return False


# dictionary
prefSong = {"artist": "Metallica", "genre": "Heavy Metal", "preferedAlbum": "Master of Puppets",
            "musicsInAlbum": "8", "preferedMusic": "Master of Puppets", "prefMusicTime": "8.58"}
# list of keys
songParameter = ["artist", "genre", "preferedAlbum",
                 "musicsInAlbum", "preferedMusic", "prefMusicTime"]
# code to guess the value of the key i want
while (True):
    print("Welcome to DICIO GUESSER! Please insert the key and try to guess its value\nThe key list are in the following:")
    print(songParameter)
    keyName = input("What key do you want to guess?\n")
    valueName = input("Make your guess, whats the key value?\n")
    guessResult = dicioGuesser(keyName, valueName)
    # to leave the loop
    if guessResult is False:
        break


for i in songParameter:
    print(prefSong[i])

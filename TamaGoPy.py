

# That python file is the main launcher
# The game is compatible with 2 languages
# There are 2 python files (1 per language)

# Main Input loop
loop = True
choice = str()

print("***************")
print("Welcome")
print("Tamagopy Alpha 1.4")
print("***************")

# Language select
while loop:

    # Available languages are displayed in a list
    print("Please select the Game language")
    print("--------------------------------")
    print("Français, France : fr_fr")
    print("English, US : en_us")
    print("*********************************")
    print("Please Type the language code")
    print("Example : Type en_us if to play English US")
    print("-------")
    choice = input("Language code : ")

    if choice.lower() == "en_us":
        print("Launching the Game With En-us language...")
        
        # Importing en_us Game core
        from en_us import Game

    elif choice.lower() == "fr_fr":
        print("Launching the Game with Fr-Fr language...")

        # Import fr_fr game core
        from fr_fr import Game


    Game1 = Game()
    Game1.run()

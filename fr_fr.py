import time
import random
import pickle

# This is the code for the french FR version of the game


# The Player Class
class player():
        def __init__(self):
                self.name = ""

# The Main class, Tamagopy
class Tamagopy():
        def __init__(self, parent):

                # This class needs the Game class
                self.parent = parent

                # The name inputed of the Tamagopy
                self.name = ""

                # The stats data
                self.hunger = 0
                self.weakness = 0
                self.pee = 0
                self.poo = 0
                self.affection = 10
                self.dirtiness = 0

                # gameover needs to keep in mind its warns
                self.wash_warn = False
                self.hunger_warn = False
                self.pee_warn = False
                self.poo_warn = False
                self.sleep_warn = False
                self.affection_warn = False

        # First Method, eat
        def eat(self):

                # Checks if Tamagopy can eat
                if self.hunger == 0:
                        print(self.name, "ne peut pas manger, il n'a pas faim.")
                        self.check_all()


                else:
                        print(self.name, "est en train de manger...")

                        # Eating time
                        time.sleep(7)

                        # Primary effect
                        self.hunger -= 8
                        if self.hunger < 0:
                                self.hunger = 0

                        # Successfully
                        print(self.name, "a fini de manger.")

                        # Secondary effects
                        self.pee += 3
                        self.poo += 4
                        self.dirtiness += 4
                        self.weakness += 1
                        self.check_all()

        # Second Method, sleeping
        def sleep(self):

                # We need to check if Tamagopy can sleep
                if self.weakness > 10:
                        self.weakness = 10
                        print(self.name, "ne peut pas dormir, il n'est pas fatigué")
                        self.check_all()
        
                
                else:
                        print(self.name, "est en train de dormir...")
                        
                        # Sleep time
                        time.sleep(60)

                        # Successfully
                        print(self.name, "a fini de dormir.")

                        # Primary effect
                        self.weakness = 0

                        # Secondary effects
                        self.pee += 3
                        self.hunger += 4
                        self.poo += 4
                        self.dirtiness += 4
	
                        # Don't forget to check all
                        self.check_all()

        # Third method, going to WC
        def wc(self):

                # We need to check if Tamagopy can make poo or pee
                if self.poo < 2 or self.pee < 1:
        
                        print(self.name, "n'a pas envie d'aller aux toillettes")         
		
                else:

                        print(self.name, "va aux toillettes")

                        # WC time
                        time.sleep(7)

                        # Successfully
                        print(self.name, "sort des toilettes")

                        # Primary effects
                        self.pee = 0
                        self.poo = 0

                        # Secondary effects
                        self.dirtiness += 1
                        self.hunger += 2

                        self.check_all()

        # This method, play, to keep attachment
        def play(self):


                # Successfully
                print(self.name, "est en train de jouer")
                
                # playing time
                time.sleep(5)

                # Primary effect
                self.affection += 2

                # We can't go over 100% affection
                if self.affection > 10:
                        self.affection = 10

                # Secondary effects
                self.dirtiness += 3
                self.hunger += 3
                self.weakness += 4

                # Don't forget to check
                self.check_all()

        # Methods that simply displays statistics
        def statistics(self):

                # The name of the Tamagopy
                print("Nom :", self.name)

                # Its dirtiness level
                print("Niveau de Saleté :", self.dirtiness, "/10")

                # His weakness (will be weak if he doesn't slept)
                print("Niveau de fatigue :", self.weakness, "/10")

                # Affection level
                print("Niveau d'affection :", self.affection, "/10")

                # Pee
                print("Vessie :", self.pee, "/10")

                # Poo
                print("Colon :", self.poo, "/10")

                # Hunger level
                print("Niveau de faim :", self.hunger, "/10")


        # Wash method, to keep clean and healthy
        def wash(self):
                print(self.name, "se lave")
                
                # Wash time
                time.sleep(10)

                # Successfully
                print(self.name, "est tout propre maintenant")

                # Primary effect
                self.dirtiness = 0

                # Secondary effects
                self.affection += 3
                self.hunger += 1

                # Don't forget to check
                self.check_all()

        # The check all method, very important.
        # We need it to check if Tamagopy is healthy
        # This is important for GameOver
        def check_all(self):

                # Checks critical dirtiness 
                if self.dirtiness >= 10:

                        # The Game will end if True
                        if self.wash_warn == True:
                                self.game_over(self.name + " est mort du thétanos au bout de deux jours. \n Laissons son âme en paix")

                        # A warning will be displayed
                        # If the player doesn't do anything to fix it
                        # The warn well become Game Over
                        # Else the warn will erase
                        elif self.wash_warn == False:
                                print(self.name, "est très sale ! Vous feriez mieux de le laver !")
                                self.wash_warn = True

                # Same thing with affection
                if self.affection <= 0:

                        # ...
                        if self.affection_warn == True:
                                self.game_over(self.name + " a fugué, et vous l'avez retrouvé son cadavre en décomposition dans une ruelle la semaine suivante. \n Devasté par la tristess et la douleur d'avoir perdu un être si cher, vous vous êtes laissé mourir.")
                                

                        # I do not need to comment everything...
                        elif self.affection_warn == False:
                                print(self.name, "est en manque d'affection. Vous devriez vous en occuper.")
                                self.affection_warn = True


                # Okay I'm done
                if self.weakness >= 10:

                        if self.sleep_warn == True:
                                self.game_over("Le coeur de " + self.name + " a cessé de battre et il est mort sur son lit d'hôpital.")
                                

                        elif self.sleep_warn == False:
                                print("Je crois que vous devriez mettre,", self.name, "au lit, Il est très fatigué.")
                                self.sleep_warn = True


                if self.pee >= 10:

                        if self.pee_warn == True:
                                self.game_over(self.name + " Est mort d'une infection après que sa vessie ait explosée.")
                        

                        elif self.pee_warn == False:
                                print(self.name, "devrait aller aux toilettes")
                                self.pee_warn = True


                if self.poo >= 10:

                        if self.poo_warn == True:
                                self.game_over(self.name + " est mort d'une occlusion intestinale. \nFranchement le chirurgien aurait pu faire quelque chose ! \nIl n'avait qu'à avoir une bonne secrétaire.")
	

                        elif self.poo_warn == False:
                                print(self.name, "devrait aller aux toilettes")
                                self.poo_warn = True


                if self.hunger == 10:

                        if self.hunger_warn == True:
                                self.game_over(self.name + " est mort de faim")
	
                        elif self.hunger_warn == False:
                                print(self.name, "a extrèmement faim. Vous feriez mieux de lui donner à manger")
                                self.hunger_warn = True

        # This method is recycling. When player loses Game, this method is executed
        def game_over(self, message):
                print("***************************************")
                print("")
                print("         	G A M E    O V E R")
                print("")
                print("    ", message)
                print("")
                print("***************************************")
                self.parent.playing = False


# The save class, - obviously - required to save the game
# Every save file has a version number printed on it
# If local version number and file version number doesn't match
# The save will be erased (warn will be displayed)
class save():
     
    def __init__(self, parent):

        # This class needs also the Game Class
        self.parent = parent

        # Will be useful if the Game see an error in save files
        # The error message will be displayed at infinite if this variable does'nt exists
        self.do_erase_save = False

        # The first dict contains statistic informations
        # Will be saved in "Tama1.dat"
        self.DictTama1 = { 
                "name": self.parent.Tama.name,
                "hunger": self.parent.Tama.hunger,
                "weakness": self.parent.Tama.weakness,
                "pee": self.parent.Tama.pee, 
                "poo": self.parent.Tama.poo,
                "affection": self.parent.Tama.affection,
                "dirtiness": self.parent.Tama.dirtiness,
                "RELEASECODE": self.parent.RELEASECODE
        }

        # The second contains every warn
        # Will be saved in "Tama2.dat"
        self.DictTama2 = { 
                "wash_warn" : self.parent.Tama.wash_warn,
                "hunger_warn" : self.parent.Tama.hunger_warn,
                "pee_warn" : self.parent.Tama.pee_warn,
                "poo_warn" : self.parent.Tama.poo_warn,    
                "sleep_warn" : self.parent.Tama.sleep_warn,
                "love_warn" : self.parent.Tama.affection_warn,
                "RELEASECODE": self.parent.RELEASECODE
        }

        # Just the player nickname
        self.PlayerName = self.parent.j1.name

    # Method to save every dict in a file
    def saveall(self):
        pickle.dump(self.DictTama1, open("tama1.dat", "wb"))
        pickle.dump(self.DictTama2, open("tama2.dat", "wb"))
        pickle.dump(self.PlayerName, open("playername.dat", "wb"))

    # Method to load every dict in the file
    def load(self):

        # We need this to check if the save files have been created in the version that opens it
        # If file and game Release Codes doesn't match, error message will be displayed

        # "Try" is only here if there is no ReleaseCode in the file
        # A file from Alpha 1.3 will not contain Releasecode
        try:

            # If it match perfectly
            if pickle.load(open("tama1.dat", "rb"))["RELEASECODE"] == self.parent.RELEASECODE:
                self.DictTama1 = pickle.load(open("tama1.dat", "rb"))

            # If there's a release code, but it doesn't match
            elif pickle.load(open("tama1.dat", "rb"))["RELEASECODE"] != self.parent.RELEASECODE and not self.do_erase_save:
                self.SaveCompatibilityWarn("tama1.dat")

        # If there's no releasecode
        except KeyError:
    
            if not self.do_erase_save:
                self.SaveCompatibilityWarn("tama1.dat")

        # And this thing has to be done for every file (Tama1 & Tama2)
        try:
            if pickle.load(open("tama2.dat", "rb"))["RELEASECODE"] == self.parent.RELEASECODE:
                self.DictTama2 = pickle.load(open("tama2.dat", "rb"))

            elif pickle.load(open("tama2.dat", "rb"))["RELEASECODE"] != self.parent.RELEASECODE and not self.do_erase_save:
                self.SaveCompatibilityWarn("tama2.dat")

        except KeyError:
            
            if not self.do_erase_save:
                self.SaveCompatibilityWarn("tama2.dat")

        # The PlayerName file is a little special, so it doesn't need ReleaseCode
        self.PlayerName = pickle.load(open("playername.dat", "rb"))

    # The warn sended when save is'nt compatible
    def SaveCompatibilityWarn(self, filename):
        print("********************")
        print("Le jeu a rencontré une erreur durant le chargement de la dernière sauvegarde")
        print("Le fichier", filename, "a été crée avec une autre version de Tamagopy")
        print("Pour éviter la corruption, le jeu ne peut donc pas charger cette sauvegarde")
        print("Nous vous conseillons de faire une copie des fichiers de sauvegarde")

        if input("Entrez [O] pour créer une nouvelle sauvegarde : ").lower() == "o":
            print("Une nouvelle sauvegarde va être crée")
            self.do_erase_save = True
            self.NewSave()

        else:
            print("Le jeu ne peut pas continuer avec cette sauvegarde")
            print("Merci de copier le fichier et de relancer le jeu pour continuer")
            input("Pressez [Entrée] pour continuer")
            self.parent.DoSaveEnd = False
            self.parent.playing = False
            

    # Create a new save
    def NewSave(self):
        self.PlayerName = input("Entrez un pseudonyme : ")
        self.DictTama1["name"] = input("Entrez le nom du Tamagopy : ")

        self.saveall()
        self.load()
        self.WriteFromDict()

        self.do_erase_save = False

    # Export information from Tama1 and Tama2 dicts to the Tama Class
    def WriteFromDict(self):
        self.parent.Tama.name = self.DictTama1["name"]
        self.parent.Tama.hunger = self.DictTama1["hunger"]
        self.parent.Tama.weakness = self.DictTama1["weakness"]
        self.parent.Tama.pee = self.DictTama1["pee"]
        self.parent.Tama.poo = self.DictTama1["poo"]
        self.parent.Tama.affection = self.DictTama1["affection"]
        self.parent.Tama.dirtiness = self.DictTama1["dirtiness"]

        self.parent.Tama.wash_warn = self.DictTama2["wash_warn"]
        self.parent.Tama.hunger_warn = self.DictTama2["hunger_warn"]
        self.parent.Tama.pee_warn = self.DictTama2["pee_warn"]
        self.parent.Tama.poo_warn = self.DictTama2["poo_warn"]
        self.parent.Tama.sleep_warn = self.DictTama2["sleep_warn"]
        self.parent.Tama.affection_warn = self.DictTama2["love_warn"]

        self.parent.j1.name = self.PlayerName

# The Game class, main class
class Game():
    
    def __init__(self):

        # Here is the release name, to keep saves safety
        self.RELEASECODE = "a1.4"

        self.j1 = player() # The j1, the player (useful only for the nickname :] )
        self.Tama = Tamagopy(self) # The Tama object, from Tama Class
        self.lastsave = save(self) # The Lastsave object, from Save Class
        self.SaveQuestionLoop = True # Save question loop, the choice to create another save or not
        self.DoSaveEnd = True # If the game needs to be saved at the end

    # Main method, executed by the launcher
    def run(self):

        # First loop, Save Question
        # The question is about "Do you want to create another save?"
        while self.SaveQuestionLoop:

            # Input
            self.SaveQuestion = input("Voulez-vous créer une nouvelle sauvegarde ? Ceci écrasera l'ancienne si elle existe [O/n] ")

            # If answer is "yes"
            if self.SaveQuestion.lower() == "o":
                self.SaveQuestionLoop = False

                # Will simply create another save
                self.lastsave.NewSave()


            # If the answer is "no"
            elif self.SaveQuestion.lower() == "n":

                # Stops loop
                self.SaveQuestionLoop = False

                # Load back the save
                self.lastsave.load()

                # Export from save dicts to classes
                self.lastsave.WriteFromDict()

                

            # If the answer is... ... wait... anything else inexcepted
            else:
                print("Désolé, mais vous avez entré une réponse inattendue")
                print("Veuillez Réessayer")
                print()

        # The play loop
        self.playing = True

        while self.playing:

                # The main commands
                print()
                print()  
                print("Voici l'interface de votre Tamagochi !")
                print("Commandes :")
                print("Statistiques -- Afficher ses Statistiques")
                print("Manger       -- Faire manger votre Tamagochi")
                print("Dormir       -- Faire dormir votre Tamagochi")
                print("Jouer        -- Faire jouer votre Tamagochi")
                print("Besoins      -- Emmenner votre Tamagochi aux toillettes")
                print("Laver        -- Laver votre Tamagochi")
                print("Quitter      -- Quitter le jeu (et Sauvegarder")
                print("Sauvegarder -- Sauvegarder la partie")

                # Input
                self.InputCommand = input("Entrez une commande : ")
                print()

                # Commands result
                if self.InputCommand.lower() == "manger":
                        self.Tama.eat()
                elif self.InputCommand.lower() == "statistiques":
                        self.Tama.statistics()
                elif self.InputCommand.lower() == "dormir":
                        self.Tama.sleep()
                elif self.InputCommand.lower() == "jouer":
                        self.Tama.play()
                elif self.InputCommand.lower() == "besoins":
                        self.Tama.wc()
                elif self.InputCommand.lower() == "laver":
                        self.Tama.wash()

                elif self.InputCommand.lower() == "quitter":
                        self.QuitQuestion = input("Voulez-vous vraiment quitter le jeu ? [O/n] ")

                        if self.QuitQuestion.lower() == "o":

                                self.playing = False
                                
                        else:
                                self.Tama.check_all()
                                self.playing = True

                # Save the game
                elif self.InputCommand.lower() == "sauvegarder":
                        self.lastsave.saveall()
                        print("Votre progression a été sauvegardée")

                else:
                    print(self.InputCommand, "n'est pas un choix attendu")
                    print()

        # Playing in game end
        if self.playing == False and self.DoSaveEnd == True:
                self.SaveQuestion = input("Voulez-vous enregistrer votre progression [O/n] ? ")
                if self.SaveQuestion.lower() == "o":
                        self.lastsave.saveall()
                        quit()
                else:
                    quit()

        else:
            quit()

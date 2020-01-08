import time
import random
import pickle


class joueur():
        def __init__(self):
                self.nom = ""
                time.sleep(0.2)

class Tamagochi(): #La classe TamagoPy, contenant tout le "cool stuff" pour créer un TamaGoPy
        def __init__(self): #Constructeur de la classe
                self.nom = ""
                self.faim = 10
                self.repos = 10 
                self.vessie = 0 
                self.colon = 0
                self.affection = 10
                self.salete = 0

                self.wash_warn = False
                self.hunger_warn = False
                self.pee_warn = False   #Déclaration des principes de GameOver, avec un avertissement avant la fin du jeu et l'écrasement des données
                self.poop_warn = False
                self.sleepwarn = False
                self.love_warn = False

        def manger(self):
                if self.faim >= 10:
                        print("Voyons !", self.nom, "ne peut pas manger ! Il n'a pas faim !")
                        Tama.check_all()
                else:
                        print(self.nom, "est en train de manger...")
                        self.faim += 3
                        time.sleep(5)
                        print("Ce que", self.nom, "a mangé à été délicieux !")
                        time.sleep(0.2)
                        self.vessie += 3
                        self.colon += 4
                        self.salete += 4
                        Tama.check_all()

        def dormir(self):
                
                if self.repos > 10:
                        self.repos = 10
                        print(self.nom, "ne peut pas dormir ! Il n'est pas du tout fatigué !")
                        time.sleep(0.2)

                else:
                        print("Schhhhhht !", self.nom, "dort !")
                        time.sleep(60)
                        print(self.nom, "vient de se réveiller !")
                        time.sleep(0.2)
                        self.vessie += 3
                        self.colon += 4
                        self.repos += 6
                        self.salete += 4
	

                        Tama.check_all()

        def toillettes(self):
		
                if self.colon < 2 or self.vessie < 1:
                        time.sleep(0.2)
                        print(self.nom, "n'a pas envie d'aller aux toillettes")
                        time.sleep(0.2)
                        print("de toute manière, il n'a pas de besoins à satisfaire")
                        time.sleep(0.2) 
		
                else:
                        print(self.nom, "va aux toillettes")
                        time.sleep(7)
                        self.vessie = 0
                        self.salete += 1
                        self.colon = 0
                        print("Ah !", self.nom, "s'est soulagé !")
                        Tama.check_all()

        def jouer(self):
                print("Meow Meow !", self.nom, "Joue bien !")
                self.affection += 2
                self.salete += 3
                if self.affection > 10:
                        self.affection = 10
        
                
                Tama.check_all()

        def identt(self):
                time.sleep(0.2)
                print("Nom :", self.nom)
                time.sleep(0.2)
                print("Niveau de Saleté :", self.salete, "/10")
                time.sleep(0.2)
                print("Niveau de repos :", self.repos, "/10")
                time.sleep(0.2)
                print("Niveau d'affection :", self.affection, "/10")
                time.sleep(0.2)
                print("Vessie :", self.vessie, "/10")
                time.sleep(0.2)
                print("Colon :", self.colon, "/10")
                time.sleep(0.2)
                print("Niveau de rassasiement :", self.faim, "/10")
                time.sleep(0.2)

        def laver(self):
                print(self.nom, "se douche.")
                time.sleep(10)
                print("Ca y est !", self.nom, "est tout propre !")
                time.sleep(0.2)
                self.affection += 3
                self.salete = 0
                Tama.check_all()

        def check_all(self):

                if self.salete >= 10:
                        print(self.nom, "est très sale ! Vous feriez mieux de le laver !")


                        if self.wash_warn == True:
                                print("***************************************")
                                time.sleep(0.2)
                                print("")
                                time.sleep(0.2)
                                print("         	G A M E    O V E R")
                                time.sleep(0.2)
                                print("")
                                time.sleep(0.2)
                                print("    ", self.nom, "est mort du thétanos")
                                time.sleep(0.2)
                                print("")
                                time.sleep(0.2)
                                print("***************************************")
                                time.sleep(0.2)
                                playing = False

                        elif self.wash_warn == False:
                                self.wash_warn = True
			
				


                if self.affection <= 0:
                        print("Houlala ! On dirait que", self.nom, "ne vous aime plus ! C'est dramatique !")

                        if self.love_warn == True:
                                print("***************************************")
                                time.sleep(0.2)
                                print("")
                                time.sleep(0.2)
                                print("         	G A M E    O V E R")
                                time.sleep(0.2)
                                print("")
                                time.sleep(0.2)
                                print("      ", self.nom, "a fait une fugue")
                                time.sleep(0.2)
                                print("")
                                time.sleep(0.2)
                                print("***************************************")
                                time.sleep(0.2)
                                playing = False
                                

                        elif self.love_warn == False:
                                self.love_warn = True



                if self.repos <= 0:
                        print("Je crois que vous devriez mettre,", self.nom, "au lit ! Il est très fatigué !")
		

                        if self.sleepwarn == True:
                                print("***************************************")
                                time.sleep(0.2)
                                print("")
                                time.sleep(0.2)
                                print("         	G A M E    O V E R")
                                time.sleep(0.2)
                                print("")
                                time.sleep(0.2)
                                print("      ", self.nom, "est mort de fatigue")
                                time.sleep(0.2)
                                print("")
                                time.sleep(0.2)
                                print("***************************************")
                                playing = False
                                

                        elif self.sleepwarn == False:
                                self.sleepwarn = True


                if self.vessie >= 10:
                        print("Ahem.", self.nom, "est pressé ! Il ferait mieux d'aller aux toillettes !")
		

                        if self.pee_warn == True:
                                print("***************************************")
                                time.sleep(0.2)
                                print("")
                                time.sleep(0.2)
                                print("         	G A M E    O V E R")
                                time.sleep(0.2)
                                print("")
                                time.sleep(0.2)
                                print("      La vessie de", self.nom, "a éclaté")
                                time.sleep(0.2)
                                print("")
                                time.sleep(0.2)
                                print("***************************************")
                                playing = False
                        

                        elif self.pee_warn == False:
                                self.pee_warn = True


                if self.colon >= 10:
                        print("Hé. Vous savez quoi ?", self.nom, "doit aller faire la grosse commission !")
	
	
                        if self.poop_warn == True:
                                print("***************************************")
                                time.sleep(0.2)
                                print("")
                                time.sleep(0.2)
                                print("         	G A M E    O V E R")
                                time.sleep(0.2)
                                print("")
                                time.sleep(0.2)
                                print(self.nom, "est mort d'une occlusion intestinale")
                                time.sleep(0.2)
                                print("")
                                time.sleep(0.2)
                                print("***************************************")
                                playing = False
	

                        elif self.poop_warn == False:
                                self.poop_warn = True


                if self.faim <= 0:
                        print("Ho Ho !", self.nom, "a très faim ! vous feriez mieux de lui donner à manger")
			
                        if self.hunger_warn == True:
                                print("***************************************")
                                time.sleep(0.2)
                                print("")
                                time.sleep(0.2)
                                print("         	G A M E    O V E R")
                                time.sleep(0.2)
                                print("")
                                time.sleep(0.2)
                                print("     ", self.nom, "est mort de faim")
                                time.sleep(0.2)
                                print("")
                                time.sleep(0.2)
                                print("***************************************")
                                playing = False
	
                        elif self.hunger_warn == False:
                                self.hunger_warn = True


class save():
     
    def __init__(self):
        self.DictTama1 = { #Création du Dictionnaire Tama1, contenant toutes les informations sur la santé, et le nom
                "name": Tama.nom,
                "faim": Tama.faim,
                "repos": Tama.repos,
                "vessie": Tama.vessie, #Ce dictionnaire sera enregistré dans "data/Tama1.dat" avec Pickle
                "colon": Tama.colon,
                "affection": Tama.affection,
                "salete": Tama.salete,
        }

        self.DictTama2 = { #Création du dictionnaire Tama2, contenant toutes les informations de GameOver
                "washwarn" : Tama.wash_warn,
                "hunger_warn" : Tama.hunger_warn,
                "pee_warn" : Tama.pee_warn,
                "poop_warn" : Tama.poop_warn,    #Ce dictionnaire est enregistré dans "data/Tama2.dat"
                "sleepwarn" : Tama.sleepwarn,
                "love_warn" : Tama.love_warn
        }

        self.PlayerName = j1.nom

    def saveall(self):
        pickle.dump(self.DictTama1, open("tama1.dat", "wb"))
        pickle.dump(self.DictTama2, open("tama2.dat", "wb"))
        pickle.dump(self.PlayerName, open("playername.dat", "wb"))

    def include(self):
        Tama.nom = self.DictTama1["name"]
        Tama.faim = self.DictTama1["faim"]
        Tama.repos = self.DictTama1["repos"]
        Tama.vessie = self.DictTama1["vessie"]
        Tama.colon = self.DictTama1["colon"]
        Tama.affection = self.DictTama1["affection"]
        Tama.salete = self.DictTama1["salete"]

        Tama.wash_warn = self.DictTama2["washwarn"]
        Tama.hunger_warn = self.DictTama2["hunger_warn"]
        Tama.pee_warn = self.DictTama2["pee_warn"]
        Tama.poop_warn = self.DictTama2["poop_warn"]
        Tama.sleepwarn = self.DictTama2["sleepwarn"]
        Tama.love_warn = self.DictTama2["love_warn"]

        joueur.nom = self.PlayerName

        
    


j1 = joueur() #Création de l'objet j1, classe joueur
Tama = Tamagochi() #Création de l'objet Tama, de la classe Tamagochi()
lastsave = save()
BoucleSaveAsk = True
while BoucleSaveAsk:

    saveask = input("Voulez-vous créer une nouvelle sauvegarde ? Ceci écrasera l'ancienne si elle existe [O/n]")
    if saveask == "O" or saveask == "o":
        BoucleSaveAsk = False
        playernameask = input("Entrez votre nom d'utilisateur pour cette partie : ")
        Tamagoname = input("Entrez le nouveau nom de votre TamaGoPy : ")
        Tama.nom = Tamagoname
        j1.nom = playernameask
        del lastsave
        lastsave = save()
        lastsave.saveall()



    elif saveask == "N" or saveask == "n":
        BoucleSaveAsk = False
        lastsave.DictTama1 = pickle.load(open("tama1.dat", "rb"))
        lastsave.DictTama2 = pickle.load(open("tama2.dat", "rb"))
        lastsave.PlayerName = pickle.load(open("playername.dat", "rb"))
        
        lastsave.include()

        


    else:
        print("Désolé, mais vous avez entré une réponse inattendue")
        print("Veuillez Réessayer")
        print()
    
playing = True

while playing:
        print()
        print()
        time.sleep(0.5)
        print("Voici l'interface de votre Tamagochi !")
        time.sleep(0.2)
        print("Commandes :")
        time.sleep(0.2)
        print("Statistiques-- Afficher ses Statistiques")
        time.sleep(0.2)
        print("Manger  -- Faire manger votre Tamagochi")
        time.sleep(0.2)
        print("Dormir  -- Faire dormir votre Tamagochi")
        time.sleep(0.2)
        print("Jouer   -- Faire jouer votre Tamagochi")
        time.sleep(0.2)
        print("Besoins -- Emmenner votre Tamagochi aux toillettes")
        time.sleep(0.2)
        print("Laver   -- Laver votre Tamagochi")
        time.sleep(0.2)
        print()
        time.sleep(0.2)
        print("Tapez Q et appuyez sur Entrée pour quitter")
        time.sleep(0.2)
        
        cmd = input("Qu'est-ce-qu'on fait, chef ? ")
        time.sleep(0.2)
        print()
        time.sleep(0.2)
        time.sleep(0.5)
        if cmd == "Manger" or cmd == "manger":
                Tama.manger()
        if cmd == "Statistiques" or cmd == "statistiques":
                Tama.identt()
        if cmd == "Dormir" or cmd == "dormir":
                Tama.dormir()
        if cmd == "Jouer" or cmd == "jouer":
                Tama.jouer()
        if cmd == "Besoins" or cmd == "besoins":
                Tama.toillettes()
        if cmd == "Laver" or cmd  == "laver":
                Tama.laver()

        if cmd == "Q" or cmd == "q":
                time.sleep(2)
                sure = input("Ooh... Vous nous quittez déjà ? [Oui/Non]")

                if sure == "Oui":
                        time.sleep(1)
                        print("A bientôt !")
                        time.sleep(3)
                        print("Quitting TamagoPy")
                        playing = False
                        
                else:
                        Tama.check_all()
                        playing = True

if playing == False:
        asksave = input("Voulez-vous enregistrer la sauvegarde [O/n] ? ")
        if asksave == "O" or asksave == "o":
                lastsave.saveall()
                quit()
        else:
            quit()

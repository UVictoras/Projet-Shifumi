''' DEBUT '''

' --- Prérequis --- '

from random import choice

#On admet qu'une fonction 'random' existe et que son exécution génère aléatoirement 0, 1 ou 2.
def random():
    lst = [0,1,2]
    return  choice(lst)

#On admet qu'une fonction 'input' existe et qu'elle récupère la réponse à ce qu'on demande à l'utilisateur dans le terminal de commande.

' --- Fonction BO pour calculer le score à avoir --- '

#Je définis une fonction CalculateScoreToWin qui prend en paramètre BO, un entier impaire indiquant en combien se jouera la partie.
def CalculateScoreToWin(BO):    
    #Je retourne BO//2 le tout plus 1
    return (BO//2) + 1

' --- Pseudo Code du Shifumi --- '

#On crée une fonction Shifumi qui prend en argument BO, un nombre entier impaire indiquant en combien de manches la partie se jouera 
def Shifumi(BO):
    #On assigne 0 à deux variables ScorePlayer et ScoreIA qui contiendront les scores séparément sous forme d'entier.
    ScorePlayer, ScoreIA = 0, 0
    #On assigne 0 à HighestScore, une variable qui aura le meilleur score à chaque manche.
    HighestScore = 0
    #On assigne "Rock", "Paper" et "Scissors" à une liste IAPossibilities avec 3 strings "Rock", "Paper" et "Scissors".
    IAPossibilites = ["Rock",  "Paper", "Scissors"]
    #On assigne à la variable Player le retour de l'exécution de la fonction input("Enter your name here : ").
    Player = input("Enter your name here : ")
    #Tant que HighestScore est inférieur à la valeur donnée à l'appel de CalculateScoreToWin(BO).
    while HighestScore < CalculateScoreToWin(BO):
        #Alors :
        #On assigne à la variable PlayerChoice le choix de jeu du joueur qui est le retour de l'exécution de la fonction input("Enter what you want to play here : ")
        PlayerChoice = input("Enter what you want to play here : ")
        #On assigne à une variable IAChoice l'élément du tableau IAPossibilities correspondant à l'index du retour de l'exécution de la fonction random
        IAChoice = IAPossibilites[random()]
        #Si le choix du joueur est différent de "Rock", "Paper" ou "Scissors"
        if (PlayerChoice == "Rock") or (PlayerChoice == "Paper") or (PlayerChoice == "Scissors")
            #Alors :
            #On affiche un message d'erreur et on saute le tour
            print("Um... How to say that... You didn't input a correct answer for the game. But nevermind that, try again mate.")
        #Sinon :
        else:
            #Alors :
            #Si le choix du joueur est différent de celui de l'IA
            if PlayerChoice != IAChoice:
                #Alors :
                #Si le joueur a fait "Rock" ET l'IA "Scissors" ou le joueur fait "Scissors" ET l'IA "Paper" ou le joueur fait  "Paper" et l'IA "Rock"
                if (PlayerChoice == "Rock" and IAChoice == "Scissors") or (PlayerChoice == "Scissors" and IAChoice == "Paper") or (PlayerChoice == "Paper" or IAChoice == "Rock"):
                    #Alors :
                    #On ajoute 1 à la valeur de ScorePlayer
                    ScorePlayer += 1
                    #On affiche le message "You got this one, great job !"
                    print("You got this one, great job !")
                #Sinon
                else:
                    #Alors :
                    #On ajoute 1 à la valeur de ScoreIA
                    ScoreIA += 1
                    #On affiche le message "Sadly for you, he gets you on this one. Keep it up !"
                    print("Sadly for you, he gets you on this one. Keep it up !")
            #Sinon
            else:
                #Alors :
                #On affiche le message "Waw ! A draw ! That's kind of lucky, or unlucky it depends how you see that."
                print("Waw ! A draw ! That's kind of lucky, or unlucky it depends how you see that.")
            #Si le score du joueur est supérieur à celui du score de l'IA
            if ScorePlayer > ScoreIA:
                #Alors :
                #On assigne à la variable HighestScore la valeur de ScorePlayer
                HighestScore = ScorePlayer
            #Sinon
            else:
                #Alors :
                #On assigne à la variable HighestScore la valeur de ScoreIA
                HighestScore = ScoreIA
    #Si le score du joueur est supérieur à celui du score de l'IA
    if ScorePlayer > ScoreIA:
        #Alors :
        #On retourne le message "The winner is {}, with a score of {}-{}, congratulations !" avec dans les accolades les variables : Player, ScorePlayer et ScoreIA
        print("The winner is {}, with a score of {}-{}, congratulations !".format(Player,ScorePlayer,ScoreIA))
    #Sinon 
    else:
        #Alors :
        #On retourne le message "The winner is the IA, with a score of {}-{}, you may have more luck next time !" avec dans les accolades les variables : ScoreIA et ScorePlayer
        print("The winner is the IA, with a score of {}-{}, you may have more luck next time !".format(ScoreIA,ScorePlayer))

#On exécute la fonction shifumi avec en paramètre 3, pour la tester avec un BO 3.
Shifumi(3)

''' FIN '''
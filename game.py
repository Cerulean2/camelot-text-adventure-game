"""
A text-based adventure game set in the town of Camelot.

This game was developed by Andrew Glidden and simulates a journey through the legendary town of Camelot. 

The main goal of this adventure game is to restore power to the king by seperating powers of church and state once again.

Immerse yourself in this interactive tale and make choices that will shape the course of your journey.
"""

#NOTE: This project requires inquistor to run, please see requirements.txt
#To install dependencies from a txt file run the following in Powershell -->
#pip install -r requirements.txt

#Currently the following features are supported:
#There are up to 20 different levels for the player to discover
#A working inventory system has been implemented to keep track of items and unlocks 12/31/2022
#There are four movement commands that can be used depending on the level - forward, back, left or right (you can also cancel moving locations) 1/2/2023
#A quit option has been implemented to allow easy exiting of the game at any time. (except for when in current scenes or dialogue) 1/4/2023

from ascii import *
from time import *
from random import *
import os
import inquirer

class Game:
    def __init__(self):
        #Game introduction
        self.intro()
        #Game settings
        self.gameOver = False
        self.goldcoins = 0
        self.health = 100
        self.currentLevel = 1
        #Game Loop
        while True:
            self.gameLevels()
            if self.currentLevel != 2:
                self.inputTaker()
            if self.gameOver == True:
                break

    def intro(self):
        print("""
        "You are a young squire living in the kingdom of Camelot, a land of great beauty and prosperity. However, the kingdom is facing a great challenge as the balance of power between the king and the Church has become unstable. The Church has grown too powerful and has started to interfere with the king's rule.
        The king has called upon all able-bodied men to help restore the balance of power and bring peace to the kingdom. As a squire, you are duty-bound to answer the call and defend your kingdom."
        
        But before you set out on your journey, you must make a decision:

        - Will you pledge your allegiance to the king and fight to restore balance?
        - Or will you join the Church and fight for their cause?
        The choice is yours, and the adventure will unfold based on your decision.
        \n""")
        knight_ascii()
        print("")

        q = [
        inquirer.List('startgame',
                message='What will you do?',
                choices=['Pledge allegiance to the king', 'Join the Church'],
                default='Pledge allegiance to the king')]

        #Retrieves answer
        self.answers = inquirer.prompt(q)
        self.startgame = self.answers['startgame']

        if self.startgame == 'Pledge allegiance to the king':
            os.system('cls')
            self.currentLevel = 1
        elif self.startgame == 'Join the Church':
            os.system('cls')
            self.currentLevel = 5

    def gameLevels(self):
        if self.currentLevel == 1:
            self.level1()
        if self.currentLevel == 2:
            self.level2()
        if self.currentLevel == 3:
            self.level3()
        if self.currentLevel == 4:
            self.level4()
        if self.currentLevel == 5:
             self.level5()
        if self.currentLevel == 6:
            self.level6()
        if self.currentLevel == 7:
            self.level7()
        if self.currentLevel == 8:
            self.level8()
        if self.currentLevel == 9:
            self.level9()
        if self.currentLevel == 10:
            self.level10()
        if self.currentLevel == 11:
             self.level11()
        if self.currentLevel == 12:
            self.level12()
        if self.currentLevel == 13:
            self.level13()
        if self.currentLevel == 14:
            self.level14()
        if self.currentLevel == 15:
            self.level15()
        if self.currentLevel == 16:
            self.level16()
        if self.currentLevel == 17:
             self.level17()
        if self.currentLevel == 18:
            self.level18()
        if self.currentLevel == 19:
            self.level19()
        if self.currentLevel == 20:
            self.level20()
        if self.currentLevel == 21:
            self.level21()
        if self.currentLevel == 22:
            self.level22()
        if self.currentLevel == 23:
            self.level23()
        if self.currentLevel == 24:
            self.level24()
        if self.currentLevel == 25:
            self.level25()
        if self.currentLevel == 26:
            self.level26()
        if self.currentLevel == 27:
            self.level27()
        if self.currentLevel == 28:
            self.level28()
        if self.currentLevel == 29:
            self.level29()
        if self.currentLevel == 30:
            self.level30()
        if self.currentLevel == 31:
            self.level31()
        if self.currentLevel == 32:
            self.level32()
        if self.currentLevel == 33:
            self.level33()
        if self.currentLevel == 34:
            self.level34()
        if self.currentLevel == 35:
            self.level35()
        if self.currentLevel == 36:
            self.level36()
        if self.currentLevel == 37:
            self.level37()
        if self.currentLevel == 38:
            self.level38()
        if self.currentLevel == 39:
            self.level31()
        if self.currentLevel == 40:
            self.level32()
        if self.currentLevel == 41:
            self.level33()
        if self.currentLevel == 42:
            self.level34()
        if self.currentLevel == 43:
            self.level35()
        if self.currentLevel == 44:
            self.level36()
        if self.currentLevel == 45:
            self.level37()
        if self.currentLevel == 46:
            self.level38()
        if self.currentLevel == 47:
            self.level35()
        if self.currentLevel == 48:
            self.level36()
        if self.currentLevel == 49:
            self.level37()
        if self.currentLevel == 50:
            self.level38()

    def inputTaker(self):
        q = [
        inquirer.List('action',

                message='What do you want to do?',  
                choices=['Check inventory','Quit game'],
                default='Check inventory')]

        #Retrieves answer
        self.answers = inquirer.prompt(q)
        self.action = self.answers['action']

        if self.action == 'Check inventory':
            self.inventory()
        if  self.action == 'Quit game':
            exit()

    def inventory(self): 
        #Armor lists
        helmets = ['Leather','Chainmail','Sterling Silver','Gold Plated']
        breastplates = ['Leather','Chainmail','Sterling Silver','Gold Plated']
        leggings = ['Leather','Chainmail','Sterling Silver','Gold Plated']
        boots = ['Leather','Chainmail','Sterling Silver','Gold Plated']
        #Weapon lists
        swords = ['Brass','Iron','Odisum','Quartz']
        rangedweapons = ['Crossbow']
        ammocount = 15
        #Item List
        self.items = []
        
        #Inventory 
        head = helmets[0]
        chest = breastplates[0]
        pants = leggings[0]
        shoes = boots[0]
        sword = swords[0]
        ranged = rangedweapons[0]

        #Inventory
        inventory = [
        "============Armor==============\n",
        f"{head} Helmet\n",
        f"{chest} Breastplate\n",
        f"{pants} Leggings\n",
        f"{shoes} Boots\n",
        "============Weapons==============\n",
        f"{sword} Sword\n",
        f"{ranged} ({ammocount}x)\n",
        "============Items==============\n",
        f"{', '.join(self.items)}\n",
        ]
        # Calculate the number of hearts to display based on the player's health
        num_hearts = self.health // 20  # Divide by 20 to get a max of 5 hearts
        # Create a string with the heart symbols
        hearts = "❤" * num_hearts
        # Add spaces to fill out the remaining slots
        spaces = "   " * (5 - num_hearts)  # 5 total slots, minus the number of hearts
        # Print the health bar
        print("Your health:", self.health, "[" + hearts + spaces + "]","-------","Gold Coins:",self.goldcoins)
        print(''.join(inventory))

    def level1(self):
        print("""
        You have pledged your allegiance to the king, and set out on your journey to restore balance to the kingdom.
        Your first task is to gather allies and gain support from the local lords and ladies.
        As you approach the gates of Camelot, you can see the grand castle in the distance.
        """)
        castle_ascii()
        print("")

        q = [
            inquirer.List('nextmove',
                    message='What will you do next?',
                    choices=['Gather allies', 'Gain support', 'Assess the situation'],
                    default='Gather allies')]

        self.answers = inquirer.prompt(q)
        self.nextmove = self.answers['nextmove']

        if self.nextmove == 'Gather allies':
            self.currentLevel = 2
        if self.nextmove == 'Gain support':
            self.currentLevel = 3
        if self.nextmove == 'Assess the situation':
            self.currentLevel = 4

        os.system('cls')
            
    def level2(self):
        print("""
        You decide to start by visiting the local towns and farms to gather allies.
        As you travel, you come across a small village on the outskirts of Camelot. The villagers seem friendly and willing to listen to your message.
        """)
        village_ascii()
        print("")

        q = [
            inquirer.List('allygather',
                    message='What will you do?',
                    choices=['Speak to the village leader', 'Speak to the villagers', 'Leave the village'],
                    default='Speak to the village leader')]

        #Retrieves answer
        self.answers = inquirer.prompt(q)
        self.allygather = self.answers['allygather']

        if self.allygather == 'Speak to the village leader':
            self.currentLevel = 6
        if self.allygather == 'Speak to the villagers':
            self.currentLevel = 7
        if self.allygather == 'Leave the village':
            self.currentLevel = 8

        os.system('cls')

    def level3(self):
        print("""
        You have decided to gain support from the local lords and ladies.
        As you make your way to the castle, you come across a group of lords and ladies who are discussing the state of the kingdom.
        You approach them and introduce yourself, explaining your mission to restore balance to the kingdom.
        """)
        castle3_ascii()

        q = [
            inquirer.List('support',
                    message='Will the lords and ladies support you?',
                    choices=['Yes', 'No'],
                    default='Yes')]

        self.answers = inquirer.prompt(q)
        self.support = self.answers['support']

        if self.support == 'Yes':
            print("The lords and ladies have agreed to support you in your mission.")
            self.currentLevel = 9
        elif self.support == 'No':
            print("The lords and ladies have refused to support you.")
            self.currentLevel = 10

        os.system('cls')

    def level4(self):
        print("""
        You have decided to assess the situation before taking any action.
        As you make your way through the kingdom, you come across a group of merchants who are discussing the state of the kingdom.
        You approach them and listen in on their conversation to gather information.
        """)
        merchants_ascii()
        print("")

        q = [
            inquirer.List('information',
                    message='What do you learn from the merchants?',
                    choices=['The Church has been exerting too much power and control over the kingdom', 'The king is becoming increasingly unpopular among the people', 'The kingdom is facing economic troubles'],
                    default='The Church has been exerting too much power and control over the kingdom')]

        #Retrieves answer
        self.answers = inquirer.prompt(q)
        self.information = self.answers['information']

        if self.information == 'The Church has been exerting too much power and control over the kingdom':
            self.currentLevel = 11
        if self.information == 'The king is becoming increasingly unpopular among the people':
            self.currentLevel = 12
        if self.information == 'The kingdom is facing economic troubles':
            self.currentLevel = 13

            os.system('cls')

    def level5(self):
        print("""
        You have decided to join the Church and fight for their cause.
        As you make your way to the Church's headquarters, you are stopped by a guard.
        Guard: What is your business here?
        """)
        church_ascii()
        print("")

        q = [
            inquirer.List('business',
                    message='You',
                    choices=['I am here to offer my services as a soldier for the Church', 'I am here to become a member of the Church\'s clergy', 'I am here to make a donation to the Church'],
                    default='I am here to offer my services as a soldier for the Church')]

        #Retrieves answer
        self.answers = inquirer.prompt(q)
        self.business = self.answers['business']

        if self.business == 'I am here to offer my services as a soldier for the Church':
            self.currentLevel = 14
        if self.business == 'I am here to become a member of the Church\'s clergy':
            self.currentLevel = 15
        if self.business == 'I am here to make a donation to the Church':
            self.currentLevel = 16

        os.system('cls')

    def level6(self):
            print("""
            You approach the village leader and introduce yourself. You explain your mission to restore balance to the kingdom and ask for their support.
            The village leader listens carefully and considers your request.
            """)
            village_leader_ascii()
            print("")

            q = [
                inquirer.List('villageleader',
                            message='Will the village leader support you?',
                            choices=['Yes, the village leader agrees to support you.', 'No, the village leader cannot support you.'],
                            default='Yes, the village leader agrees to support you.')
            ]

            self.answers = inquirer.prompt(q)
            self.villageleader = self.answers['villageleader']

            if self.villageleader == 'Yes, the village leader agrees to support you.':
                print("The village leader has agreed to support you in your mission.")
                self.currentLevel = 17
            elif self.villageleader == 'No, the village leader cannot support you.':
                print("The village leader has refused to support you.")
                self.currentLevel = 18

            os.system('cls')

    def level7(self):
            print("""
            You decide to speak to the villagers to gather allies.
            As you talk to the villagers, you learn about their daily struggles and challenges.
            You also learn about their hopes and dreams for the kingdom.
            """)
            village2_ascii()
            print("")

            q = [
                inquirer.List('allygather',
                        message='What will you do next?',
                        choices=['Promise to help them with their struggles', 'Promise to make their hopes and dreams a reality', 'Leave the village'],
                        default='Promise to help them with their struggles')]

            #Retrieves answer
            self.answers = inquirer.prompt(q)
            self.allygather = self.answers['allygather']

            if self.allygather == 'Promise to help them with their struggles':
                print("The villagers are not happy with your promises. They are distrustful of those outside their community.")
                self.currentLevel = 19
            if self.allygather == 'Promise to make their hopes and dreams a reality':
                print("The villagers happy with your promises. They trust your intentions are pure and agree to fight with you.")
                self.currentLevel = 20
            if self.allygather == 'Leave the village':
                self.currentLevel = 21

            os.system('cls')
        
    def level8(self):
        print("""
        You decide to leave the village and continue your journey to gather allies.
        As you travel, you come across a group of knights who have pledged their allegiance to the king. They are willing to join your cause and help restore balance to the kingdom.
        """)
        knights_ascii()
        print("")

        q = [
            inquirer.List('join',
                    message='Will you join the knights?',
                    choices=['Yes', 'No'],
                    default='Yes')]

        self.answers = inquirer.prompt(q)
        self.join = self.answers['join']

        if self.join == 'Yes':
            print("You have gained the support of the knights.")
            self.currentLevel = 22
        elif self.join == 'No':
            print("You have refused the knights' offer of support.")
            self.currentLevel = 23

        os.system('cls')

    def level9(self):
        print("""
        With the support of the lords and ladies, you feel more confident in your mission.
        You make your way to the castle and request an audience with the king.
        The king listens to your proposal and agrees to help restore balance to the kingdom.
        """)
        king_ascii()
        print("")

        q = [
            inquirer.List('nextmove',
                    message='What will you do next?',
                    choices=['Gather an army', 'Begin negotiations with the Church', 'Focus on economic reform'],
                    default='Gather an army')]

        self.answers = inquirer.prompt(q)
        self.nextmove = self.answers['nextmove']

        if self.nextmove == 'Gather an army':
            self.currentLevel = 24
        if self.nextmove == 'Begin negotiations with the Church':
            self.currentLevel = 25
        if self.nextmove == 'Focus on economic reform':
            self.currentLevel = 26

        os.system('cls')

    def level10(self):
        print("""
        The lords and ladies have refused to support you in your mission to restore balance to the kingdom.
        You are left to ponder your next move, as you realize that gaining support from the local nobility may be more difficult than you thought.
        """)

        q = [
            inquirer.List('nextmove',
                    message='What will you do next?',
                    choices=['Look for alternative allies', 'Reassess your approach', 'Give up and return home'],
                    default='Look for alternative allies')]

        self.answers = inquirer.prompt(q)
        self.nextmove = self.answers['nextmove']

        if self.nextmove == 'Look for alternative allies':
            self.currentLevel = 27
        if self.nextmove == 'Reassess your approach':
            self.currentLevel = 28
        if self.nextmove == 'Give up and return home':
            self.currentLevel = 29

        os.system('cls')

    def level11(self):
        print("""
        You have learned from the merchants that the Church has been exerting too much power and control over the kingdom.
        As you ponder on what to do next, you realize that you must act quickly before the Church's influence becomes too great.
        """)
        church_ascii()
        print("")

        q = [
            inquirer.List('church',
                    message='What will you do?',
                    choices=['Investigate the Church', 'Speak with the king', 'Start a resistance'],
                    default='Investigate the Church')]

        #Retrieves answer
        self.answers = inquirer.prompt(q)
        self.church = self.answers['church']

        if self.church == 'Investigate the Church':
            self.currentLevel = 30
        if self.church == 'Speak with the king':
            self.currentLevel = 31
        if self.church == 'Start a resistance':
            self.currentLevel = 32

        os.system('cls')

    def level12(self):
        print("""
        You have learned that the king is becoming increasingly unpopular among the people.
        You decide to investigate further and gather more information about why this is happening.
        As you make your way through the kingdom, you come across a group of commoners who are discussing their grievances with the king.
        """)
        commoners_ascii()
        print("")

        q = [
            inquirer.List('grievances',
                    message='What do the commoners tell you?',
                    choices=['The king has been raising taxes', 'The king has been neglecting the needs of the people', 'The king has been making unpopular decisions'],
                    default='The king has been raising taxes')]

        self.answers = inquirer.prompt(q)
        self.grievances = self.answers['grievances']

        if self.grievances == 'The king has been raising taxes':
            self.currentLevel = 33
        if self.grievances == 'The king has been neglecting the needs of the people':
            self.currentLevel = 34
        if self.grievances == 'The king has been making unpopular decisions':
            self.currentLevel = 35

        os.system('cls')

    def level13(self):
        print("""
        You have learned that the kingdom is facing economic troubles.
        You decide to investigate and gather more information on the financial state of the kingdom.
        You visit the royal treasury and speak to the royal treasurer to gain a better understanding of the kingdom's finances.
        """)
        treasury_ascii()
        print("")

        q = [
            inquirer.List('treasury',
                    message='What do you learn from the royal treasurer?',
                    choices=['The kingdom is heavily in debt', 'The kingdom\'s resources are being mismanaged', 'The kingdom\'s taxes are too high'],
                    default='The kingdom is heavily in debt')]

        #Retrieves answer
        self.answers = inquirer.prompt(q)
        self.treasury = self.answers['treasury']

        if self.treasury == 'The kingdom is heavily in debt':
            self.currentLevel = 36
        if self.treasury == 'The kingdom\'s resources are being mismanaged':
            self.currentLevel = 37
        if self.treasury == 'The kingdom\'s taxes are too high':
            self.currentLevel = 38

        os.system('cls')

    def level14(self):
        print("""
        You have offered your services as a soldier for the Church.
        The guard takes you to the Church's military leader, who thanks you for your willingness to fight for their cause.
        They give you a choice of missions to undertake, all of which are important to the Church's goals.
        """)
        priest_ascii()
        print("")

        q = [
            inquirer.List('mission',
                    message='Which mission will you choose?',
                    choices=['Protect a holy relic on a pilgrimage', 'Fight against a rival religious sect', 'Assist in the construction of a new cathedral'],
                    default='Protect a holy relic on a pilgrimage')]

        #Retrieves answer
        self.answers = inquirer.prompt(q)
        self.mission = self.answers['mission']

        if self.mission == 'Protect a holy relic on a pilgrimage':
            self.currentLevel = 39
        if self.mission == 'Fight against a rival religious sect':
            self.currentLevel = 40
        if self.mission == 'Assist in the construction of a new cathedral':
            self.currentLevel = 41

        os.system('cls')

    def level15(self):
        print("""
        You have decided to join the Church's clergy.
        As you begin your training, you are tasked with performing various duties such as preaching to the congregation, administering sacraments, and providing spiritual guidance.
        """)
        church2_ascii()
        print("")

        q = [
            inquirer.List('duties',
                    message='What will you focus on?',
                    choices=['Preaching and teaching', 'Providing spiritual guidance', 'Administering sacraments'],
                    default='Preaching and teaching')]

        self.answers = inquirer.prompt(q)
        self.duties = self.answers['duties']

        if self.duties == 'Preaching and teaching':
            print("You spend your days preaching and teaching the word of God to the congregation.")
        elif self.duties == 'Providing spiritual guidance':
            print("You spend your days providing spiritual guidance to those in need.")
        elif self.duties == 'Administering sacraments':
                print("You spend your days administering sacraments to members of the congregation.")
        self.currentLevel = 45
            
        os.system('cls')

    def level16(self):
        print("""
        You have decided to make a donation to the Church.
        You make a generous donation and receive a blessing from the Church's leaders.
        """)
        church3_ascii()
        print("")

        q = [
            inquirer.List('contribution',
                    message='What will you do next?',
                    choices=['Make another donation', 'Leave the Church', 'Find a way to increase your influence within the Church'],
                    default='Make another donation')]

        self.answers = inquirer.prompt(q)
        self.contribution = self.answers['contribution']

        if self.contribution == 'Make another donation':
            self.currentLevel = 42
        if self.contribution == 'Leave the Church':
            self.currentLevel = 43
        if self.contribution == 'Find a way to increase your influence within the Church':
            self.currentLevel = 44

        os.system('cls')

    def level17(self):
        print("""
        With the support of the village leader, you continue to gather allies and gain support from other towns and villages in the kingdom.
        You also begin to build a reputation as a leader and a force for good among the people.
        As you continue your journey, you come across a group of knights who are also looking to restore balance to the kingdom.
        """)
        knights_ascii()
        print("")

        q = [
            inquirer.List('knights',
            message='Will the knights join your cause?',
            choices=['Yes, the knights agree to join your cause.', 'No, the knights cannot join your cause.'],
                default='Yes, the knights agree to join your cause.')]

        self.answers = inquirer.prompt(q)
        self.knights = self.answers['knights']

        if self.knights == 'Yes, the knights agree to join your cause.':
            print("The knights have agreed to join your cause and support you in your mission.")
            self.currentLevel = 22
        elif self.knights == 'No, the knights cannot join your cause.':
            print("The knights have refused to join your cause.")
            self.currentLevel = 23

    def level18(self):
        print("""
        The village leader refused to support you in your mission to restore balance to the kingdom.
        You are left to ponder your next move, as you realize that gaining support from the local townfolk may be more difficult than you thought.
        """)

        q = [
            inquirer.List('nextmove',
                    message='What will you do next?',
                    choices=['Look for alternative allies', 'Reassess your approach', 'Give up and return home'],
                    default='Look for alternative allies')]

        self.answers = inquirer.prompt(q)
        self.nextmove = self.answers['nextmove']

        if self.nextmove == 'Look for alternative allies':
            self.currentLevel = 27
        if self.nextmove == 'Reassess your approach':
            self.currentLevel = 28
        if self.nextmove == 'Give up and return home':
            self.currentLevel = 29

        os.system('cls')

    def level19(self):
        print("""
        Without the support of the villagers, you feel less confident in your mission.
        You make your way to the castle and request an audience with the king.
        The king listens to your proposal and is unhappy you were not able to gather allies for his cause.
        """)
        king_ascii()
        print("")

        q = [
            inquirer.List('nextmove',
                    message='What will you do next?',
                    choices=['Apologize to the king', 'Begin negotiations with the Church'],
                    default='Gather an army')]

        self.answers = inquirer.prompt(q)
        self.nextmove = self.answers['nextmove']

        if self.nextmove == 'Apologize to the king':
            self.currentLevel = 46
        if self.nextmove == 'Begin negotiations with the Church':
            self.currentLevel = 47

        os.system('cls')

    def level20(self):
        print("""
        With the support of the entire village, you feel more confident in your mission.
        You make your way to the castle and request an audience with the king.
        The king listens to your proposal and agrees to help restore balance to the kingdom.
        """)
        king_ascii()
        print("")

        q = [
            inquirer.List('nextmove',
                    message='What will you do next?',
                    choices=['Gather an army', 'Begin negotiations with the Church', 'Focus on economic reform'],
                    default='Gather an army')]

        self.answers = inquirer.prompt(q)
        self.nextmove = self.answers['nextmove']

        if self.nextmove == 'Gather an army':
            self.currentLevel = 24
        if self.nextmove == 'Begin negotiations with the Church':
            self.currentLevel = 25
        if self.nextmove == 'Focus on economic reform':
            self.currentLevel = 26

        os.system('cls')

    def level21(self):
        print("""
        You decide to leave the village and continue your journey to gather allies.
        As you travel, you come across a group of knights who have pledged their allegiance to the king. They are willing to join your cause and help restore balance to the kingdom.
        """)
        knights_ascii()
        print("")

        q = [
            inquirer.List('join',
                    message='Will you join the knights?',
                    choices=['Yes', 'No'],
                    default='Yes')]

        self.answers = inquirer.prompt(q)
        self.join = self.answers['join']

        if self.join == 'Yes':
            print("You have gained the support of the knights.")
            self.currentLevel = 22
        elif self.join == 'No':
            print("You have refused the knights' offer of support.")
            self.currentLevel = 23

        os.system('cls')

    def level22(self):
        print("You are in level 22")

    def level23(self):
        print("You are in level 23")

    def level24(self):
        print("You are in level 24")

    def level25(self):
        print("You are in level 25")

    def level26(self):
        print("You are in level 26")

    def level27(self):
        print("You are in level 22")

    def level28(self):
        print("You are in level 23")

    def level29(self):
        print("You are in level 24")

    def level30(self):
        print("You are in level 25")

    def level31(self):
        print("You are in level 26")

    def level32(self):
        print("You are in level 22")

    def level33(self):
        print("You are in level 23")

    def level34(self):
        print("You are in level 24")

    def level35(self):
        print("You are in level 25")

    def level36(self):
        print("You are in level 23")

    def level37(self):
        print("You are in level 24")

    def level38(self):
        print("You are in level 25")

    def level34(self):
        print("You are in level 24")

    def level35(self):
        print("You are in level 25")

    def level36(self):
        print("You are in level 23")

    def level37(self):
        print("You are in level 24")

    def level38(self):
        print("You are in level 25")

    def level39(self):
        print("You are in level 24")

    def level40(self):
        print("You are in level 25")

    def level41(self):
        print("You are in level 23")

    def level42(self):
        print("You are in level 24")

    def level43(self):
        print("You are in level 25")

    def level44(self):
        print("You are in level 24")

    def level45(self):
        print("You are in level 25")

    def level46(self):
        print("You are in level 23")

    def level47(self):
        print("You are in level 24")

    def level48(self):
        print("You are in level 25")

    def level49(self):
        print("You are in level 24")

    def level50(self):
        print("You are in level 25")

g = Game()
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
        self.currentLevel = 1
        #Game Loop
        while True:
            self.gameLevels()
            if self.gameOver == True:
                break

    def intro(self):
        print("""
        Welcome to the kingdom of Camelot, a land of great beauty and prosperity. However, the kingdom is facing a great challenge as the balance of power between the king and the Church has become unstable. The Church has grown too powerful and has started to interfere with the king's rule.
        The king has called upon all able-bodied men to help restore the balance of power and bring peace to the kingdom. As a young squire, you are duty-bound to answer the call and defend your kingdom.
        """)
        knight_ascii()
        print("")

        print("But before you set out on your journey, you must make a decision:")

        q = [
        inquirer.List('startgame',
                message='Which path will you choose?',
                choices=['Pledge allegiance to the king', 'Join the Church'],
                default='Pledge allegiance to the king')]

        self.answers = inquirer.prompt(q)
        self.startgame = self.answers['startgame']

        if self.startgame == 'Pledge allegiance to the king':
            os.system('cls')
            self.currentLevel = 1
        elif self.startgame == 'Join the Church':
            os.system('cls')
            self.currentLevel = 5

    def gameLevels(self):
        level_functions = [self.level1, self.level2, self.level3, self.level4, self.level5, self.level6, self.level7, self.level8, self.level9, self.level10, self.level11, self.level12, self.level13, self.level14, self.level15, self.level16, self.level17, self.level18, self.level19, self.level20, self.level21, self.level22, self.level23, self.level24, self.level25]
        if self.currentLevel > 0 and self.currentLevel <= 25:
            level_functions[self.currentLevel - 1]()
        if self.currentLevel == 25:
            self.gameOver = True

    def level1(self):
        print("""
        You have arrived at the neighboring kingdom of Logres, where you hope to gain the support of King Leodegrance.
        However, upon arriving, you are informed that the king is away on a hunting trip and the kingdom is facing a severe drought.
        You must make a decision on how to proceed.
        """)

        print("""
        - Attempt to sneak into Logres and gather intel on King Leodegrance's stance.
        - Send a diplomatic envoy to negotiate with Sir Kay for aid.
        - Send an army to conquer Logres and force their support.
        """)
        
        castle_ascii()
        print("")

        q = [
        inquirer.List('level_one',
        message='What will you do?',
        choices=['Sneak into Logres', 'Send a diplomatic envoy', 'Send an army'],
        default='Sneak into Logres')]

        self.answers = inquirer.prompt(q)
        self.level_one = self.answers['level_one']

        if self.level_one == 'Sneak into Logres':
            os.system('cls')
            self.currentLevel = 2
        elif self.level_one == 'Send a diplomatic envoy':
            os.system('cls')
            self.currentLevel = 3
        elif self.level_one == 'Send an army':
            os.system('cls')
            self.currentLevel = 4

    def level2(self):
        print("""
        You have successfully snuck into Logres and are now gathering intel on King Leodegrance's stance towards Camelot.
        You infiltrate the castle and overhear a conversation between Sir Kay and one of the king's advisors.
        They mention that King Leodegrance is considering an alliance with Camelot, but is hesitant due to the kingdom's current instability.
        """)

        print("""
        - Attempt to sway the advisor to support Camelot
        - Attempt to kidnap Sir Kay and use him as leverage
        - Leave Logres and report back to Camelot
        """)

        q = [
        inquirer.List('level2_sneak',
        message='What will you do?',
        choices=['Sway the advisor', 'Kidnap Sir Kay', 'Leave Logres'],
        default='Sway the advisor')]

        self.answers = inquirer.prompt(q)
        self.level2_sneak = self.answers['level2_sneak']

        if self.level2_sneak == 'Sway the advisor':
            os.system('cls')
            print("You successfully sway the advisor to support Camelot.")
            self.currentLevel = 6
        elif self.level2_sneak == 'Kidnap Sir Kay':
            os.system('cls')
            print("You attempt to kidnap Sir Kay, but the plan backfires and you are captured by Logres' guards.")
            self.currentLevel = 9
        elif self.level2_sneak == 'Leave Logres':
            os.system('cls')
            print("You leave Logres and report back to Camelot with the information you have gathered.")
            self.currentLevel = 10

    def level3(self):
        print("""
        You have sent a diplomatic envoy to negotiate with Sir Kay for aid.
        Sir Kay tells you that the kingdom of Logres is willing to offer aid to Camelot but in exchange for a favor.
        """)

        print("""
        - Agree to the favor and accept the aid
        - Refuse the favor and decline the aid
        """)

        q = [
        inquirer.List('level3_diplomatic',
        message='What will you do?',
        choices=['Agree to the favor', 'Refuse the favor'],
        default='Agree to the favor')]

        self.answers = inquirer.prompt(q)
        self.level3_diplomatic = self.answers['level3_diplomatic']

        if self.level3_diplomatic == 'Agree to the favor':
            print("You agree to the favor and accept the aid from Logres.")
            self.currentLevel = 11
        elif self.level3_diplomatic == 'Refuse the favor':
            print("You refuse the favor and decline the aid from Logres.")
            self.currentLevel = 12

        os.system('cls')

    def level4(self):
        print("""
        You have sent an army to conquer Logres and force their support.
        The battle is fierce and many lives are lost on both sides.
        """)

        print("""
        - Continue to fight and conquer Logres
        - Negotiate a surrender and spare lives
        - Retreat and regroup
        """)

        q = [
        inquirer.List('level4_conquer',
        message='What will you do?',
        choices=['Continue to fight', 'Negotiate a surrender', 'Retreat'],
        default='Continue to fight')]

        self.answers = inquirer.prompt(q)
        self.level4_conquer = self.answers['level4_conquer']

        if self.level4_conquer == 'Continue to fight':
            print("You continue to fight and eventually conquer Logres, gaining their support.")
            self.currentLevel = 13
        elif self.level4_conquer == 'Negotiate a surrender':
            print("You negotiate a surrender with Logres, sparing many lives but at the cost of losing the element of surprise.")
            self.currentLevel = 14
        elif self.level4_conquer == 'Retreat':
            print("You retreat and regroup, losing many lives but gaining valuable intel for the next battle.")
            self.currentLevel = 15

        os.system('cls')
        
    def level5(self):
        print("""
        You have joined the Church and fight for their cause.
        The Church has tasked you with recruiting new followers to increase their power within the kingdom.
        """)

        print("""
        - Recruit new followers by spreading the word of the Church through peaceful means.
        - Use force to convert non-believers to the Church's cause.
        """)
        new_pope_ascii()
        print("")

        q = [
        inquirer.List('level5_church',
        message='What will you do?',
        choices=['Peaceful recruitment', 'Use force'],
        default='Peaceful recruitment')]

        self.answers = inquirer.prompt(q)
        self.level5_church = self.answers['level5_church']

        if self.level5_church == 'Peaceful recruitment':
            print("You successfully recruit new followers to the Church through peaceful means.")
            self.currentLevel = 7
        elif self.level5_church == 'Use force':
            print("You use force to convert non-believers to the Church's cause, but it backfires and causes resentment among the people.")
            self.currentLevel = 8

        os.system('cls')

    def level6(self):
        print("""
        You have returned to Camelot with the information gathered from your adventure.
        The king is pleased with the progress you have made and has a new task for you.
        """)

        print("""
        - Train new soldiers to bolster Camelot's army
        - Strengthen alliances with neighboring kingdoms
        - Invest in new technologies and weapons
        """)

        q = [
        inquirer.List('level6',
        message='What will you do?',
        choices=['Train new soldiers', 'Strengthen alliances', 'Invest in new technologies'],
        default='Train new soldiers')]

        self.answers = inquirer.prompt(q)
        self.level6 = self.answers['level6']

        if self.level6 == 'Train new soldiers':
            os.system('cls')
            print("You begin training new soldiers to bolster Camelot's army.")
            self.currentLevel = 16
        elif self.level6 == 'Strengthen alliances':
            os.system('cls')
            print("You begin strengthening alliances with neighboring kingdoms.")
            self.currentLevel = 17
        elif self.level6 == 'Invest in new technologies':
            os.system('cls')
            print("You begin investing in new technologies and weapons.")
            self.currentLevel = 18

    def level7(self):
        pass
    def level8(self):
        pass
    def level9(self):
        pass
    def level10(self):
        pass
    def level11(self):
        pass
    def level12(self):
        pass
    def level13(self):
        pass
    def level14(self):
        pass
    def level15(self):
        pass
    def level16(self):
        pass
    def level17(self):
        pass
    def level18(self):
        pass
    def level19(self):
        pass
    def level20(self):
        pass
    def level21(self):
        pass
    def level22(self):
        pass
    def level23(self):
        pass
    def level24(self):
        pass
    def level25(self):
        pass

g = Game()
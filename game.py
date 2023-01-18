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
        self.score = 0
        self.intro()
        #Game settings
        self.gameOver = False
        #Game Loop
        while True:
            self.gameLevels()
            if self.gameOver == True:
                self.gameOverScreen()
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
            self.currentLevel = 1
        if self.startgame == 'Join the Church':
            self.currentLevel = 5

        os.system('cls')

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
            self.score += 1
            self.currentLevel = 2
        elif self.level_one == 'Send a diplomatic envoy':
            self.score += 2
            self.currentLevel = 3
        elif self.level_one == 'Send an army':
            self.score -= 5
            self.currentLevel = 4

        os.system('cls')

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

        castle2_ascii()
        print("")

        q = [
        inquirer.List('level2_sneak',
        message='What will you do?',
        choices=['Sway the advisor', 'Kidnap Sir Kay', 'Leave Logres'],
        default='Sway the advisor')]

        self.answers = inquirer.prompt(q)
        self.level2_sneak = self.answers['level2_sneak']

        if self.level2_sneak == 'Sway the advisor':
            print("You successfully sway the advisor to support Camelot.")
            self.score += 2
            self.currentLevel = 6
        elif self.level2_sneak == 'Kidnap Sir Kay':
            print("You attempt to kidnap Sir Kay, but the plan backfires and you are captured by Logres' guards.")
            self.score -= 2
            self.currentLevel = 9
        elif self.level2_sneak == 'Leave Logres':
            print("You leave Logres and report back to Camelot with the information you have gathered.")
            self.score += 1
            self.currentLevel = 10

        os.system('cls')

    def level3(self):
        print("""
        You have sent a diplomatic envoy to negotiate with Sir Kay for aid.
        Sir Kay tells you that the kingdom of Logres is willing to offer aid to Camelot but in exchange for a favor.
        """)

        print("""
        - Agree to the favor and accept the aid
        - Refuse the favor and decline the aid
        """)

        knights_ascii()
        print("")

        q = [
        inquirer.List('level3_diplomatic',
        message='What will you do?',
        choices=['Agree to the favor', 'Refuse the favor'],
        default='Agree to the favor')]

        self.answers = inquirer.prompt(q)
        self.level3_diplomatic = self.answers['level3_diplomatic']

        if self.level3_diplomatic == 'Agree to the favor':
            print("You agree to the favor and accept the aid from Logres.")
            self.score += 2
            self.currentLevel = 11
        elif self.level3_diplomatic == 'Refuse the favor':
            print("You refuse the favor and decline the aid from Logres.")
            self.score += 1
            self.currentLevel = 12

        os.system('cls')

    def level4(self):
        print("""Th
        You have sent an army to conquer Logres and force their support.
        The battle is fierce and many lives are lost on both sides.
        """)

        print("""
        - Continue to fight and conquer Logres
        - Negotiate a surrender and spare lives
        - Retreat and regroup
        """)

        army_ascii()
        print("")

        q = [
        inquirer.List('level4_conquer',
        message='What will you do?',
        choices=['Continue to fight', 'Negotiate a surrender', 'Retreat'],
        default='Continue to fight')]

        self.answers = inquirer.prompt(q)
        self.level4_conquer = self.answers['level4_conquer']

        if self.level4_conquer == 'Continue to fight':
            print("You continue to fight and eventually conquer Logres, gaining their support.")
            self.score += 1
            self.currentLevel = 13
        elif self.level4_conquer == 'Negotiate a surrender':
            print("You negotiate a surrender with Logres, sparing many lives but at the cost of losing the element of surprise.")
            self.score -= 2
            self.currentLevel = 14
        elif self.level4_conquer == 'Retreat':
            print("You retreat and regroup, losing many lives but gaining valuable intel for the next battle.")
            self.score -= 5
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
            self.score += 2
            self.currentLevel = 7
        elif self.level5_church == 'Use force':
            print("You use force to convert non-believers to the Church's cause, but it backfires and causes resentment among the people.")
            self.score -= 3
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

        king_ascii()
        print("")

        q = [
        inquirer.List('level6',
        message='What will you do?',
        choices=['Train new soldiers', 'Strengthen alliances', 'Invest in new technologies'],
        default='Train new soldiers')]

        self.answers = inquirer.prompt(q)
        self.level6 = self.answers['level6']

        if self.level6 == 'Train new soldiers':
            print("You begin training new soldiers to bolster Camelot's army.")
            self.score += 1
            self.currentLevel = 16
        elif self.level6 == 'Strengthen alliances':
            print("You begin strengthening alliances with neighboring kingdoms.")
            self.score += 2
            self.currentLevel = 17
        elif self.level6 == 'Invest in new technologies':
            print("You begin investing in new technologies and weapons.")
            self.score += 1
            self.currentLevel = 18

        os.system('cls')

    def level7(self):
        print("""
        You have begun spreading the word of the Church and gaining followers through peaceful means.
        You've traveled to different towns and villages, speaking to the people and offering them aid and guidance.
        Your efforts are paying off, and more and more people are joining the Church.
        """)

        print("""
        - Build a new church in a nearby town
        - Send missionaries to distant lands to spread the word of the Church
        - Focus on providing aid to the poor and needy in your current location
        """)

        church_ascii()
        print("")

        q = [
        inquirer.List('level_seven',
        message='What will you do?',
        choices=['Build a new church', 'Send missionaries', 'Focus on aid'],
        default='Focus on aid')]

        self.answers = inquirer.prompt(q)
        self.level_seven = self.answers['level_seven']

        if self.level_seven == 'Build a new church':
            self.score += 2
            self.currentLevel = 19
        elif self.level_seven == 'Send missionaries':
            self.score += 1
            self.currentLevel = 20
        elif self.level_seven == 'Focus on aid':
            self.score += 2
            self.currentLevel = 21

        os.system('cls')

    def level8(self):
        print("""
        You lead a group of followers to a nearby village to convert non-believers to the Church's cause.
        However, your methods of persuasion are violent and the villagers resist.
        The village becomes resentful towards the Church and word of your actions spread to nearby towns.
        """)

        village2_ascii()
        print("")

        print("""
        - Apologize to the village and attempt to make amends.
        - Double down on your methods and continue to force conversions.
        - Leave the village and focus on recruiting in other areas.
        """)

        q = [
        inquirer.List('level8',
        message='What will you do?',
        choices=['Apologize and make amends', 'Double down on methods', 'Leave the village'],
        default='Apologize and make amends')]

        self.answers = inquirer.prompt(q)
        self.level8 = self.answers['level8']

        if self.level8 == 'Apologize and make amends':
            self.score += 1
            self.currentLevel = 22
        elif self.level8 == 'Double down on methods':
            self.score -= 5
            self.currentLevel = 23
        elif self.level8 == 'Leave the village':
            self.score -= 1
            self.currentLevel = 24

        os.system('cls')

    def level9_negotiate_apology(self):
        print("You apologize for your actions and offer to help Logres with their drought crisis.")
        print("King Leodegrance and Sir Kay, impressed by your willingness to make amends, agree to an alliance with Camelot.")
        print("However, in return, they demand that Camelot provides aid to Logres to help with the drought crisis.")
        self.currentLevel = 6

    def level9_negotiate_threat(self):
        print("You threaten to reveal Sir Kay's secret plans to other kingdoms if they don't ally with Camelot.")
        print("Sir Kay, fearing the potential backlash, agrees to an alliance with Camelot.")
        print("However, your reputation and relations with Sir Kay are damaged and may cause tension within Camelot.")
        self.currentLevel = 6

    def level9_negotiate_charm(self):
        print("You use your charm and wit to try and sway King Leodegrance and Sir Kay to your side.")
        print("Your efforts are successful and they both agree to an alliance with Camelot without any major concessions.")
        print("However, your charisma and reputation may be affected in the long run.")
        self.currentLevel = 6

    def level9_fate(self):
        print("""
        After your failed attempt to kidnap Sir Kay, you are captured by Logres' guards and brought before King Leodegrance.
        The king is furious at your actions and sentences you to life in prison.
        """)

        print("""
        - Attempt to escape from prison
        - Negotiate with the king for leniency
        - Accept your fate and serve your sentence
        """)
        
        q = [
        inquirer.List('level9_fate',
        message='What will you do?',
        choices=['Escape', 'Negotiate', 'Accept fate'],
        default='Escape')]

        self.answers = inquirer.prompt(q)
        self.level9_fate = self.answers['level9_fate']

        if self.level9_fate == 'Escape':
            self.score += 1
            self.level9_escape()
        elif self.level9_fate == 'Negotiate':
            self.score += 1
            self.level9_negotiate()
        elif self.level9_fate == 'Accept fate':
            self.gameOver = True
            print("You accept your fate and spend the rest of your days in prison.")

        os.system('cls')

    def level9_negotiate(self):
        print("""
        You are brought before King Leodegrance and Sir Kay, who are both furious at your attempted kidnapping.
        However, you are given the opportunity to plead your case and negotiate for a potential alliance.
        """)

        print("""
        - Apologize for your actions and offer to help Logres with their drought crisis.
        - Threaten to reveal Sir Kay's secret plans to other kingdoms if they don't ally with Camelot.
        - Use your charm and wit to try and sway the king and Sir Kay to your side.
        """)

        q = [
        inquirer.List('negotiate',
        message='What will you do?',
        choices=['Apologize and offer help', 'Threaten Sir Kay', 'Use charm and wit'],
        default='Apologize and offer help')]

        self.answers = inquirer.prompt(q)
        self.negotiate = self.answers['negotiate']

        if self.negotiate == 'Apologize and offer help':
            self.score += 1
            self.level9_negotiate_apology()
        elif self.negotiate == 'Threaten Sir Kay':
            self.score -= 2
            self.level9_negotiate_threat()
        elif self.negotiate == 'Use charm and wit':
            self.score += 2
            self.level9_negotiate_charm()

        os.system('cls')

    def level9_escape(self):
        print("You manage to escape from your captors and return to Camelot, where you report the failure of your mission to the king.")
        q = [
        inquirer.List('level9_escape',
        message='What will you do next?',
        choices=['Try to negotiate with Logres again', 'Prepare for war', 'Abandon the mission'],
        default='Try to negotiate with Logres again')]
        self.answers = inquirer.prompt(q)
        self.level9_escape = self.answers['level9_escape']

        if self.level9_escape == 'Try to negotiate with Logres again':
            self.score += 1
            self.currentLevel = 3
        elif self.level9_escape == 'Prepare for war':
            self.score -= 2
            self.currentLevel = 17
        elif self.level9_escape == 'Abandon the mission':
            self.gameOver = True
            print("You abandon your mission and spend the rest of your days watching Camelot crumble at the sidelines.")

        os.system('cls')

    def level9(self):
        print("""
        Your plan to kidnap Sir Kay has failed and you have been captured by Logres' guards.
        You are thrown into the kingdom's dungeon and are left to rot.
        As you sit in your cell, you begin to regret your decision and realize the error of your ways.
        """)

        print("""
        - Attempt to escape from the dungeon
        - Attempt to negotiate with the guards for your release
        - Accept your fate and await execution
        """)

        warriors_ascii()
        print("")

        q = [
        inquirer.List('level9_kidnap',
        message='What will you do?',
        choices=['Attempt to escape', 'Negotiate for release', 'Accept fate'],
        default='Attempt to escape')]

        self.answers = inquirer.prompt(q)
        self.level9_kidnap = self.answers['level9_kidnap']

        if self.level9_kidnap == 'Attempt to escape':
            self.score += 1
            self.level9_escape()
        elif self.level9_kidnap == 'Negotiate for release':
            self.score += 2
            self.level9_negotiate()
        elif self.level9_kidnap == 'Accept fate':
            self.level9_fate()

        os.system('cls')

    def level10(self):
        print("""
        You have returned to Camelot and reported to the king about your findings in Logres. The king thanks you for your efforts and asks for your suggestions on how to proceed with forming alliances with other kingdoms.
        """)
        print("""
        - Offer aid to other kingdoms in exchange for their alliance.
        - Use leverage and threats to form alliances.
        - Use diplomatic means to form alliances.
        """)

        throne_ascii()
        print("")

        q = [
        inquirer.List('alliances',
        message='What will you do?',
        choices=['Offer aid', 'Use leverage', 'Use diplomatic means'],
        default='Use diplomatic means')]

        self.answers = inquirer.prompt(q)
        self.alliances = self.answers['alliances']

        if self.alliances == 'Offer aid':
            print("You offer aid to other kingdoms in exchange for their alliance.")
            print("This helps to alleviate some of the kingdom's crisis but also costs resources.")
            self.score += 1
            self.currentLevel = 11
        elif self.alliances == 'Use leverage':
            print("You use leverage and threats to form alliances.")
            print("This can be effective in the short term, but it damages your reputation and may cause tension within Camelot.")
            self.score += 2
            self.afterLevel10()
        elif self.alliances == 'Use diplomatic means':
            print("You use diplomatic means to form alliances.")
            print("This is a slower process, but it doesn't cost as much in resources or reputation.")
            self.score -= 5
            self.afterLevel10()

        os.system('cls')
        
    def afterLevel10(self):
        print("""
        Your diplomatic efforts have paid off and several kingdoms have agreed to form alliances with Camelot. However, just as you are about to celebrate your success, a messenger arrives with dire news. 
        Logres, one of the kingdoms you had formed an alliance with, is under attack by a powerful enemy kingdom. They are requesting Camelot's aid in their war.
        """)
        print("""
        - Send a small group of soldiers to aid Logres in their war.
        - Send a large army to aid Logres in their war.
        - Refuse to aid Logres in their war and focus on defending Camelot.
        """)

        castle2_ascii()
        print("")

        q = [
        inquirer.List('logres',
        message='What will you do?',
        choices=['Send a small group of soldiers', 'Send a large army', 'Refuse to aid'],
        default='Send a small group of soldiers')]

        self.answers = inquirer.prompt(q)
        self.logres = self.answers['logres']

        if self.logres == 'Send a small group of soldiers':
            self.score += 2
            self.afterLevel11()
            print("You send a small group of soldiers to aid Logres in their war.")
            print("This will help Logres but may not be enough to defeat their enemy.")
        elif self.logres == 'Send a large army':
            self.score += 1
            self.afterLevel11()
            print("You send a large army to aid Logres in their war.")
            print("This will greatly aid Logres in their war but will also leave Camelot vulnerable.")
        elif self.logres == 'Refuse to aid':
            self.score -= 5
            self.currentLevel = 12
            print("You refuse to aid Logres in their war and focus on defending Camelot.")
            print("This will keep Camelot safe but may damage relationships with other kingdoms.")

        os.system('cls')

    def level11(self):
        print("""
        You have agreed to a favor from Logres and have accepted their aid for Camelot. 
        Sir Kay informs you that the favor required is for Camelot to aid Logres in their war against a neighboring kingdom.
        """)

        print("""
        - Send a small group of soldiers to aid Logres in their war.
        - Send a large army to aid Logres in their war.
        - Refuse to aid Logres in their war.
        """)

        army_ascii()
        print("")

        q = [
        inquirer.List('favor',
        message='What will you do?',
        choices=['Send a small group of soldiers', 'Send a large army', 'Refuse to aid'],
        default='Send a small group of soldiers')]

        self.answers = inquirer.prompt(q)
        self.favor = self.answers['favor']

        if self.favor == 'Send a small group of soldiers':
            os.system('cls')
            self.score += 2
            self.afterLevel11()
        elif self.favor == 'Send a large army':
            os.system('cls')
            self.afterLevel11()
            self.currentLevel += 1
        elif self.favor == 'Refuse to aid':
            os.system('cls')
            print("You refuse to aid Logres in their war and focus on defending Camelot.")
            print("This will keep Camelot safe but may damage relationships with other kingdoms.")
            self.score -= 5
            self.currentLevel = 12

    def afterLevel11(self):
        print("""
        You send a group of soldiers to aid Logres in their war.
        As the battle rages on, you receive reports that the neighboring kingdom has strengthened their army and reinforcements are needed.
        """)
        print("""
        - Send more soldiers to aid Logres
        - Attempt to negotiate a ceasefire
        - Withdraw Camelot's army and focus on defending Camelot
        """)

        q = [
        inquirer.List('level16',
        message='What will you do?',
        choices=['Send more soldiers', 'Negotiate a ceasefire', 'Withdraw Camelot\'s army'],
        default='Send more soldiers')]

        self.answers = inquirer.prompt(q)
        self.level16 = self.answers['level16']

        if self.level16 == 'Send more soldiers':
            print("You send more soldiers to aid Logres.")
            print("This increases the chances of victory but also puts more of Camelot's soldiers at risk.")
            self.score += 1
            self.currentLevel = 16
        elif self.level16 == 'Negotiate a ceasefire':
            print("You attempt to negotiate a ceasefire with the neighboring kingdom.")
            print("This may lead to a peaceful resolution but also prolongs the war.")
            self.score -= 2
            self.gameOver = True
        elif self.level16 == 'Withdraw Camelot\'s army':
            print("You withdraw Camelot's army and focus on defending Camelot.")
            print("This keeps Camelot's soldiers safe but also may result in the loss of the war for Logres.")
            self.score -= 3
            self.currentLevel = 15

    def level12(self):
        print("""
        You have refused the favor from Logres and have declined their aid for Camelot. 
        Sir Kay informs you that the favor required was for Camelot to aid Logres in their war against a neighboring kingdom.
        """)

        print("""
        - Attempt to negotiate a different favor with Logres
        - Prepare for war with Logres
        - Seek aid from another kingdom
        """)

        battle_ascii()
        print("")

        q = [
        inquirer.List('favor',
        message='What will you do?',
        choices=['Negotiate a different favor', 'Prepare for war', 'Seek aid from another kingdom'],
        default='Negotiate a different favor')]

        self.answers = inquirer.prompt(q)
        self.favor = self.answers['favor']

        if self.favor == 'Negotiate a different favor':
            os.system('cls')
            print("You attempt to negotiate a different favor with Logres.")
            self.score += 1
            self.currentLevel += 1
        elif self.favor == 'Prepare for war':
            os.system('cls')
            print("You prepare for war with Logres.")
            self.score -= 5
            self.currentLevel += 1
        elif self.favor == 'Seek aid from another kingdom':
            os.system('cls')
            print("You seek aid from another kingdom.")
            self.score += 2
            self.currentLevel += 1

    def level13(self):
        print("""
        Your army has successfully conquered Logres and gained their support.
        However, the war has left the kingdom in shambles and many of the people are suffering.
        """)

        print("""
        - Send aid and resources to help rebuild Logres
        - Enforce strict rule and control over Logres to maintain order
        - Allow Logres to govern themselves, but with Camelot's oversight
        """)

        victory_ascii()
        print("")

        q = [
        inquirer.List('level13',
        message='What will you do?',
        choices=['Send aid and resources', 'Enforce strict rule', 'Allow self-governance'],
        default='Send aid and resources')]

        self.answers = inquirer.prompt(q)
        self.level13 = self.answers['level13']

        if self.level13 == 'Send aid and resources':
            print("You send aid and resources to help rebuild Logres, gaining the support and gratitude of the people.")
            self.score += 2
            self.currentLevel += 1
        elif self.level13 == 'Enforce strict rule':
            print("You enforce strict rule and control over Logres, maintaining order but also causing resentment among the people.")
            self.score += 1
            self.currentLevel += 1
        elif self.level13 == 'Allow self-governance':
            print("You allow Logres to govern themselves, but with Camelot's oversight. This helps maintain stability and good relations.")
            self.score += 3
            self.currentLevel += 1

        os.system('cls')

    def level14(self):
        print("""
        You have successfully negotiated a surrender with Logres, sparing many lives but at the cost of losing the element of surprise.
        Sir Kay is impressed with your diplomatic skills and offers to form an alliance with Camelot.
        """)

        print("""
        - Accept the alliance and work towards a peaceful resolution
        - Refuse the alliance and continue to push for a victory
        - Attempt to negotiate better terms for the alliance
        """)

        advisors_ascii()
        print("")

        q = [
        inquirer.List('level14_surrender',
        message='What will you do?',
        choices=['Accept alliance', 'Refuse alliance', 'Negotiate better terms'],
        default='Accept alliance')]

        self.answers = inquirer.prompt(q)
        self.level14_surrender = self.answers['level14_surrender']

        if self.level14_surrender == 'Accept alliance':
            print("You accept the alliance and work towards a peaceful resolution with Logres.")
            self.score += 1
            self.gameOver = True
        elif self.level14_surrender == 'Refuse alliance':
            print("You refuse the alliance and continue to push for a victory, potentially leading to more deaths.")
            self.score -= 2
            self.gameOver = True
        elif self.level14_surrender == 'Negotiate better terms':
            print("You attempt to negotiate better terms for the alliance with Logres.")
            self.score += 1
            self.gameOver = True

        os.system('cls')

    def level15(self):
        print("""
        You retreat and regroup, losing many lives but gaining valuable intel for the next battle.
        You regroup your army and devise a new strategy for the next battle.
        """)
        print("""
        - Use the intel gained from the retreat to launch a surprise attack on Logres
        - Negotiate with Logres for a peaceful resolution
        - Attempt to ally with another kingdom to defeat Logres together
        """)

        army_ascii()
        print("")

        q = [
        inquirer.List('level15',
        message='What will you do?',
        choices=['Launch a surprise attack', 'Negotiate', 'Ally with another kingdom'],
        default='Launch a surprise attack')]

        self.answers = inquirer.prompt(q)
        self.level15 = self.answers['level15']

        if self.level15 == 'Launch a surprise attack':
            print("You use the intel gained from the retreat to launch a surprise attack on Logres.")
            print("This can be risky but may lead to a quick victory if successful.")
            self.score += 2
            self.currentLevel = 17
        elif self.level15 == 'Negotiate':
            print("You negotiate with Logres for a peaceful resolution.")
            print("This is a slower process but can lead to a more lasting peace.")
            self.score -= 1
            self.gameOver = True
        elif self.level15 == 'Ally with another kingdom':
            print("You attempt to ally with another kingdom to defeat Logres together.")
            print("This can be a good strategy as it lessens the burden of the war on Camelot, but it also means giving up some control and potentially sharing the spoils of victory.")
            self.score += 1
            self.gameOver = True

        os.system('cls')

    def level16(self):
        print("""
        Your efforts to train new soldiers have paid off. Camelot's army is now stronger and better prepared for battle.
        """)
        print("""
        - Launch a surprise attack on Logres, using your newly trained soldiers
        - Continue to negotiate for a peaceful resolution
        - Attempt to ally with another kingdom to defeat Logres together
        """)

        battle_ascii()
        print("")

        q = [
        inquirer.List('level16',
        message='What will you do?',
        choices=['Launch a surprise attack', 'Negotiate', 'Ally with another kingdom'],
        default='Launch a surprise attack')]

        self.answers = inquirer.prompt(q)
        self.level16 = self.answers['level16']

        if self.level16 == 'Launch a surprise attack':
            print("You use the newly trained soldiers to launch a surprise attack on Logres.")
            print("This can be risky but may lead to a quick victory if successful.")
            self.score += 2
            self.currentLevel = 17
        elif self.level16 == 'Negotiate':
            print("You continue to negotiate for a peaceful resolution with Logres.")
            print("This is a slower process but can lead to a more lasting peace.")
            self.score -= 1
            self.gameOver = True
        elif self.level16 == 'Ally with another kingdom':
            print("You attempt to ally with another kingdom to defeat Logres together.")
            print("This can be a strong strategy, but it may take time to secure the alliance.")
            self.score += 1
            self.gameOver = True

        os.system('cls')

    def level17(self):
        print("""
        You have decided to prepare for war against Logres. You gather your armies and begin to fortify your borders.
        """)
        print("""
        - Focus on building defenses to protect your kingdom
        - Launch a surprise attack on Logres
        - Attempt to ally with other kingdoms to strengthen your army
        """)

        castle2_ascii()
        print("")

        q = [
        inquirer.List('level17',
        message='What will you do?',
        choices=['Build defenses', 'Launch a surprise attack', 'Ally with other kingdoms'],
        default='Build defenses')]

        self.answers = inquirer.prompt(q)
        self.level17 = self.answers['level17']

        if self.level17 == 'Build defenses':
            print("You focus on building defenses to protect your kingdom.")
            print("This will help to protect your kingdom but may not lead to a quick victory.")
            self.score += 1
            self.gameOver = True
        elif self.level17 == 'Launch a surprise attack':
            print("You launch a surprise attack on Logres.")
            print("This can be risky but may lead to a quick victory if successful.")
            self.score += 2
            self.gameOver = True
        elif self.level17 == 'Ally with other kingdoms':
            print("You attempt to ally with other kingdoms to strengthen your army.")
            print("This can take time but can lead to a stronger army and more allies in the war.")
            self.score += 3
            self.gameOver = True

        os.system('cls')

    def level18(self):
        print("""
        You have decided to invest in new technologies and weapons to improve Camelot's military capabilities.
        """)
        print("""
        - Invest in new armor and weapons for soldiers
        - Research and develop new siege weapons
        - Invest in new communication technologies
        """)

        village_leader_ascii()
        print("")

        q = [
        inquirer.List('level18',
        message='What will you do?',
        choices=['Invest in new armor and weapons', 'Research and develop new siege weapons', 'Invest in new communication technologies'],
        default='Invest in new armor and weapons')]

        self.answers = inquirer.prompt(q)
        self.level18 = self.answers['level18']

        if self.level18 == 'Invest in new armor and weapons':
            print("You begin investing in new armor and weapons for soldiers.")
            self.score += 1
            self.gameOver = True
        elif self.level18 == 'Research and develop new siege weapons':
            print("You begin researching and developing new siege weapons.")
            self.score += 2
            self.gameOver = True
        elif self.level18 == 'Invest in new communication technologies':
            print("You begin investing in new communication technologies.")
            self.score += 3
            self.gameOver = True

        os.system('cls')

    def level19(self):
        print("""
        You have decided to build a new church in a nearby town, in order to spread the word of the Church and gain more followers.
        """)
        print("""
        - Use funds from the Church to construct the new building
        - Raise funds through donations from followers
        - Use forced labor from non-believers to construct the church
        """)

        church3_ascii()
        print("")

        q = [
        inquirer.List('level19',
        message='What will you do?',
        choices=['Use Church funds', 'Raise funds through donations', 'Use forced labor'],
        default='Use Church funds')]

        self.answers = inquirer.prompt(q)
        self.level19 = self.answers['level19']

        if self.level19 == 'Use Church funds':
            print("You use funds from the Church to construct the new building.")
            self.score += 1
            self.currentLevel += 1
        elif self.level19 == 'Raise funds through donations':
            print("You raise funds through donations from followers.")
            self.score += 2
            self.currentLevel += 1
        elif self.level19 == 'Use forced labor':
            print("You use forced labor from non-believers to construct the church.")
            print("This can be efficient but it may lead to resentment from the local population.")
            self.score -= 5
            self.currentLevel += 1

        os.system('cls')

    def level20(self):
        print("""
        You have decided to send missionaries to distant lands to spread the word of the Church.
        You choose a group of dedicated and devout followers to embark on this mission.
        """)
        print("""
        - Send the missionaries to a nearby kingdom with a different religion
        - Send the missionaries to a distant and unfamiliar land
        - Have the missionaries focus on converting people within Camelot first
        """)

        church2_ascii()
        print("")

        q = [
        inquirer.List('level20',
        message='Where will you send the missionaries?',
        choices=['Nearby kingdom with different religion', 'Distant and unfamiliar land', 'Focus on converting people within Camelot'],
        default='Nearby kingdom with different religion')]

        self.answers = inquirer.prompt(q)
        self.level20 = self.answers['level20']

        if self.level20 == 'Nearby kingdom with different religion':
            print("You send the missionaries to a nearby kingdom with a different religion.")
            print("This can be a challenging task but can lead to many new converts.")
            self.score += 2
            self.currentLevel += 1
        elif self.level20 == 'Distant and unfamiliar land':
            print("You send the missionaries to a distant and unfamiliar land.")
            print("This can be a risky endeavor but can also lead to many new converts and spreading the Church's influence.")
            self.score += 3
            self.currentLevel += 1
        elif self.level20 == 'Focus on converting people within Camelot':
            print("You have the missionaries focus on converting people within Camelot first.")
            print("This is a safer option but can also limit the Church's growth and influence.")
            self.score -= 1
            self.currentLevel += 1

        os.system('cls')

    def level21(self):
        print("""
        You focus on providing aid to the poor and needy in your current location.
        You establish soup kitchens and shelters for the homeless, and provide medical care to the sick and injured.
        """)

        print("""
        - Expand aid efforts to nearby towns and villages
        - Use the Church's resources to establish schools and education programs
        - Focus on creating jobs and economic opportunities for the community
        """)

        treasury_ascii()
        print("")

        q = [
        inquirer.List('level21',
        message='What will you do?',
        choices=['Expand aid efforts', 'Establish schools and education programs', 'Create jobs and economic opportunities'],
        default='Expand aid efforts')]

        self.answers = inquirer.prompt(q)
        self.level21 = self.answers['level21']

        if self.level21 == 'Expand aid efforts':
            print("You expand aid efforts to nearby towns and villages, helping even more people in need.")
            self.score += 1
            self.gameOver = True
        elif self.level21 == 'Establish schools and education programs':
            print("You use the Church's resources to establish schools and education programs, helping to improve the community's literacy and future prospects.")
            self.score += 2
            self.gameOver = True
        elif self.level21 == 'Create jobs and economic opportunities':
            print("You focus on creating jobs and economic opportunities for the community, helping to improve their financial stability and independence.")
            self.score += 3
            self.gameOver = True

        os.system('cls')

    def level22(self):
        print("""
        You apologize to the village and offer to help them with their struggles.
        The villagers are hesitant at first, but eventually forgive you and accept your offer of aid.
        """)
        print("""
        - Continue to provide aid to the village and nearby towns.
        - Focus on rebuilding the Church's reputation in the area.
        - Use the village as a base for spreading the Church's message to nearby towns and villages.
        """)

        village_ascii()
        print("")

        q = [
        inquirer.List('level22',
        message='What will you do?',
        choices=['Continue to provide aid', 'Rebuild Church reputation', 'Use village as a base'],
        default='Continue to provide aid')]

        self.answers = inquirer.prompt(q)
        self.level22 = self.answers['level22']

        if self.level22 == 'Continue to provide aid':
            print("You continue to provide aid to the village and nearby towns, improving the Church's reputation and gaining support.")
            self.score += 1
            self.gameOver = True
        elif self.level22 == 'Rebuild Church reputation':
            print("You focus on rebuilding the Church's reputation in the area, through peaceful means and community service.")
            self.score += 2
            self.gameOver = True
        elif self.level22 == 'Use village as a base':
            print("You use the village as a base for spreading the Church's message to nearby towns and villages, increasing the Church's reach and influence.")
            self.score += 3
            self.gameOver = True

        os.system('cls')

    def level23(self):
        print("""
        You continue to force conversions in the village and other nearby towns, using violent methods.
        This leads to widespread resentment and hostility towards the Church and your followers.
        """)

        print("""
        - Apologize for your actions and attempt to make amends.
        - Continue to use violent methods to convert non-believers.
        - Leave the area and focus on recruiting in other regions.
        """)

        commoners_ascii()
        print("")

        q = [
        inquirer.List('level23',
        message='What will you do?',
        choices=['Apologize and make amends', 'Continue violent methods', 'Leave the area'],
        default='Apologize and make amends')]

        self.answers = inquirer.prompt(q)
        self.level23 = self.answers['level23']

        if self.level23 == 'Apologize and make amends':
            print("You apologize for your actions and attempt to make amends with the villagers and other towns, but the damage may be irreversible.")
            self.score -= 5
            self.gameOver = True
        elif self.level23 == 'Continue violent methods':
            print("You continue to use violent methods to convert non-believers, causing further resentment and possibly leading to open rebellion.")
            self.score -= 8
            self.gameOver = True
        elif self.level23 == 'Leave the area':
            print("You leave the area and focus on recruiting in other regions, but you leave behind a trail of anger and hatred.")
            self.score -= 3
            self.gameOver = True

    os.system('cls')

    def level24(self):
        print("""
        You leave the village and focus on recruiting in other areas.
        This allows you to avoid further conflict with the village and continue spreading the Church's message in other places.
        """)
        print("""
        - Visit nearby towns and villages to recruit new followers
        - Start a fundraising campaign to support the Church's efforts
        - Focus on providing aid to the poor and needy in other areas
        """)

        village2_ascii()
        print("")

        q = [
        inquirer.List('level24',
        message='What will you do?',
        choices=['Visit nearby towns and villages', 'Start a fundraising campaign', 'Focus on providing aid'],
        default='Visit nearby towns and villages')]

        self.answers = inquirer.prompt(q)
        self.level24 = self.answers['level24']

        if self.level24 == 'Visit nearby towns and villages':
            print("You visit nearby towns and villages to recruit new followers.")
            self.gameOver = True
            self.score += 1
        elif self.level24 == 'Start a fundraising campaign':
            print("You start a fundraising campaign to support the Church's efforts.")
            self.score += 2
            self.gameOver = True
        elif self.level24 == 'Focus on providing aid':
            print("You focus on providing aid to the poor and needy in other areas.")
            self.score += 3
            self.gameOver = True

        self.gameOver = True
        os.system('cls')

    def gameOverScreen(self):
        print(f"""
        * End Game Score - ({self.score}) *
        \n""")

        if self.score >= 25:
             print("Your decisions were Very Ideal. You made the best choices for the kingdom of Camelot and its people.")
        elif self.score >= 15:
             print("Your decisions were Ideal. You made mostly the best choices for the kingdom of Camelot and its people.")
        elif self.score >= 10:
             print("Your decisions were Slightly Ideal. You made a mix of good and not so good choices for the kingdom of Camelot and its people.")
        elif self.score >= 5:
              print("Your decisions were Slightly Not Ideal. You made a mix of not so good and bad choices for the kingdom of Camelot and its people.")
        else:
             print("Your decisions were Not Ideal. You made mostly bad choices for the kingdom of Camelot and its people.")

        endscreen_ascii()
        print("")

g = Game()
"""Steven Nim
November 23, 2014
The Python Programming Challenge. This is a text-based game of surviving the wild"""


#-------------------------BACKPACK-------------------------
#The user can gath a small variety of items during the game. Here's a quick list:
#A broken cell phone, a bag of gumdrops, an axe, a harpoon, and a bucket.
backpack = "|"

#-------------------------------------------------PART 1: TRUCK-------------------------------------------------
#This is the title.
titleGame = """  _ _   _                            _ 
 ( ) \ | | __ _ _ __  _ __   ___  __| |
 |/|  \| |/ _` | '_ \| '_ \ / _ \/ _` |
   | |\  | (_| | |_) | |_) |  __/ (_| |
   |_| \_|\__,_| .__/| .__/ \___|\__,_|
               |_|   |_|   """
#Try to print in the center of the page but fail cause ASCII art is hard.
print titleGame.center(70,  )
print "A game of struggle, stress, and frustration... during the debugging stage."
print "It's actually about getting kidnapped and theives with sweet tooths. Enjoy!"
#These variables are used multiple time throughout the game.
#For when the user has already done that.
noAgain = "You've already done that."
#For when nothing interesting happens.
noWork = "Nothing interesting happens."
#A text break indicating the narrator's turn to speak.
narr = "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
#A text break indicating when the user gets an item.
itemBreak = "=================================="
#For function purposes.
text = ""
#Import the random module, bringing in many functions and variables for randomizing numbers and strings.
import random
#The user's health will be used in the battles throughout the game. It refills to max after every fight.
userHealth = 10
#Import sleep from the time module. "Sleep" will help make time gaps between printing characters.
from time import sleep
#Import some special, system-specific variables and functions.
import sys

#Take a string and print one character every 0.8 seconds on the same line, then skipping to the next line when all finished.
def waitAcrossSkip(text):
        for i in text:
                print i,
                sleep(1)
        #End the line and skips to the next.
        sys.stdout.write('\n')
        #
        sys.stdout.flush()
waitAcrossSkip('...')

print "Put Python in Fullscreen for best experience."

#Take a string and print one character every 0.8 seconds, then skipping to the next line AFTER EACH CHARACTER.
def waitDown(text):
	for i in text:
		print i
		sleep(1)
	sys.stdout.flush()
waitDown('...')

#Larry, an NPC, calls "Hey!" at the user three times.
for i in range(1,4):
	print "Hey!"
	sleep(2)

#Take a string and print one character every 0.8 seconds on the same line, but NOT skipping to the next line upon completion.
def waitAcross(text):
        for i in text:
                print i,
                sleep(1)
        sys.stdout.flush()
waitAcross('...')

#The user wakes up after Larry yells this.
print "I'm talkin' to you, lad!"
#The user wakes up, taking in their surroundings and trying to remember what happended before this.
print narr
print "You slowly stir awake. Your head aches a bit, but you quickly shake it off."
waitAcross('...')
print """What happened? You were hiking on a quaint mountain trail, but you can't remember anything after that. You take a look at your current surroundings.
print It's dark, but not too dark. You can see a little bit thanks to a small streak of light entering a crack in what appears to be... metal doors?
The metal doors and the steady bumps of the floor seems to indicate that you\'re stuck in the back of a small delivery truck with a bunch of junk and another person."""
print """             V   ~~~   ~~~   ~~~
          _|_| |=========================|
         (___| |                    ~~~~~|~
      __//__]| |                      ~~~|~~
    >|:___ '||'|                  ~~~~~~~|~
     [/.-.\= |-|.-._.-.===========.-._.-.=;
     -|(o)|\-~~|(o)|(o)\~~''~''~~|(o)|(o)\ """
#Quick little interval...
waitDown('...')
#Sometimes the text can get long and hard to read since Python prints everything at an ungodly speed. Sometimes, sleep doesn't work well enough.
#In those cases, there's the "breakWords" function I have here. It'll slow down the text and make sure that the user has time to read everything.
breakWordsText = ""
areYouAwake = ""
def breakWords(breakWordsText):
        areYouAwake = raw_input(breakWordsText)
breakWords('Enter anything to continue.')
#Quick little interval...
waitDown('...')
print "You turn to your right and notice your cell phone lying on the floor. You quickly scoop it back up."
#The user picks up their cell phone, which is now broken. This function is used whenever a new item is picked up.
item = ""
def itemGet(item):
        print itemBreak
        print "You got a(n): " + item 
        print itemBreak
itemGet("Broken Cell Phone")

print narr
print """Unfortunately, its screen is cracked and it doesn't seems to be turning on, so it's pretty useless...
You put your phone away in your backpack, still slung across your back from the hike, and turn to the person who called to you, an aged man with a white beard and a kind face."""
print narr
waitAcrossSkip('...')
#The cell phone is added to the backpack. Note that this broken cell phone is never used during the rest of the game.
backpack = backpack + "broken cell phone | "
#Larry asks the user for their name, which the user will input themselves.
#If they do not enter anything, Larry will politely ask again. What a gentleman.
print "????: Top of the mornin' to you, lad. I wish that was the case, but we seem to be in deep water right about now."
name = raw_input("Before I ramble further, however, I'd like to know your name, young'un.")
while name == "":
        name = raw_input("Don't be shy, young'un! It's just your name I'd like, please.")
#Freeing Larry.
print "????: Oh, so your name is " + name + ". It's a pleasure. Wish our meeting could've been in a better place. Do ya mind untying these knots on meh?"
print narr
waitAcross('*untie*')
print "You untie the knots around the man's hands, and he does the same for you. It's tricky, but both of you manage to get your hands and feet free."
print narr
#Here's Larry. Just imagine that he's more wrinkly. He is actually quite old!
print """                  .-"```'.
                 /        |
                | .'  _  _|
                \(\   6  6 
                 | \   _\ |
                 |\ `~`= `/
                 | '.___.'
             .'` \     |_
                  '-__ / `-"""
#Larry talks a bit about himself.
print "????: Since you told me a bit 'bout you, I guess I should do the same..."
print """????: My name's Larry. I was havin' myself a grand ol' walk along the trail when these two goons came up to me and attacked!
I tried to battle back, but they were tough whippersnappers! I was knocked unconscious and thrown into this here delivery truck."""
print """Larry: I just woke me-self up a few minutes before you did. I took a quick look for an escape, and I found 'un! The lock on that there door
could be shattered by somethin' tough. Think there's anythin' nearby we could use?"""
#Another break.
waitDown('...')
breakWords('Type anything to continue. We have to make sure you\'re catching up with all of this!')
waitDown('...')
print """You look around the truck. The light shining through the door is faint, but still helpful. You find spot some bullets, a hammer, a stick from a tree, and a bag of gumdrops.
Everything else is inside tightly wrapped cardboard boxes."""
#These are used to check if the user has already picked an incorrect item once before. I could've used booleans here, but if it works, then keep it working, I guess.
bullets = 0
stick = 0
gumdropsCount = 0
#The user must pick between one of the four items. The bullets and the stick are useless. The bag of gumdrops can be put in the backpack. The hammer is the correct choice.
itemChoice = raw_input("Which item do you take to destroy the lock?")
while itemChoice != "hammer":
        #If the user picks the bullets
        if itemChoice == "bullets":
                #If the user has already picked this item before, then prevent them from doing so again.
                if bullets == 1:
                        print noAgain
                        itemChoice = raw_input("Which item do you take to destroy the lock?")
                #If this is the user's first time picking this item, give them this message.
                else:
                        print "You take the bullets but you realize that they're just shell casings. You toss them aside."
                        itemChoice = raw_input("Which item do you take to destroy the lock?")
                        bullets = 1
        #If the user picks the stick
        elif itemChoice == "stick":
                if stick == 1:
                        print noAgain
                        itemChoice = raw_input("Which item do you take to destroy the lock?")
                else:
                        print "You pick up the stick and poke the lock with it. Nothing interesting happens."
                        itemChoice = raw_input("Which item do you take to destroy the lock?")
                        stick = 1
        #If the user picks the gumdrops
        elif itemChoice == "gumdrops":
                if gumdropsCount == 1:
                        print noAgain
                        itemChoice = raw_input("Which item do you take to destroy the lock?")
                else:
                        #Picking the gumdrops will add the item to the user's backpack. It's useful for skipping a portion of the adventure later.
                        print "You pick up the bag of gumdrops and store it in your pocket for later. 42 of them will last you a while."
                        itemGet("BAG OF GUMDROPS")
                        backpack = backpack + "gumdrops| "
                        gumdropsCount = 1
                        print "You current have the following items in your backpack: " + backpack
                        itemChoice = raw_input("Which item do you take to destroy the lock?")
        #If the user doesn't pick any of the choices, then the game will ask again.
        else:
                print "You decide to keep thinking about what to do. Hmmm..."
                itemChoice = raw_input("Which item do you take to destroy the lock?")
#This will display when the user picks the hammer, the correct option.
print narr
print """You grab the hammer and bash the lock with it several times. The lock finally shatters, and the back doors of the truck fly open.
You quickly peek your head out and take in the sight of a barren path in a dense forest. You head back in and turn to Larry."""
print narr
print "Larry: Aye, my lad! You've gotten us an exit. We can retreat into these here woods and figure out what we should do from that there. Let's make haste!"
#Break before next part.
waitDown('......')
breakWords('Type anything to begin Part 2: Firewood.')
waitDown('...')

#---------------------------------------------PART 2: FIRE----------------------------------------------

#You and Larry arrive at a clearing in the woods you escaped to and you decide to camp for the night since it's already getting dark out.
print narr
print """You and Larry wander deep into the woods, far from where you escaped the burglars' truck. You end up in a quiet clearing surrounded by thick, tall oak trees.
Catching your breath for a second, you turn to Larry and ask about what you two should do next."""
print narr
waitAcrossSkip('...')
print """              ,@@@@@@@,
       ,,,.   ,@@@@@@/@@,  .oo8888o.
    ,&%%&%&&%,@@@@@/@@@@@@,8888\88/8o
   ,%&\%&&%&&%,@@@\@@@/@@@88\88888/88'
   %&&%&%&/%&&%@@\@@/ /@@@88888\88888'
   %&&%/ %&%%&&@@\ V /@@' `88\8 `/88'
   `&%\ ` /%&'    |.|        \ '|8'
       |o|        | |         | |
       |.|        | |         | |
    \\/ ._\//_/__/  ,\_//__\\/.  \_//__/_"""
print """Larry: I think we should be settin' up camp here, lad. I believe we can go find ourselves out of this place tomorrow, as it's gettin' mighty dark now.
What're some things we need... aye, food and water are definitely real necessities. Shelter'll be one too, but I can do that. 
I used to be a carpenter, I tell ya! Per'aps we should also gather us some firewood as well."""
waitAcross('...')
print "wait! I have some stuff from the truck earlier! Grabbed it as we got out... it may come in handy for gatherin' things."
#Now originally, I had the user pick which option they wanted to do first, but that idea apparently crashed and burned, so instead we now have linear progression.
#THANKS PYTHON
print narr
print "Larry empties a small sack. Its contents, including an axe, now rest on the ground. You tell Larry that you would like to find some firewood first."
print narr
print "Larry: Alright, lad. Don't bother gettin' any wood for me, I have my own axe. Go on, grab your own!"
#Add the axe to the user's backpack.
itemGet("AXE")
backpack = backpack + "axe| "
#Display the user's current items.
print "You current have the following items in your backpack: " + backpack
#Another break.
breakWords('Type anything to continue. The secret to life, maybe?')
print narr
print """You begin to search for an oak tree thin enough to chop down. As Larry searches quite some distance from you,,
you stumble upon the perfect tree. Thin enough to chop down, but hard enough to burn for a long while. You eagerly swing your axe at the tree,
when suddenly..."""
print narr
waitAcross('...')
print "ROAAAAAAR!"
print narr
print "You've awakened an angry tree spirit! The spirit escapes through a crack in the tree and faces you. It's large and lumbering."
print narr
print "Tree Spirit: You dare to attack my home?! You will pay with your life!"
waitDown('...')
#Quick break before the battle...
breakWords('Type anything to begin the battle against the Tree Spirit! (MOVESET: attack, block)')
#Battle Sequence! Here are the two things the Tree Spirit can do.
treeSpiritList = ['attack', 'block']
#It starts at 8 health.
treeSpiritHealth = 8
#A counter for turns.
turn = 0
#Loop all of this until the Tree Spirit's health is 0, meaning that it's dead.
while treeSpiritHealth != 0:
        print "+++++++++++++++++++++++++++++++++++++++++++++++++"
        #Display both fighters' health.
        print "Your health: {} || Tree Spirit's health: {}".format(userHealth, treeSpiritHealth)
        #Yes, the user can die. If they do, it's game over! No really, the game will end.
        if userHealth == 0:
                print "You feel dizzy... *fwump*"
                print "YOU'RE DEAD! RESTART TO TRY AGAIN!"
                waitAcross('GAME OVER')
                sys.exit()
        #Turn count increases by 1 each turn.
        turn = turn + 1
        #Print "TURN" and the current turn number.
        print "{}: {}".format("TURN", turn)
        #Ask the user whether they want to attack, block, or... sing?
        treeSpiritUser = raw_input("What will you do? Your options are: Attack, block, sing.")
        #Here, we randomly pick between the Tree Spirit's attacks to see which one it'll do.
        treeSpiritFoe = (random.choice(treeSpiritList))
        #The user will know what the Tree Spirit does after they have entered their move.
        print "The Tree Spirit " + treeSpiritFoe + "s!"
        #If both of you attack, the Tree Spirit will take 2 damage.
        if treeSpiritUser == "attack" and treeSpiritFoe == "attack":
                print """You swing you axe at the Tree Spirit, and the Tree Spirit swings its heavy arm. Your weapons collide and bounce off one another.
It looks like the Tree Spirit got the brunt of that engage."""
                treeSpiritHealth = treeSpiritHealth - 2
        #If you try to attack and the Tree Spirit blocks, you take 2 damage.
        elif treeSpiritUser == "attack" and treeSpiritFoe == "block":
                print "You swing your axe at the Tree Spirit but it blocks your attack and throws you back. You quickly regain composure, but you feel weaker."
                userHealth = userHealth - 2
        #If you block the Tree Spirit's attack, then the Tree Spirit takes 2 damage.
        elif treeSpiritUser == "block" and treeSpiritFoe == "attack":
                print """The Tree Spirit lunges at you but you block the attack with your axe and push the spirit back.
With the spirit dazed, you jump in and bring your axe down onto your enemy. That oughta show 'em!"""
                treeSpiritHealth = treeSpiritHealth - 2
        #If you both block, nothing happens.
        elif treeSpiritUser == "block" and treeSpiritFoe == "block":
                print "You both get ready to block, but none of you attack. You instead stare down your foe."
        #If you sing, nothing bad happens. You just look like a weirdo.
        elif treeSpiritUser == "sing":
                print "You begin to sing your favourite song for no reason. The Tree Spirit looks at you confused and stops its move."
        #If you type in anything else, you'll GET SMASHED.
        else:
                print "You decide to do nothing... so the Tree Spirit smashes you in the face."
                userHealth = userHealth - 2
#Upon victory, the user will have their health restored and the Spirit will die. You eturn to the campsite with the firewood.
userHealth = 10
print "Tree Spirit: ugh... you will.. urff..."
print narr
print """The Tree Spirit collapses onto the forest floor and explodes in a plume of green dust. With the spirit out of your way,
you peacefully chop down the now-abandoned, thin oak tree. You later return to the campsite with a bundle of firewood in your arms."""
print narr
#Quick break before the next part.
waitDown('......')
breakWords('Type anything to begin Part 3: Food.')
waitDown('...')
#---------------------------------------------PART 3: FOOD----------------------------------------------
print narr
print "You return to the campsite to find Larry hauling a log onto a pile of other logs. You drop the firewood and tell Larry that you wish to look for food now."
print narr
print "Larry: Alright laddy. Ooof! That was heavy... Here, take this harpoon I snuck outta that truck. You can probably catch a fish or two with it."
#Add a harpoon to the user's ever-growing arsenal.
itemGet("HARPOON")
backpack = backpack + "harpoon| "
print "You current have the following items in your backpack: " + backpack
#BREAK
breakWords('Type anything to continue. How about your birthday?')
#Time to go fishing!
waitDown('...')
print narr
print """You head out alone and eventually stumble upon a small river.
you spot some fish in the river. You instantly notice a nice, shiny gold looking fish that seems like it would make a suitable meal (Gumdrops aren't a meal).
You plunge your harpoon into the river, and pull out the fish you desired. That was easy! You turn around to return to the campsite..."""
waitAcross('...')
print "and stand face to face with a ravenous black bear. Uh oh."
print """                  
     :"'._..---.._.'";
     `.             .'
     .'    \   /    `.
    :      a   a      :                 __....._
    :     _.-0-._     :---'""'"-....--'"        '.
     :  .'   :   `.  :                          `,`.
      `.: '--'--' :.'                             ; ;
       : `._`-'_.'                                ;.'
       `.   '"'                                   ;
        `.               '                        ;
         `.     `        :           `            ;
          .`.    ;       ;           :           ;
        .'    `-.'      ;            :          ;`.
    __.'      .'      .'              :        ;   `.
  .'      __.'      .'`--..__      _._.'      ;      ;
  `......'        .'         `'""'`.'        ;......-'
        `.......-'                 `........'"""
print "You remove the fish from the harpoon and throw it to the side. You'll need the harpoon to take down this starving, angry, bear."
print narr
#Quick break before the battle...
breakWords('Type anything to begin the battle against the Black Bear! (MOVESET: attack, block, roar)')
#The second battle! The bear has a wider set of moves than the Tree Spirit, and more health!.
bearList = ['attack', 'block', 'roar']
bearHealth = 10
bearTaunt = 0
turn = 0
#Do this until the bear's health is at 0... AND IT'S DEAD.
while bearHealth != 0:
        print "+++++++++++++++++++++++++++++++++++++++++++++++++"
        #Display both fighters' health.
        print "Your health: {} || Bear's health: {}".format(userHealth, bearHealth)
        #You can still die.
        if userHealth == 0:
                print "You feel dizzy... *fwump*"
                print "YOU'RE DEAD! RESTART TO TRY AGAIN!"
                waitAcross('GAME OVER')
                sys.exit()
        #Turns are still counted.
        turn = turn + 1
        print "{}: {}".format("TURN", turn)
        #You still can attack and block the bear, but now you can taunt it too!
        bearUser = raw_input("What will you do? Your options are: Attack, block, taunt.")
        #Bear's move is randomly picked.
        bearFoe = (random.choice(bearList))
        #If the user taunts the bear, the bear will, for certain, attack on the next turn. However, the user can only taunt once.
        if bearTaunt == 1:
                bearFoe = 'attack'
                bearTaunt = bearTaunt + 1
        #Tell the user what the bear does after they've picked their move.
        print "The black bear " + bearFoe + "s!"
        #If both of you attack, the bear will take 2 damage.
        if bearUser == "attack" and bearFoe == "attack":
                print """The bear swings at you but you impale it's arm with your harpoon first. Ouch! That's gotta hurt!"""
                bearHealth = bearHealth - 2
        #If you attack but the bear blocks, then you take 2 damage.
        elif bearUser == "attack" and bearFoe == "block":
                print "You lunge at the bear, but the animal punches you in the stomach and tosses you aside. You quickly regain composure, but ouch..."
                userHealth = userHealth - 2
        #If you block the bear's attack, then the bear takes 2 damage.
        elif bearUser == "block" and bearFoe == "attack":
                print "The bear charges at you but you sidestep it and pierce your harpoon through its back. Yowch!"
                bearHealth = bearHealth - 2
        #If you both block, then nothing happens.
        elif bearUser == "block" and bearFoe == "block":
                print "You both stare each other down. Grrrr..."
        #If the bear roars while you attack, your attack will fail.
        elif bearUser == "attack" and bearFoe == "roar":
                print "You attempt to jump in, but the bear roars at you. Causing you to flinch and halt your attack."
        #If the bear roars at you while you block, you'll take 2 damage.
        elif bearUser == "block" and bearFoe == "roar":
                print "The bear roars at you, and sends you flying into a tree. You pick yourself up but you feel a pain in your back..."
                userHealth = userHealth - 2
        #Taunting the bear was explained earlier.
        elif bearUser == "taunt":
                if bearTaunt == 0:
                        print "You taunt the bear, getting it even more angry. It's sure to attack next turn!"
                else:
                        print "You attempt to taunt the bear but it fails. Your taunt only worked once!"
                bearTaunt = bearTaunt + 1
        #Doing something else will still get you smashed. SMASHED.
        else:
                print "You decide to do nothing... so the black bear smashes you in the face."
                userHealth = userHealth - 2
#Refill health to max.
userHealth = 10
print narr
print "The bear finally succumbs to its injuries and collapses. You grab your fish from the sidelines and head back to the campsite."
print narr
#Break before next part.
waitDown('......')
breakWords('Type anything to begin Part 4: Water.')
waitDown('...')
#---------------------------------------------PART 4: WATER----------------------------------------------
#User returns to the campsite and drops off the fish. Time to fetch drinking water!
print narr
print """You return to the campsite to find Larry attempting to construct a wooden fort. It seems that progress is going slow for him.
You place the fish on top of a log and catch Larry's attention."""
print narr
waitAcrossSkip('...')
print "Larry: Eh? You got the food? Fantastic! Looks like all we need is some drinkin' water. Here, take this bucket."
#The user gets a bucket. NAAAAICE.
itemGet("BUCKET")
backpack = backpack + "bucket | "
print "You current have the following items in your backpack: " + backpack
print "Larry: Be aware, lad. Many of the rivers here aren't safe to drink. Examine closely and carefully. Good luck."
#Break.
breakWords('Type anything to continue. Could you tell me your favourite food?')
#The user will arrive at an old cabin where they will meet a new character.
print narr
print """You head out from the campsite and deep into the woods. You comb every inch of the woods near the campsite,
but you are unsuccessful in finding any good water sources. You decide to wander farther, and you eventually stumble upon an
old, little cabin in the woods. Risking your luck, you go up the creaking porch and knock on the rickety door. Maybe someone inside can help."""
print narr
#Print knock slowly.
waitAcross("*knock*")
#Someone answers the door.
print "The door opens to a young man."
print "????: Who are you?"
print narr
print """The young man is dressed in almost entirely black. His black shoes match his black pants, shirt, cloak,
and headband. The man has a brown, burlap sack slung over his shoulder, and his bright, lime green hair stands out from the rest of his attire."""
#Asking for names, round 2! If you want, you can give a new name... after all, the best way to con a thief is to lie.
name = raw_input("I asked you for your name. Gonna give it to me?:")
while name == "":
        name = raw_input("Let's not make this complicated. I don't wanna grab the knife... So, what is your name?:")
print narr
print "???: Oh, so you're " + name + ". Interesting."
#Meet Gradden, sly thief and candy enthusiast.
print """I usually go by Gradden. In case my attire hasn't told you already, I'm a thief.
I wouldn't mind robbing anyone blind, even if it means harming anyone along the way. I'd steal from you, but you look lost and broke. What happened to you?"""
#Break.
breakWords('Type anything to continue. Try reciting your favourite quote here or something...')
#More Gradden time. The goons who kidnapped you were slain by Gradden for their valuables. Yeesh.
print narr
print "You quickly tell Gradden about the kidnapping and the truck."
print narr
print """Gradden: I see. I did just come back from a nice little standoff with two thugs in a truck like that. May have been them.
But no matter, I killed them both and raided their goods, which wasn't much. I did, however, grab this."""
waitAcrossSkip("...")
print narr
print "Gradden retreats into the cabin for a second and comes back with a case of water bottles in one hand, and his sack still in the other."
print narr
print """Gradden: Found this baby in the back of the truck. Since you two seem to be so keen on camping out, I could give you this. After all,
there's no water or food in this cabin, and I'm heading off soon, meaning that I already have my stash of rations, water, and weapons all in this sack.
By rations of course, I mean candy. Candy's great, ya know? Even an adult like me can't resist the allure of sweets... heh heh..."""
#Break.
breakWords('Type anything to continue. What is your favourite idea?')
#Gradden isn't going to let go of something of his so easily. He'll want to quiz you for fun first!
print "Gradden: But anyways... I have the time to test your mettle. Do you really deserve this drinking water... or not? Lemme quiz you. Heh heh."
print narr
print "It seems that Gradden isn't going to let go of the case of bottles so easily. You're going to have to live up to his demands..."
#If you have the grumdrops from the truck, he'll hand over the water without asking any questions.
if gumdropsCount == 1:
        print "Unless..."
        waitAcrossSkip('...')
        print "You pull out the gumdrops from your backpack."
        print narr
        print """Gradden: Where'd you get that?! ...All of those for the water? ...You know what, fine! You make a good deal.
This case of water bottles for your candy! Just hand that to me... and you can have all of these... ahahaha! Yes! Precious sweets!"""
        print "Thanks for your cooperation, " + name + "! See ya around! Eheheheh... 42 big ones! I've struck it big!"
        print narr
        waitAcrossSkip('...')
        print "Gradden slips behind you and scurries off into the forest, chuckling to himself. You grab the case of water and return to the campsite."
#Otherwise, it's time for the Gradden riddle quiz!
else:
        print narr
        print "Gradden: Alright, " + name + ". Here it goes. The best riddle I know! Can you figure it out?"

        #The user must type in the answer for the first riddle. The correct answer is "mushroom"
        riddle1 = raw_input("||>> What kind of room has no doors or windows?")
        #If the user gets it wrong, Gradden will ask again.
        while riddle1 != "mushroom":
                print "Gradden: WRONG! I bet I got you stumped! I'm a nice guy though, I'll let you try again!"
                riddle1 = raw_input("||>> What kind of room has no doors or windows?")
        
        #This prints if the user gets the first riddle right.
        print "CORRECT?! Argh! How'd you get that one? I'm not done yet... here's another, greater than the last!"
        
        #The user must type in the answer for the second riddle. The correct answer is "coffin"
        riddle2 = raw_input("""||>> Who makes it, has no need of it.
||>> Who buys it, has no use for it. 
||>> Who uses it can neither see nor feel it. 
||>> What is it?""")
        #If the user gets it wrong, Gradden will ask again.
        while riddle2 != "coffin":
                print "Gradden: WRONG! Try again, sucker!"
                riddle2 = raw_input("""||>> Who makes it, has no need of it.
||>> Who buys it, has no use for it. 
||>> Who uses it can neither see nor feel it. 
||>> What is it?""")
        #This prints if the user gets the second riddle right.
        print "Gradden: CORRECT AGAIN?! Ack, stop! You'll never solve this third and final one, though!"

        #The user must type in the answer for the third riddle. The correct answer is "eye"
        riddle3 = raw_input("""||>> Pronounced as one letter but written with three, only two different letters are used to make me.
||>> I'm double, I'm single I'm black, blue, and gray.
||>> I'm read from both ends and the same either way.""")
        #If the user gets it wrong, Gradden will ask again.
        while riddle3 != "eye":
                #The "||>>" is for clarity purposes. It makes it easier to distinguish Gradden's text from the question. 
                print "Gradden: Ahahahaha! WRONG! Try, try again, sucker!"
                riddle3 = raw_input("""||>> Pronounced as one letter but written with three, only two different letters are used to make me.
||>> I'm double, I'm single I'm black, blue, and gray.
||>> I'm read from both ends and the same either way.""")
        
        #Gradden wil hand over the water upon correctly guessing the third riddle.
        print "Gradden: Aaaaaaagh! CORRECT! Fine! You win!"
        print narr
        print """Gradden slips by you and retreats into the woods with his burlap sack over his shoulder, cursing about how he was 'unfairly bested'.
You scratch your head in confusion, then grab the case of water bottles and begin to head back to the camp."""
#Beginning of final part.
waitDown('......')
breakWords('Type anything to proceed to the Part 5: Final Fight & Rescue.')
waitDown('...')
#---------------------------------------------PART 5: FINAL FIGHT & RESCUE----------------------------------------------		
#You tell Larry to come spend the night in the cabin.
print narr
print "You return to the campsite to find Larry still trying to construct the fort."
print narr
print "Larry: Agh! Blast this! I'm rusty after all of these years of retirement... Oh, hello lad!"
print narr
print "You tell Larry about the cabin, and Gradden."
print narr
waitAcrossSkip("...")
print "Larry: A thief, eh? Lucky us for not gettin' on his bad side. But a cabin... ah well, let's put our luck on the table. Let's go, laddy!"
#Break Time! No cookies though.
breakWords('Type anything to continue. Heheheheheh...')
#You and Larry eat, drink and sleep, but you're awaken in the middle of the night...
print narr
print """You and Larry head to the old cabin and use your firewood to light the fireplace. You cook your fish on the flames and enjoy the bottled water.
You douze the fire and head to sleep shortly after, and you opt to take the old couch while Larry gets the mattress he found in a closet."""
waitAcrossSkip("Later...")
print """You wake up to a crashing sound outside. You check out the window... and you find a creature outside shaped like the Tree Spirit
you killed earlier. Grabbing your axe from your backpack, you head out to confront the creature."""
waitAcrossSkip('...')
print """Elder Guard: You! You killed my brother! Ask the Elder Tree Guardian, I will smite you down!"""
#The Elder Tree Guardian (a.k.a Elder Guard) attacks!
breakWords('Type anything to begin the last battle, against the Elder Tree Guardian! (MOVESET: attack, block, ingrain)')
#Elder Tree's moves.
elderList = ['attack', 'block', 'ingrain']
elderHealth = 12
turn = 0
#Do this until the Elder Guard's health is at 0... AND IT'S DEAD.
while elderHealth != 0:
        print "+++++++++++++++++++++++++++++++++++++++++++++++++"
        #Display both fighters' health.
        print "Your health: {} || Elder Guard's health: {}".format(userHealth, elderHealth)
        #You can still die.
        if userHealth == 0:
                print "You feel dizzy... *fwump*"
                print "YOU'RE DEAD! RESTART TO TRY AGAIN!"
                waitAcross('GAME OVER')
                sys.exit()
        #Turns are still counted.
        turn = turn + 1
        print "{}: {}".format("TURN", turn)
        #You still can attack and block the bear, but now you can taunt it too!
        elderUser = raw_input("What will you do? Your options are: attack, block, charge.")
        #Bear's move is randomly picked.
        elderFoe = (random.choice(elderList))
        #Tell the user what the Elder Guard does after they've picked their move.
        print "The Elder Tree " + elderFoe + "s!"
        #If both of you attack, the Elder Guard will take 2 damage.
        if elderUser == "attack" and elderFoe == "attack":
                print """You and the Elder Guard jump at each other. You barely dodge the Guard's lumbering arm and you manage to smash your axe into its side. Ouch!"""
                elderHealth = elderHealth - 2
        #If you attack but the elder blocks, then you take 2 damage.
        elif elderUser == "attack" and elderFoe == "block":
                print "You lunge at the Elder Guard but are knocked aside by its heavy arm. Your ribs are starting to ache..."
                userHealth = userHealth - 2
        #If you block the Elder Guard's attack, then it takes 2 damage.
        elif elderUser == "block" and elderFoe == "attack":
                print "The Elder Guard throws a ball of green energy at you, but a nice deflection with your axe sends the energy ball back at it!"
                elderHealth = elderHealth - 2
        #If you both block, then nothing happens.
        elif elderUser == "block" and elderFoe == "block":
                print "You both stare each other down. The Elder Guard mutters something about beating you into the ground."
        #If the Elder Guard plants its roots and you attack, then the Guard's heal is cancelled and it takes damage.
        elif elderUser == "attack" and elderFoe == "ingrain":
                print """"You attempt to swing your axe at the Elder Guard while it plants several roots into the ground.
You manage to cut off its roots, causing the Elder Guard to scream in pain and angrily look you down."""
                elderHealth = elderHealth - 2
        #If the Elder Guard plants its roots while you're blocking, the Guard will heal without repercussions.
        elif elderUser == "block" and elderFoe == "ingrain":
                print "You prepare to block, but the Elder Guard extends tree roots out of its body and into the earth. It has healed some of health back!"
                #If the Elder is already at full health, then he heals for nothing.
                if elderHealth < 12:
                        elderHealth = elderHealth + 2
        #If the Elder Guard plants its roots while you're charging, it heals and you take damage.
        elif elderUser == "charge" and elderFoe == "ingrain":
                print "You charge in, but the Elder Guard extends tree roots from its body and knocks you aside before planting them into the earth to restore health. Nice job."
                if elderHealth < 12:
                        elderHealth = elderHealth + 2
                userHealth = userHealth - 2
        #If you charge at the Elder Guard while it's blocking, you break its stance and the Guard will take 2 damage.
        elif elderUser == "charge" and elderFoe == "block":
                print "You charge in as the Elder Guard stands it ground. With amazing strength, you tackle the Guard down onto the ground!"
                elderHealth = elderHealth - 2
        #If you charge at the Elder Guard while it's attacking, you dodge it and the Guard will take 2 damage.
        elif elderUser == "charge" and elderFoe == "attack":
                print "You charge in as the Elder Guard charges in as well. You sidestep the Elder Guard's swinging arm and smash you axe into its back!"
                elderHealth = elderHealth - 2
        #Doing something else will still get you smashed. SMASHED.
        else:
                print "You decide to do nothing... so the black bear smashes you in the face."
                userHealth = userHealth - 2
#Refill health to max after the fight.
userHealth = 10
#After the fight, you go back to sleep.
print narr
print "The Elder Tree Guardian collapses and disappears into a puff of black smoke. As it fades away, you can hear its parting words."
print narr
waitAcrossSkip('...')
print "Elder Tree Guardian: Curse you... scoundrel..."
print narr
print "You turn back into the cabin to get back to sleep. Surprisingly, Larry slept through your entire skirmish outside."
print narr
#Break before ending.
breakWords('Type anything to continue. Wow, what a battle!')
#Final segment. You're rescued, thanks to Gradden!
print narr
print "You wake up to a knock on the door. Larry is already up and opening the door as you stumble out of bed."
print narr
waitAcrossSkip('...')
print "Larry: Wha...? Rescue? Are you sure... oh, you have the identification all right. Come over here, lad! We're saved!"
print narr
print "You walk over to Larry as two search and rescue workers enter. You can recognize the logo of the local law force on the arms of their coats."
print narr
print """S&R Worker: Yep, both of them fit the description. We're glad to have found you so soon after you went missing,
and it's thanks to the assistance of this odd man clad in black who disappeared shortly after giving us the information.
Now c'mon, your relatives are probably worried sick. Let's go back to the hotel."""
print narr
print "You and Larry board the S&R workers' helicopter and take off into the direction of the hotel."
waitDown('......')

#THE END. Now for some credits!
theEnd = "THE END"
print theEnd.center(40,  )
print """CREDITS:
STEVEN NIM
STEVEN NIM
STILL STEVEN NIM"""
waitAcrossSkip('...')
print """SPECIAL THANKS TO:
ICS 2o & MR. B CUTTEN
CODECADEMY
GOOGLE
PYTHON 2.7 IDLE GUI
NOTEPAD ++
CHRIS.COM FOR THE ASCII ART
MR. ROGERS
BILL CLINTON
TONY TIGER"""

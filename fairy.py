#!/usr/bin/env python3

import os,time,random,sys

Red = "\033[0;31m"
Green = "\033[0;32m"
Orange = "\033[0;33m"
Blue = "\033[0;34m"
Purple = "\033[0;35m"
Cyan = "\033[0;36m"
White = "\033[0;37m"

sp = 0.05

def slow_print(str):
  for letter in str:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(sp)
  print()

def slow_inp(str):
  for letter in str:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(sp)
  input()

rep = 0
money = 0
pay_inc = 1
stakes = 1

#Holiness
#GoodDeads
#BadDeads
#Death
#Goal_in_Life

games = ["Fortnite","Minecraft","GTA 5","Halo 3"]
metals = ["adamantium","gold","diamonds","pig guts"]

tnames = ["Frank","Bill","Tina","Suzie","Leonardo","Billy","Lana","Dunder","Dic","Seven","Miley","Napolean","Dwayne","Shet"]
lnames = [" Costanza"," Da Vinci"," Backwards"," Miflin"," Smasher"," Dicky"," Carleone"," Cirus"," Buck"," The Rock"," Hed"," Wad"]

deaths = ["Swam in each of the 7 major Oceans","Had a wee into the deepest part of the Grand Canyon",
          "Swam with wild pigs in Exuma, Bahamas","Giving Birth","Was able to fit 3 Creme Eggs in their mouth at one time"
    ,"Was almost killed in a shootout","Thirst","Hunger","Drowned in a desert","Electrocuted by Computer","Starved in a kitchen",
          "Brain exploded from simple math equation 2+2","Choked on a taco","Drowned in saliva","From an infection of horse tooth in body",
          'From a deadly pandemic',"Killed by someone who they killed in "+random.choice(games),
          "Ate a pinecone","Stepped on a small sized lego","Dabbed and was killed by those haters"]

goals = ["To Be the richest human ever","To Have two kids","To Be feared","To be famous","To die old","To die young","To write a book","To be epic","To get all the girls/guys","To have a mansion made out of "+random.choice(metals),"To own a fish","To make over $30 in 30 minutes without a job","To be a dentist","To make a friend","To never get a pimple","To kill a shark made out of "+random.choice(metals),"To have a step brother named "+random.choice(tnames),"To have a kid with a toe nail abnormality","To have a pet skunk with heavy mutations","To climb mount everest.","To have ebola","To have a pet rabbit without a nose and three ears."]

wishes = ["Hope's their day is more beautiful than a unicorn farting rainbows", ""]

prayers = ["Please make my toes equal length","Please let me have 1,000,000 V-BuCKs","Please let me keep my job",
           "Please make my husband have bigger muscles","Will you make my friend have ebola so I don't have to visit her basketball game"]

os.system('clear')

print('''

$$$$$$$\  $$\            $$\     $$\             $$\                           $$$$$$$$\       $$\                     
$$  __$$\ \__|           $$ |    $$ |            $$ |                          $$  _____|      \__|                    
$$ |  $$ |$$\  $$$$$$\ $$$$$$\   $$$$$$$\   $$$$$$$ | $$$$$$\  $$\   $$\       $$ |   $$$$$$\  $$\  $$$$$$\  $$\   $$\ 
$$$$$$$\ |$$ |$$  __$$\\_$$  _|  $$  __$$\ $$  __$$ | \____$$\ $$ |  $$ |      $$$$$\ \____$$\ $$ |$$  __$$\ $$ |  $$ |
$$  __$$\ $$ |$$ |  \__| $$ |    $$ |  $$ |$$ /  $$ | $$$$$$$ |$$ |  $$ |      $$  __|$$$$$$$ |$$ |$$ |  \__|$$ |  $$ |
$$ |  $$ |$$ |$$ |       $$ |$$\ $$ |  $$ |$$ |  $$ |$$  __$$ |$$ |  $$ |      $$ |  $$  __$$ |$$ |$$ |      $$ |  $$ |
$$$$$$$  |$$ |$$ |       \$$$$  |$$ |  $$ |\$$$$$$$ |\$$$$$$$ |\$$$$$$$ |      $$ |  \$$$$$$$ |$$ |$$ |      \$$$$$$$ |
\_______/ \__|\__|        \____/ \__|  \__| \_______| \_______| \____$$ |      \__|   \_______|\__|\__|       \____$$ |
                                                               $$\   $$ |                                    $$\   $$ |
                                                               \$$$$$$  |                                    \$$$$$$  |
                                                                \______/                                      \______/ 

''')

slow_print("""
  Hello, and welcome to the magical Birthday Fairy game. Today must be your Birthday, so we're going to have some fun together. 
  If this is your first time playing, perhaps you'd like to see a few instructions and pointers? Y/N

""")
b = input(Orange+">>"+White)
os.system('clear')
if b == "y":
  slow_print(Cyan+"When you see '*' please press enter")
  input("*")
  os.system('clear')
if b == "y":
  slow_print(White+'''
  You have been designated as the 'Birthday Fairy'. All other people who share the same birthday have made some birthday wishes. 
  As the birthday Fairy, you have to decide whether to grant them their wish, or keep all their wishes for your own enjoyment.
  
  Well, enough of all this.... What's your name, Birthday Fairy?
  
  ''')
if b == "n":
  slow_print("Enter a name")
nad = input(Green+"Fairy ")
name = "Fairy "+nad
slow_print(White+"Nice to meet you "+Green+name+White+"! It's time for you to have some fun.")
input("*")


while True:
  os.system('clear')
  if rep < -20:
    slow_print(Red+"You did such a bad job, the Fairy Godmother has taken you off of Birtjday Fairy duties. Now, go to your room")
    break
  slow_print(Green+"Reputation: "+str(rep))
  slow_print(Green+"Fairy Coins: "+str(money))
  slow_print(White+"\nCommands")
  slow_print("[1] Decide Birthday Wishes")
  slow_print("[2] Buy Items")
  slow_print("[3] Answer Prayers")
  slow_print("[4] End Game")
  ch = input(Orange+">>"+White)
  if ch == "4":
    break
  if ch == "3":
    os.system('clear')
    slow_print(White+"A prayer has just arrived!")
    pla = random.choice(prayers)
    slow_print(Orange+"\n"+pla+White)
    print("Will you accept the prayer (y/n)")
    p_y_n = input(Orange+">>"+White).lower()
    print("\n\n")
    if p_y_n == "n":
      if pla == "Please make my toes equal length":
        slow_print(White+"His toes stayed the correct length rather than growing the same length, in later years he was happy about this. "+Green+"Heaven Coins + 1"+White)
        money += 1
      if pla == "Please let me keep my job":
        slow_print("He was later found dead on the street after going homeless. "+Red+"Your reputation has decreased.")
        rep -= random.randrange(stakes, (stakes+3))
      if pla == "Will you make my friend have ebola so I don't have to visit her basketball game":
        slow_print("She ended up having to go to her friends basketball game. She was mad the whole time, but you saved her friend's life. "+Green+"Heaven Coins + 1")
        money += 1
      if pla == "Please let me have 1,000,000 V-BuCKs":
        slow_print(White+"He ended up stealing his moms credit card and making the purchase, him and his mom are now homeless. "+Red+"Your reputation decreased"+White)
      if pla == "Please make my husband have bigger muscles":
        slow_print(White+"She learned to live with her husbands small muscles. "+Green+"Heaven Coins + 1"+White)
        money += 1
    if p_y_n == "y":
      if pla == "Please make my toes equal length":
        slow_print(White+"His toes grew to equal lengths. All of his future girlfriends left him for this reason. "+Red+"Your reputation decreased.")
        rep -= random.randrange(stakes, (stakes+3))
      if pla == "Please let me have 1,000,000 V-BuCKs":
        slow_print(White+"He randomly woke up with 1,000,000 V-BuCkS, his mother was glad since he didn't rob her for V-BuCkS."+Green+" Heaven Coins + 1"+White)
        money += 1
      if pla == "Please let me keep my job":
        slow_print(White+"He kept his job and had a good life. "+Green+"Heaven Coins + 1")
        money += 1
      if pla == "Will you make my friend have ebola so I don't have to visit her basketball game":
        slow_print("Her friend got ebola and died. She never had a basketball game for her to attend. "+Red+"Your reputation decreased."+White)
        rep -= random.randrange(stakes, (stakes+3))
      if pla == "Please make my husband have bigger muscles":
        slow_print(White+"Her husbands muscles got so big that there was not a pair of clothe that fits him. "+Red+"Your reputation decreased"+White)
    input("*")
  if ch == "2":
    os.system('clear')
    slow_print(White+"Items:")
    print(White+"[1] Paper")
    print(Green+"INFO: Cost 5 heaven coins, makes you think faster, increases average pay by 1$.")
    print(White+"[2] Weights")
    print(Green+"INFO: Cost 7 heaven coins Makes God pay less attention to your work")
    print(White+"[3] Tuxedo")
    print(Green+"INFO: Cost 14 heaven coins. Makes you look more professional, and increases your average pay by $2")
    choice = input(Orange+">>"+White)
    os.system('clear')
    if choice == "3":
      if money >= 14:
        money -= 14
        slow_print(White+"You bought a tuxedo to up your professional look. Your pay was increased by $2.")
        pay_inc += 2
      else:
        slow_print("You don't have the money for this fancy object.")
    if choice == "2":
      if money >= 7:
        slow_print("You bought weights, you big muscles make god think you'll do a better job!")
        money -= 7
        if stakes > 2:
          stakes -= 3
        else:
          if stakes > 0:
            stakes -= 1
      else:
        slow_print("You don't have enough money to afford expensive items like this.")
      input("*")
    if choice == "1":
      if money >= 5:
        slow_print("You bought "+Green+"Paper"+White+" Your expected pay has been increased!")
        pay_inc += 1
        money -= 5
      else:
        slow_print("You are too poor for expensive things!")
      input("*")
  if ch == "1":
    os.system('clear')
    goal = random.choice(goals)
    holiness = random.randrange(-100,100)
    caus_of_dea = random.choice(deaths)
    tmoney = random.randrange(-10000,2000000)
    looks = random.randrange(-100,100)
    age_dead = random.randrange(18,100)
    if age_dead < 18:
      tmoney = 0
    if holiness > random.randrange(-10,10):
      p = random.randrange(5,15)
    else:
      p = random.randrange(1,5)
    good_deads = random.randrange((p-5),p)
    if good_deads < 0:
      good_deads = 1
    bad_deads = random.randrange(0,10)
    tname = random.choice(tnames)+random.choice(lnames)
    slow_print(White+"It's " + tname+White + "'s Birthday \n")
    slow_print(Green+"Holiness: "+str(holiness))
    slow_print(Green+"Total Good Deads: "+str(good_deads))
    slow_print(Green+"Total Bad Deads: "+str(bad_deads))
    slow_print(Green+"Money: $"+str(tmoney))
    slow_print(Green+"Looks: "+str(looks)+"/100")
    slow_print(Green+"Age this Birthday: "+str(age_dead))
    slow_print(Orange+"\nFavorite life experience "+caus_of_dea)
    slow_print(Orange+"Goal in life: "+goal)
    slow_print(White+"\nYou make the choice, is there fate [1] Heaven or [2] Hell")
    h_or_he = input(Orange+">>"+White)
    if h_or_he == "1":
      slow_print("\nYou sent them to "+Green+"Heaven"+White+"!")
      if holiness < random.randrange(-10,10) and bad_deads > good_deads:
        rep -= random.randrange(stakes,(stakes+5))
        slow_print("Your reputation was damaged from making a bad decision. You will not be getting paid")
      elif age_dead < 10:
        slow_print("\nYou made the right choice, children go straight to heaven.")
        rep += random.randrange(1,4)
      elif good_deads == bad_deads:
        slow_print("God was happy to have another invited into heaven!")
        rep += 1
      elif holiness > random.randrange(1,10) and good_deads > bad_deads:
        rep += random.randrange(1,4)
        hbucks = random.randrange(pay_inc,(pay_inc + 4))
        money += hbucks
        slow_print("God was proud of your decision, your reputation went up and you were awarded "+Green+str(hbucks)+" Heaven Coins"+White+"!")
      else:
        slow_print("Your decision was mediocre")
        rep += 1
    elif h_or_he == "2":
      slow_print("\nYou sent them to "+Red+"Hell"+White+"!")
      if holiness < random.randrange(-10,10) and bad_deads > good_deads:
        rep += random.randrange(1,4)
        hbucks = random.randrange(pay_inc,(pay_inc + 4))
        money += hbucks
        slow_print(White+"God was proud of your decision. He has awarded you "+Green+str(hbucks)+" Heaven Coins"+White+"! Your reputation increased.")
      elif good_deads == bad_deads:
        slow_print("God would've rather you sent them to heaven, because, the more the merrier!")
        rep -= stakes
      elif age_dead < 10:
        rep -= random.randrange(stakes,(stakes+4))
        slow_print("You lost respect for sending a child to hell!")
      elif holiness > random.randrange(-10,10) and good_deads > bad_deads:
        rep -= random.randrange(stakes,(stakes+4))
        slow_print("Your reputation was damaged for making a poor decision, you will not earn any Heaven Coins today.")
      else:
        slow_print("God didn't care enough to judge your opinion, he was proud of you for taking care of business")
        rep += 1
    else:
      slow_print("You dipped on that person, you were in fear of making a bad decision.")
    stakes += 1
    input("*")

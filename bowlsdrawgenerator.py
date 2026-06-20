# for bowls coz i want to.

import random
selected_name = ""
skips_names = []
threes_names = []
twos_names = []
leads_names = []
total_teams = 4
modes = ["4s","3s","2s","S"]
positions = "Lead","Two","Three","Skip"

mode = ""

total_teams = int(input("How many teams?"))

while mode not in modes:
    mode = input("4s,3s,2s or Singles(S):")

#
# GETS THE PLAYERS.
#
while len(leads_names) < total_teams:
        name = input("Enter the lead/player's name.").strip()
        leads_names.append(name)
        print("Added Player " + name)
if mode == "3s" or mode == "4s":
    while len(twos_names) < total_teams:
        name = input("Enter the twos name.").strip()
        twos_names.append(name)
        print("Added Player " + name)
if mode == "4s":
    while len(threes_names) < total_teams:
        name = input("Enter the threes name.").strip()
        threes_names.append(name)
        print("Added Player " + name)
if mode != "S":
    while len(skips_names) < total_teams:
        name = input("Enter the skips name.").strip()
        skips_names.append(name)
        print("Added Player " + name)
        
if mode == "4s":
    #INPUT PLAYERS.

    for i in range(0,total_teams):     
        skipselection = random.choice(skips_names) 
        threeselection = random.choice(threes_names)
        twoselection = random.choice(twos_names)
        leadselection = random.choice(leads_names)
        print("Team " + str(i+1) + ": " + skipselection + ", " + threeselection + ", "+ twoselection + ", " + leadselection)
        skips_names.remove(skipselection)
        threes_names.remove(threeselection)
        twos_names.remove(twoselection)
        leads_names.remove(leadselection)
elif mode == "3s":
        for i in range(0,total_teams):     
            skipselection = random.choice(skips_names) 
            twoselection = random.choice(twos_names)
            leadselection = random.choice(leads_names)
            print("Team " + str(i+1) + ": " + skipselection + ", "+ twoselection + ", " + leadselection)
            skips_names.remove(skipselection)
            twos_names.remove(twoselection)
            leads_names.remove(leadselection)
elif mode == "2s":
        for i in range(0,total_teams):     
            skipselection = random.choice(skips_names) 
            leadselection = random.choice(leads_names)
            print("Team " + str(i+1) + ": " + skipselection + ", " + leadselection)
            skips_names.remove(skipselection)
            leads_names.remove(leadselection)
elif mode == "S":
        for i in range(0,total_teams):     
            leadselection = random.choice(leads_names)
            print("Player " + str(i+1) + ": " + leadselection)
            leads_names.remove(leadselection)
else:
     print("Something went wrong. Please try again.")
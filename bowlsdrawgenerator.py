# for bowls coz i want to.

import random
selected_name = ""
skips_names = []
threes_names = []
twos_names = []
leads_names = []
total_teams = 4
modes = ["4s","3s","2s","S"]
fours_positions = ["Skip","Three","Two","Lead"]
triples_positions = ["Skip","Two","Lead"]
pairs_positions = ["Skip","Lead"]
singles_positions = ["Player"]

rounds = 0
qualifying = False
random_teams = False
teams = {}

mode = ""

#
# GETS THE PLAYERS.
#
def getPlayers(total_teams,random_teams):
    if random_teams:
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
    else:
         team_number = 0
         while len(teams) < total_teams:
            if mode == "S":
                team_number += 1
                name = input("Enter player " + str(team_number) + "'s name:").strip()
                print("Player " + str(team_number) + ": " + name)
                teams[team_number] = dict(zip(singles_positions,name))
            elif mode == "2s":
                team_number += 1
                skip_name = input("Enter Skip " + str(team_number) + "'s name:").strip()   
                leads_name = input("Enter Lead " + str(team_number) + "'s name:").strip()
                print("Team " + str(team_number) + ": " + skip_name + ", " + leads_name)
                team_members = [skip_name, leads_name]
                teams[team_number] = dict(zip(pairs_positions,team_members))
            elif mode == "3s":
                team_number += 1
                skip_name = input("Enter Skip " + str(team_number) + "'s name:").strip()
                twos_name = input("Enter Two " + str(team_number) + "'s name:").strip()   
                leads_name = input("Enter Lead " + str(team_number) + "'s name:").strip()
                print("Team " + str(team_number) + ": " + skip_name + ", " + twos_name + ", " + leads_name)
                team_members = [skip_name, twos_name, leads_name]
                teams[team_number] = dict(zip(triples_positions,team_members))
            elif mode == "4s":
                team_number += 1
                skip_name = input("Enter Skip " + str(team_number) + "'s name:").strip()
                threes_name = input("Enter Three " + str(team_number) + "'s name:").strip() 
                twos_name = input("Enter Two " + str(team_number) + "'s name:").strip()   
                leads_name = input("Enter Lead " + str(team_number) + "'s name:").strip()
                print("Team " + str(team_number) + ": " + skip_name + ", " + threes_name + ", " + twos_name + ", " + leads_name)
                team_members = [skip_name, threes_name, twos_name, leads_name]
                teams[team_number] = dict(zip(fours_positions,team_members))  

def getRandomTeams(total_teams):

    if mode == "4s":
        for i in range(0,total_teams):     
            skipselection = random.choice(skips_names) 
            threeselection = random.choice(threes_names)
            twoselection = random.choice(twos_names)
            leadselection = random.choice(leads_names)
            print("Team " + str(i+1) + ": " + skipselection + ", " + threeselection + ", "+ twoselection + ", " + leadselection)
            team_members = [skipselection,threeselection,twoselection,leadselection]
            team_number = f"Team: {i+1}"
            teams[team_number] = dict(zip(fours_positions,team_members))
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
                team_members = [skipselection,twoselection,leadselection]
                team_number = f"Team: {i+1}"
                teams[team_number] = dict(zip(triples_positions,team_members))
                skips_names.remove(skipselection)
                twos_names.remove(twoselection)
                leads_names.remove(leadselection)
    elif mode == "2s":
            for i in range(0,total_teams):     
                skipselection = random.choice(skips_names) 
                leadselection = random.choice(leads_names)
                print("Team " + str(i+1) + ": " + skipselection + ", " + leadselection)
                team_members = [skipselection,leadselection]
                team_number = f"Team: {i+1}"
                teams[team_number] = dict(zip(pairs_positions,team_members))
                skips_names.remove(skipselection)
                leads_names.remove(leadselection)
    elif mode == "S":
            for i in range(0,total_teams):     
                leadselection = random.choice(leads_names)
                print("Player " + str(i+1) + ": " + leadselection)
                team_number = f"Team: {i+1}"
                teams[team_number] = dict(zip(singles_positions,leadselection))
                leads_names.remove(leadselection)
    else:
        print("Something went wrong. Please try again.")

#output excel spreadsheet of teams and rounds, even qualifying/ko on another sheet?
#also potential capability to fill in results (unsure of logistics atm)
#add ability to be able to input custom teams, not just rng ones
def generateDraw(teams,rounds):
     print("not yet")

     
     
total_teams = int(input("How many teams?"))

while mode not in modes:
    mode = input("4s,3s,2s or Singles(S):")

is_qualifying = input("Is it qualifying?")
if is_qualifying.upper == "YES" or is_qualifying.upper == "Y":
     qualifying = True

is_random_teams = input("Is it random teams?")
if is_random_teams.upper == "YES" or is_random_teams.upper == "Y":
     random_teams = True

rounds = int(input("How many rounds?"))

getPlayers(total_teams,random_teams)
if random_teams:
    getRandomTeams(total_teams)
generateDraw(teams,rounds)

#print(teams)
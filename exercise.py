# idk why this is even code atp lmao

import random
import math

program = []
selected = {}
biasExercises = []
defaultBias = ['chest','core','core'] 

exercises = {
    'chest': {
        'Push Up': ['10','15','20','failure'],
        'Incline Push Up': ['5','10','15','failure'],
    },
    'shoulder': {
        'Pike Pushups': [5,'failure'],
        'Handstand Pushups': [3,4,5,'failure']
    },
    'tricep': {
        'Floor Dips': [10,15,'failure'],
        'Diamond Pushups': [5,10,15,'failure']
    },
    'back': {
        'Lying Row': [10,15,'failure']
    },
    'bicep': {
        'Reverse Incline Pushup': [10,15,'failure']
    },
    'legs': {
        'Lunges': ['10 each side','failure'],
        'Squats': [10,15,'failure']
    },
    'core': {
        'Hollow Hold': ['20s', '30s','failure'],
        'Crunches': [10,15,'failure'],
        'Reverse Crunches': [10,15,'failure'],
        'Mountain Climbers': ['10 each side','20 each side','30 each side','failure'],
    },
    'combo': {
        'Plank': ['30s','1min','failure'],
        'Knee Ups': [20,30,'failure'],
        'Star Jumps': [50,75,100],
        'Burpees': [5,10,'failure']
    }
}

def generateRandomExercises():
    for outer_key, inner_dict in exercises.items():
        key, value = random.choice(list(inner_dict.items()))
        selected[outer_key] = {key: value}

def addBias(bias):
    counter = 0
    for b in bias:
        chosen = b + str(counter)
        biased = exercises[b]
        key, value = random.choice(list(biased.items()))
        selected[chosen] = {key: value}
        counter += 1

def appendExercises():
    for s in selected.items():
        t = str(s)
        clean = t.replace("'", "").replace("{", "").replace("}", "").replace(")", "").replace("]", "").replace("(","").replace("[","")
        parts = [p.strip() for p in clean.split(",")]
        muscle = parts[0]
        exercise = parts[1].split(":")
        exercisereal = exercise[0]
        reps1 = exercise[1]
        reps = parts[2:]
        reps.append(reps1)
        realreps = []
        for r in reps:
            q = r.replace(' ', '')
            realreps.append(q)
        program.append("Do " + exercisereal + " for " + str(random.choice(realreps)) + " reps.")

def displayAndShuffleProgram():
    random.shuffle(program)
    for p in program:
        print(p)

#------------------------------------------------------------------------------------------

for d in defaultBias:
    biasExercises.append(d)

done = False
while not done:
    bias = input("Name an exercise to bias, use the non-plural form. Keep going until done, then select any key to continue.")
    if bias in exercises:
        biasExercises.append(bias)
    else:
        done = True

#print(biasExercises)

generateRandomExercises()
if len(biasExercises) > 0:
    addBias(biasExercises)
appendExercises()
displayAndShuffleProgram()
# idk why this is even code atp lmao

import random
import math

exercises = {
    'chest': ['Push Up','Incline Pushup'],
    'shoulder': ['Pike Pushups', 'Handstand Pushups'],
   'tricep': ['Floor Dips','Diamond Pushups'],
    'bicep': ['Inverted Row'],
    'back': ['Inverted Row'],
    'legs': ['Lunges','Squat'],
    'core': ['Mountain Climbers','Side Plank','Hollow Hold','Reverse Crunches','Crunches'],
    'combo': ['Plank','Star Jumps','Burpees','Knee Ups']
}
reps = [5,10,15,20,"failure"]

result = {key: random.choice(values) for key, values in exercises.items()}
count = 1
for r in result.items():
    s = str(r)
    s = s.split(',')
    exercise = s[1].strip(" ')") 
    print("Exercise " + str(count) + " : " + exercise + " for " + str(random.choice(reps)) + " reps.")
    count += 1
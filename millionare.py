import random
import requests #using the-trivia-api
import sys

#add text based high scores aswell

def choose_question(difficulty):
    url = f"https://the-trivia-api.com/v2/questions?difficulties={difficulty}"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to fetch questions: {response.status_code}")
        return None
    #print(response.json())
    data = response.json()

    if not data:
        print("No questions received from the API.")
        return None
    
    filter_data = [d for d in data if d['difficulty'] == difficulty]
    relevant_info = []
    selected_question = random.choice(filter_data)

    incorrect_answers = selected_question.get('incorrectAnswers', [])
    correct_answer = selected_question.get('correctAnswer', None)
    question_text = selected_question.get('question', {}).get('text', None)

    if incorrect_answers and correct_answer and question_text:
        relevant_info.extend(incorrect_answers)
        relevant_info.append(correct_answer)
        relevant_info.append(question_text)
    else:
        print("lolol no data loser")
    return relevant_info

def main_game():
    money_earned = 0
    question_number = 1
    money_banked = 0 #banks at 1k then 32k
    money_values = [100, 200, 300, 500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 125000, 250000, 500000, 1000000]
    lifelines = ["50-50", "Phone A Friend", "Ask The Audience", "Ask The Host"]
    abcd = ["A","B","C","D"]
    eliminated = False # for now until better way of implementing
    difficulty = "easy"

    print("Welcome to Who Wants to be a Millionaire!")

    if eliminated == False:  
        info = choose_question(difficulty)

        correct_letter = ""
        correct_answer = info[3]
        answers = info[:4]
        random.shuffle(answers)

        print("Question "+ str(question_number) + ":")
        print("You have earned $" + str(money_earned) + ", and banked $" + str(money_banked) + ".")
        print(info[4])
        for a in range(4):
            print(abcd[a] + ": " + answers[a])
            if answers[a] == correct_answer:
                correct_letter = abcd[a]

        guess = input("Type the letter, or use 'L' for a lifeline: ")
        if guess == 'L' or guess == 'l':
            print("L")
        elif guess in ['A', 'B', 'C', 'D']:
            guess = guess.capitalize()
            if guess == correct_letter:
                print("Correct!")
            else:
                print("Game over. You earned $" + str(money_earned) + ", but you banked $" + str(money_banked) + ".")
        else:
            print("Invalid input. Please try again.")
    else:
        sys.exit("a")



main_game()

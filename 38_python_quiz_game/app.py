def new_game():
    guesses = []
    correct_guesses = 0
    current_question = 1
    question_number = 1 
    
    for key in questions: 
        print("--------------------")
        print(key)
        for i in options[question_number-1]: 
            print(i)
        guess = input("Ans => ").upper()
        guesses.append(guess) 
        correct_guesses =+ check_answer(questions.get(key), guess)
        question_number += 1
        
    display_score(correct_guesses, guesses)

def check_answer(answer, guess): 
    if answer == guess: 
        print("CORRECT")
        return 1
    else: 
        print("WRONG")
        return 0

def display_score(correct_guesses, guesses): 
    print("--------------------")
    print("Result: ")
    
    print("Answers: ", end="")
    for i in questions: 
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses: 
        print(i, end=" ")
    print()
    
    score = (correct_guesses/len(questions))*100 
    
    print("Your Final Score is: " + str(score) + "%")

def play_again(): 
    response = input("Play Again?: (yes / no)").upper()
    
    if response == "YES": 
        return True 
    else: 
        return False

questions = {
    "Who created Python?: ": "A", 
    "What year was python created?: ": "B", 
    "Python is tributed to which comedy group? ": "C", 
    "Is The Earth Round?": "A"
}

options = [
    ["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"], 
    ["A. 1989", "B. 1991", "C. 2000", "D. 2016"], 
    ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"], 
    ["A. Yes", "B. No", "C. Sometimes", "D. What's Earth?"]
]

new_game() 

while play_again(): 
    new_game()
        
print("Bye...")

from datetime import datetime

questions = [
    ("What is the capital of Nepal: ", "kathmandu"),
    ("Which subject should you not cheat in, col100 or apl100: ", "col100"),
    ("On a scale of 1 to 10, how depressed do you think I am? (Hint: I, too, study in IITD. ONLINE.): ", "10"),
    ("yes/no: Am I stupid for putting thought in random questions on a random file in a random assignment: ", "yes")
]

def quiz_me():
    print("Answer the questions asked. Do not use any uppercase letters.")
    score = 0
    
    for i in range(len(questions)):
        ans = input(f"{i+1}. {questions[i][0]}")
        
        if ans == questions[i][1]:
            score += 1
            print("Correct! Your score is now", score)

        else:
            print("Wrong answer :( your score is stuck at", score)

def main():
    start = datetime.now()
    quiz_me()

    print(f"Congratulations! you successfully wasted {(datetime.now()-start).seconds} seconds of you life!", )
import random
import json
import datetime

secret = random.randint(1, 5)
attempts = 0
username = str(input("What is your name: "))
#score_data = {"attempts": attempts, "date": datetime.datetime.now()}
#hogy kell a json-ba soronkent irni??
with open("score_list.json", "r") as score_file:
    score_list = json.loads(score_file.read())
    print("Top scores: " + str(score_list))

for score_dict in score_list:
   print(str(score_dict["attempts"]) + " attempts, date: " + score_dict.get("date") + " secretnumber: "
         + (str(score_dict.get("secretnumber"))) + " username: " + (str(score_dict.get("username"))))
 #        + " wrong tips " + (str(score_dict.get("wrongtips"))))

while True:

    guess = int(input("Guess the secret number (between 1 and 5): "))
    attempts += 1

    if guess == secret:
        score_list.append({"attempts": attempts, "date": str(datetime.datetime.now()), "secretnumber": str(secret),
                           "username": str(username)})

        with open("score_list.json", "w") as score_file:
            score_file.write(json.dumps(score_list))
        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")
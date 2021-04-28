import random
import datetime

secret = random.randint(1, 5)
attempts = 0
username = str(input("What is your name: "))
with open("score.txt", "r") as score_file:
    best_score = int(score_file.read())
    print("Top scores: " + str(best_score))

# for score_dict in score_list:
#    print(str(score_dict["attempts"]) + " attempts, date: " + score_dict.get("date") + " secretnumber: "
#          + (str(score_dict.get("secretnumber"))) + " username: " + (str(score_dict.get("username"))))
while True:

    guess = int(input("Guess the secret number (between 1 and 5): "))
    attempts += 1

    if guess == secret:
        # score_list.append({"attempts": attempts, "date": str(datetime.datetime.now()), "secretnumber": str(secret),
        #                    "username": str(username)})
        if attempts < best_score:
            with open("score.txt", "w") as score_file:
                score_file.write(str(attempts))
        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")
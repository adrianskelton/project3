import gspread
import questions
# ascii artwork for the game
import artwork
from google.oauth2.service_account import Credentials
import json
import os
from colorama import init, Fore, Back, Style

# Every Google account has as an IAM (Identity and Access Management)
# configuration which specifies what the user has access to.
# The SCOPE lists the APIs that the program should access in order to run.

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

creds = json.load(open("creds.json"))
CREDS = Credentials.from_service_account_info(creds)
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("animal_game")
worksheet = SHEET.worksheet("scoreboard")

global score
score = 0

"""
Function to clear the screen
"""


def clearScreen():
    os.system("clear")


# Sort sheet A -> Z by column 'B'
worksheet.sort((2, "des"))
# This sorts the excell scoreboard sheet and deletes some rows
clear_range = "A13:A20"
empty_values = [[""]] * 8  # Create an empty list with 8 rows
worksheet.update(clear_range, empty_values)


"""
The set of 15 questions that is used during the game. Questions
imported from questions.py file. Source of questions credited in the
 readme.
"""
quiz_data = questions.quiz_data

"""
The start of the game asking the player to enter their name
"""


def game_start():
    clearScreen()
    asci_art = artwork.artwork

    print(asci_art)

    global playername
    playername = input(
        " Welcome to the amazing animal quiz game\n Please enter your name\n"
    )
    if len(playername) <= 20 and len(playername) >= 1:
        update_scoreboard([playername], "scoreboard")
        option_screen()
        return
    else:
        input("Please enter a name shorter than 20 characters\n")


"""
The option screen function is defined below giving the four choices
for the player after they have entered their player name
"""


def option_screen():
    global choice
    choice = ""
    while True:
        print(f'\033[2J')
        print("Welcome " + playername + "." +
              " You now have the following options: \n")
        print("1) Play the quiz.\n")
        print("2) Read the rules.\n")
        print("3) High scores.\n")
        print("4) Exit to start.\n")

        choice = input("Enter choice:  ")
        choice = choice.strip()

        if choice == "1":
            print("Quiz starting, good luck!")
            run_quiz(quiz_data)
        elif choice == "2":
            rules()
        elif choice == "3":
            show_scoreboard()
        elif choice == "4":
            print("Game Exited")
            break
        else:
            print("ERROR! Invalid option please select 1, 2, 3 or 4\n ")
            input("Press Enter to continue...")


# OPTION 2 Rules of the game
def rules():
    print(f'\033[2J')
    print("=========================================================")
    print("HOW TO PLAY THE ANAZING ANIMAL QUIZ")
    print("Take the quiz to test your animal general knowledge.")
    print("There are 15 multiple choice questions.")
    print("Select your answer by typing 'a', 'b', 'c' or 'd'\n"
          "and pressing Enter afterwards.\n")
    input("Press Enter to continue...")
    print("=========================================================")


"""
This function updates the animal game worksheet
"""


def update_scoreboard(new_row, worksheet):
    """
    Update the animal game worksheet,
    adding a new row with the list data provided.
    """
    worksheet_to_update = SHEET.worksheet(worksheet)

    # adds new row to the end of the current data
    worksheet_to_update.append_row(new_row)

    print(f"{worksheet} worksheet updated successfully\n")


def update_final_score():
    worksheet.update_cell(12, 2, "")


"""
Function to show the scoreboard
This is called in the main menu at the start when selected by the user
"""


def show_scoreboard():
    print("TOP 10 SCORES - ANIMAL QUIZ\n")
    worksheet = SHEET.worksheet("scoreboard")
    scoreboard_players = worksheet.col_values(1)[
        1:11
    ]  # Assuming players are in column A starting from row 2
    scoreboard_scores = worksheet.col_values(2)[
        1:11
    ]  # Assuming scores are in column B starting from row 2

    for player, score in zip(scoreboard_players, scoreboard_scores):
        print("PLAYER: {} || POINTS: {} ||".format(player, score))

    input("Press Enter to continue...")


"""
My function is called once the game has ended and prints out if
the score was good or bad based on the users final score"
"""


def score_grading(final_score):
    print("======================================================\n")
    print(f"Your score was {final_score}")
    if final_score <= 7:
        print("This was less than average, you could do better")
    elif final_score >= 8:
        print("That's abouve average, well done!")
    gameover_option()


"""
My function called once the game is over to ask the player what they
want to do next
"""


def gameover_option():
    print("======================================================\n")
    print("Play again? Press p and enter otherwise press r and enter to return to the main menu")
    option = (input("Make your selection now..."))
    if option not in ["p", "r"]:
        print("Incorrect choice. Please enter p or r and press enter")
    elif option == "p":
        print("quiz function")
    elif option == "r":
        print("return to restart of game")


"""
Runs through questions in the quiz and answers get user's input and changes
the score by 1 if correct depending on the answer.
"""


def run_quiz(quiz_data):
    score = 0
    final_score = 0
    for guess in quiz_data:
        user_answer = ""
        while user_answer not in ["A", "B", "C", "D"]:
            print(f'\033[2J')
            print("=========================================================")
            print(f"{guess['question']}")
            print("=========================================================")

            for key, value in guess["answers"].items():
                print(f"\t{key}: {value}")
            user_answer = input("Select answer and press enter...\n")
            user_answer = user_answer.upper()

            if user_answer not in ["A", "B", "C", "D"]:
                print("ERROR! Please select 'A', 'B', 'C', or 'D' as an answer.\n")

            else:
                if user_answer == guess["correct_answer"]:
                    # smiling face with sunglasses
                    print(Fore.GREEN + 'Correct! ''\033[39m')
                    print("\N{smiling face with sunglasses} ")
                    print(f"{guess['fact']}")
                    score += 1
                    input("Press Enter to continue...")
                else:
                    print(Fore.RED + 'Incorrect! ''\033[39m')
                    print(
                        "\N{loudly crying face}",
                        "Better luck with the next question\n")
                    print(f"{guess['fact']}")
                    input("Press Enter to continue...")

    final_score = score
    score_grading(final_score)
    input("Press Enter to continue...")
    worksheet = SHEET.worksheet("scoreboard")
    # Update final score into spreadsheet
    worksheet.update_cell(13, 2, final_score)
    # Sort sheet A -> Z by column 'B'
    worksheet.sort((2, "des"))
    # game_start()


game_start()

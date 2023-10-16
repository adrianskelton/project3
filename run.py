import gspread
from google.oauth2.service_account import Credentials
import json
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


# Sort sheet A -> Z by column 'B'
worksheet.sort((2, "des"))
# This sorts the excell scoreboard sheet and deletes some rows
clear_range = "A13:A20"
empty_values = [[""]] * 8  # Create an empty list with 8 rows
worksheet.update(clear_range, empty_values)

# import questions
"""
The set of 15 questions that is used during the game. Source of 
questions credited in the readme.
"""
quiz_data = [
    {
        #question 1
        "question": "What animal has the longest lifespan?",
        "answers": {
            "A": "Locust",
            "B": "Elephant",
            "C": "Blue Whale",
            "D": "Giant Tortoise",
        },
        "correct_answer": "D",
        "fact": "The lifespan of the giant tortoise is about 150 years,"
        "making it the longest-living animal on the planet."
        "In captivity, some giant tortoises have lived as long as 177 years.",
    },
    {
        "question": "What is the only mammal capable of true flight?",
        "answers": {
            "A": "Bat",
            "B": "Ocelot",
            "C": "Hummingbird",
            "D": "Flying Squirrel",
        },
        "correct_answer": "A",
        "fact":
        "Bats are the only mammals capable of true flight."
        "A bat's wing is constructed very much like the human hand,"
        "with extremely elongated fingers and membranes stretched between."
        "Bats can be found almost anywhere in the world except for areas"
        "with extreme temperatures such as polar regions and deserts. "
        "In fact, there are almost 1,000 species of bats worldwide,"
        "ranging in size from less than an inch to almost six feet. "
        "Many species of bats are considered endangered.",
    },
    {
        "question": "What is the fastest bird in the world?",
        "answers": {
            "A": "PEREGRINE FALCON",
            "B": "SPINE-TAILED SWIFT",
            "C": "HARPY EAGLE",
            "D": "HORNED SUNGEM",
        },
        "correct_answer": "A",
        "fact":
        "Able to dive at almost 200 miles per hour, the peregrine falcon is"
        "not only the fastest flying bird in the world, but the fastest animal"
        "on earth. Although several subspecies, including the Arctic peregrine"
        " falcon and the American peregrine falcon, were once considered "
        "endangered, they have made a successful recovery and are no longer "
        "listed on the endangered species list. The peregrine falcon can be "
        "found on every continent except Antarctica.",
    },
    
]
# Start screen of the game asking the players name


def game_start():
    artwork = """\
   / \   _ __ (_)_ __ ___   __ _| |  / _ \ _   _(_)____
  / _ \ | '_ \| | '_ ` _ \ / _` | | | | | | | | | |_  /
 / ___ \| | | | | | | | | | (_| | | | |_| | |_| | |/ / 
/_/   \_\_| |_|_|_| |_| |_|\__,_|_|  \__\_\\__,_|_/___|
                    """

    print(artwork)

    global playername
    playername = input(
        "Welcome to the amazing animal quiz game\n Please enter your name\n"
    )
    if len(playername) <= 20 and len(playername) >= 1:
        update_scoreboard([playername], "scoreboard")
        option_screen()
        return
    else:
        input("Please enter a name shorter than 20 characters\n")


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
    print("Select your answer by typing 'a', 'b', 'c' or 'd' and pressing Enter afterwards.\n")
    input("Press Enter to continue...")
    print("=========================================================")

# This function updates the scoreboard


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

def score_grading(final_score):
    if final_score <= 2:
        print("your score was less than average could do better")
    elif final_score >= 2:
        print("your score was good, well done!")
    input("Press Enter to continue...")
    print("Game is now restarting")


def run_quiz(quiz_data):
    """
    Runs through questions in the quiz and answers get user's input and changes the score by 1 if correct depending on the answer.
    """
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

            if user_answer not in guess["answers"]:
                print("ERROR! Please select a, b, c, or d as an answer.\n")

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
    print(f"Well done your score was {final_score}")
    score_grading(final_score)
    input("Press Enter to continue...")
    worksheet = SHEET.worksheet("scoreboard")
    # Update final score into spreadsheet
    worksheet.update_cell(13, 2, final_score)
    # Sort sheet A -> Z by column 'B'
    worksheet.sort((2, "des"))
    # game_start()


game_start()

import gspread
import questions  # located in questions.py
import artwork    # ascii artwork for the game artwork.py
from google.oauth2.service_account import Credentials
import json
import os
from colorama import init, Fore, Back, Style  # color styling

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
score = 0  # initialize the score


def line_break():
    """
    makes the code more readable
    """
    print("=========================================================")


quiz_data = questions.quiz_data  # initialize quiz data questions


def game_start():
    """
    The start of the game asking the player to enter their name
    """
    # Sort sheet A -> Z by column 'B'
    worksheet.sort((2, "des"))
    # This sorts the excel scoreboard sheet and deletes some rows
    clear_range = "A13:A20"
    empty_values = [[""]] * 8  # Create an empty list with 8 rows
    worksheet.update(clear_range, empty_values)
    # Specify the row numbers you want to delete (in this case, rows 13 to 20)
    rows_to_delete = list(range(13, 20))
    # Delete the specified rows
    for row in reversed(rows_to_delete):
        worksheet.delete_rows(row)
    print(f'\033[2J')
    asci_art = artwork.artwork
    print(asci_art)

    while True:
        global playername
        playername = input(
            " Welcome to the amazing animal quiz game\n" +
            Fore.BLUE + " Please enter your name\033[39m\n"
        )
        if len(playername) <= 20 and len(playername) >= 1:
            update_scoreboard([playername], "scoreboard")
            option_screen()
            break  # exit the loop if the name is valid
        else:
            if playername:  # Checks if something is entered
                input("Please enter your name\n")
            else:
                print(
                    Fore.RED + "ERROR!\033[39m Please enter a name with at"
                    "least one but less than 20 characters.\n")


def option_screen():
    """
    The option screen function is defined below giving the four choices
    for the player after they have entered their player name
    """
    global choice
    choice = ""
    while True:
        print(f'\033[2J')
        print(Fore.BLUE + "Welcome " + playername + "." +
              " You now have the following options: \033[39m\n")
        print("1) Play the quiz.\n")
        print("2) Read the rules.\n")
        print("3) High scores.\n")
        print("4) Exit to start.\n")

        choice = input(Fore.BLUE + "Enter choice:  \033[39m\n")
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
            print(Fore.RED + "ERROR!\033[39m Invalid option please "
                  "select 1, 2, 3 or 4\n ")
            input(Fore.BLUE + "Press Enter to continue...\033[39m")


def rules():
    """
    Option 2 called from the game menu option. This function
    prints out the rules of the game.
    """
    print(f'\033[2J')
    line_break()
    print(Fore.BLUE + "HOW TO PLAY THE AMAZING ANIMAL QUIZ\033[39m")
    line_break()
    print("Take the quiz to test your animal general knowledge.")
    print("There are 15 multiple choice questions.")
    print("Select your answer by typing 'a', 'b', 'c' or 'd'\n"
          "and pressing Enter afterwards.\n")
    line_break()
    input(Fore.BLUE + "Press Enter to continue...\033[39m")


def update_scoreboard(new_row, worksheet):
    """
    Update the animal game worksheet,
    adding a new row with the list data provided.
    """
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(new_row)
    print(f"{worksheet} worksheet updated successfully\n")


def show_scoreboard():
    """
    Function to show the scoreboard
    This is called in the main menu at the start when selected by the user
    """
    print("TOP 10 SCORES - ANIMAL QUIZ\n")
    worksheet = SHEET.worksheet("scoreboard")
    scoreboard_players = worksheet.col_values(1)[
        1:11
    ]
    scoreboard_scores = worksheet.col_values(2)[
        1:11
    ]
    for player, score in zip(scoreboard_players, scoreboard_scores):
        print("PLAYER: {} || POINTS: {} ||".format(player, score))
    input(Fore.BLUE + "Press Enter to continue...\033[39m")


def score_grading(final_score):
    """
    My function is called once the game has ended and prints out if
    the score was good or bad based on the users final score
    """
    line_break()
    print(Fore.BLUE + "GAME OVER!\033[39m")
    print(Fore.BLUE + f"Your score was {final_score}\033[39m")
    if final_score <= 7:
        print(Fore.BLUE +
              "This was less than average, you could do better\033[39m")
    elif final_score >= 8:
        print(Fore.BLUE + "That's above average, well done!\033[39m")
    gameover_option()


def gameover_option():
    """
    My function called once the game is over to ask the player what they
    want to do next
    """
    line_break()
    print("\nPlay again? Press p and enter otherwise press q to quit")
    option = (input("Make your selection now..."))
    if option not in ["p", "q"]:
        print("Incorrect choice. Please enter p or q and press enter")
    elif option == "q":
        print(f'\033[2J')
        print("Thank you for playing, enjoy your day further!")
        print("If you want to play again click Run Program above")
    elif option == "p":
        global score
        score = 0  # Reset the score
        game_start()  # Start a new game


def run_quiz(quiz_data):
    """
    Runs through questions in the quiz and answers get user's input and changes
    the score by 1 if correct depending on the answer
    """
    global score
    score = 0
    final_score = 0
    for guess in quiz_data:
        user_answer = ""
        while user_answer not in ["A", "B", "C", "D"]:
            line_break()
            print(f"{guess['question']}")
            line_break()

            for key, value in guess["answers"].items():
                print(f"\t{key}: {value}")
            user_answer = input(Fore.BLUE + "Select answer and press"
                                " enter...\033[39m\n")
            user_answer = user_answer.upper()

            if user_answer not in ["A", "B", "C", "D"]:
                print(
                    Fore.RED + "ERROR!\033[39m Please select 'A', 'B',"
                               " 'C', or 'D' as an answer.\n")

            else:
                if user_answer == guess["correct_answer"]:
                    print(Fore.GREEN + 'Correct! ''\033[39m')
                    print("\N{smiling face with sunglasses} ")
                    print(f"{guess['fact']}")
                    score += 1
                    input(Fore.BLUE + "Press Enter to continue...\033[39m")
                else:
                    print(Fore.RED + 'Incorrect! ''\033[39m')
                    print(
                        "\N{loudly crying face}",
                        "Better luck with the next question\n")
                    print(f"{guess['fact']}")
                    input(Fore.BLUE + "Press Enter to continue...\033[39m")
    final_score = score
    worksheet = SHEET.worksheet("scoreboard")
    worksheet.update_cell(13, 2, final_score)  # Update final score into sheet
    worksheet.sort((2, "des"))  # Sort sheet A -> Z by column 'B'
    score_grading(final_score)
    input(Fore.BLUE + "Press Enter to continue...\033[39m")


game_start()
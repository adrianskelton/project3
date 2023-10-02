import gspread
from google.oauth2.service_account import Credentials
import json

# Every Google account has as an IAM (Identity and Access Management)
# configuration which specifies what the user has access to.
# The SCOPE lists the APIs that the program should access in order to run.

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

creds = json.load(open('creds.json'))
CREDS = Credentials.from_service_account_info(creds)
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("animal_game")

"""
Terminal based animal quiz game
"""
## Option Screen after the player has entered their name
def option_screen():
    print("Welcome " + PLAYERNAME +"." + " You now have the following options: \n")
    print(f"1) Play the quiz.\n")
    print(f"2) Read the rules.\n")
    print(f"3) High scores.\n")
    print(f"4) Exit to start.\n")

## Rules of the game
##placeholder for rules

PLAYERNAME = input("Welcome to the amazing animal quiz game please enter your name\n")

if len(PLAYERNAME) <= 20:
    print("Entry is valid!")
    option_screen()
else:
    input("Please enter a name shorter than 20 characters\n")   

##def update_score():
def update_scoreboard(new_row, worksheet):
    """
    Update the animal game worksheet,
    adding a new row with the list data provided.
    """
    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)

    # adds new row to the end of the current data
    worksheet_to_update.append_row(new_row)

    print(f"{worksheet} worksheet updated successfully\n")


##print("score updated")

"""
First set of questions
"""

#print("Welcome " + playername + " please select an option below:\n")


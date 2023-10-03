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
playername = ""

"""
First set of questions
"""
quiz_data = [
    {"question": "What animal has the longest lifespan?", 
         
     "answers": {"A": "Locust",
                 "B": "Elephant",
                 "C": "Blue Whale",
		        "D": "Giant Tortoise"},
     "correct_answer": "D", "fact": "The lifespan of the giant tortoise is about 150 years, making it the longest-living animal on the planet. In captivity, some giant tortoises have lived as long as 177 years."},
     
    {"question": "What is the only mammal capable of true flight?",
     "answers": {"A": "Bat",
                 "B": "Ocelot",
                 "C": "Hummingbird",
		         "D": "Flying Squirrel"},
    "correct_answer": "A", "fact": 'Bats are the only mammals capable of true flight. A bats wing is constructed very much like the human hand, with extremely elongated fingers and membranes stretched between. Bats can be found almost anywhere in the world except for areas with extreme temperatures such as polar regions and deserts. In fact, there are almost 1,000 species of bats worldwide, ranging in size from less than an inch to almost six feet. Many species of bats are considered endangered.',
     },

    {"question": "What animal has the longest lifespan?", 
         
     "answers": {"A": "Locust",
                 "B": "Elephant",
                 "C": "Blue Whale",
		        "D": "Giant Tortoise"},
     "correct_answer": "D", "fact": "The lifespan of the giant tortoise is about 150 years, making it the longest-living animal on the planet. In captivity, some giant tortoises have lived as long as 177 years."},
     
    {"question": "What is the only mammal capable of true flight?",
     "answers": {"A": "Bat",
                 "B": "Ocelot",
                 "C": "Hummingbird",
		         "D": "Flying Squirrel"},
    "correct_answer": "A", "fact": 'Bats are the only mammals capable of true flight. A bats wing is constructed very much like the human hand, with extremely elongated fingers and membranes stretched between. Bats can be found almost anywhere in the world except for areas with extreme temperatures such as polar regions and deserts. In fact, there are almost 1,000 species of bats worldwide, ranging in size from less than an inch to almost six feet. Many species of bats are considered endangered.',
     },

]

#Start screen of the game asking the players name
def game_start():
    print("""\

                                       ._ o o
                                       \_`-)|_
                                    ,""       \ 
                                  ,"  ## |   ಠ ಠ. 
                                ," ##   ,-\__    `.
                              ,"       /     `--._;)
                            ,"     ## /
                          ,"   ##    /


                    """)
    global playername
    playername = input("Welcome to the amazing animal quiz game please enter your name\n")
    if len(playername) <= 20:
        print("playername has been entered")

        update_scoreboard([playername], "scoreboard")
        return
    else:
        input("Please enter a name shorter than 20 characters\n")   

    """##Option Screen after the player has entered their name
def option_screen():
        print("Welcome " + playername +"." + " You now have the following options: \n")
        print(f"1) Play the quiz.\n")
        print(f"2) Read the rules.\n")
        print(f"3) High scores.\n")
        print(f"4) Exit to start.\n")""" 

    def option_screen():
        global option_screen
        choice=""
        while True:
            print("Welcome " + playername +"." + " You now have the following options: \n")
            print("1) Play the quiz.\n")
            print("2) Read the rules.\n")
            print("3) High scores.\n")
            print("4) Exit to start.\n")

            choice = input("Enter choice")
            choice = choice.strip()

            if (choice == "1"):
                run_quiz(quiz_data)
            elif(choice == "2"): 
                print("rules link")
            elif(choice == "3"):
                print("high score placeholder")
            elif(choice == "4"): 
                game_start()
                break
            else:
                print("invalid option please try again")

##this function updates the scoreboard
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

##get scoreboard

## Rules of the game
##placeholder for rules

##print("score updated")
def run_quiz(quiz_data):
    """
    Runs through questions in the quiz and answers get users input and changes the score by 1 if correct depending on the answer.
    """
    score = 0
    for guess in quiz_data:
        user_answer = ""
        while user_answer not in ['A', 'B', 'C', 'D']:
            print(f"{guess['question']}")

            for key, value in guess['answers'].items():
                print(f"\t{key}: {value}")
            user_answer = input("what is your answer?\n")
            user_answer = user_answer.upper()

            if user_answer not in guess['answers']:
                print("Please select a, b, c or d as an answer\n")
        
        if user_answer == guess['correct_answer']:
            print(f"Correct!\n")
            print(f"{guess['fact']}")
            score += 1
        else:
            print(f"Sorry thats incorrect, better luck next question\n")
    final_score(score)


#print("Welcome " + playername + " please select an option below:\n")

game_start ()
run_quiz(quiz_data)
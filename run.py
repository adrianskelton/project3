import gspread
from google.oauth2.service_account import Credentials
import json

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

"""
First set of questions
"""
quiz_data = [
    {
        "question": "What animal has the longest lifespan?",
        "answers": {
            "A": "Locust",
            "B": "Elephant",
            "C": "Blue Whale",
            "D": "Giant Tortoise",
        },
        "correct_answer": "D",
        "fact": "The lifespan of the giant tortoise is about 150 years, making it the longest-living animal on the planet. In captivity, some giant tortoises have lived as long as 177 years.",
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
        "fact": "Bats are the only mammals capable of true flight. A bats wing is constructed very much like the human hand, with extremely elongated fingers and membranes stretched between. Bats can be found almost anywhere in the world except for areas with extreme temperatures such as polar regions and deserts. In fact, there are almost 1,000 species of bats worldwide, ranging in size from less than an inch to almost six feet. Many species of bats are considered endangered.",
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
        "fact": "Able to dive at almost 200 miles per hour, the peregrine falcon is not only the fastest flying bird in the world, but the fastest animal on earth. Although several subspecies including the Arctic peregrine falcon and the American peregrine falcon were once considered endangered, they have made a successful recovery and are no longer listed on the endagered species list. The peregrine falcon can be found on every continent except Antarctica.",
    },
    {
        "question": "A newborn kangaroo is about the size of a..?",
        "answers": {
            "A": "Grapefruit",
            "B": "Lima Bean",
            "C": "Watermelon",
            "D": "Plum",
        },
        "correct_answer": "B",
        "fact": "A newborn kangaroo is about 1 inch in length -- approximately the size of a lima bean. Still essentially a fetus, the newborn kangaroo swims through its mother's fur to reach her pouch where it latches onto a teat which swells inside its mouth. The baby kangaroo or joey will remain fused to the teat for four to five weeks. After 7 to 8 months inside its mother's pouch, the infant will venture outside, returning only to feed. In the case of multiple infants belonging to the same mother, each infant feeds only from its own individual teat, and each teat provides a different mix of nutrients depending on the age of that particular infant.",
    },
    {
        "question": "What is the gestation period of a blue whale?",
        "answers": {
            "A": "4-6 Months",
            "B": "10-12 Months",
            "C": "16-18 Months",
            "D": "2 Years",
        },
        "correct_answer": "B",
        "fact": "The gestation period of a blue whale is approximately 10 to 12 months. Usually, only one calf is born at a time, although twins have been reported on rare occasions. Most calves, which weigh about 2 1/2 tons, are born in late fall or winter and will usually stay with their mother for 6 to 8 months until they are weaned.",
    },
    {
        "question": "What is the smallest mammal in the world?",
        "answers": {
            "A": "Bumblebee bat",
            "B": "Pygmy marmoset",
            "C": "Western harvest mouse",
            "D": "Numbat",
        },
        "correct_answer": "A",
        "fact": "The smallest mammal in the world is the bumblebee bat which lives along the River Kwai in western Thailand. An endangered species, the bumblebee bat is not much larger than an actual bumblebee (1.2 in) and weighs less than a penny (0.07 oz). Of course, there are several mammals similar in size to the bumblebee bat, and the designation of which one is actually the smallest can sometimes be contentious. Another animal which is sometimes awarded the title of world's smallest mammal is Savi's pygmy shrew, a tiny insectivore small enough to run through the tunnels of large earthworms. Each day, this pygmy shrew consumes insects and spiders up to 2 to 4 times its own body weight.\n",
    },
    {
        "question": "How far away can a wolf smell its prey??",
        "answers": {
            "A": "Nearly 4 miles/6.4kms",
            "B": "Nearly 2 miles/3.2km",
            "C": "Nearly 1 mile/1.6km",
            "D": "Nearly half a mile/0.8km",
        },
        "correct_answer": "B",
        "fact": "A wolf has two hundred million scent cells inside its nose and can smell 100 times better then a human being. Under favorable conditions, it can smell its prey from about 1.75 miles away.\n",
    },
    {
        "question": "What is the world's most poisonous spider?",
        "answers": {
            "A": "Daddy long legs",
            "B": "Brazilian wandering spider",
            "C": "Brown Recluse",
            "D": "Sydney funnel spider",
        },
        "correct_answer": "B",
        "fact": "According to the Guiness Book of World Records the most poisonous (or venomous) spider in the world is the Brazilian wandering spider (Phoneutria nigriventer) or banana spider. Its venom is so potent that just 0.006 mg (0.00000021 oz) can kill a mouse, making it the most active neurotoxic venom of any known spider.\n",
    },
    {
        "question": "How many times can a hummingbird flap its wings per second?",
        "answers": {"A": "80", "B": "160", "C": "20", "D": "40"},
        "correct_answer": "D",
        "fact": "A hummingbird can flap its wings about 80 times per second, causing an audible humming sound. Due to the unique structure of their wings, hummingbirds can fly left, right, up, down, backwards, or even upside down. They can also hover by flapping their wings in a figure-eight pattern. And their wings aren't the only fast-moving body part -- they have a heart rate of approximately 1,260 beats per minute!",
    },
    {
        "question": "What animal has the highest blood pressure?",
        "answers": {"A": "Giraffe", "B": "Elephant", "C": "Flea", "D": "Blue whale"},
        "correct_answer": "A",
        "fact": "Because of its extremely long neck, the giraffe must rely on its oversized heart (two feet long and twenty-five pounds!) to pump blood all the way to its head. As a result, the giraffe has the highest blood pressure of any animal: 280/180 mmHg (millimeters of mercury) at heart level when prone -- more than twice the blood pressure of an average human. Not surprisingly, because of their high blood pressure, giraffes are prone to heart attacks.",
    },
    {
        "question": "How big is the largest known ant colony?",
        "answers": {
            "A": "3.7 miles",
            "B": "370 miles",
            "C": "3700 miles",
            "D": "37 miles",
        },
        "correct_answer": "C",
        "fact": "The largest recorded contiguous colony of ants in the world stretches 3,700 miles (6,000 kilometres) from northern Italy, through the south of France to the Atlantic coast of Spain, and is made up of a species of Argentine ant (Linepithema humile) introduced into Europe during the 1920s.",
    },
    {
        "question": "How many times does a giant panda poop each day?",
        "answers": {"A": "20", "B": "10", "C": "5", "D": "40 times"},
        "correct_answer": "D",
        "fact": "The average daily diet of a giant panda consists of 20 to 30 lbs of bamboo. Given this voluminous diet, the giant panda defecates up to 40 times a day.",
    },
    {
        "question": "What is the largest of the great apes?",
        "answers": {
            "A": "Western lowland gorilla",
            "B": "Eastern lowland gorilla",
            "C": "Mountain gorilla",
            "D": "Orangutang",
        },
        "correct_answer": "C",
        "fact": "Reaching an average height of 6 feet tall and weighing 400 to 500 pounds, the mountain gorilla is the largest of the great apes. Found only in the mountains of Rwanda, Zaire, and Uganda, mountain gorillas have been victimized by poaching as well as the destruction of much of their natural habitat. Like all other subspecies of gorilla, the mountain gorilla is considered an endangered species.",
    },
    {
        "question": "What makes the Burmese sneezing monkey sneeze?",
        "answers": {"A": "Salt", "B": "Rain", "C": "Bananas", "D": "Danger"},
        "correct_answer": "B",
        "fact": "The Burmese sneezing monkey (Rhinopithecus strykeri), also called the Burmese snub-nosed monkey, is known in local dialects of Lisu people as mey nwoah and Law Waw people as myuk na tok te, both of which mean 'monkey with an upturned face'. Rain allegedly causes it to sneeze due to the short upturned nasal flesh around its nostrils. People from the area report that it sits with its head directed downwards, hiding its face between its knees when it rains.",
    },
    {
        "question": "What colour is spider blood?",
        "answers": {
            "A": "Black",
            "B": "Blue",
            "C": "Yellow",
            "D": "Red",
        },
        "correct_answer": "B",
        "fact": "In humans, oxygen is bound to hemoglobin, a molecule that contains iron and gives blood its red color. In spiders, oxygen is bound to hemocyanin, a molecule that contains copper rather than iron, making their blood blue.",
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
        "Welcome to the amazing animal quiz game please enter your name\n"
    )
    if len(playername) <= 20 and len(playername) >= 1:
        print("playername has been entered")
        update_scoreboard([playername], "scoreboard")
        option_screen()
        return
    else:
        input("Please enter a name shorter than 20 characters\n")


def option_screen():
    global choice
    choice = ""
    while True:
        print("Welcome " + playername + "." + " You now have the following options: \n")
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
            print("invalid option please try again\n ")


# OPTION 2 Rules of the game
def rules():
    print(f"\nWelcome to the animal game quiz {playername}!")
    print("Take the quiz to test your animal general knowledge.")
    print("There are 15 multiple choice questions.")
    print("Select your answer by typing 'a', 'b' or 'c'.\n")
    input("Press Enter to continue...")


def update_scoreboard(new_row, worksheet):  # This function updates the scoreboard
    """
    Update the animal game worksheet,
    adding a new row with the list data provided.
    """
    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)

    # adds new row to the end of the current data
    worksheet_to_update.append_row(new_row)

    print(f"{worksheet} worksheet updated successfully\n")


def update_final_score():
    worksheet.update_cell(13, 2, "")


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
        print("PLAYER: {} POINTS {} ".format(player, score))

    input("Press Enter to continue...")


def run_quiz(quiz_data):
    """
    Runs through questions in the quiz and answers get user's input and changes the score by 1 if correct depending on the answer.
    """
    score = 0
    final_score = 0
    for guess in quiz_data:
        user_answer = ""
        while user_answer not in ["A", "B", "C", "D"]:
            print(f"{guess['question']}")

            for key, value in guess["answers"].items():
                print(f"\t{key}: {value}")
            user_answer = input("what is your answer?\n")
            user_answer = user_answer.upper()

            if user_answer not in guess["answers"]:
                print("Please select a, b, c, or d as an answer\n")

        if user_answer == guess["correct_answer"]:
            # smiling face with sunglasses
            print("\N{smiling face with sunglasses} " " Correct!")
            print(f"{guess['fact']}")
            score += 1
            print(score)
        else:
            print(
                f"Incorrect!",
                "\N{loudly crying face}",
                "Better luck next question\n",
            )
            print(score)
    final_score = score
    print(final_score)
    ##print(f"your final score is"final_score)
    worksheet = SHEET.worksheet("scoreboard")
    worksheet.update_cell(13, 2, final_score)  # Update final score into spreadsheet
    playername = ""
    # Sort sheet A -> Z by column 'B'
    worksheet.sort((2, "des"))
    ##game_start()


game_start()

# ANIMAL QUIZ

Animal-Quiz WAS my third project for Code Institute Full Stack development program. This project is focused on python programming language and also integrates a spreadsheet shared on google drive, I learned a lot during this program such as defininite and indefinite iteration of loops and when to use them apporpriately for example in error handling intil a condition is met or in the quiz game where a set of 15 questions were iterated through.

I also learnt about checking for bugs and using the pep8 python style conventions, which I checked throughout the coding process so that I could remind myself of best practices when it came to spacing, white space and other rules. I tried my best to keep the code clean, readable and have docstrings that were to the point but descriptive enough to convey what the code did. I kept the ascii art and the questions for the quiz in seperate python files and imported them into the main run.py file to keep the main python file looking less cluttered. 

The inspiration for the game came from my two children Axel and Hannah and their love for animal facts and the natural world in general. 


![Animal Quiz website image](https://i.ibb.co/6nx2BN1/screenshot.png)

Visit the live site [here](https://animalgame-470e463a9700.herokuapp.com/ "Link to animal quiz on heroku")

---

## CONTENTS

* [Project Overview](#project-overview)
  * [Project Goals](#project-goals)

* [User Experience](#user-experience)
  * [User Expectations](#user-expectations)
  * [User Stories](#user-stories)

* [Design](#design)
  * [Imagery](#imagery)
  * [Structure](#structure)
  * [Wireframes](#wireframes)
  * [Design process](#design-process)

* [Features](#features)
  * [Google Sheets](#google-sheets-with-player-name-and-score)
  * [Intro with name input](#intro-with-name-input)
  * [Options](#options)
  * [Leader-board](#leader-board)
  * [Rules](#rules)
  * [Play the quiz](#play-the-quiz)
  * [Facts after guess](#facts-after-guess)
  * [Quiz end messages](#quiz-end-messages)

 * [Front-end features](#front-end-features)
   * [Background Image](#background-image)
   * [Title heading](#title-heading)

* [Future Implementations](#future-implementations)

* [Technologies Used](#technologies-used)
  * [Languages Used](#languages-used)
  * [Programs Used](#programs-used)

* [Deployment](#deployment)

* [Testing](#testing)
  * [Manual testing](#manual-testing)
  * [Unfixed bugs](#unfixed-bugs)
  * [Additional notes on testing](#additional-notes-on-testing)
  * [Automated testing](#automated-testing)

* [Credits](#credits)
  * [Code used and adapted](#code-used-and-adapted)
  * [Websites visited to gather knowledge](#websites-visited-to-gather-knowledge)
  * [Acknowledgments](#acknowledgments)

---

## **Project Overview**

### **Project Goals**
- Create a game in python
- Understand the concepts of the code written and how the code is executed
- Create data manipulation of an excel spreadsheet using gspread and python
- Have no bugs and if there are some have them documented

---

## **User Experience**
- Understand the purpose of the site
- Find out the rules of the game and have them easy to understand
- Have the game be fun and informative
- Give a fact about the animal wether regardless if question is answered correctly or incorrectly
- Have a scoring system where the player can see their score on the leader-board 

### **User Expectations**
- I want to easily know what this site is for
- I want to easily and clearly navigate through the site
- If I need help it is easily available
- I want to see what my score was at the end of the game
- I want to enjoy the game and learn something new

### **User Stories**

- As a user I want an easy to understand game
- As a user I want to be able to see what I scored at the end of the game
- As a user I would like to learn something new playing the game
- As a user I would like to see the scoreboard to know how I placed against others

---

## **Design**

The game was designed to look a bit brighter and livelier than just a terminal screen so I chose a nice royalty free background from pexels.com.
I also added some colors to the text with colorama and happy and sad emojis for if the user got something correct or incorrect.

### **Imagery**

Background chameleon image from pexels.com

![](https://i.ibb.co/H7rz38r/pexels-george-lebada-567540-1.jpg)


### **Structure**


![](assets/images/readme_images/flow_chart.png)

The flowchart above shows the general flow of the game. 

 
### **Wireframes**

Due to the nature of the project being mostly backend no wireframes were made or needed

### **Design process**

- Colorama module was used for text output color of the terminal
- Green was used for correct inputs and answers
- Red was used only for error messages and incorrect answers
- Blue was used for general messages such as "push enter to continue"
- Emojis were used only when displaying if answers were correct or incorrect
- I tried to make the code as clean as possible by making linebreaks a function so that it did not look cluttered and I could just call the line-break function


---

## **Features**

### **Google Sheets with player name and score**

Google sheets were used to store the players name and score. The playername and score were stored using gsheets module and all changes were made on the animal_game excell sheet. 

The simplest way I could think of for a scoreboard was to reorder the sheet by descending score and also to delete the rows from 12 to 19 at the start of the game. This would ensure a clean slate for the new players name to be put in. When the game ends the final score is inserted into the game and the column is then again checked that the scores descend in order, putting the high scorer at the top.

![](assets/images/readme_images/screenshot_sheet.png)

### **Intro with name input**

![](assets/images/readme_images/screenshot_start.png)

The user is welcomed to the game and asked to input their name. The game then checks via a while loop function if the user name is more than zero but less than 20 characters long. If it does not get this input it has the below error. 

![](assets/images/readme_images/screenshot_name_error.png)

### **Options**

![](assets/images/readme_images/screenshot_options.png)

Once the name is correctly entered the player is given four choices, as seen above.
1) Play the game
2) Read the rules
3) High scores
4) Exit to start

![](assets/images/readme_images/screenshot_options_incorrect.png)

If none of the correct options are entered an error is shown, as pictured above.

### **Leader-board**

![](assets/images/readme_images/screenshot_highscores.png)

The leader-board is saved in the google excel sheet and is sorted by descending points to show who is on top of the leader-board.

### **Rules**

![](assets/images/readme_images/screenshot_rules.png)

The rules of the game are shown (above)

### **Play the Quiz**


The game questions work with a function loop through the questions stored in quiz_data one at a time, the list of all the questions is saved as questions.py 

I did this to make the run.py look much less cluttered, this is done by using the import statement at the beginning of run.py and then calling the list from the function later in the run.py

 If the user does not enter a valid option of a, b, c or d then an error message is shown in red requesting a correct input, as shown below.


### **Facts after guess**

![](assets/images/readme_images/screenshot_facts.png)

I thought it would be nice to have the facts displayed after the question was answered so the user could learn something.

The user then presses enter to continue to the next question. I considered using a clear screen function so that it would seem cleaner on the screen but thought it was more beneficial to scroll up if the user wanted to read an old question before the game ended.

### **Quiz end messages** 

![](assets/images/readme_images/screenshot_gameover.png)

Game over message is displayed along with the score and wether the score was above or below average worked out by the score grading function.\
This is a very simple function that checks if the final score is less than or more than 7 out of 15 to say if it was below or above average and also works out the percentage of correct answers.

The user is then asked if they want to play again or quit the game. The function checks if the input is p then it will reset the score and restart the game. Otherwise it will quit the game, if q is selected. If an incorrect choice is selected then an error will be shown until the user selects one of the above.

The message below is shown if the user selects to quit.

![](assets/images/readme_images/screenshot_quit.png)

## **Front-end features**

### **Background image**
The frontend is very basic with just the chameleon background added to make the game-play area look a bit more vibrant. 

![](https://i.ibb.co/H7rz38r/pexels-george-lebada-567540-1.jpg)

### **Title Heading**

ANIMAL QUIZ above the terminal window which compliments the terminal window below it. I added a drop shadow in the css to make the title more visible as there was too much white in the background image.

![](assets/images/readme_images/screenshot_header.png)

---

## **Future Implementations**

- The choice of different categories can be introduced, such as reptiles, aquatic or flying animals.
- A social share button will be added in a footer so the user can share the game on popular social media platforms.
- A github link will also be placed in the footer once the game is at a point where it has more features so others can see the repository on github should they be interested. 

---

## **Technologies Used**

[Colorama](https://pypi.org/project/colorama/) - Used for the colours in the terminal\
[Code Spell Checker v2.20.3](https://opencollective.com/code-spell-checker)Addon for VSCode used to check spelling\
[Lucid Chart](https://www.lucidchart.com/pages/) - Used for making the flowchart seen in this readme\
VSCodes spell checker addon was used to check for spelling errors


### **Languages Used**

Python - Used for the game functionality \
HTML and CSS edited - for the styling of the page and background image


### **Programs Used**

Photoshop was used to edit the screenshots

---

## **Deployment**

The project was deployed on github, the command 'python3 run.py' was used in terminal to launch the game and once there was a good enough portion of the game written it was then deployed on heroku early in the project to avoid problems later on with incompatibility. The following steps were taken for deployment:


1. Add dependencies in GitPod to requirements.txt file with command "pip3 freeze > requirements.txt"
2. Commit and push to GitHub
3. Go to the Heroku Dashboard
4. Click "Create new app"
5. Name app and select location
5. Add Config Vars for Creds and Port in Settings tab
6. Add the buildbacks to Python and NodeJS in that order
7. Select appropriate deployment method, GitHub
8. Connect to Github and link to repository
9. Enable automatic deployment and/or deploy manually
10. Click on Deploy

---

## **Testing**

### **Manual Testing**

|           Action            |        Expectation                           | Outcome |
| :-------------------------: |   :-------------------------------------:    | :-----: |
|           Game start        |   The game starts when program is run        |  Pass   |
|      Terminal clears        |         Any old messages are cleared         |  Pass   |
|      Ascii Art called        |         Ascii art is displayed correctly         |  Pass   |
|      Enter nothing at name entry       |         An error will be displayed         |  Pass   |
|      Enter too many characters at name entry (over 20)       |         An error will be displayed         |  Pass   |
|      Enter valid name      |         User will be welcomed and option screen will show         |  Pass   |
|      Enter invalid option at option screen      |         Error message shown         |  Pass   |
|      Select rules option at option screen      |         Rules are shown         |  Pass   |
|      Enter pressed at rules option      |         Return to main option screen         |  Pass   |
|      Select high scores option at option screen     |         List of top 10 scores shown        |  Pass   |
|      Enter pressed at the high score screen      |         Return to main option screen         |  Pass   |
|      Quit game option selected at option screen      |         Game ended message shown         |  Pass   |
|      Play game option selected      |         Game is started with good luck message and question with options shown         |  Pass   |
|      Each question tested      |        Output matches the desired correct or incorrect answer       | Pass
|      End of game       |         Game over message with score and wether score was above or below average. The player is given two options to play again or quit. If play again is selected the player is sent back to the start or if quit is selected, they game ends with a message to the user.        |  Pass  |


### **Unfixed bugs**

When the game is run the following error shows though it does not affect the functioning of the overall game. 

/app/.heroku/python/lib/python3.11/site-packages/gspread/worksheet.py:1069: UserWarning: [Deprecated][in version 6.0.0]: method signature will change to: 'Worksheet.update(value = [[]], range_name=)' arguments 'range_name' and 'values' will swap, values will be mandatory of type: 'list(list(...))'

I tried to upgrade the gspread module and pip also as suggested in [this post](https://stackoverflow.com/questions/66730666/gspread-worksheet-update-error-worksheet-has-no-attribute-update) from stackoverflow however this did not solve it. I then used the clear screen function instead, so that the player does not see this message at the welcome screen and it does not negatively impact the user experience, the functionality is unaffected by this error.

### **Additional notes on testing**

During the design process I often tested and improved up the functionality of the game. I knew I wanted the game to look visually pleasing so used an ascii artwork for the game but this looked cluttered with the code so I imported it from a separate file in artwork.py

This also avoided long line pep8 errors when putting run.py through the validator. I realized during the creation of the validation of the input options that there was case sensitivity which was solved by adding .lower() after the input to convert the input to lowercase before checking if the input was valid.

**Colorama** 

Problem: Colorama module was not working I thought it was not compatible with heroku but then realized it was not in the requirements.txt as it was added after initial deployment.

Fix: Ran command Pip Freeze > Requirements.txt
from terminal and pushed everything to heroku and it worked, solution found on code institute slack community.\

**Validation and looping**

Problem: When I entered a blank name it would give the error but when I retried to enter a blank name it would freeze. 

Fix: I needed to make a while loop instead for this and function and then also changed my game over function to a while loop so that the error message displayed until the required input was entered to break out of the loop.


### **Automated testing**

Ran the code through code institutes Python Linter [pep8 validator](https://pep8ci.herokuapp.com/#)

![](assets/images/readme_images/screenshot_linter.png)

**Result:** No errors

---

## **Credits**

Game Questions were taken from this website [follow link](https://wehavekids.com/education/Multiple-Choice-Quiz-How-well-do-you-know-animals-suitable-for-kids)
Ascii Art generated with Ascii Art Website [follow link](https://www.asciiart.eu/text-to-ascii-art)


### **Code used and adapted**

Some of the code for the functionality was adapted from here. Namely the quiz data function [follow link](https://github.com/cornishcoder1/Food_of_Japan_Quiz/blob/main/run.py)



### **Websites visited to gather knowledge**

[Gsheets tutorial 1](https://www.youtube.com/watch?v=wrR0YLzh4DQ) Using Google Sheets with Python (Complete Beginner GSpread Tutorial!) \
[Gsheets tutorial 2](https://www.youtube.com/watch?v=cnPlKLEGR7E&t=589s&ab_channel=TechWithTim) Python Google Sheets API Tutorial - 2019
\
[Emojis](https://www.makeuseof.com/how-to-include-emojis-in-your-python-code) and how to add them\
[W3Schools](https://www.w3schools.com/) used when I getting stuck with implementation of code
Help sorting gspread by column.. [Stackoverflow](https://stackoverflow.com/questions/50938274/sort-a-spread-sheet-via-gspread) help with spreadsheet sort function
[Upper and lowercase Error handling solution](https://www.quora.com/How-do-I-allow-both-lower-and-uppercase-input-in-Python)
[Percentage calculation](https://stackoverflow.com/questions/5306756/how-to-print-a-percentage-value) help from stackoverflow

###  **Acknowledgments**

Thanks to all the help and support via the slack community for peer code review and all the support from the community when handling imposter syndrome, you are all appreciated.\
Thanks to my kids for inspiring me to do this quiz (and most other things in life too) 


[Back to top ⇧](#animal-quiz)

***





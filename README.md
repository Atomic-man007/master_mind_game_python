# master_mind_game_python

>This is a Python implementation of the classic Mastermind board game. In this game, one player sets a code consisting of four >colored pegs and the other player tries to guess the code in a limited number of turns.

>I used python and colorama to make print variables visually attractive in command-line.

>The game is played on the command line, and the user is prompted for input at each turn. The computer generates a random code at >the beginning of the game, and the user has to guess the code by entering their own code. After each guess, the computer >provides feedback in the form of correct and incorrect positions. A correct peg indicates that one of the pegs in the guess is >the correct color and in the correct position, while a incorrect peg indicates that one of the pegs in the guess is the correct >color but in the wrong position.

>The game ends when the user correctly guesses the code or runs out of turns. The user can also choose to quit the game at any >time or he can choose to try again the game.

**How to Play**
To play the game, follow these steps:

Clone the repository to your local machine.

Navigate to the *master_mind_game_python* directory.
Run the `mastermind.py` file in the command line: python `mastermind.py`
The computer will generate a *random code* and prompt you to enter your guess.
Enter your guess by typing the first letter of each color **(e.g. R G B Y)** space seperated.
After each guess, the computer will provide feedback in the form of correct and incorrect pegs.
Continue guessing until you either correctly guess the code or run out of turns.

*Configuration*
The game can be configured by editing the `config.py` file. Here are the available configuration options:

**COLORS**: A list of the colors that can be used in the code. The default colors are red, green, blue, yellow, orange, and white etc.
**CODE_LENGTH**: The length of the code. The default length is 4.
**TRIES**: The maximum number of turns allowed. The default is 10.

Reference: [Youtube](https://www.youtube.com/watch?v=sP-gFDreaQ4&t=859s)
Creditc: **Tech with tim**
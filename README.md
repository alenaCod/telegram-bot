## Guess the Number

<img width="466" alt="Screenshot 2024-06-25 at 13 01 07" src="https://github.com/alenaCod/telegram-bot/assets/33168098/54bbe11c-390b-4c6c-915e-d6935528a49c">

This project is a Telegram bot developed using the Python telebot library. It allows users to play a simple "Guess the
Number" game directly within any Telegram chat. The bot picks a random number between 1 and 100, and players try to
guess the number.

### Features
 - Start a new game at any time using a custom Telegram keyboard.
 - Guess numbers until the correct one is found, with feedback on whether each guess is too high or too low.
 - Ability to exit the game at any time.
 - Persistent game state for each user during active sessions.

### Requirements
To run this project, you need Python 3.6 or higher, and the following packages:

 - pyTelegramBotAPI (also known as telebot)
 - python-dotenv
 - os
 - random

### Bot Commands
 - /start - Initiates interaction with the bot, presents the main menu.
 - Interactive buttons:
    - Play "Guess the Number"😉 - Starts a new game session.
    - Exit the game 🤨 - Exits the current game session.

### How to Play
 - Send /start to the bot.
 - Click on the Play "Guess the Number"😉 button to start a new game.
 - Enter your guesses as numbers. The bot will guide you if the guess is too high or too low.
 - Continue guessing until you find the correct number.
 - You can exit the game at any time by pressing the Exit the game 🤨 button.
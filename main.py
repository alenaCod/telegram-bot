import telebot as tb
from telebot import types
import random
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('TELEGRAM_BOT_TOKEN')
bot = tb.TeleBot(token)

users_game_state = {}


def start_new_game(user_id):
    number = random.randint(1, 100)
    users_game_state[user_id] = {'number': number, 'attempts': 0}
    return "A number between 1 and 100 has been chosen. Try to guess it!😀"


def get_start_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    play_button = types.KeyboardButton(text='Play "Guess the Number"😉')
    markup.add(play_button)
    return markup


def get_game_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    quit_button = types.KeyboardButton(text='Exit the game 🤨')
    markup.add(quit_button)
    return markup


@bot.message_handler(commands=['start'])
def get_start(message):
    mess_id = message.chat.id
    markup = get_start_keyboard()
    bot.send_message(mess_id, text='<b>Hello</b>, I am a test bot, ready to entertain you.😜', parse_mode='HTML', reply_markup=markup)


@bot.message_handler(func=lambda message: message.text)
def handle_message(message):
    chat_id = message.chat.id
    text = message.text
    match text:
        case 'Play "Guess the Number"😉':
            greeting = start_new_game(chat_id)
            markup = get_game_keyboard()
            bot.send_message(chat_id, text=greeting, reply_markup=markup)
        case 'Exit the game 🤨':
            if chat_id in users_game_state:
                del users_game_state[chat_id]
                markup = get_start_keyboard()
                bot.send_message(chat_id, text="You have exited the game.", reply_markup=markup)
            else:
                bot.send_message(chat_id, text="You are not in the game currently.", reply_markup=get_game_keyboard())
        case _:
            if chat_id in users_game_state:
                process_guess(message)
            else:
                bot.send_message(chat_id, text="Choose an option from the keyboard or send /start to start the game.", reply_markup=get_start_keyboard())


def process_guess(message):
    chat_id = message.chat.id
    guess_text = message.text
    if not guess_text.isdigit():
        bot.send_message(chat_id, text="You entered a letter. Please enter a number.", reply_markup=get_game_keyboard())
        return
    guess = int(guess_text)
    game = users_game_state[chat_id]
    game['attempts'] += 1
    markup = get_game_keyboard()
    if guess < game['number']:
        bot.send_message(chat_id, text="Too low! Please try again.", reply_markup=markup)
    elif guess > game['number']:
        bot.send_message(chat_id, text="Too high! Please try again.", reply_markup=markup)
    else:
        bot.send_message(chat_id, text=f"You guessed it! The number was {game['number']}. It took you {game['attempts']} attempts.", reply_markup=get_start_keyboard())
        del users_game_state[chat_id]


bot.polling(none_stop=True)
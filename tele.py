import telebot
import config
import sql_tools as sqlt
from telebot.types import InputMediaPhoto as imp

bot = telebot.TeleBot(config.TOKEN)

u_name = ''
u_surname = ''
nums_a = ''
nums_d = ''
comnt_a = ''
comnt_d = ''



print('Server started...')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_sticker(chat_id=message.chat.id, sticker='CAACAgIAAxkBAAEFR31i0IKjq89tigSy9TbvVxAVV7_0wQACAQEAAladvQoivp8OuMLmNCkE')
    mess = '''Здравствуйте!
Это бот, который поможет сделать ваши фотографии еще лучше!🤩🤩

Вы можете выбрать до 4х фотографий от каждого из наших фотографов.😎😎😎

Ребята-фотографы просят Вас помочь им и подсказать, 
что именно изменить в ретуши ваших кадров. 🤔🤔🤔

Для этого ответьте на несколько вопросов, используя предложенные инструкции.
🤞🤞🤞🤞🤞🤞🤞🤞
    '''
    bot.send_message(message.chat.id, mess, parse_mode='html')
    bot.send_message(message.chat.id, 'Введите своё Имя и Фамилию (через пробел)')
    bot.register_next_step_handler(message, get_name)

@bot.message_handler(content_types=['text'])
def get_name(message):
    global u_name
    global u_surname
    tmp = (message.text).split(' ')
    u_name = tmp[0]
    u_surname = tmp[1]
    
    bot.send_media_group(message.chat.id, [imp(open('tutorial/a1.png', 'rb')), imp(open('tutorial/a2.png', 'rb')), imp(open('tutorial/a3.png', 'rb')), imp(open('tutorial/a4.png', 'rb'))])
    bot.send_message(message.chat.id, '''ИНСТРУКЦИЯ❗️❗️❗️

Чтобы узнать номер фотографии, войдите в свойства и введите номер фотографии (photo00-<номер>.jpg)
    ''')
    bot.send_message(message.chat.id, 'https://disk.yandex.ru/d/RWTpLvJ8NbO0eg')
    bot.send_message(message.chat.id, 'Введите номера 4х фотографий от Анастасии (Перечисляйте номера через пробел)')
    bot.register_next_step_handler(message, get_nums_a)

def get_nums_a(message):
    global nums_a
    nums_a = message.text
    bot.send_message(message.chat.id, 'Введите комментарий к фотографиям Анастасии')
    bot.register_next_step_handler(message, comment_a)

def comment_a(message):
    global comnt_a
    comnt_a = message.text
    
    bot.send_media_group(message.chat.id, [imp(open('tutorial/d1.png', 'rb')), imp(open('tutorial/d2.png', 'rb')), imp(open('tutorial/d3.png', 'rb')), imp(open('tutorial/d4.png', 'rb'))])
    bot.send_message(message.chat.id, '''ИНСТРУКЦИЯ❗️❗️❗️

Чтобы узнать номер фотографии, войдите в свойства и введите номер фотографии (188A<номер>.jpg) 

ВВОДИТЬ НЕОБХОДИМО С УЧЁТОМ НУЛЕЙ!!☝️☝️☝️
    ''')
    bot.send_message(message.chat.id, 'https://disk.yandex.ru/d/O8GnkUla4x2Gog')
    bot.send_message(message.chat.id, 'Введите номера 4х фотографий от Дмитрия (Перечисляйте номера через пробел)')
    bot.register_next_step_handler(message, get_nums_d)

def get_nums_d(message):
    global nums_d
    nums_d = message.text
    bot.send_message(message.chat.id, 'Введите комментарий к фотографиям Дмитрия')
    bot.register_next_step_handler(message, comment_d)
    
    
def comment_d(message):
    global u_name, u_surname, nums_a, nums_d, comnt_a, comnt_d
    comnt_d = message.text

    mess = f'''<b>Вас зовут: </b> {u_name} {u_surname}
<b>Ваши выбранные фотографии для Анастасии: </b> {nums_a}
<b>Комментарий: </b> {comnt_a}
<b>Ваши выбранные фотографии для Дмитрия: </b>{nums_d}
<b>Комментарий: </b> {comnt_d}'''
    bot.send_message(message.chat.id, mess, parse_mode='html')

    #send data
    arr_a = nums_a.split(' ')
    arr_d = nums_d.split(' ')
    if len(arr_a) < 4:
        arr_a = sqlt.append_4(arr_a)
    if len(arr_d) < 4:
        arr_d = sqlt.append_4(arr_d)
    user_id = message.from_user.username
    '''if user_id == 'None':
        user_id = message.contact.phone_number'''
    try:
        sqlt.add(user_id ,u_name, u_surname, arr_a[0], arr_a[1], arr_a[2], arr_a[3], arr_d[0], arr_d[1], arr_d[2], arr_d[3], comnt_a, comnt_d)
        bot.send_message(message.chat.id, 'База данных успешно обновлена!')
        bot.send_message(message.chat.id, 'Если данные не верны, то напишите разработчику! @OmenesDev')
    except:
        bot.send_message(message.chat.id, 'Произошла ошибка, обратитесь к разработчику! @OmenesDev')
        print(user_id, u_name, u_surname, "Data Base Error")

    

bot.infinity_polling(timeout=10, long_polling_timeout = 5)

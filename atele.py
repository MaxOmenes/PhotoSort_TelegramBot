from telebot.async_telebot import AsyncTeleBot
import config
import sql_tools as sqlt

bot = AsyncTeleBot(config.TOKEN)

u_name = ''
u_surname = ''
nums_a = ''
nums_d = ''
comnt_a = ''
comnt_d = ''

print('Server started...')

@bot.message_handler(commands=['start'])
async def start(message):
    mess = '''Здравствуйте! 
<b>Это телеграм бот</b>'''
    await bot.send_message(message.chat.id, mess, parse_mode='html')
    await bot.send_message(message.chat.id, 'Введите своё имя')
    return

@bot.message_handler(content_types=['text'])
async def get_name(message):
    global u_name
    u_name = message.text
    await bot.send_message(message.chat.id, 'Введите свою Фамилию')
    return

async def get_surname(message):
    global u_surname
    u_surname = message.text
    await bot.send_message(message.chat.id, 'Введите 4 номера фотографий Анастасии')
    return


async def get_nums_a(message):
    global nums_a
    nums_a = message.text
    await bot.send_message(message.chat.id, 'Введите комментарий к фотографиям Анастасии')
    return 

async def comment_a(message):
    global comnt_a
    comnt_a = message.text
    await bot.send_message(message.chat.id, 'Введите 4 номера фотографий Дмитрия')
    return

async def get_nums_d(message):
    global nums_d
    nums_d = message.text
    await bot.send_message(message.chat.id, 'Введите комментарий к фотографиям Дмитрия')
    return
    
    
async def comment_d(message):
    global u_name, u_surname, nums_a, nums_d, comnt_a, comnt_d
    comnt_d = message.text

    mess = f'''<b>Вас зовут: </b> {u_name} {u_surname}
<b>Ваши выбранные фотографии для Анастасии: </b> {nums_a}
<b>Комментарий: </b> {comnt_a}
<b>Ваши выбранные фотографии для Дмитрия: </b>{nums_d}
<b>Комментарий: </b> {comnt_d}'''
    await bot.send_message(message.chat.id, mess, parse_mode='html')

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
        await bot.send_message(message.chat.id, 'База данных успешно обновлена!')
    except:
        await bot.send_message(message.chat.id, 'Произошла ошибка, обратитесь к разработчику!')


import asyncio
asyncio.run(bot.polling())
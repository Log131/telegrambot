from aiogram import Dispatcher,Bot,executor,types
import asyncio
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


token = '5162602636:AAHtUb-m25lZ18_fGdomamEo9XZekfASi8c'
bot = Bot(token=token)

dp = Dispatcher(bot=bot)



global task_state_, task_state_5, task_state_0, task_state_6, task_state_8
task_state_ = False
task_state_5 = False
task_state_0 = False
task_state_6 = False
task_state_8 = False

def start_keys():
    x = InlineKeyboardMarkup()
    s = InlineKeyboardButton(text='Открыть видео', callback_data='link_0')
    x.add(s)

    return x
    




@dp.message_handler(commands=['start'])
async def start_(msg: types.Message):
    strts = 'https://i.yapx.ru/V3K3J.jpg'
    await msg.answer_photo(photo=strts)
    await msg.answer('Привет! \n \n Этот бот поможет вам разобраться в тонкостях и важных аспектах свадьбы! \n \n Мы подготовили три коротких обучающих видео с полезной информацией, о которой вы наверняка не знали . Мы расскажем вам о всех секретах организации вашей свадьбы, как сделать все круто, качественно и не переплатить! \n \n Смотрите видео, как сэкономить первые 10% при бронировании любого подрядчика для свадьбы.' , reply_markup=start_keys())





def post_0():
    x = InlineKeyboardMarkup()
    s = InlineKeyboardButton(text='Перейти по ссылке', url='https://telegra.ph/Sokrashchaem-rashody-pri-organizacii-svadby-na-10-20-04-01')
    x.add(s)

    return x
def post_1():
    x = InlineKeyboardMarkup()
    s = InlineKeyboardButton(text='Перейти по ссылке', url='https://telegra.ph/Gde-najti-podryadchikov-za-vash-byudzhet-za-odin-den-04-02')
    x.add(s)

    return x
def post_():
    x = InlineKeyboardMarkup()
    s = InlineKeyboardButton(text='Перейти по ссылке', url='https://telegra.ph/Kak-sozdat-svadbu-mechty-i-ne-pereplatit-04-02')
    x.add(s)

    return x


def task_():
    x = InlineKeyboardMarkup()
    s = InlineKeyboardButton(text='Открыть статью', callback_data='data_0')
    x.add(s)

    return x


def task_0():
    x = InlineKeyboardMarkup()
    s = InlineKeyboardButton(text='Открыть видео', callback_data='data_1')
    x.add(s)

    return x

def task_5():
    x = InlineKeyboardMarkup()
    s = InlineKeyboardButton(text='Открыть статью', callback_data='data_')
    x.add(s)

    return x
def task_6():
    x = InlineKeyboardMarkup()
    s = InlineKeyboardButton(text='Открыть видео', callback_data='data_6')
    x.add(s)

    return x

def task_8():
    x = InlineKeyboardMarkup()
    s = InlineKeyboardButton(text='Открыть статью', callback_data='data_5')
    x.add(s)

    return x

@dp.callback_query_handler(text='link_0')
async def video_(css: types.CallbackQuery):

    await css.message.delete()
    await css.message.answer('https://www.youtube.com/watch?v=bqtVKRyAvXI')

    await asyncio.sleep(5)

    age = 'https://i.yapx.ru/V3I0z.png'
    
    await css.message.answer_photo(photo=age, caption='Здесь вы узнаете: \n что такое агентские проценты и как с помощью одной фразы при общении с заказчиком получить скидку!', reply_markup=task_())
    
    wed_ = 'https://i.yapx.ru/V3K4w.png'
    global task_state_
    task_state_ = True
    wed = 'https://i.yapx.ru/V3I3J.png'
    podrya_ = 'https://i.yapx.ru/V3K6X.png'
    podrya = 'https://i.yapx.ru/V3I9A.png'
    while task_state_:
        await asyncio.sleep(5)
        if task_state_:
            await css.message.answer_photo(photo=age, caption='Вы где ? \n Время и идет, ваше событие все ближе \n Открывайте статью', reply_markup=task_())
            await asyncio.sleep(5)
            if task_state_:
                await css.message.answer_photo(photo=wed_, caption='Сам себе организатор: как создать свадьбу мечты и не переплатить', reply_markup=task_0())
                await asyncio.sleep(5)
                if task_state_:
                    await css.message.answer_photo(photo=wed_, caption='Вы где ? \n Время и идет, ваше событие все ближе \n Открывайте видео', reply_markup=task_0())
                    await asyncio.sleep(5)
                    if task_state_:
                        await css.message.answer_photo(photo=wed, caption='*У вас всего одна попытка, ошибки в организации не допустимы !!!* \n \n Как создать свадьбу мечты и не перепалить, забирайте пошаговую инструкцию!', reply_markup=task_5(), parse_mode='Markdown')
                        await asyncio.sleep(5)
                        if task_state_:
                            await css.message.answer_photo(photo=wed, caption='Вы где ? \n Время и идет, ваше событие все ближе \n Открывайте статью', reply_markup=task_5())
                            await asyncio.sleep(5)
                            if task_state_:
                                await css.message.answer_photo(photo=podrya_, caption='Сам себе организатор: как сэкономить на свадьбе, с помощью одной фразы', reply_markup=task_6())
                                await asyncio.sleep(5)
                                if task_state_:
                                    await css.message.answer_photo(photo=podrya_, caption='Вы где ? \n Время и идет, ваше событие все ближе \n Открывайте видео ', reply_markup=task_6())
                                    await asyncio.sleep(5)
                                    if task_state_:
                                        await css.message.answer_photo(photo=podrya, caption='Здесь вы узнаете: \n где найти всех подрядчиков и площадки быстро, просто и за любой бюджет!', reply_markup=task_8())
                                        await asyncio.sleep(5)
                                        if task_state_:
                                            await css.message.answer_photo(photo=podrya, caption='Вы где ? \n Время и идет, ваше событие все ближе \n Открывайте статью', reply_markup=task_8())
                                            await asyncio.sleep(5)
                                            task_state_ = False
                                            break
        else:
            return
                                        

                                            
        
    
    


@dp.callback_query_handler(text='data_0')
async def posts_0(css: types.CallbackQuery):


    
    
    await css.answer()
    global task_state_, task_state_5, task_state_0, task_state_6, task_state_8
    task_state_ = False
    task_state_5 = False
    task_state_0 = False
    task_state_6 = False
    task_state_8 = False
    await css.message.delete()
    age = 'https://i.yapx.ru/V3I0z.png'
    await css.message.answer_photo(photo=age,caption='Ссылка на статью', reply_markup=post_0())
    
    await asyncio.sleep(5)
    wed_ = 'https://i.yapx.ru/V3K4w.png'
    await css.message.answer_photo(photo=wed_, caption='Сам себе организатор: как создать свадьбу мечты и не переплатить', reply_markup=task_0())
    wed = 'https://i.yapx.ru/V3I3J.png'
    podrya_ = 'https://i.yapx.ru/V3K6X.png'
    podrya = 'https://i.yapx.ru/V3I9A.png'
    task_state_0 = True
    while task_state_0:
        await asyncio.sleep(5)
        if task_state_0:
            await css.message.answer_photo(photo=wed_, caption='Вы где ? \n Время и идет, ваше событие все ближе \n Открывайте видео', reply_markup=task_0())
            await asyncio.sleep(5)
            if task_state_0:
                await css.message.answer_photo(photo=wed, caption='*У вас всего одна попытка, ошибки в организации не допустимы !!!* \n \n Как создать свадьбу мечты и не перепалить, забирайте пошаговую инструкцию!', reply_markup=task_5(), parse_mode='Markdown')
                await asyncio.sleep(5)
                if task_state_0:
                    await css.message.answer_photo(photo=wed, caption='Вы где ? \n Время и идет, ваше событие все ближе \n Открывайте статью', reply_markup=task_5())
                    await asyncio.sleep(5)
                    if task_state_0:
                        await css.message.answer_photo(photo=podrya_, caption='Сам себе организатор: как сэкономить на свадьбе, с помощью одной фразы', reply_markup=task_6())
                        await asyncio.sleep(5)
                        if task_state_0:
                            await css.message.answer_photo(photo=podrya_, caption='Вы где ? \n Время и идет, ваше событие все ближе \n Открывайте видео ', reply_markup=task_6())
                            await asyncio.sleep(5)
                            if task_state_0:
                                await css.message.answer_photo(photo=podrya, caption='Здесь вы узнаете: \n где найти всех подрядчиков и площадки быстро, просто и за любой бюджет!', reply_markup=task_8())
                                await asyncio.sleep(5)
                                if task_state_0:
                                    await css.message.answer_photo(photo=podrya, caption='Вы где ? \n Время и идет, ваше событие все ближе \n Открывайте статью', reply_markup=task_8())
                                    await asyncio.sleep(5)
                                    task_state_0 = False
                                    break
        else:
            return



@dp.callback_query_handler(text='data_1')
async def video_5(css: types.CallbackQuery):
    await css.answer()
    global task_state_, task_state_5, task_state_0, task_state_6, task_state_8
    task_state_ = False
    task_state_5 = False
    task_state_0 = False
    task_state_6 = False
    task_state_8 = False
    await css.message.delete()
    
    await css.message.answer('https://www.youtube.com/watch?v=XvQDNVu4vn0')
    await asyncio.sleep(5)
    
    wed = 'https://i.yapx.ru/V3I3J.png'
    
    await css.message.answer_photo(photo=wed, caption='*У вас всего одна попытка, ошибки в организации не допустимы !!!* \n \n Как создать свадьбу мечты и не перепалить, забирайте пошаговую инструкцию!', reply_markup=task_5(), parse_mode='Markdown')
    
    
    wed = 'https://i.yapx.ru/V3I3J.png'
    podrya_ = 'https://i.yapx.ru/V3K6X.png'
    podrya = 'https://i.yapx.ru/V3I9A.png'
    task_state_5 = True
    while task_state_5:
        await asyncio.sleep(5)
        if task_state_5:
            await css.message.answer_photo(photo=wed, caption='Вы где ? \n Время и идет, ваше событие все ближе \n Открывайте статью', reply_markup=task_5())
            await asyncio.sleep(5)
            if task_state_5:
                await css.message.answer_photo(photo=podrya_, caption='Сам себе организатор: как сэкономить на свадьбе, с помощью одной фразы', reply_markup=task_6())
                await asyncio.sleep(5)
                if task_state_5:
                    await css.message.answer_photo(photo=podrya_, caption='Вы где ? \n Время и идет, ваше событие все ближе \n Открывайте видео ', reply_markup=task_6())
                    await asyncio.sleep(5)
                    if task_state_5:
                        await css.message.answer_photo(photo=podrya, caption='Здесь вы узнаете: \n где найти всех подрядчиков и площадки быстро, просто и за любой бюджет!', reply_markup=task_8())
                        await asyncio.sleep(5)
                        if task_state_5:
                            await css.message.answer_photo(photo=podrya, caption='Вы где ? \n Время и идет, ваше событие все ближе \n Открывайте статью', reply_markup=task_8())
                            await asyncio.sleep(5)
                            task_state_5 = False
                            break
        else:
            return




@dp.callback_query_handler(text='data_')
async def posts_6(css: types.CallbackQuery):
    await css.answer()
    global task_state_, task_state_5, task_state_0, task_state_6, task_state_8
    task_state_ = False
    task_state_5 = False
    task_state_0 = False
    task_state_6 = False
    task_state_8 = False
    await css.message.delete()
    wed = 'https://i.yapx.ru/V3I3J.png'
    await css.message.answer_photo(photo=wed,caption='Ссылка на статью', reply_markup=post_())
    
    
    await asyncio.sleep(5)
    podrya_ = 'https://i.yapx.ru/V3K6X.png'
    await css.message.answer_photo(photo=podrya_, caption='Сам себе организатор: как сэкономить на свадьбе, с помощью одной фразы', reply_markup=task_6())
    
    

    task_state_6 = True
    podrya = 'https://i.yapx.ru/V3I9A.png'
    while task_state_6:
        await asyncio.sleep(5)
        if task_state_6:
            await css.message.answer_photo(photo=podrya_, caption='Вы где ? \n Время и идет, ваше событие все ближе \n Открывайте видео ', reply_markup=task_6())
            await asyncio.sleep(5)
            if task_state_6:
                await css.message.answer_photo(photo=podrya, caption='Здесь вы узнаете: \n где найти всех подрядчиков и площадки быстро, просто и за любой бюджет!', reply_markup=task_8())
                await asyncio.sleep(5)
                if task_state_6:
                    await css.message.answer_photo(photo=podrya, caption='Вы где ? \n Время и идет, ваше событие все ближе \n Открывайте статью', reply_markup=task_8())
                    await asyncio.sleep(5)
                    task_state_6 = False
                    break
        else:
            return

@dp.callback_query_handler(text='data_6')
async def video_0(css: types.CallbackQuery):
    await css.answer()
    global task_state_, task_state_5, task_state_0, task_state_6, task_state_8
    task_state_ = False
    task_state_5 = False
    task_state_0 = False
    task_state_6 = False
    task_state_8 = False
    await css.message.delete()
    await css.message.answer('https://www.youtube.com/watch?v=ErXYpHWUxrc')
    
    await asyncio.sleep(5)
    podrya = 'https://i.yapx.ru/V3I9A.png'

    await css.message.answer_photo(photo=podrya, caption='Здесь вы узнаете: \n где найти всех подрядчиков и площадки быстро, просто и за любой бюджет!', reply_markup=task_8())
    
    

    
    task_state_8 = True
    while task_state_8:
        await asyncio.sleep(5)
        if task_state_8:
            await asyncio.sleep(5)
            await css.message.answer_photo(photo=podrya, caption='Вы где ? \n Время и идет, ваше событие все ближе \n Открывайте статью', reply_markup=task_8())
            task_state_8 = False
            break
        else:
            return

@dp.callback_query_handler(text='data_5')
async def post_s0(css: types.CallbackQuery):
    x = InlineKeyboardMarkup()
    s = InlineKeyboardButton(text='Ссылка', url='http://samsebeorg.ru/#package')
    x.add(s)
    await css.answer()
    global task_state_, task_state_5, task_state_0, task_state_6, task_state_8
    task_state_ = False
    task_state_5 = False
    task_state_0 = False
    task_state_6 = False
    task_state_8 = False
    await css.message.delete()
    podrya = 'https://i.yapx.ru/V3I9A.png'
    await css.message.answer_photo(photo=podrya, caption='Ссылка на статью', reply_markup=post_1())
    
    await asyncio.sleep(5)

    await css.message.answer('Вы посмотрели три обучающих видео. Узнали несколько крутых фишек, которые можно прямо сейчас применить на практике.')
    
    await css.message.answer('Это реально простые и рабочие советы! Вам наверняка хотелось бы узнать еще больше фишек, которые помогут быстро и легко подготовится к свадьбе. Так же у вас может быть множество вопросов и непонимания по-организации свадьбы. \n Мы приготовили просто гору полезного и простого в освоении материала для вас. \n Мы покажем то, что не расскажем ни один организатор! \n Вы реально сэкономите на организации, без потери качества и не ошибетесь в выборе подрядчиков.')
    
    await css.message.answer('Вам больше не нужен организатор, вы сможете сделать все сами! \n Что бы ознакомиться с ценами и программой, жмите на кнопку и переходите по ссылке', reply_markup=x)
    





if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
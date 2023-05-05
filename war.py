from aiogram import Dispatcher,Bot,executor,types

from aiogram.dispatcher.middlewares import LifetimeControllerMiddleware


import sqlite3

token = '5984947658:AAFEJNgy0rXV8FxfVRsV7uvcgS8Co1Mi24w'

bot = Bot(token=token)
dp = Dispatcher(bot=bot)
global tbase, tc
tbase = sqlite3.connect('tes.db')
tc = tbase.cursor()
with tbase:
    tc.execute('CREATE TABLE IF NOT EXISTS wars_(user_id PRIMARY KEY, war DEFAULT 0)')










@dp.message_handler(commands=['war'])
async def warxd_(msg: types.Message):
    try:
        
        chat_admins = await bot.get_chat_member(chat_id='@OwnerOtziv', user_id=msg.from_user.id)
        
        
        
        
        
        
        
        if chat_admins.status == 'creator' or chat_admins.status == 'administrator':
            with tbase:
                s_ = tc.execute('SELECT war FROM wars_ WHERE user_id = ?', (msg.reply_to_message.from_user.id,)).fetchone()
            
            
            
        
            with tbase:
                tc.execute('INSERT OR IGNORE INTO wars_(user_id) VALUES(?)',(msg.reply_to_message.from_user.id,))
            with tbase:
                tc.execute('UPDATE wars_ SET war = war + 1 WHERE user_id = ?',(msg.reply_to_message.from_user.id,))
            with tbase:
                s = tc.execute('SELECT war FROM wars_ WHERE user_id = ?', (msg.reply_to_message.from_user.id,)).fetchone()
            await bot.send_message(msg.reply_to_message.from_user.id, text=f'Вы получили предупреждение ‼️ ‼️ ‼️ {s[0]}/5')
            await bot.send_message(msg.chat.id, text=f'@{msg.reply_to_message.from_user.username}        Вы получили предупреждение ‼️ ‼️ ‼️{s[0]}/5')
            if s_[0] >= 5:
                with tbase:
                    tc.execute('UPDATE wars_ SET war = 0 WHERE user_id = ?', (msg.reply_to_message.from_user.id,))
                await bot.send_message(msg.reply_to_message.from_user.id, text=f'Вы были удалены из чата')
                await bot.send_photo(msg.chat.id, photo='https://i.yapx.ru/V9rL7.png',caption=f'@{msg.reply_to_message.from_user.username} Был отправлен в ЧВК Шелби 🫡')
                await bot.ban_chat_member(msg.chat.id, user_id=msg.reply_to_message.from_user.id)
        else:

            pass
    
    except Exception as e:
        print(e)



@dp.message_handler(commands=['card'])
async def payments_(msg: types.Message):
    await msg.answer(f'_Реквизиты Отзывничка_ : \n 🏦 Тинькофф Банк \n 💳 5536914054972405 \n \n 🏦 Сбербанк \n 💳 2202203293150142 \n \n 📲 +79106265792 (Для переводов по номеру, актуальны только те банки, которые указаны выше ☝️ )\n \n 🤖 💳Савушкин С.В.', parse_mode='Markdown')


@dp.message_handler(commands=['del'])
async def delxd_(msg: types.Message):
    
    
    
    try:
        chat_admins = await bot.get_chat_member(chat_id='@OwnerOtziv', user_id=msg.from_user.id)
        if chat_admins.status == 'creator' or chat_admins.status == 'administrator':
            s = msg.reply_to_message.from_user.username
            with tbase:
                tc.execute('UPDATE wars_ SET war = war - 1 WHERE user_id = ?', (msg.reply_to_message.from_user.id,))
                s_ = tc.execute('SELECT war FROM wars_ WHERE user_id = ? ',(msg.reply_to_message.from_user.id,)).fetchone()
            

            await bot.send_message(msg.chat.id, text=f'@{s} Предупреждения сняты {s_[0]}/5')
    except:
        pass



if __name__ == '__main__':
   
    executor.start_polling(dp, skip_updates=True)

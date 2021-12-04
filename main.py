
import random
import os,sys
import  vk
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll,VkBotEventType, VkBotMessageEvent
from vk_api.longpoll import VkLongPoll,VkEventType
import datetime


vk_session = vk_api.VkApi(token="ed0b0b611d463d2a75ade59094a88c66a80b1a00ddc928b9f4c358b1ab8758550b904c8957c27ad1f547b")

longpoll = VkBotLongPoll(vk_session,209315300)
print('Запускается вроде...')

def send(id, text):
    vk_session.method("messages.send", {"chat_id":id, "message": text,"random_id":0})
hello = ['дарова,заебал','салам попалам', 'салаааам', 'привет',  'ооо, дарова ', ' внимательно слушаю', 'ага', 'мг', '...', 'да блять, что нужно?', '-\-', 'фига, я кому-то нужен', 'да что такое!!!?!?!', '?']
oskr = ['мать ебал','пошёл сам нахуй','ясно, клоун','ты не забывай, кто тебе интернет в будку провёл','дурачок']
zachet = ['сдашь','не сдашь','зачёт','не зачёт']
proc = random.randint(1,100)
imena1 = ['Виноградова Т.', "Сергеева А.","Дюбкова Д", "Крылова. Д.", "Котович Т", "Ильич Л.", "Семенник В.","Дробышев И.","Никифоров Д.","Павловей А.","Бутько А.","Малышкин В.","Строганова О.","Пирович К.","Мацкевич И.","Кузюк М.","Казак Е.","Клочек В.", "Серафимович Ю","Алимпиев В.","Балыш А."]
imena2 = ['Виноградова Т.', "Сергеева А.","Дюбкова Д", "Крылова. Д.", "Котович Т", "Ильич Л.", "Семенник В.","Дробышев И.","Никифоров Д.","Павловей А.","Бутько А.","Малышкин В.","Строганова О.","Пирович К.","Мацкевич И.","Кузюк М.","Казак Е.","Клочек В.", "Серафимович Ю","Алимпиев В.","Балыш А."]

im1 = (random.choice(imena1))
im2 = (random.choice(imena2))
schitala = (im1+'+'+im2+''+'=')
for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        if event.from_chat:
            id = event.chat_id
            msg = event.message.text

        im1 = (random.choice(imena1))
        im2 = (random.choice(imena2))

        if msg in ["Валера",'ухтыбля',"Ухтыбля","#ухтыбля"]:
           send(id, random.choice(hello))
        if msg in ['пошёл нахуй','Иди нахуй','Сам клоун']:
            send(id,random.choice(oskr))

        if msg == 'Фортуна':
            send(id,random.choice(zachet))

        #if msg == 'Шип':
         #   send(id,im1+'+'+im2+''+'='+str(random.randint(1,100))+'%')

        if msg == "Валера, загадай число":
            send(id,'Загадал')
            chisla = ['1','2','3','4','5','6','7','8','9','10']
            igra = random.choice(chisla)

            for msg in igra:
                for event in longpoll.listen():
                    if event.type == VkBotEventType.MESSAGE_NEW:
                        if event.from_chat:
                            id = event.chat_id
                            msg = event.message.text

                        if msg == igra:
                             send(id,'Сюдаааааа')
                             break


                        else:
                          send(id,'Лошара')

        if msg == 'Команды':
          send(id,'Валера довольно способный парень, правда немножечко туповат, но ничего страшного\n1.Привет\n(тут Валерка с вами познакомиться,но правда я не знаю с каким тоном он вам это скажет)\n2.Фортуна\n(тут Валерка предскажет сдадите ли вы зачёт или сессию :) )\n3.Шип\n(оооо, вот здесь Валерка проверит вас и вашего партнёра на совместимость)\n4.Валера, загадай число\n(а здесь вы будете с Валеркой угадывать число,которое он загадал)\n5.Токсик\n(тут показываеться ваш уровень токсичности)')


        if msg == 'Токсик':
          send(id,'Ну, ты токсичен на'+'-->'+str(random.randint(1,100))+'%')


        if msg == 'Шип':
          send(id,'Ну давай, пиши, Имя Фамилия + Имя Фамилия')

          for event in longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                if event.from_chat:
                    id = event.chat_id
                    msg = event.message.text

                if msg == msg:
                    send(id,msg+"="+str(random.randint(1,100))+'%')
                break
























































































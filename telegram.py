from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty


class TelegramBOT:

     def __init__(self,phone, api_id, api_hash):
        self.phone = phone
        self.apiID = api_id
        self.apiHash = api_hash
        self.login(phone,api_id,api_hash)

     def code_security(self, cmd):
        return str(input(cmd))

     def login(self,phone, api_id, api_hash):

        client = TelegramClient(phone, api_id, api_hash)
        client.connect()
        if not client.is_user_authorized():
            client.send_code_request(phone)
            client.sign_in(phone, self.code_security('[ C ] - Code Segurity : '))

        def extract_groups():
            chats = []
            groups = []
            chats.extend(client(GetDialogsRequest(offset_date=None, offset_id=0, offset_peer=InputPeerEmpty(),
                                                                                  limit=200,   hash=0)).chats)
            for chat in chats:
                if (not "broadcast"  in str(chat)):
                    pass
                else:
                    if chat.broadcast != True  and chat.megagroup == True :
                        groups += [chat]
                    elif chat.broadcast != False  :
                        groups += [chat]



            for group in range(len(groups)):
                if groups[group].title != groups[group].title[0:3]:
                    print('You are here = %s'% groups[group].title)
            exit()
        extract_groups()



api_id="0000000"
api_hash='1111111111111'
phone="2222222222222"

TelegramBOT(phone, api_id, api_hash)

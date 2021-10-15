'''
TelegramMegaGroupMovingTool by alexcarchiar, realized because I hate repetitive tasks.
It's mostly just a script, don't take it as final code.
It will work, but you may need to adapt it.
If you have any problems, don't hesitate to contact me!
(visit alessandrochiarelli.com to find out how)

This version works with megagroups and possibly even channels, but I haven't tested channels yet
can't promise my spaghetti code works.

In order for it to work:
- get your api id and api hash from Telegram developer website
- get the link of the originial group (t.me/joinchat/SomeRandomCharacters)
- get the link of the new group (t.me/joinchat/SomeOtherRandomCharacters)
- the bot will add all users (NOT BOTS) from the original group to the newer one

You should import this file into an other and use it as a class
Remember that this is meant to be used with CLI! Telegram might ask you to log in the app!
I am not collecting any data, I'm just using Telethon. Read Telegram and Telethon documentation
if you have any concerns.

Check requirements.txt to install the required dependencies

As you can see, once you construct the class, it will immediately add all users.
It is a super quick tool!
'''

from telethon import TelegramClient
import telethon
from telethon.tl.functions.messages import AddChatUserRequest, GetDialogsRequest
from telethon.tl.functions.channels import InviteToChannelRequest 
from telethon.tl.types import InputPeerEmpty
from time import sleep

class TelegramGroupMovingTool():

    def __init__(self, api_id, api_hash, original_group_link, new_group_link):
        self.api_id = api_id
        self.api_hash = api_hash
        self.original_group_link = original_group_link
        self.new_group_link = new_group_link

        self.client = TelegramClient('anon', api_id, api_hash)
        with self.client:
            self.client.loop.run_until_complete(self.__main())

    async def __main(self):
        # Getting information about yourself
        original_group = await self.client.get_entity(self.original_group_link)
        new_group = await self.client.get_entity(self.new_group_link)
        participants = await self.client.get_participants(original_group)
        n=0;
        for part in participants:
            n+=1
            if n==10:
                n=0
                sleep(120)
            users = []
            if part.bot == False and part.is_self == False:
                users.append(part)
            try:
                await self.client(InviteToChannelRequest(new_group.id, users))
            except Exception as e: 
                print(e)

        '''print("Adding users:")
        for part in participants:
            if part.bot == False and part.is_self == False:
                print(str(part.id) + " " + str(part.first_name) + " " + str(part.last_name))
                print(str(part.id) + "wtf")
                await self.client(InviteToChannelRequest(new_group.id, part))
'''
if __name__ == '__main__':
    print("""This is a tool to move all members from a group to another one.
            Look at github.com/alexcarchiar/TelegramGroupMovingTool
            to know how to use it. Make sure to have your own api from Telegram.
            The program may ask you to insert your telephone number: add it in
            this way: +(Country Code)(Number)""")
    api_id = input("Insert api id\n")
    api_hash = input("Insert api hash\n")
    original_group_link = input("Insert original group link\n")
    new_group_link = input("Insert new group link\n")
    TelegramGroupMovingTool(api_id, api_hash, original_group_link, new_group_link)

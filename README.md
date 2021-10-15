# TelegramGroupMovingTool
TelegramGroupMovingTool is a small python script that I created for my students' team in order to move all participants from one group to another. Customize it as you wish!

## Installation
Python 3 is required as well as Telethon and its dependencies
```console
# install required Python 3 modules
$ python -m pip install -r requirements.txt
```

## Setup
In order to use the Tool, you first need to:
- Create your own Telegram api id and hash [Click here to go to telegram](https://my.telegram.org/)
- get the link of the originial group (t.me/joinchat/SomeRandomCharacters)
- get the link of the new group (t.me/joinchat/SomeOtherRandomCharacters)
- the bot will add all users (NOT BOTS) from the original group to the newer one
- 
## Usage
### Method 1: Run directly
**TelegramBlaster** can be run directly by executing the following command
```console
$ python3 TelegramGroupMovingTool.py
```
Using this method the program will ask you the api keys (possibly the phone number) and the group links.

### Method 2: Import script
**TelegramGroupMovingTool** can be imported in your Python script and used in the following way
```python
from TelegramGroupMovingTool import TelegramGropuMovingTool
TelegramGroupMovingTool(api_id, api_hash, original_group_link, new_group_link)
```

## New Update:

If you need to add people from a group to a megagroup, use the new module TelegramMegaGroupMovingTool.py . Remember that in order to avoid being detected as a flood spam by Telegram, the tool stops for two minutes every time it adds new people. In order to run it, do the same as for the other script.    

##### Created by [Alessandro Chiarelli](https://github.com/alexcarchiar) because I hate repetitive tasks!

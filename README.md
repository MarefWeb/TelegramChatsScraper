# Telegram channel/chat parser by keywords
It's simple, install dependencies: ```pip install -r requirements.txt```.  

Specify in config.py:
- client information (api_id, api_hash, session_name),
- recipient (to whom all these messages will be sent),
- channel names (where the messages will come from),
- keywords (words the message should contain). 

Everything is ready to work.  
Now run: ```python bot.py``.

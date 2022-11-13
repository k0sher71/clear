## Clear Discord Messages
A simple aplication for clearing messages in Discord

## Configuration

- Change your token in:

```
token = "your token here"
```
- Change command for clear in line 24. The default is "clear", change it to the word you want to be your command.

```python
async def clear(ctx, limit: int = None):
```

- If you want to use a prefix so that only the message with it makes the cleaner work, such as ".clear" or something else, set your prefix on line 2 in "prefix".

```
prefix = ""
```

## For use

-  For the perfect use is has necessited the Python 3.10.0
- After installation of Python 3.10.0, open your command prompt and paste:

```
pip install discord.py==1.7.3
```

- After installing the discord.py package version 1.7.3, initialize the archive main.py
- If main.py starts successfully, a message will appear with your account username (example below) and it is ready to use.

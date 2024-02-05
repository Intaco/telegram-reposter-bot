# Telegram reposter bot

This simple USER API based bot is capable of reposting from multiple sources to specified target chat

To get started you need to edit `.env` file and specify four env variables:

`API_ID` and `API_HASH` are both your registered [Telegram app credentials](https://my.telegram.org/auth?to=apps) 

`TARGET_CHAT_NAMES` are, obviously, names of the chats where outputs goes to. Target chat names are separated by `;;;`

`SOURCE_CHAT_NAMES` contains names of your source chats. If you need multiple chat support for one target chat, separate names with `,,,`.
If you have multiple target chats you need to separate your `SOURCE_CHAT_NAMES` with `;;;`.

For example:
You have `TARGET_CHAT_NAMES=CHAT_A;;;CHAT_B`, and `SOURCE_CHAT_NAMES=CHAT_1,,,CHAT_2;;;CHAT_3`
Then you will have this source to target chat's mapping:
```
CHAT_1 reposts to CHAT_A
CHAT_2 reposts to CHAT_A
CHAT_3 reposts to CHAT_B
```

If you have both python3.6 and pipenv preinstalled in your system, you can simply then run the bot via:

```
pipenv shell
python main.py
``` 

If you're looking for a always-restarting docker container please feel free to use the projects Dockerfile
```
docker build -t reposter .
docker container run --interactive --restart=always reposter
``` 

### After bot start you will be once prompted to enter your telegram credentials. After that, you can add `-d` flag to docker run command to start container in background

# Telegram reposter bot

This simple USER API based bot is capable of reposting from multiple sources to specified target chat

To get started you need to edit `.env` file and specify four env variables:

`API_ID` and `API_HASH` are both your registered [Telegram app credentials](https://my.telegram.org/auth?to=apps) 

`TARGET_CHAT_NAME` is, obviously, name of the chat where all the output goes to

`SOURCE_CHAT_NAMES` contains names of your source chats. If you need multiple chat support, separate names with `,,,`

If you have both python3.6 and pipenv preinstalled in your system, you can simply then run the bot via:

```
pipenv shell
python main.py
``` 

If you're looking for a always-restarting docker container please feel free to use the projects Dockerfile
```
docker build -t reposter .
docker container run --it --restart=always reposter
``` 

### After bot start you will be once prompted to enter your telegram credentials. After that, you can add `-d` flag to docker run command to start container in background

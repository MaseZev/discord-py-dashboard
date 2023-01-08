<h1 align=center>discord-ext-dashboard</h1>
<p align=center>Веб-перехватчик и расширение discord.py на основе запросов для создания панели инструментов бота.</p>

## Установка
```py
# ЕСЛИ УСТНОВЛЕН
pip install --upgrade discord-ext-dashboard

# ЕСЛИ НЕ УСТАНОВЛЕН
python3 -m pip install --upgrade discord-ext-dashboard
```

## Применение
### Предпосылки
Прежде чем приступить к работе, вам понадобится несколько вещей:
 - Вебхук в секретном канале (если у кого-то есть доступ, он сможет все получить лягушку а это плохо).
 - Правильно размещенный бот [**discord.py**](https://github.com/Rapptz/discord.py)
 
 И так поехали!(жабы топ)

### Примеры
#### Бот
```py
import discord
from discord.ext import commands
from discord.ext.dashboard import Dashboard

bot = commands.Bot(command_prefix="!")
bot_dashboard = Dashboard(bot,
	"secret_key", 
	"https://your-bot-website.com/dashboard"
)

@bot.event
async def on_ready():
	print(f"Bot is online as {bot.user}")

@bot.event
async def on_message(message):
	await bot_dashboard.process_request(message)

@bot_dashboard.route
async def guild_count(data):
	return len(bot.guilds)

@bot_dashboard.route
async def member_count(data):
	return await bot.fetch_guild(data["guild_id"]).member_count

bot.run("your-token-here")
```


#### Веб-сервер
```py
from quart import Quart, request
from discord.ext.dashboard import Server

app = Quart(__name__)
app_dashboard = Server(
	app,
	"secret_key", 
	webhook_url="https://your-private-discord-webhook.com",
	sleep_time=1
)

@app.route("/")
async def index():
	guild_count = await app_dashboard.request("guild_count")
	member_count = await app_dashboard.request("member_count", guild_id=776230580941619251)

	return f"Guild count: {guild_count}, Server member count: {member_count}"

@app.route("/dashboard", methods=["POST"])
async def dashboard():
	# Don't worry about authorization, the bot will handle it
	await app_dashboard.process_request(request)
        
        
if __name__ == "__main__":
        app.run()
```


Обратите внимание, что Cogs в настоящее время не поддерживаются.
<br>
Вам также нужно будет использовать Quart в качестве веб-сервера. Переключиться с другой библиотеки несложно.
<br><br>

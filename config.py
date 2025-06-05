# Cyberspace bot

##This source serves as a base for Cyberspace store bots.
##It aims to be as modular as possible, allowing adding new features with minor effort.

## Example config file
#6203838763:AAFKHxOaQilei4GnWtvyJ6NPXI03qwhuFI8
##```python
# Your Telegram bot token.
BOT_TOKEN = "6300471754:AAFp6xclaS4xjlEfzMzvQ40iljpIg_MViCA"

# Telegram API ID and Hash. This is NOT your bot token and shouldn't be changed.
API_ID = 28798075
API_HASH = "dde9939fb55e753bd8a98446421d024e"

# Chat used for logging errors.
LOG_CHAT = -4631480574

# Chat used for logging user actions (like buy, gift, etc).
ADMIN_CHAT = 6543538187
GRUPO_PUB = -4631480574


# How many updates can be handled in parallel.
# Don't use high values for low-end servers.
WORKERS = 20

# Admins can access panel and add new materials to the bot.
ADMINS = [6543538187]

# Sudoers have full access to the server and can execute commands.
SUDOERS = [6543538187]

# All sudoers should be admins too
ADMINS.extend(SUDOERS)

GIFTERS = [6543538187]

# Bote o Username do bot sem o @
# Exemplo: default
BOT_LINK = "Lojateste2_bot"



# Bote o Username do suporte sem o @
# Exemplo: suporte
BOT_LINK_SUPORTE = "Lojateste2_bot"
##```

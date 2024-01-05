import os

from dotenv import load_dotenv

load_dotenv(".env")

DEVS = [
    2104193674, # joo
    1271323777, # gutama
    1757306905, # Vynnnn
]

KYNAN = list(map(int, os.getenv("KYNAN", "isi id kalian").split()))

API_ID = int(os.getenv("API_ID", "17250424"))

API_HASH = os.getenv("API_HASH", "753bc98074d420ef57ddf7eb1513162b")

BOT_TOKEN = os.getenv("BOT_TOKEN", "6455437707:AAEfcAzWnj4KElzbLV-8VSZbVB5CrtDeOwQ")

OWNER_ID = int(os.getenv("OWNER_ID", "482945686"))

USER_ID = list(map(int, os.getenv("USER_ID", "1054295664 876054262 793488327 5573141376 482945686").split()))

LOG_UBOT = int(os.getenv("LOG_UBOT", "-1001625266512"))

LOG_SELLER = int(os.getenv("LOG_SELLER", "-1001916459727"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1001608847572 -1001538826310 -1001876092598 -1001864253073 -1001451642443 -1001825363971 -1001797285258 -1001927904459 -1001287188817 -1001812143750 -1001608701614 -1001473548283 -1001861414061").split()))

MAX_BOT = int(os.getenv("MAX_BOT", "25"))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

OPENAI_KEY = os.getenv(
    "OPENAI_KEY",
    "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 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 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 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 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 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",
).split()

MONGO_URL = os.getenv(
    "MONGO_URL",
    "mongodb+srv://botsebar15:1234@cluster0.wnpxjhu.mongodb.net/?retryWrites=true&w=majority",
)

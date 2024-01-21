import os

from dotenv import load_dotenv

load_dotenv(".env")

DEVS = [
    2104193674, # joo
    1271323777, # gutama
    1757306905, # Vynnnn
]


API_ID = int(os.getenv("API_ID", "28805535"))

API_HASH = os.getenv("API_HASH", "25c5b085046408ee8abee7773d7499ea")

BOT_TOKEN = os.getenv("BOT_TOKEN", "6750394970:AAHyVrRPtKgdOB8Jo74Rs08Wh3fkaFdjSe0")

OWNER_ID = int(os.getenv("OWNER_ID", "1757306905"))

USER_ID = list(map(int, os.getenv("USER_ID", "1757306905").split()))

LOG_UBOT = int(os.getenv("LOG_UBOT", "-1002003800097")) #contoh -123456789

LOG_SELLER = int(os.getenv("LOG_SELLER", "-1002078982723")) #contoh -123456789

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002003800097 -1002078982723 -1001841041794 -1001781720956 -1002104344623").split()))

MAX_BOT = int(os.getenv("MAX_BOT", "25"))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

OPENAI_KEY = os.getenv(
    "OPENAI_KEY",
    "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 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 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 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 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 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",
).split()

MONGO_URL = os.getenv(
    "MONGO_URL",
    "mongodb+srv://Kuro:Kuro@cluster0.8i68gfk.mongodb.net/?retryWrites=true&w=majority",
)

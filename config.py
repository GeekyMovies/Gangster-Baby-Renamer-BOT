import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "23311160")

API_HASH = os.environ.get("API_HASH", "2a1366013eca4256bce853346dbcda49")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5899883059:AAHDCdZzocLyGPVePJ1nZlzlFf-kfYged8k") 

FORCE_SUB = os.environ.get("FORCE_SUB", "@geeky_movies") 

DB_NAME = os.environ.get("DB_NAME","geekymovies")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://Geekymovies:Geekymovies@cluster0.7llffit.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5691018873').split()]

PORT = os.environ.get("PORT", "8080")

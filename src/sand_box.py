
from decouple import config


port = config('SERVER_PORT', cast=int)
print(port)
DB = config('ACCESS_DB', cast=str)
print(DB)
from dotenv import load_dotenv
import os

# [SERVER PART]

HOST_NAME = 'localhost'
PORT_NUMBER = 8000
# website urls
ROUTES = ["/", "/login", "/registration", "/profile"]

# [ANALYZE PART]

load_dotenv()

LOG_DIR = "logs/"
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
INDEX_NAME = "web-analysis"
PATH_FILE_BASIC = BASE_DIR + "\\data\\"

KAFKA_LOCALHOST = "localhost:9092"
GROUP_ID = "counters"

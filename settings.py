from dotenv import load_dotenv
import os

# [SERVER PART]

SERVER_NAME = "server-test"
HOST_NAME = 'localhost'
PORT_NUMBER = 8000
# website urls
ROUTES = ["/", "/login", "/registration", "/profile"]

# [ANALYZE PART]

load_dotenv()

LOG_DIR = "logs/"
INDEX_NAME = "web-analysis"
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
PATH_FILE_BASIC = BASE_DIR + "\\AnalizeData\\configs\\data\\"

KAFKA_LOCALHOST = "localhost:9092"
GROUP_ID = "counters"

# [ELASTICSEARCH PART]

HOST_ELASTIC = "localhost"
PORT_ELASTIC = 9200

from datetime import datetime
import pytz
from azure.storage.blob import BlobClient

def get_current_date():
    current_date = datetime.now(pytz.timezone('UTC')).date()
    return current_date


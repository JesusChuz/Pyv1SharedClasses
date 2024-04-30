from datetime import datetime
import pytz

def get_current_date():
    current_date = datetime.now(pytz.timezone('UTC')).date()
    return current_date


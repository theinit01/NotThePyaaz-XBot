'''
module for logging activities
'''

import datetime
import pytz

LOG_FILE = 'bot_log.txt'

def log_activity(activity):
    # Get the current UTC time
    utc_now = datetime.datetime.utcnow()

    # Convert UTC time to IST
    ist_timezone = pytz.timezone('Asia/Kolkata')  # Indian Standard Time
    ist_now = utc_now.replace(tzinfo=pytz.utc).astimezone(ist_timezone)

    # Format timestamp as per your requirement
    timestamp = ist_now.strftime('%Y-%m-%d %H:%M:%S')

    # Prepare log entry
    log_entry = f"[{timestamp}] - {activity}"

    # Write log entry to file
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(log_entry + '\n')
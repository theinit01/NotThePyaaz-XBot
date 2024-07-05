'''
module for logging activities
'''

import datetime

LOG_FILE = 'bot_log.txt'

def log_activity(activity):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"[{timestamp}] - {activity}"
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(log_entry + '\n')
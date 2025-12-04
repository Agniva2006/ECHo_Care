import os
from datetime import datetime
import json


JPATH = "data/journal"
os.makedirs(JPATH, exist_ok=True)


def save_entry(user_text):
    date = datetime.utcnow().strftime("%Y-%m-%d_%H%M%S")
    fname = os.path.join(JPATH, f"entry_{date}.txt")
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(user_text)
    return fname


def weekly_summary():
# naive summary: count emotion keywords
    entries = os.listdir(JPATH)
    recent = entries[-7:]
    return f"You have {len(entries)} journal entries; {len(recent)} in the last 7 saves."
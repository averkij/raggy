from datetime import datetime

import constants as con


def log(msg):
    print(msg)
    with open(con.LOG_FILE, "a", encoding="utf-8") as fout:
        date = datetime.now().strftime("%d.%m.%Y %H:%M")
        fout.write(f"[{date}] {msg}\n")

import sys
from libs import Connect
import time
try:
    start_time = time.time()
    p = Connect(user="u1", pwd="cisco", host="192.168.122.100", port=22)
    # remove limitation of console output
    p.send_command("terminal length 0")

    # go into privilege mode
    p.send_command("enable")
    print(p.send_command("cisco"))

    # get current config
    result = p.send_command("show run")
    print(repr(result))
    splitter = "Current configuration"

    config_text = splitter + "".join(result.split(splitter)[1:])
    print(config_text)

    with open("file_timestamp.txt", "w") as file:
        file.write(config_text)

    end_time = time.time()
    print(f"Scrit took {end_time - start_time} seconds")
except Exception as e:
    print(e, file=sys.stderr)

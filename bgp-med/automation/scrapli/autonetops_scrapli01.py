import sys
sys.path.append("..")
from helpers import read_yaml, save_file

from rich import print as rprint, inspect
from scrapli import Scrapli

# Read the device list from the YAML file
device_list = read_yaml("../inventory_scrapli.yaml")

for device in device_list:
    conn = Scrapli(**device)
    conn.open()

    conn.send_configs([
        "interface Loopback0",
        "description AUTONETOPS",
    ])

    output = conn.send_command("show interfaces description")
    print(f"{device['host']} - {output.result}")
    #save_file(f"{device['host']}_backup.txt", backup.result)

    conn.close()


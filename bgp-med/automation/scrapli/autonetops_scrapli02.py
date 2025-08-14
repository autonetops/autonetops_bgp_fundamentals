import sys
sys.path.append("..")
from helpers import read_yaml, save_file

from rich import print as rprint, inspect
from scrapli import Scrapli
from scrapli.exceptions import ScrapliAuthenticationFailed, ScrapliConnectionError

# Read the device list from the YAML file
device_list = read_yaml("../inventory_scrapli.yaml")

for device in device_list:
    print(f"Connecting to {device['host']}...")
    try:
        with Scrapli(**device) as conn:
            conn.send_configs([
                "interface Loopback0",
                "description AUTONETOPS",
            ])

            output = conn.send_command("show interfaces description")
            print(f"{device['host']} - {output.result}")
            #save_file(f"{device['host']}_backup.txt", backup.result)
    except ScrapliAuthenticationFailed as auth_err:
        rprint(f"[red]Authentication failed for {device['host']}: {auth_err}[/red]")
    except ScrapliConnectionError as conn_err:
        rprint(f"[red]Connection error for {device['host']}: {conn_err}[/red]")
    except Exception as e:
        rprint(f"[red]Error w/ {device['host']}: {e}[/red]")



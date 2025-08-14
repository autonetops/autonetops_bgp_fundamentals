import sys
sys.path.append("..")
from helpers import read_yaml, save_file

from napalm import get_network_driver
from napalm.base.exceptions import ConnectionException
from rich import print as rprint
import ipdb


device_list = read_yaml('../inventory_napalm.yaml')

for device in device_list:
    driver = get_network_driver(device['optional_args']['driver'])

    try:
        with driver(**device) as conn:
            conn.load_merge_candidate(config='ip name-server 1.1.1.1')
            conn.commit_config()
            output = conn.cli(['show ip interface brief'])

            print(output)
    except ConnectionException as conn_err:
        rprint(f"[red]Connection error for {device['hostname']}: {conn_err}[/red]")
    except Exception as e:
        rprint(f"[red]Error w/ {device['hostname']}: {e}[/red]")
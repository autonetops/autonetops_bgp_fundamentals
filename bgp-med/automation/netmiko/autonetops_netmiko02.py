import sys
sys.path.append("..")
from helpers import read_yaml, save_file

from rich import print as rprint, inspect
from netmiko import ConnectHandler, NetmikoAuthenticationException
import ipdb

# Read the device list from the YAML file
device_list = read_yaml("../inventory_netmiko.yaml")

for device in device_list:
    try:
        with ConnectHandler(**device) as conn_device:
            device_backup = conn_device.send_command("show running-config")
            save_file(f"{device['host']}_backup.txt", device_backup)
    except NetmikoAuthenticationException as auth_err:
        rprint(f"[red]Authentication failed for {device['host']}: {auth_err}[/red]")
    except Exception as e:
        rprint(f"[red]Error w/ {device['host']}: {e}[/red]")



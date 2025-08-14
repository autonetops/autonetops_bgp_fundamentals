import sys
sys.path.append("..")
from helpers import read_yaml, save_file

from rich import print as rprint, inspect
from netmiko import ConnectHandler
import ipdb

# Read the device list from the YAML file
device_list = read_yaml("../inventory_netmiko.yaml")

for device in device_list:
    
    conn_device = ConnectHandler(**device)
    device_backup = conn_device.send_command("show running-config")
    save_file(f"{device['host']}_backup.txt", device_backup)

    conn_device.disconnect()
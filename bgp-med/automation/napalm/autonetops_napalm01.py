import sys
sys.path.append("..")
from helpers import read_yaml, save_file

from napalm import get_network_driver
import ipdb


device_list = read_yaml('../inventory_napalm.yaml')

for device in device_list:
    driver = get_network_driver(device['optional_args']['driver'])

    conn = driver(**device)
    conn.open()

    conn.load_merge_candidate(config='ip name-server 1.1.1.1')
    conn.commit_config()
    output = conn.cli(['show ip interface brief'])

    print(output)

    conn.close()

from napalm import get_network_driver
import yaml
import ipdb
import ncclient

def read_yaml(path):
    with open('inventory.yaml', 'r') as f:
        device_list = yaml.safe_load(f)
    return device_list

def save_file(path, data):
    
    with open(path, 'w') as f:
        f.write(data)

device_list = read_yaml('inventory.yaml')

"""for device in device_list:
    driver = get_network_driver(device['optional_args']['driver'])
    conn = driver(**device)
    conn.open()
    conn.load_replace_candidate(filename=f'{device["hostname"]}_config.txt')
    has_changes = conn.compare_config()

    if has_changes:
        print(has_changes)
        confirm = input(f'Changes detected for {device["hostname"]}. Do you want to commit? (yes/no): ')
        if confirm.lower() == 'yes':
            conn.commit_config()
    else:
        print(f'No changes detected for {device["hostname"]}')
    #config = conn.get_config(retrieve='running', sanitized=True)
    #save_file(f'{device["hostname"]}_config.txt', config['running'])


    conn.close()
"""
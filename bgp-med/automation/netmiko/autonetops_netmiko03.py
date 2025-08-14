import sys
sys.path.append("..")
from helpers import read_yaml, save_file

from rich import print as rprint, inspect
from netmiko import ConnectHandler, NetmikoAuthenticationException
import ipdb
from jinja2 import Environment, FileSystemLoader

# Read the device list from the YAML file
device_list = read_yaml("../inventory_netmiko.yaml")

def build_template_info(template_name, tempate_info):
    env = Environment(loader=FileSystemLoader('../templates'))
    template = env.get_template(f'{template_name}.j2')
    config = template.render(template_info)

    return config

for device in device_list:

    template_info = device.pop("templates_info")
    try:
        with ConnectHandler(**device) as conn_device:
            for template_name in template_info:
                print(template_name)
                config = build_template_info(template_name, template_info[template_name])
                rprint(f"[green]Configuring {device['host']} with template: {config}[/green]")
                conn_device.enable()
                conn_device.send_config_set(config.splitlines())
                print(config)

            
    except NetmikoAuthenticationException as auth_err:
        rprint(f"[red]Authentication failed for {device['host']}: {auth_err}[/red]")
    except Exception as e:
        rprint(f"[red]Error w/ {device['host']}: {e}[/red]")



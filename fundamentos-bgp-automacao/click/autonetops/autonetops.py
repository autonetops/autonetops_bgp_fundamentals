import click
import yaml
import os
from jinja2 import Template
from netmiko import ConnectHandler
from .utils.utils import debug_msg, check_result
import ipdb


@click.group(help="Utilities for autonetops automation.")
@click.option("--debug", is_flag=True, help="Print debug messages during procesing")
@click.option("--cli-verbose", is_flag=True, help="Stream CLI connection info to screen")
@click.option(
    "-i",
    "--inventory",
    default="task1.yaml",
    help="The network inventory file to operate on",
)
@click.pass_context
def cli(ctx, invetory, debug, cli_verbose):
    """Autonetops CLI tool for network automation."""

    ctx.ensure_object(dict)

    ctx.obj["debug"] = debug
    ctx.obj["cli_verbose"] = cli_verbose
    
    # load the inventory file
    with open(inventory) as f:
        inventory = yaml.safe_load(f)

    # save the inventory file in the context
    ctx.obj["inventory"] = inventory
    ctx.obj["network_username"] = os.getenv("lab_username")
    ctx.obj["network_password"] = os.getenv("lab_password")

@click.group(help="Utilities for configuring tasks.")
@click.command(name="task", help="Render configuration from task<TASK_NUMBER>.yaml and task<TASK_NUMBER>.j2, display it, and push the configuration to a device.")
@click.pass_context
def task(ctx, task_number):
    """
    Render configuration from task<TASK_NUMBER>.yaml and task<TASK_NUMBER>.j2,
    display it, and push the configuration to a device.
    """
    # Define filenames based on the task number
    yaml_file = f"task{task_number}.yaml"
    j2_file = f"task{task_number}.j2"
    
    # Load YAML file containing device configuration data
    try:
        with open(yaml_file, 'r') as yf:
            data = yaml.safe_load(yf)
    except FileNotFoundError:
        click.echo(f"YAML file {yaml_file} not found!")
        return

    try:
        device_data = list(data.values())[0]
    except (AttributeError, IndexError):
        click.echo("Error processing YAML file. Ensure it has the correct structure.")
        return

    # Load the Jinja2 template file
    try:
        with open(j2_file, 'r') as tf:
            template_content = tf.read()
    except FileNotFoundError:
        click.echo(f"Jinja2 template file {j2_file} not found!")
        return

    # Render the template with the YAML data
    template = Template(template_content)
    rendered_config = template.render(**device_data)

    # Display the rendered configuration
    click.echo("\n--- Rendered Configuration ---")
    click.echo(rendered_config)
    click.echo("--- End of Configuration ---\n")

    # Define the device connection details.
    # You should update these values according to your environment.
    device = {
        'device_type': 'cisco_ios',   # or any other supported type
        'host': '192.168.1.1',          # device IP address
        'username': 'admin',            # device username
        'password': 'admin',            # device password
        'secret': 'admin',              # enable/privilege mode password if needed
    }

    # Push the configuration to the device using Netmiko
    try:
        click.echo("Connecting to device...")
        net_connect = ConnectHandler(**device)
        net_connect.enable()  # Enter enable mode if required

        # Netmiko's send_config_set expects a list of commands.
        config_lines = rendered_config.splitlines()
        click.echo("Pushing configuration...")
        output = net_connect.send_config_set(config_lines)
        click.echo("Configuration pushed successfully. Device response:")
        click.echo(output)

        net_connect.disconnect()
    except Exception as e:
        click.echo(f"Failed to push configuration: {e}")

cli.add_command(task)

if __name__ == '__main__':
    cli()

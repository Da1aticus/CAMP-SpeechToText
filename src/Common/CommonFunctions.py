import yaml

def ParseConfiguration(yamlFile):
    # parse configuration 
    try:
        with open(f"{yamlFile}", "r") as file:
            config = yaml.safe_load(file)
            
    except FileNotFoundError:
        click.echo(f"Error: The file {file} was not found.")
        return
    
    except yaml.YAMLError as e:
        click.echo(f"Error: The file {file} is not a valid YAML file.")
        return
    
    return config
#!/usr/bin/env python3
import subprocess
import requests
import json
import typer

app = typer.Typer()

def repo(name):
    return name
def project(type_of):
    return type_of

def create(repo, project_type):
    new_directory = f'Projects/{repo}'

    URL = f'https://api.github.com/user/repos'
    TOKEN = 'GitHub Personal Access Token'
    AUTHENTICATION = f"token {TOKEN}"

    jsonPayload = {"name": repo}

    headers = {"Accept": "appliechoion/vnd.github.v3+json",
                "Authorization": AUTHENTICATION      
                }

    response = requests.post(URL, headers=headers, data=json.dumps(jsonPayload))

    def project_creator(commands):
        project_creator = [subprocess.run(command) for command in commands]

# Lists of commands that will create the individual project folder with the proper coding language and files needed.
    
    # Python Project Folder
    commands_py = [
        ['mkdir',f'{new_directory}'],
        ['touch',f'{new_directory}/{repo}.py'],
        ['ln', f'{new_directory}/{repo}.py', f'{repo}.py'],
        ['chmod', '+x', f'{repo}.py'],
        ['git', 'init',f'{new_directory}'],
        ['code', f'{new_directory}/']
        ]

    # Bash Script Project Folder
    commands_bash = [
        ['mkdir',f'{new_directory}'],
        ['cp', 'prompts/bash.sh', f'{new_directory}/{repo}.sh'],
        ['ln', f'{new_directory}/{repo}.sh', f'{repo}.sh'],
        ['chmod', '+x',f'{repo}.sh'],
        ['git', 'init',f'{new_directory}'],
        ['code', f'{new_directory}/']
        ]

    if project_type == 'py': 
        project_creator(commands_py)
    elif project_type == 'sh': 
        project_creator(commands_bash)

# Confirms that the project template was created successfully.
    if response.status_code == 201:
        print(f"\n'{repo}' was successfully created!!!\n")
    else:
        print(f'\n{response.status_code}')
        print(f'{response.content}\n')

@app.command()
def py(name: str):
    create(repo(name), project('py'))

@app.command()
def sh(name: str):
    create(repo(name), project('sh'))

if __name__ == "__main__":
    app()
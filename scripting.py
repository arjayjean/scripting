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
        # Creates a directory on your local system for your project
        ['mkdir',f'{new_directory}'],
        # Creates a file for your project in the directory that was previously created
        ['touch',f'{new_directory}/{repo}.py'],
        # Creates a file on your home directory with a "hard link" to the file in your project directory 
        ['ln', f'{new_directory}/{repo}.py', f'{repo}.py'],
        # Provides the previously created file permissions to be executed
        ['chmod', '+x', f'{repo}.py'],
        # Turns your directory into a Git repository
        ['git', 'init',f'{new_directory}'],
        # Opens Visual Studio Code
        ['code', f'{new_directory}/']
        ]

    # Bash Script Project Folder
    commands_bash = [
        # Creates a directory on your local system for your project
        ['mkdir',f'{new_directory}'],
        # Creates a copy of a file with a prefilled shebang (#!/bin/bash); 
        # Indicates to the system how we want this file to be executed, which will be using the absolute path to our Bash executable.
        ['cp', 'prompts/bash.sh', f'{new_directory}/{repo}.sh'],
        # Creates a file on your home directory with a "hard link" to the file in your project directory 
        ['ln', f'{new_directory}/{repo}.sh', f'{repo}.sh'],
        # Provides the previously created file permissions to be executed
        ['chmod', '+x',f'{repo}.sh'],
        # Turns your directory into a Git repository
        ['git', 'init',f'{new_directory}'],
        # Opens Visual Studio Code
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
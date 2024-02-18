# GPT Command Translator

## Overview

This project leverages the OpenAI API to translate user input into commands compatible with the operating system the script is run on. As a bonus, you can add this program as a command straight into your Terminal for easy use (See "Setting Up PATH for Easy Access" section).

## Features

- Auto-detects the operating system (Windows, MacOS, Linux).
- Translates input commands to the detected operating system's command syntax.
- Utilizes OpenAI's GPT models for accurate command translation.

## Requirements

- Python 3
- OpenAI Python Package
- Requests Package

Ensure you have an OpenAI API key set up in your environment to use their services.

## Installation

Clone this repository to your local machine using:

`git clone https://github.com/ZakYeo/gpt-command.git`

Navigate to the project directory:

`cd gpt-command`

Install the required Python packages:

`pip install openai requests`

## Usage

To use the script, open your Terminal and navigate to the directory where the script is saved. Then, execute the script with your command as an argument. The syntax is as follows:

`python gpt.py <command>`

Replace `<command>` with the command you wish to translate. For example, if you want to translate "list all files" into a command compatible with your operating system, you would use:

`python gpt.py "list all files"`

The script will output the translated command based on the operating system it detects.

## Setting Up PATH for Easy Access

To run `gpt.py` from any directory without having to specify its full path, you can run the provided script, `add_to_path.sh`, which automates this process for you.

This script automatically creates an alias gpt that points to your gpt.py script, allowing you to run the script from any directory in your Terminal without needing to add it to your PATH. The alias is added to your ~/.zshrc file. After running the script, please restart your Terminal or run source ~/.zshrc to apply the changes.

### Using the Setup Script (MacOS)

1. Open a Terminal and navigate to the directory where `gpt.py` is located.
2. Ensure that `add_to_path.sh` is in the same directory as `gpt.py` and is executable. You can make it executable by running:

   `chmod +x add_to_path.sh.sh`

3. Run the setup script:

   `./add_to_path.sh.sh`

This script automatically adds the current directory (where `gpt.py` is located) to your `PATH` by appending a line to your `~/.zshrc` file. After running the script, please restart your Terminal or run `source ~/.zshrc` to apply the changes.

Now, you can simply type `gpt <command>` from any directory in your Terminal to run the script.

### Setting Up on Windows

To facilitate running `gpt.py` on Windows from any directory, a PowerShell script has been provided. This script adds the directory containing `gpt.py` to your user's PATH environment variable, allowing the `gpt` command to be recognized globally.

1. Open PowerShell and navigate to the directory where `gpt.py` is located.
2. Ensure that `Add-GptPath.ps1` is in the same directory as `gpt.py`.
3. Execute the PowerShell script to add the directory to your PATH:

   `.\add_to_path.ps1`

If you encounter restrictions due to execution policies, you can temporarily bypass the policy for running this script with:

`powershell -ExecutionPolicy Bypass -File .\Add-GptPath.ps1`

After running the script, you may need to restart PowerShell or your computer for the changes to take effect. Now, you can simply type `gpt <command>` from any directory in your Command Prompt or PowerShell to run `gpt.py`.

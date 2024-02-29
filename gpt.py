#!/usr/bin/env python3

import sys
import platform
from openai import OpenAI
import os
import json
model = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
client = OpenAI()


def query_gpt(content, system_context=""):
    """
    Query chatGPT with the given content and system context.
    """
    if system_context:
        system_context = f"Translate to {system_context} terminal command."

    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_context},
            {"role": "user", "content": content}
        ]
    )

    return completion.choices[0].message.content

def load_custom_commands(json_file):
    """
    Loads custom commands from a JSON file.
    """
    try:
        with open(json_file, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print("Error decoding JSON. Please check the syntax of your commands file.")
        sys.exit(1)

def get_system_context(os_name):
    """
    Returns the system context for the given operating system.
    """
    return {
        "Darwin": "MacOS",
        "Linux": "Linux",
        "Windows": "Windows"
    }.get(os_name, "generic")

if __name__ == "__main__":
    custom_commands_file = 'custom_commands.json'
    custom_commands = load_custom_commands(custom_commands_file)
    os_name = platform.system()

    if len(sys.argv) > 1:
        # Determine if the first argument is a recognized command
        command = sys.argv[1]
        if command in custom_commands:
            # Custom command found in JSON
            content = " ".join(sys.argv[2:])
            system_context = custom_commands[command]
            translated_content = query_gpt(content, system_context)
        elif command == "cmd":
            # 'cmd' command processing with dynamic system context
            content = " ".join(sys.argv[2:])
            system_context = get_system_context(os_name)
            translated_content = query_gpt(content, system_context)
        else:
            # No recognized command or 'cmd', treat the entire input as content
            content = " ".join(sys.argv[1:])
            translated_content = query_gpt(content)
    else:
        print("Usage: gpt.py <command> <content> OR gpt.py <content> for no specific context")
        sys.exit(1)

    print(translated_content)
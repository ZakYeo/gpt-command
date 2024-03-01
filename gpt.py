#!/usr/bin/env python3

import sys
import platform
from openai import OpenAI
import os
import json
import argparse

model = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
should_load_custom_commands = os.getenv("LOAD_CUSTOM_COMMANDS", "true") == "true"

custom_commands_file = 'custom_commands.json'
cmd_system_context = "Translate to {} terminal command."
client = OpenAI()


def query_gpt(messages):
    """
    Query chatGPT with the given list of messages.
    """
    completion = client.chat.completions.create(
        model=model,
        messages=messages
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


def continuous_shell(custom_commands, os_name):
    """
    Enters a continuous shell for querying chatGPT, remembering previous interactions.
    """
    print("""
        ChatGPT Continuous Shell
        Prefix with your custom command to use it.
        Type 'exit' or 'quit' to exit.
        """)
    conversation_history = []
    while True:
        user_input = input(">>> ")
        if user_input.lower() in ['exit', 'quit']:
            print("Exiting continuous shell.")
            sys.exit(0)

        message = {"role": "user", "content": user_input}
        command_parts = user_input.split(maxsplit=1)  # Split input into command and the rest
        command = command_parts[0]
        if custom_commands and command in custom_commands:
            system_context = custom_commands[command]
            conversation_history.append({"role": "system", "content": system_context})
        elif user_input == "cmd":
            system_context = get_system_context(os_name)
            conversation_history.append({"role": "system", "content": system_context})

        conversation_history.append(message)

        response_content = query_gpt(conversation_history)
        print(response_content)
        conversation_history.append({"role": "assistant", "content": response_content})

def main():
    parser = argparse.ArgumentParser(description='Query GPT with custom or system commands.')
    parser.add_argument('command', nargs='?', default='', help='The command or query to process.')
    parser.add_argument('query', nargs='*', help='Additional query.')
    parser.add_argument('-c', '--continuous', action='store_true', help='Enter a continuous shell to query ChatGPT.')
    args = parser.parse_args()


    if should_load_custom_commands:
        custom_commands = load_custom_commands(custom_commands_file)
    else:
        custom_commands = {}
    os_name = platform.system()

    if args.continuous:
        continuous_shell(custom_commands, os_name)
    elif args.command:
        messages = []  # Construct the message list for a single interaction
        command = args.command
        content = " ".join(args.query)

        if custom_commands and command in custom_commands:
            # Execute custom command handler
            system_context = custom_commands[command]
            messages.append({"role": "system", "content": system_context})
        elif command == "cmd":
            # Execute built-in cmd command
            system_context = get_system_context(os_name)
            messages.append({"role": "system", "content": cmd_system_context.format(system_context)})

        messages.append({"role": "user", "content": content if content else command})

        translated_content = query_gpt(messages)
        print(translated_content)
    else:
        print("Usage: Provide a command and/or content. Use --help for more information.")
        sys.exit(1)

if __name__ == "__main__":
    main()
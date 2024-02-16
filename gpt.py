#!/usr/bin/env python3

import sys
import platform
from openai import OpenAI
import requests

client = OpenAI()

def translate_command(command, os_name):
    # Normalize the os_name for common operating systems
    os_context = {
        "Darwin": "MacOS",
        "Linux": "Linux",
        "Windows": "Windows"
    }.get(os_name, "generic")

    system_context = f"You are now a translator. You translate the input into its {os_context} compatible command."

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_context},
            {"role": "user", "content": command}
        ]
    )
    return completion.choices[0].message.content

if __name__ == "__main__":
    os_name = platform.system()
    if len(sys.argv) < 2:
        print("Usage: gpt <command>")
    else:
        command = " ".join(sys.argv[1:])
        translated_command = translate_command(command, os_name)
        print(translated_command)

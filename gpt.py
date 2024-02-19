#!/usr/bin/env python3

import sys
import platform
from openai import OpenAI


client = OpenAI()


def translate_command(command, os_name):
    """
    A script that translates shell commands into their equivalents for different operating systems.

    This script uses OpenAI's GPT model to translate given shell commands into their equivalent forms for MacOS, Linux, or Windows operating systems. It determines the target operating system based on the execution environment and expects the input command as a command-line argument. The script normalizes the operating system name to one of the common operating systems (MacOS, Linux, Windows) or defaults to 'generic' if the OS is not recognized. It then constructs a prompt for the GPT model to generate the translated command specifically for the identified operating system.

    Usage:
        Run the script with the command to translate as an argument.
        Example: `python3 script_name.py <command_to_translate>`

        The script outputs the translated command to the standard output.

    Note:
        - The script requires an OpenAI API key to be configured in the environment or through the OpenAI client library's configuration.
    """
    os_context = {
        "Darwin": "MacOS",
        "Linux": "Linux",
        "Windows": "Windows"
    }.get(os_name, "generic")

    system_context = f"Translate the following command into its {os_context} compatible equivalent. Provide only the translated command as a response."

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

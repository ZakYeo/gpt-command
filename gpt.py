#!/usr/bin/env python3

import sys
import platform
from openai import OpenAI
import os

model = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
client = OpenAI()


def query_gpt(content, os_name, use_system_context):
    """
    The script can be used in two ways:
        1. Without specifying a system context, which translates the given content without adding any specific system context to the translation process. Useful for general content translations.
            Usage: python gpt.py <content>
            Example: python gpt.py "list all files"

        2. With a system context, which includes the system context in the translation, making the content translation specific to the operating system the script is run on. Use this option when you need the translated content to be specifically tailored for MacOS, Linux, or Windows.
            Usage: python gpt.py cmd <content>
            Example: python gpt.py cmd "list all files"

    Note:
        - The script requires an OpenAI API key to be configured in the environment or through the OpenAI client library's configuration.
    """
    os_context = {
        "Darwin": "MacOS",
        "Linux": "Linux",
        "Windows": "Windows"
    }.get(os_name, "generic")

    if use_system_context:
        system_context = f"Translate the following content into its {os_context} compatible equivalent. Provide only the translated content as a response."
    else:
        system_context = ""

    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_context},
            {"role": "user", "content": content}
        ]
    )

    return completion.choices[0].message.content


if __name__ == "__main__":
    os_name = platform.system()
    use_system_context = False

    # Check for 'cmd' argument to determine if system context should be used
    if len(sys.argv) >= 3 and sys.argv[1] == "cmd":
        content = " ".join(sys.argv[2:])
        use_system_context = True
    elif len(sys.argv) >= 2:
        content = " ".join(sys.argv[1:])
    else:
        print("Usage: gpt.py <content> OR gpt.py cmd <content> for system context")
        sys.exit(1)

    translated_content = query_gpt(content, os_name, use_system_context)
    print(translated_content)

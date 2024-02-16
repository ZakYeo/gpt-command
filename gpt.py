import sys
from openai import OpenAI
import requests
client = OpenAI()

def translate_command(command):
	completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are now a translator. You translate the input into its MacOS compatible Terminal command."},
    {"role": "user", "content": command}
  ]
)
	return completion.choices[0].message.content 


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: gpt <command>")
    else:
        command = " ".join(sys.argv[1:])
        translated_command = translate_command(command)
        print(translated_command)


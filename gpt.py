import sys



def translate_command(command):
	print(f"Received command: {command}")
	return command

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("Usage: gpt <command>")
	else:
		command = " ".join(sys.argv[1:])
		translated_command = translate_command(command)
		print(translated_command)


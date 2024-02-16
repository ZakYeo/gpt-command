#!/bin/zsh

# Use the current directory as the location for gpt.py
GPT_PY_DIR="$(pwd)/gpt.py"
ALIAS_COMMAND="alias gpt='python3 $GPT_PY_DIR'"

# Check if the alias is already in the .zshrc file
if grep -qF -- "$ALIAS_COMMAND" ~/.zshrc; then
    echo "Alias for 'gpt' already exists in .zshrc."
else
    # If it's not, add it to .zshrc
    echo "$ALIAS_COMMAND" >> ~/.zshrc
    echo "Alias for 'gpt' has been added to your .zshrc. Please restart your Terminal or run 'source ~/.zshrc'."
fi

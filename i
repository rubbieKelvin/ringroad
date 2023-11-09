#!/bin/bash
# Interactive command manager

# ANSI color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Define the map of arguments to commands
declare -A commands

commands["fe"]="bun run dev"
commands["be"]="pipenv run python manage.py runserver 7000"
commands["mk-migrations"]="pipenv run python manage.py makemigrations"
commands["migrate"]="pipenv run python manage.py migrate"

# Print a helpful usage message
print_usage() {
  echo "Usage: $0 <command>"
  echo "Available commands:"
  for cmd in "${!commands[@]}"; do
    echo -e "  ${YELLOW}$cmd${NC}: ${commands[$cmd]}"
  done
}

# Check if an argument is provided
if [ "$#" -ne 1 ]; then
  print_usage
  exit 1
fi

# Check if the provided argument is in the map
if [ "${commands[$1]+exists}" ]; then
  command_to_run="${commands[$1]}"
  echo -e "${GREEN}Running \"$1\": $command_to_run ${NC}"
  eval "$command_to_run"
else
  echo -e "${RED}Invalid command \"$1\" ${NC}"
  print_usage
  exit 1
fi

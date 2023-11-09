#!/bin/bash
# Interactive command manager

# ANSI color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Declare commands array
declare -a commands

commands=(
  "fe:bun run dev"
  "be:python3.11 -m pipenv run python manage.py runserver 7000"
  "mk-migrations:pipenv run python manage.py makemigrations"
  "migrate:pipenv run python manage.py migrate"
  "mac-install-bun:bash ./scripts/bun-install-mac.sh"
)

# Print a helpful usage message
print_usage() {
  echo "Usage: $0 <command>"
  echo "Available commands:"
  for cmd in "${commands[@]}"; do
    IFS=':' read -r -a cmd_parts <<< "$cmd"
    echo -e "  ${YELLOW}${cmd_parts[0]}${NC}: ${cmd_parts[1]}"
  done
}

# Check if an argument is provided
if [ "$#" -ne 1 ]; then
  print_usage
  exit 1
fi

# Check if the provided argument is in the array
found=false
for cmd in "${commands[@]}"; do
  IFS=':' read -r -a cmd_parts <<< "$cmd"
  if [ "${cmd_parts[0]}" == "$1" ]; then
    command_to_run="${cmd_parts[1]}"
    found=true
    break
  fi
done

if $found; then
  echo -e "${GREEN}Running \"$1\": $command_to_run ${NC}"
  eval "$command_to_run"
else
  echo -e "${RED}Invalid command \"$1\" ${NC}"
  print_usage
  exit 1
fi

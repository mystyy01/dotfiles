#!/usr/bin/env bash
# Get input from Rofi
prompt=$(rofi -dmenu -p "Ask AI:")
# If user cancels, exit
[ -z "$prompt" ] && exit

# Call Python script
answer=$(python3 ~/ai_query.py "$prompt")

# Show answer in a second Rofi window
echo "$answer" | rofi -dmenu -p "Answer"
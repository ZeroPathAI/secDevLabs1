import os

# WARNING: Security Risk - This code executes arbitrary system commands from user input
# This could allow malicious users to run dangerous commands on your system
# Purpose: Takes user input and executes it as a system command using the whoami utility
os.system(input("whoami"))

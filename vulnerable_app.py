
# Intentionally Vulnerable Python Script for Educational Purposes
# Shows 5 common web application threats

import os
import subprocess
import json

# 1. Command Injection Vulnerability
user_command = input("Enter a command to run: ")
os.system(user_command)   # ❌ Vulnerable: executes user input directly

# 2. Hardcoded Credentials (Insecure Authentication)
USERNAME = "admin"        # ❌ Vulnerable
PASSWORD = "12345"        # ❌ Vulnerable

print("Logging in with hardcoded credentials...")
print(f"Username: {USERNAME}, Password: {PASSWORD}")

# 3. Insecure Deserialization
def load_settings(data):
    return json.loads(data)     # ❌ Vulnerable if attacker controls input

user_json = input("Enter JSON settings: ")
settings = load_settings(user_json)

# 4. Insecure File Handling (Path Traversal)
file_name = input("Enter file name to read: ")
with open(file_name, "r") as f:     # ❌ Allows reading any system file
    print(f.read())

# 5. Running shell commands with shell=True
subprocess.call("ls -la", shell=True)   # ❌ Encourages unsafe shell usage

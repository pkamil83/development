import subprocess

def open_calculator():
    subprocess.call(["open", "-a", "Calculator"])

def perform_calculation():
    subprocess.call(["osascript", "-e", 'tell application "Calculator" to activate', '-e', 'tell application "System Events" to keystroke "2"', '-e', 'tell application "System Events" to keystroke "+"', '-e', 'tell application "System Events" to keystroke "2"', '-e', 'tell application "System Events" to keystroke "="'])

open_calculator()
perform_calculation()

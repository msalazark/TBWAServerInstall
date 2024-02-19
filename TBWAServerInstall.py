import subprocess

# Lista de comandos a ejecutar
commands = [
    "launchctl load /Library/LaunchAgents/com.tbwa.start_server_macos.plist",
    "launchctl load /Library/LaunchAgents/com.tbwa.start_monitor_macos.plist",
    "launchctl load /Library/LaunchAgents/com.tbwa.start_captura_macos.plist"
]

starts = [
    "launchctl start com.tbwa.start_server_macos",
    "launchctl start com.tbwa.start_monitor_macos",
    "launchctl start com.tbwa.start_captura_macos"
]

# Ejecutar cada comando en la lista
for command in commands:
    subprocess.run(command, shell=True)

# Ejecutar cada comando en la lista
for start in starts:
    subprocess.run(start, shell=True)

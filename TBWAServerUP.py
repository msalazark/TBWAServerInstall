import subprocess

starts = [
    "launchctl start com.tbwa.start_server_macos",
    "launchctl start com.tbwa.start_monitor_macos",
    "launchctl start com.tbwa.start_captura_macos"
]


# Ejecutar cada comando en la lista
for start in starts:
    subprocess.run(start, shell=True)


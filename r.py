import winreg

def check_registry():
    key = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
    registry_changes = []

    try:
        registry = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key)
        for i in range(0, winreg.QueryInfoKey(registry)[1]):
            name, value, _ = winreg.EnumValue(registry, i)
            if "malware" in name.lower():
                registry_changes.append(name)
        winreg.CloseKey(registry)
    except Exception as e:
        print(f"Error reading registry: {e}")

    return registry_changes

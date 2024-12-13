import winreg

def check_registry():
    key = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
    suspicious_registry = []

    try:
        registry = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key)
        for i in range(0, winreg.QueryInfoKey(registry)[1]):
            name, value, _ = winreg.EnumValue(registry, i)
            if "malware" in name.lower() or "suspicious" in value.lower():
                suspicious_registry.append(f"Suspicious registry entry: {name} = {value}")
        winreg.CloseKey(registry)
    except Exception as e:
        print(f"Error reading registry: {e}")

    return suspicious_registry

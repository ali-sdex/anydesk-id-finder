import os
import re

def get_anydesk_id():
    user_profile = os.environ.get('USERPROFILE')
    config_path = os.path.join(user_profile, 'AppData', 'Roaming', 'AnyDesk', 'system.conf')

    if not os.path.exists(config_path):
        return "system.conf file not found."

    try:
        with open(config_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        match = re.search(r'ad\.anynet\.id=(\d+)', content)
        if match:
            return f"AnyDesk ID: {match.group(1)}"
        else:
            return "AnyDesk ID not found in the file."
    except Exception as e:
        return f"Error reading file: {e}"


if __name__ == '__main__':
    print(get_anydesk_id())

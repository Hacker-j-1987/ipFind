#coded by cyber-j
import os
import requests

os.system("clear")

print('''
██╗██████╗░███████╗██╗███╗░░██╗██████╗░
██║██╔══██╗██╔════╝██║████╗░██║██╔══██╗
██║██████╔╝█████╗░░██║██╔██╗██║██║░░██║
██║██╔═══╝░██╔══╝░░██║██║╚████║██║░░██║
██║██║░░░░░██║░░░░░██║██║░╚███║██████╔╝
╚═╝╚═╝░░░░░╚═╝░░░░░╚═╝╚═╝░░╚══╝╚═════╝░ 1.0''')

print('')

def get_ip_location(ip_address):
    try:
        response = requests.get(f'https://ipinfo.io/{ip_address}/json')
        data = response.json()

        if 'error' in data:
            return f"Error: {data['error']['message']}"

        return {
            'IP Address': data.get('ip', 'N/A'),
            'Hostname': data.get('hostname', 'N/A'),
            'City': data.get('city', 'N/A'),
            'Region': data.get('region', 'N/A'),
            'Country': data.get('country', 'N/A'),
            'Location': data.get('loc', 'N/A'),
            'Postal': data.get('postal', 'N/A'),
            'Org': data.get('org', 'N/A')
        }
    except requests.RequestException as e:
        return f"Request failed: {e}"

if __name__ == "__main__":
    ip = input("Enter an IP address : ")
    if not ip.strip():
        ip = 'me'  # Using 'me' gets your own IP address

    location = get_ip_location(ip)

    if isinstance(location, dict):  # Check if the output is a dictionary
        print("")
        print("IP Location Information:")
        print("")
        for key, value in location.items():
            print(f"→{key}: {value}")
    else:
        print(location)  # Print the error message
print("")
ex = input("Do You Want To Continue (y/n) :")

if ex == 'y':
   os.system("python ipFind.py")
else:
   os.system("clear")

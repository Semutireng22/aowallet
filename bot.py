import requests
import time
import schedule
import random
from colorama import Fore, Style, init

# Inisialisasi colorama
init(autoreset=True)

# Daftar alamat yang akan diisi secara manual
addresses = []

def print_banner():
    banner = f"""
{Fore.CYAN}
██╗   ██╗ ██████╗ ██████╗      █████╗ ██╗██████╗ ██████╗ ██████╗  ██████╗ ██████╗  
██║   ██║██╔════╝ ██╔══██╗    ██╔══██╗██║██╔══██╗██╔══██╗██╔══██╗██╔═══██╗██╔══██╗
██║   ██║██║  ███╗██║  ██║    ███████║██║██████╔╝██║  ██║██████╔╝██║   ██║██████╔╝
██║   ██║██║   ██║██║  ██║    ██╔══██║██║██╔══██╗██║  ██║██╔══██╗██║   ██║██╔═══╝ 
╚██████╔╝╚██████╔╝██████╔╝    ██║  ██║██║██║  ██║██████╔╝██║  ██║╚██████╔╝██║     
 ╚═════╝  ╚═════╝ ╚═════╝     ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝ 
{Style.RESET_ALL}
{Fore.GREEN}====================================================
     BOT                : AoWallet Faucet 
     Telegram Channel   : https://t.me/UGDairdrop
====================================================
{Style.RESET_ALL}
"""
    print(banner)

def add_address():
    print(Fore.YELLOW + "Tambahkan alamat yang ingin diklaim:")
    while True:
        address = input(Fore.CYAN + "Masukkan alamat (atau ketik 'done' untuk selesai): ")
        if address.lower() == "done":
            break
        addresses.append(address)
        print(Fore.GREEN + f"Alamat {address} telah ditambahkan.")

def request_faucet_for_addresses():
    if not addresses:
        print(Fore.RED + "Tidak ada alamat yang dimasukkan. Silakan tambahkan alamat terlebih dahulu.")
        return

    print(Fore.CYAN + "\n=== Mulai Klaim Faucet ===")
    url = "https://faucet.chivesweave.org/faucet.php"
    headers = {"Content-Type": "application/json"}

    for index, address in enumerate(addresses, start=1):
        payload = {
            "Code": "GetXweByStakingAr",
            "Address": address,
            "Rule": "EveryDay",
            "TokenName": "Chivesweave",
            "GetAmount": "1 Xwe"
        }
        try:
            response = requests.post(url, json=payload, headers=headers)
            if response.status_code == 200:
                response_json = response.json()
                if response_json.get("status") == "error":
                    message = response_json.get("message")
                    if message == "Have sent, please try again tomorrow":
                        print(Fore.YELLOW + f"[{index}/{len(addresses)}] Klaim untuk {address} sudah dilakukan sebelumnya. Silakan coba lagi besok.")
                    elif message == "Need your wallet balance more than 0.1 AR":
                        print(Fore.RED + f"[{index}/{len(addresses)}] Klaim untuk {address} gagal. Saldo dompet harus lebih dari 0.1 AR.")
                    else:
                        print(Fore.RED + f"[{index}/{len(addresses)}] Gagal klaim untuk {address}.")
                else:
                    print(Fore.GREEN + f"[{index}/{len(addresses)}] Berhasil klaim untuk {address}")
            else:
                print(Fore.RED + f"[{index}/{len(addresses)}] Gagal klaim untuk {address}. Status: {response.status_code}")
        except Exception as e:
            print(Fore.RED + f"[{index}/{len(addresses)}] Terjadi kesalahan untuk {address}: {str(e)}")

        # Penundaan acak antara 10-30 detik agar terlihat seperti manusia
        delay = random.randint(10, 30)
        print(Fore.YELLOW + f"Menunggu selama {delay} detik sebelum klaim berikutnya...")
        time.sleep(delay)

    print(Fore.CYAN + "=== Klaim Faucet Selesai ===")

def start_scheduler():
    schedule.every(24).hours.do(request_faucet_for_addresses)
    print(Fore.MAGENTA + "\nKlaim otomatis akan dilakukan setiap 24 jam.")
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    print_banner()
    add_address()

    print(Fore.YELLOW + "\nAlamat yang akan diklaim:")
    for addr in addresses:
        print(Fore.CYAN + f"- {addr}")
    
    print(Fore.MAGENTA + "\nMemulai proses klaim...")
    request_faucet_for_addresses()
    start_scheduler()

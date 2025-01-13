##  AoWallet Faucet Claimer

Bot untuk melakukan claim otomatis setiap 24 jam

## Buat Wallet

1. Buat wallet di [AoWallet](https://web.aowallet.org/home/)
2. Buat PIN dan simpan pharsenya
3. Isi wallet 0.1 AR (kalian bisa beli di CEX kesayangan)
4. Copy alamat kalian
5. Done

## Cara Pakai Script

1. Clone repo
```
git clone https://github.com/Semutireng22/aowallet.git
```
2. Buka folder repo
```
cd aowallet
```
3. Install requirement
```
pip install -r requirements.txt
```
4. Install screen biar bisa 24 jam nonstop
```
apt install screen -y
```
5. Buat screen baru
```
screen -S aowallet
```
6. jalankan botnya
```
python3 bot.py
```

Tingal paste alamat kalian. BTW  ini bisa multi account caranya cukup paste alamat terus `ENTER`. Jika alamat kaian sudah di paste semua tinggal ketik `done` maka bot akan mengeksekusi alamat kalian.

## Channel & Grup Komunitas
- [UGD Airdrop](https://t.me/UGDairdrop)
- [Ngopi UGD](https://t.me/ngopiUGD)

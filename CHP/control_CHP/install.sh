sudo apt update && sudo apt upgrade
sudo apt install build-essential git dkms bc samba samba-common-bin hostpad fimware-realtek

echo "[myshare]
comment = Samba на Linux
path = /home
guest ok = yes
read only = no
browsable = yes
writable = yes" | sudo tee -a /etc/samba/smb.conf


#install wifi drivers
git clone https://github.com/morrownr/8821cu-20210916.git
cd 8821cu-20210916
sudo ./install-driver.sh

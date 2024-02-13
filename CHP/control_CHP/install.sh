sudo apt update && sudo apt upgrade

sudo apt install samba samba-common-bin

echo "[myshare]
comment = Samba на Linux
path = /home
guest ok = yes
read only = no
browsable = yes
writable = yes" | sudo tee -a /etc/samba/smb.conf

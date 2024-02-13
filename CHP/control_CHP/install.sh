sudo apt update && sudo apt upgrade
sudo apt install build-essential git dkms bc samba samba-common-bin



#install wifi drivers
git clone https://github.com/morrownr/8821cu-20210916.git
cd 8821cu-20210916
sudo ./install-driver.sh


#add a wifi repeter
cat > /etc/systemd/system/apsys.service
echo "[Unit]
Description=apsys

[Service]
Type=oneshot
ExecStart=/bin/bash -c "sleep 20 && create_ap --no-virt wlan1 wlan0 chp 12345678"

[Install]
WantedBy=multi-user.target" | sudo tee -a /etc/systemd/system/apsys.service
systemctl deamon-reload
systemctl enable apsys.service

echo "[myshare]
comment = Samba на Linux
path = /home
guest ok = yes
read only = no
browsable = yes
writable = yes" | sudo tee -a /etc/samba/smb.conf

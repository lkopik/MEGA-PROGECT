sudo apt update -y && sudo apt install build-essential git dkms bc -y

git clone https://github.com/morrownr/8821cu-20210916.git

cd 8821cu-20210916

sudo ./install-driver.sh

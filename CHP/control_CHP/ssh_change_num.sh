#!/bin/bash

host="192.168.12.1"
username="main"
password="20182007"

remote_file="/home/main/hp.txt"

current_value=$(sshpass -p "$password" ssh "$username"@"$host" "cat \"$remote_file\"")

# Вычтите 4 из числа
new_value=$((current_value - 3))

# Запишите новое значение обратно в файл
sshpass -p "$password" ssh "$username"@"$host" "echo \"$new_value\" > \"$remote_file\""

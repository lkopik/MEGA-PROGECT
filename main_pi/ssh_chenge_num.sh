#код для изменения значения файла hp.txt (хп города)

#!/bin/bash

# Установите значения для удаленной машины, на которой нужно изменить файл
host="REMOTE_HOST"
username="REMOTE_USERNAME"
password="REMOTE_PASSWORD"

# Установите путь к файлу, который нужно изменить на удаленной машине
remote_file="/path/to/remote/file.txt"

# Получите текущее значение числа из файла
current_value=$(sshpass -p "$password" ssh "$username"@"$host" "cat \"$remote_file\"")

# Вычтите 4 из числа
new_value=$((current_value - 4))

# Запишите новое значение обратно в файл
sshpass -p "$password" ssh "$username"@"$host" "echo \"$new_value\" > \"$remote_file\""

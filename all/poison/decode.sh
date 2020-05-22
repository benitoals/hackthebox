#!/bin/bash
# secret.txt contains encoded text
secret=$(<secret.txt)
for i in {1..13}; do
        secret=$(<<<"$secret" base64 --decode)
done
echo "$secret"

set -e
ssh root@45.10.161.56 'cd /root/gzpharma && git pull --recurse-submodules'
ssh root@45.10.161.56 'cd /root/gzpharma && docker-compose up -d --build'
ssh root@45.10.161.56 'cp /root/GZpharma/infrastructure/nginx.conf /etc/nginx/sites-enabled/gzpharma.conf'
ssh root@45.10.161.56 'sudo nginx -s reload'



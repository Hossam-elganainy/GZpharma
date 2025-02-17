set -e
ssh root@45.10.161.56 'cd /root/yanbo3 && git pull --recurse-submodules'
ssh root@45.10.161.56 'cd /root/yanbo3 && docker-compose up -d --build'
ssh root@45.10.161.56 'cp /root/yanbo3/infrastructure/nginx.conf /etc/nginx/sites-enabled/yanbo3.conf'
ssh root@45.10.161.56 'sudo nginx -s reload'



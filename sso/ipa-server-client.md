# IPA Server

Server Specs: 

- 4GB memory
- 2 vCPU min.

## Step wise configurations over ipa-server

I chose rocky 9.5 (minimal iso)

1. update the repos
    - `dnf update`
2. rename the host
    - `hostnamectl set-hostname ipa-server`
    - write ipa-server at first place inside /etc/hosts in front of your sever address
3. set timezone
    - `timedatectl set-timezone Asia/Karachi`
    - `timedatectl` --> to verify the set time zone
4. sync time of all servers
    - configure chrony
    - edit /etc/chrony.conf
        
        - ```
            server 0.pool.ntp.org iburst
            server 1.pool.ntp.org iburst
            server 2.pool.ntp.org iburst
            server 3.pool.ntp.org iburst

            makestep 1.0 3
            rtcsync
            minsources 2
            log measurements statistics tracking
          ```
    - systemctl restart chronyd
    - systemctl enable chronyd
    - timedatectl status --> to confirm


> Likewise steps on ipa-client from 1-4


5. server-side

ipa-server-install --domain=gfm.support \
  --realm=GFM.SUPPORT \
  --no-ntp \
  --ds-password "@32&ipa76Passw0rd" \
  --admin-password "@32&ipa76Passw0rd" \
  --unattended


> ipa user-add test --first=Test --last=User --email=test@gfm.support --password --> (password1) 


6. ipa-client

ipa-client-install --domain=gfm.support \
  --server=ipa.gfm.support \
  --realm=GFM.SUPPORT \
  --principal=admin \
  --password="@32&ipa76Passw0rd" \
  --mkhomedir \
  --no-ntp \
  --force-ntpd

  ipa-client-install --domain=gfm.support \
  --server=ipa.gfm.support \
  --realm=GFM.SUPPORT \
  --principal=admin \
  --password="YourAdminPassword" \
  --mkhomedir \
  --no-ntp

sudo ipa-client-install --mkhomedir --no-ntp --server=ipa.gfm.support --domain=gfm.support --realm=GFM.SUPPORT --principal=admin --password="@32&ipa76Passw0rd"

admin password : adminpass






====================================================





# Teleport

https://teleport.gfm.support

## Issues:

1. no track of identity via vpn connections
2. no trail of history of user activity
3. no RBAC
4. distributed private keys -- security flaw

## Fixes:

1. alerts for each user sessions logins/logouts
2. live monitoring of users active sessions
3. Complete recording of each user session
4. zero trust centralized control and RBAC
5. no need to add/use individual keys for authentication
6. grant and revoke user access with single click
7. third parties integrations like, jenkins, aws, web-apps, etc
8. ssh tunneling to private servers
9. by default teleport gives Multifactor Authentications for all users

## Demo

- To delete a ssh resource
  - `tctl nodes ls`
  - `tctl rm node/<UUID>`
  
- To add ssh resources:
  - 

## Disaster recovery plan
  - move teleport to aws
  - enable daily snapshots 
  - S3 retention policy for logs/sessions







`teleport-admin` / `@pkgfm-#telep0rt&)oP5L`


@pkgfm-#telep0rt&)oP5L

cwefgt3l3p#$&p0rt1ngoP5L  <--- active

====

# Teleport Installation in Ubuntu 

- Add the GPG key

`curl https://deb.releases.teleport.dev/teleport-pubkey.asc | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/teleport.gpg`

- Add the APT repo (adjust the `stable` version if needed)

`echo "deb [signed-by=/etc/apt/trusted.gpg.d/teleport.gpg] https://deb.releases.teleport.dev/ stable main" | sudo tee /etc/apt/sources.list.d/teleport.list`

- Update the APT cache

`sudo apt update`

- Install teleport

`sudo apt install teleport`

- Verify Installation

`teleport version`



====================================


# UAT

version: '3.8'
 
services:
  rabbitmq:
    image: rabbitmq:3.13.6-management
    container_name: rabbitmq
    restart: always
    ports:
      - "5672:5672"
      - "15672:15672"
    environment:
      RABBITMQ_DEFAULT_USER: myuser
      RABBITMQ_DEFAULT_PASS: SelTUpHENTyleVitaBaS
    volumes:
      - rabbitmq_data:/var/lib/rabbitmq
      - rabbitmq_logs:/var/log/rabbitmq
 
  redis:
    image: redis:7.2-alpine
    container_name: redis
    hostname: redis
    restart: always
    ports:
      - "6379:6379"
    environment:
      - REDIS_PASSWORD=amANartusKAOmOnATEra
      - REDIS_PORT=6379
    volumes:
      - redis_data:/var/lib/redis
 
 
  redis-gui:
    image: rediscommander/redis-commander:latest
    container_name: redis-gui
    restart: always
    depends_on:
      - redis
    environment:
      - REDIS_HOSTS=redis
      - HTTP_USER=root
      - HTTP_PASSWORD=amANartusKAOmOnATEra
    ports:
      - "8082:8081"
 
volumes:
  rabbitmq_data:
  rabbitmq_logs:
  redis_data:


======================

# DEV

version: '3.8'

services:
  rabbitmq:
    image: rabbitmq:3.13.6-management
    container_name: rabbitmq
    restart: always
    ports:
      - "5672:5672"
      - "15672:15672"
    environment:
      RABBITMQ_DEFAULT_USER: myuser
      RABBITMQ_DEFAULT_PASS: SelTUpHENTyleVitaBaS
    volumes:
      - rabbitmq_data:/var/lib/rabbitmq
      - rabbitmq_logs:/var/log/rabbitmq

  redis:
    image: redis:7.2-alpine
    container_name: redis
    hostname: redis
    restart: always
    ports:
      - "6379:6379"
    environment:
      - REDIS_PASSWORD=amANartusKAOmOnATEra
    volumes:
      - redis_data:/data
    command: >
      sh -c "rm -rf /data/* && 
             redis-server --appendonly no --save"

  redis-gui:
    image: rediscommander/redis-commander:latest
    container_name: redis-gui
    restart: always
    depends_on:
      - redis
    environment:
      - REDIS_HOSTS=redis
      - HTTP_USER=root
      - HTTP_PASSWORD=amANartusKAOmOnATEra
    ports:
      - "8082:8081"

volumes:
  rabbitmq_data:
  rabbitmq_logs:
  redis_data:



===================================
===================================





`sudo -u postgres psql -c "CREATE USER repuser WITH REPLICATION ENCRYPTED PASSWORD 'mubasher321';"`

# create healthcheck user on master-node
sudo -u postgres psql -c "CREATE USER healthcheck WITH PASSWORD 'mubasher321';"
sudo -u postgres psql -c "GRANT pg_monitor TO healthcheck;"

# confirm the user creation and streaming replication (by running checking it from failover-node)
sudo -u postgres psql -c "SELECT usename FROM pg_user WHERE usename = 'healthcheck';"

# generate md5 passwords
sudo pg_md5 -m -u healthcheck mubasher321


sudo -u postgres psql -c "ALTER USER postgres WITH PASSWORD 'mubasher321' ENCRYPTED PASSWORD 'md5';"

==================================






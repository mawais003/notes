# PGPOOL

Here is some of its intro in bullets below:

- An open-source middleware for PostgreSQL that provides connection pooling, load balancing, high availability (HA), and query caching.
- works just like nginx infront of multiple postgres database servers/nodes
- Sits between the database client and PostgreSQL servers, acting as a proxy to manage connections and distribute queries.
- port 9999


## Installtion of PGPool

Install from official guide, follow official documentations.

## My Current Setup Configurations

I have installed pgpool2 (using `postgres` user) and there are 2 postgres db servers that are configured as backend nodes (master and slave)

- we are using pgpool internal master-slave replications (writes only on master and reads can be loadbalanced)


root@markets-pgpool:/etc/pgpool2# pwd
/etc/pgpool2
root@markets-pgpool:/etc/pgpool2# ls -ltrh
total 88K
-rw-r----- 1 postgres postgres  49K Apr 17 09:08 pgpool.conf.default
-rw-r----- 1 postgres postgres 3.7K Apr 18 10:42 pgpool.conf.cutomized
drwxr-xr-x 2 postgres postgres 4.0K Apr 18 16:02 certs
-rw-r--r-- 1 postgres postgres 3.6K Apr 21 05:32 pool_hba.conf
-rwxr-xr-x 1 postgres postgres  803 Apr 21 13:20 failover.sh
-rw-r--r-- 1 postgres postgres 1.2K Apr 21 14:46 pcp.conf
-rw-r----- 1 postgres postgres 6.5K Apr 23 06:03 pgpool.conf_backup
-rw-r----- 1 postgres postgres  237 May 19 07:59 pool_passwd
-rw-r--r-- 1 root     root     3.7K Jul  8 10:00 pgpool.conf
root@markets-pgpool:/etc/pgpool2# 


> Here is the /etc/pgpool2/pgpool.conf

```
#------------------------------------------------------------------------------
# CONNECTION SETTINGS
#------------------------------------------------------------------------------
listen_addresses = '*'                     # Listen on all IP addresses
port = 9999                                # Pgpool-II port
num_init_children = 1000                    # Max concurrent connections (tune as needed)
max_pool = 30                               # Connections per user/database pair
child_life_time = 3000                      # Time before child process is terminated
connection_life_time = 3000                 # Time before backend connection is closed
client_idle_limit = 3000                    # Disconnect idle clients after 10 minutes
 
#------------------------------------------------------------------------------
# BACKEND SETTINGS
#------------------------------------------------------------------------------
backend_hostname0 = '172.31.202.168'       # Master (primary server)
backend_port0 = 5432
backend_weight0 = 0
load_balance_node = true                        # No weight for master (only write queries)
backend_data_directory0 = '/var/lib/pgsql/data'
backend_flag0 = 'ALLOW_TO_FAILOVER'
backend_application_name0 = 'server0'
 
backend_hostname1 = '172.31.193.21'       # Slave (standby server)
backend_port1 = 5432
backend_weight1 = 1                          # Weight for load balancing (read queries)
load_balance_node = true                    # Allow read queries
backend_data_directory1 = '/var/lib/pgsql/data'
backend_flag1 = 'ALLOW_TO_FAILOVER'
backend_application_name1 = 'server1'
 
 
#------------------------------------------------------------------------------
# AUTHENTICATION
#------------------------------------------------------------------------------
enable_pool_hba = on                       # Use pg_hba.conf for client authentication
pool_passwd = 'pool_passwd'                # Path to password file
authentication_timeout = 60                # Timeout for authentication
 
#------------------------------------------------------------------------------
# LOAD BALANCING
#------------------------------------------------------------------------------
load_balance_mode = on                     # Enable load balancing for read queries
master_slave_mode = on
statement_level_load_balance = on
#------------------------------------------------------------------------------
# MEMORY CACHE
#------------------------------------------------------------------------------
#memory_cache_enabled = on                  # Enable memory cache

#cache_safe_mem = 15GB                       # Reserved memory for query caching
#memqcache_expire = 200
#------------------------------------------------------------------------------
# LOGGING
#------------------------------------------------------------------------------
log_directory = '/var/log/postgresql'          # Directory for log files
log_filename = 'pgpool.log'                # Log file name
log_connections = on                       # Log incoming connections
log_disconnections = on                    # Log disconnections
log_statement = on                         # Log all SQL statements
log_per_node_statement = on                # Log queries per node
log_line_prefix = '%t: pid %p: '           # Timestamp and process ID in logs
connection_cache = on

#Health Check
health_check_period = 60               # check every 10 seconds
health_check_user = 'postgres'    # user to perform health checks
health_check_password = 'mubasher321'
health_check_database = 'tadawuly_prod'     # or any available db
health_check_timeout = 20
health_check_max_retries = 1
health_check_retry_delay = 1
```


> Here is /etc/pgpool2/pool_hba.conf

```
# Put your actual configuration here
# ----------------------------------
#
# If you want to allow non-local connections, you need to add more
# "host" records. In that case you will also need to make pgpool listen
# on a non-local interface via the listen_addresses configuration parameter.
#

# TYPE  DATABASE    USER        CIDR-ADDRESS          METHOD

# "local" is for Unix domain socket connections only
local   all         all                               trust

#host    all         all         172.31.0.0/16         scram-sha-256

host    all         all         172.31.0.0/16        md5 

# IPv4 local connections:
host    all         all         127.0.0.1/32          trust
host    all         all         ::1/128               trust

```

> Here is my /etc/pgpool2/pool_passwd 

```
postgres:md5ed31d19598d79330b31244edb713149e
healthcheck:md5d30e283933fadb8542d3df6e3db25cae
```

> Here is my /etc/pgpool2/pcp.conf

``` 
# PCP Client Authentication Configuration File

postgres:md5ed31d19598d79330b31244edb713149e
healthcheck:md5d30e283933fadb8542d3df6e3db25cae
```

## Here is pgpool monitoring setup

- The only problem with multinode (where we are having multiple backend ndoes) pgpool cluster is that pgpool periodically checks the status of backend nodes and sends them the incoming queries only if it finds their health_status as up.
- It then writes this status as `up` or `down` as per condition inside `/var/log/postgresql/pgpool_status`
- If by somehow, pgpool2 finds any node as `down`, it will write `down` in that status file but will never go to that down node again to check its status (even though it was backed up in a while)
- It will keep looking at this status file, and it will never route the db queries to `down` (declared) nodes (inside pgpool_status file).
- To resolve it, we need to manually flush/empty that status file to make pgpool2 go to all the nodes again and fetch their fresh status.

To address this issue, I have created a bash script to do this recovery process and I have placed another bash script inside crontab to monitor this pgpool_status file for any `down` entry/entries and if it finds any, it will trigger the recovery script.


> pgpool_status file monitoring script | `/usr/local/bin/pgpool_cron_monitor.sh`


```
#!/bin/bash

STATUS_FILE="/var/log/postgresql/pgpool_status"
RECOVERY_SCRIPT="/usr/local/bin/pgpool_recovery.sh"
LOG_FILE="/var/log/pgpool_cron_monitor.log"

# Check if the status file exists
if [[ ! -f "$STATUS_FILE" ]]; then
    echo "$(date) :: ERROR: Status file not found: $STATUS_FILE" >> "$LOG_FILE"
    exit 1
fi

# Check for 'down' anywhere in the file
if grep -q "down" "$STATUS_FILE"; then
    echo "$(date) :: Detected 'down' in status file. Starting recovery..." >> "$LOG_FILE"

    # Run recovery script
    $RECOVERY_SCRIPT

    if [[ $? -eq 0 ]]; then
        echo "$(date) :: Recovery script completed successfully. Sleeping 30s..." >> "$LOG_FILE"
        sleep 30
    else
        echo "$(date) :: ERROR: Recovery script failed!" >> "$LOG_FILE"
    fi
else
    echo "$(date) :: Status OK (no 'down' found)." >> "$LOG_FILE"
fi
```

- Add above script in crontab and schedule it to run `* * * * *`

> Below is my revovery script that is being called in above monitoring script | `/usr/local/bin/pgpool_recovery.sh`

```
#!/bin/bash

# === Configuration ===
STATUS_FILE="/var/log/postgresql/pgpool_status"
LOG_DIR="/var/log/pgpool2_recovery-logs"
EMAIL="ps_notifications@globalfinancialmedia.com"
TIMESTAMP=$(date "+%Y%m%d_%H%M%S")
LOG_FILE="$LOG_DIR/recovery_$TIMESTAMP.log"

# === Ensure log dir exists ===
mkdir -p "$LOG_DIR"

# === Logging Function ===
log() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') :: $1" >> "$LOG_FILE"
}

log "=== Starting pgpool2 recovery ==="

# === Stop pgpool2 ===
log "Stopping pgpool2.service..."
systemctl stop pgpool2.service
if [[ $? -ne 0 ]]; then
    log "ERROR: Failed to stop pgpool2.service"
    {
        echo "To: $EMAIL"
        echo "Subject: ❌ pgpool2 Recovery Failed"
        echo
        cat "$LOG_FILE"
    } | msmtp -t
    exit 1
fi
log "pgpool2.service stopped successfully."

# === Clear pgpool_status as postgres user ===
log "Clearing $STATUS_FILE as postgres user..."
sudo -u postgres bash -c "truncate -s 0 $STATUS_FILE"

# Check if still not empty — fallback to overwrite
if [[ -s $STATUS_FILE ]]; then
    log "WARNING: Truncate failed, attempting manual overwrite..."
    sudo -u postgres bash -c "echo -n '' > $STATUS_FILE"
    sleep 1
fi

# Final verification
if [[ -s $STATUS_FILE ]]; then
    log "WARNING: $STATUS_FILE is still not empty — proceeding anyway."
else
    log "$STATUS_FILE successfully cleared."
fi

# === Start pgpool2 ===
log "Starting pgpool2.service..."
systemctl start pgpool2.service
if [[ $? -ne 0 ]]; then
    log "ERROR: Failed to start pgpool2.service"
    {
        echo "To: $EMAIL"
        echo "Subject: ❌ pgpool2 Recovery Failed"
        echo
        cat "$LOG_FILE"
    } | msmtp -t
    exit 1
fi
sleep 5

# === Final check ===
if systemctl is-active --quiet pgpool2.service; then
    log "pgpool2.service is running correctly."
    log "=== pgpool2 recovery completed successfully ==="
    {
        echo "To: $EMAIL"
        echo "Subject: ✅ pgpool2 Recovery Successful"
        echo
        cat "$LOG_FILE"
    } | msmtp -t
else
    log "ERROR: pgpool2.service is not active after restart."
    {
        echo "To: $EMAIL"
        echo "Subject: ❌ pgpool2 Recovery Failed"
        echo
        cat "$LOG_FILE"
    } | msmtp -t
    exit 1
fi
```


## Alternate monitoring way

We can create a systemd service to monitor the status of our pgpool and notify us incase of any failure.

> Here is my systemd file details.

```
root@markets-pgpool:/etc/pgpool2# systemctl status pgpool-monitor.service 
● pgpool-monitor.service - PGPool Status Monitoring Service
     Loaded: loaded (/etc/systemd/system/pgpool-monitor.service; enabled; preset: enabled)
     Active: active (running) since Tue 2025-07-15 06:38:28 UTC; 3 weeks 1 day ago
   Main PID: 406893 (pgpool-monitor)
      Tasks: 2 (limit: 9316)
     Memory: 3.5M (peak: 5.1M swap: 8.0K swap peak: 8.0K)
        CPU: 576ms
     CGroup: /system.slice/pgpool-monitor.service
             ├─406893 /bin/bash /usr/local/bin/pgpool-monitor
             └─603522 inotifywait -q -e modify /var/log/postgresql/pgpool_status

Notice: journal has been rotated since unit was started, output may be incomplete.
```

> `/etc/systemd/system/pgpool-monitor.service` file

```
root@markets-pgpool:/etc/pgpool2# cat /etc/systemd/system/pgpool-monitor.service;
[Unit]
Description=PGPool Status Monitoring Service
After=network.target

[Service]
Type=simple
ExecStart=/usr/local/bin/pgpool-monitor
Restart=always
RestartSec=5
User=postgres
Group=postgres
StandardOutput=syslog
StandardError=syslog
SyslogIdentifier=pgpool-monitor

[Install]
WantedBy=multi-user.target
root@markets-pgpool:/etc/pgpool2# 
```

> Here is my `/usr/local/bin/pgpool-monitor` file

```
#!/bin/bash

# Configuration
STATUS_FILE="/var/log/postgresql/pgpool_status"
#STATUS_FILE="/tmp/pgpool_dummy_test"
#ALERT_EMAIL="a.aslam@globalfinancialmedia.com" 
ALERT_EMAIL="ps@globalfinancialmedia.com"  
LOG_FILE="/var/log/pgpool-monitor.log"
#MSMTP_CONFIG="/etc/msmtprc"
MSMTP_CONFIG="/var/lib/postgresql/.msmtp/msmtprc"

# Function to log messages
log() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" >> "$LOG_FILE"
}

# Function to send alert email using msmtp
send_alert() {
    local subject="PGPool Status Alert: $1"
    local message="PGPool status alert detected at $(date)\n\n$2\n\nCurrent status:\n$(cat "$STATUS_FILE")"
    
    log "Sending alert: $subject"
    echo -e "Subject: $subject\n\n$message" | msmtp --file="$MSMTP_CONFIG" -a default "$ALERT_EMAIL"
}

# Verify msmtp is configured
if [ ! -f "$MSMTP_CONFIG" ]; then
    log "Error: msmtp configuration not found at $MSMTP_CONFIG"
    exit 1
fi

# Initialize
log "PGPool monitoring service starting"
LAST_STATUS=$(cat "$STATUS_FILE")

# Check initial status
if grep -q "down" <<< "$LAST_STATUS"; then
    send_alert "Initial Problem Found" "Service started with problematic status"
fi

# Continuous monitoring using inotifywait
while true; do
    # Wait for file modification
    inotifywait -q -e modify "$STATUS_FILE" >/dev/null 2>&1
    
    # Small delay to ensure file is completely written
    sleep 0.5
    
    CURRENT_STATUS=$(cat "$STATUS_FILE")
    
    # Check if status changed
    if [ "$CURRENT_STATUS" != "$LAST_STATUS" ]; then
        log "Status change detected"
        LAST_STATUS="$CURRENT_STATUS"
        
        # Check for any 'down' status
        if grep -q "down" <<< "$CURRENT_STATUS"; then
            send_alert "Status Changed to Down" "PGPool status has changed to 'down'"
        fi
    fi
done
```

> Here is the inotify service running as below:

```
root@markets-pgpool:/etc/pgpool2# ps aux | grep -i inotify
postgres  603522  0.0  0.0   2896  1408 ?        S    07:12   0:00 inotifywait -q -e modify /var/log/postgresql/pgpool_status
root      604007  0.0  0.0   7076  2304 pts/1    S+   07:51   0:00 grep --color=auto -i inotify
root@markets-pgpool:/etc/pgpool2# cat /var/log/postgresql/pgpool_status
up
up
root@markets-pgpool:/etc/pgpool2# 
root@markets-pgpool:/etc/pgpool2# 
```

> using below msmtp creds:

```
root@markets-pgpool:~# cat .msmtprc 
#msmtprc script

# ~/.msmtprc

defaults
auth           on
tls            on
tls_trust_file /etc/ssl/certs/ca-certificates.crt
logfile        ~/.msmtp.log

account        default
host           email-smtp.eu-west-1.amazonaws.com
port           587
from           no-reply@feedgfm.com
user           AKIASJCIOUV6KLKZNTN7
password       BHU6mHGwlxxjlIvaRcnX0n6yJqbDLvX6Wsm7ljDbIdjW
tls_starttls   on
tls_certcheck  off
root@markets-pgpool:~# 
```

> Here are public/private ssh key pairs to server

```
ubuntu@markets-pgpool:~$ cat .ssh/
authorized_keys  id_rsa           id_rsa.pub       known_hosts      known_hosts.old  
ubuntu@markets-pgpool:~$ cat .ssh/id_rsa
-----BEGIN OPENSSH PRIVATE KEY-----
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
-----END OPENSSH PRIVATE KEY-----
ubuntu@markets-pgpool:~$ 
ubuntu@markets-pgpool:~$ 
ubuntu@markets-pgpool:~$ cat .ssh/id_rsa.pub 
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCVC2lVEw1kP5nzAE/p7KigoRduCQGLUh19QNUAahwQVCBi8YxP+bV3o78vqWGCLGAm6/7T6adQCpRziT/N156ZHwMuxuCrOHOR1uNnvgsyg3jn3jnQIdtQymHNbW41hhRp/LUv3i+8ZxMCTAys2QSFo/LYOzO08Mt923GxW/FlcABjAZ32KkHMuA994hSsSOKpMBC5A1WIzWIdjUYR3vIz6H0+FFo6kyxMlPtMZK50dNVndDUt0V+LbNKDUcI3CbopZppuoaWCvhyjNzGWJev6CTjf8WN7CfVwllkes4osB2Xn9nj1hm4FHeoPVQS+fWA2Tcg2NeALMCA//Z4GPn8Xf5wBWgo5gj8DkgsJoOT5wtwgDmv5mRNdo+ZZGpmpHF6RxYags31JPSGKTF0P4DccOXvtaebjEbEyMDq0I7QO18WGFEkogEpHKotTKKkDG38XYCYzGE82zjjiy0JsS/bZxm9Yr1ZGUX4cXMjaxUtlLpoYFoMa7+R3URewCUL0RT7ad5/a6ODVvv5dsZnHuZvtMzajIOUWGVYV7YGRM+oCsuvGZZDOmvJjUcCoUWbn1+iqBEpRFuFPTgptZWKk2pn9iFvx8pjUOUwTSbJzuN6c9LgDvU2xbUF8V3QhHPTx/Tpa+pNYTPsPhSpuK+merYida+9nzsJqieOsQq/8ObL58w== abdul.basit@example.com
ubuntu@markets-pgpool:~$ 
```
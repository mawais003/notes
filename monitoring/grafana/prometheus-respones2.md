location /tenaris/ir/{
     add_header Content-Security-Policy "frame-ancestors http://Tenarissaudisteelpipes.com http://www.Tenarissaudisteelpipes.com https://Tenarissaudisteelpipes.com https://www.Tenarissaudisteelpipes.com http://sspipe.com http://www.sspipe.com https://sspipe.com https://www.sspipe.com http://*.platformsh.site http://www.*.platformsh.site https://*.platformsh.site https://www.*.platformsh.site";
     add_header X-Content-Security-Policy "frame-ancestors http://Tenarissaudisteelpipes.com http://www.Tenarissaudisteelpipes.com https://Tenarissaudisteelpipes.com https://www.Tenarissaudisteelpipes.com http://sspipe.com http://www.sspipe.com https://sspipe.com https://www.sspipe.com http://*.platformsh.site http://www.*.platformsh.site https://*.platformsh.site https://www.*.platformsh.site";
     rewrite ^ /tenarisemberUrl/ last;
        }

#     location /tenaris/mobile/tenaris/tdwl/1320{
#     add_header Content-Security-Policy "frame-ancestors ";
#     add_header X-Content-Security-Policy "frame-ancestors ";
#     rewrite ^ /tenarisemberUrl/ last;
#        }

     location /tenarisemberUrl/{
     add_header Content-Security-Policy "frame-ancestors http://Tenarissaudisteelpipes.com http://www.Tenarissaudisteelpipes.com https://Tenarissaudisteelpipes.com https://www.Tenarissaudisteelpipes.com http://sspipe.com http://www.sspipe.com https://sspipe.com https://www.sspipe.com http://*.platformsh.site http://www.*.platformsh.site https://*.platformsh.site https://www.*.platformsh.site";
     add_header X-Content-Security-Policy "frame-ancestors http://Tenarissaudisteelpipes.com http://www.Tenarissaudisteelpipes.com https://Tenarissaudisteelpipes.com https://www.Tenarissaudisteelpipes.com http://sspipe.com http://www.sspipe.com https://sspipe.com https://www.sspipe.com http://*.platformsh.site http://www.*.platformsh.site https://*.platformsh.site https://www.*.platformsh.site";
     #alias /usr/share/nginx/html/ir-static/new_static_sites/IR-HTML5/index.html;
     alias      /usr/share/nginx/html/ir-static/tenaris/;
     index index.html;
        }



s3 bucket:
https://assets.sharikatmubasher.com/snippets/index.html
 
sharikat website address:
https://sharikatmubasher.com

 
At first I will explain you my current architect and I will need your help to complete my new task.


Current Architect:

I have a cloudfront distribution (EEZ6JI8QQ21N2) that has an S3 bucket (sm-prod-data) as origin, and to access the content inside this bucket I use URL as assets.sharikatmubasher.com.


I have a website sharikatmubasher.com and here I am explaining you how this site is being served. (I have a cloudfront distribution "E3FGIHYPR9SN1Z" with an attached ALB as its origin and ALB is having an ec2 instance as its target, and application is running inside that ec2 isntance, So when request comes for sharikatmubasher.com, it is resolved by route53 and reaches the cloudfront distribution "E3FGIHYPR9SN1Z" and from here it reaches the server as I explained just now)


Now below is my task , that we need to do now:

When I search https://sharikatmubasher.com/snippets/index.html in browser, it should load for me the content from inside the S3 bucket, present at https://assets.sharikatmubasher.com/snippets/index.html (becasue https://assets.sharikatmubasher.com is my alternate domain name present in a cloudfront distribution "EEZ6JI8QQ21N2" where I have attached an S3 "sm-prod-data" as its origin)

https://sharikatmubasher.com/snippets/index.html is just an example, I actually want to see whatever present inside https://assets.sharikatmubasher.com/snippets/<object-name> when I hit in browser https://sharikatmubasher.com/snippets/<object-name>


Give me detailed steps for this task, solution should not disturb the current running architecture (and should be safe, as it is production environment), and solution should only be from AWS console only.


# current sm-uat-s3 permission

{
    "Version": "2008-10-17",
    "Id": "PolicyForCloudFrontPrivateContent",
    "Statement": [
        {
            "Sid": "AllowCloudFrontServicePrincipal",
            "Effect": "Allow",
            "Principal": {
                "Service": "cloudfront.amazonaws.com"
            },
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::sm-uat-s3-bucket/*",
            "Condition": {
                "StringEquals": {
                    "AWS:SourceArn": "arn:aws:cloudfront::612328295331:distribution/E37V6NSV56M4IC"
                }
            }
        }
    ]
}


# updated policy for sm-uat-s3

{
    "Version": "2008-10-17",
    "Id": "PolicyForCloudFrontPrivateContent",
    "Statement": [
        {
            "Sid": "AllowCloudFrontServicePrincipal",
            "Effect": "Allow",
            "Principal": {
                "Service": "cloudfront.amazonaws.com"
            },
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::sm-uat-s3-bucket/*",
            "Condition": {
                "StringEquals": {
                    "AWS:SourceArn": [
                        "arn:aws:cloudfront::612328295331:distribution/E37V6NSV56M4IC",
                        "arn:aws:cloudfront::612328295331:distribution/EYW86JG25PIEN"
                    ]
                }
            }
        }
    ]
}




location /tenaris/ir/{
     add_header Content-Security-Policy "frame-ancestors http://Tenarissaudisteelpipes.com http://www.Tenarissaudisteelpipes.com https://Tenarissaudisteelpipes.com https://www.Tenarissaudisteelpipes.com http://sspipe.com http://www.sspipe.com https://sspipe.com https://www.sspipe.com http://*.platformsh.site http://www.*.platformsh.site https://*.platformsh.site https://www.*.platformsh.site";
     add_header X-Content-Security-Policy "frame-ancestors http://Tenarissaudisteelpipes.com http://www.Tenarissaudisteelpipes.com https://Tenarissaudisteelpipes.com https://www.Tenarissaudisteelpipes.com http://sspipe.com http://www.sspipe.com https://sspipe.com https://www.sspipe.com http://*.platformsh.site http://www.*.platformsh.site https://*.platformsh.site https://www.*.platformsh.site";
     rewrite ^ /tenarisemberUrl/ last;
        }

#     location /tenaris/mobile/tenaris/tdwl/1320{
#     add_header Content-Security-Policy "frame-ancestors ";
#     add_header X-Content-Security-Policy "frame-ancestors ";
#     rewrite ^ /tenarisemberUrl/ last;
#        }

     location /tenarisemberUrl/{
     add_header Content-Security-Policy "frame-ancestors http://Tenarissaudisteelpipes.com http://www.Tenarissaudisteelpipes.com https://Tenarissaudisteelpipes.com https://www.Tenarissaudisteelpipes.com http://sspipe.com http://www.sspipe.com https://sspipe.com https://www.sspipe.com http://*.platformsh.site http://www.*.platformsh.site https://*.platformsh.site https://www.*.platformsh.site";
     add_header X-Content-Security-Policy "frame-ancestors http://Tenarissaudisteelpipes.com http://www.Tenarissaudisteelpipes.com https://Tenarissaudisteelpipes.com https://www.Tenarissaudisteelpipes.com http://sspipe.com http://www.sspipe.com https://sspipe.com https://www.sspipe.com http://*.platformsh.site http://www.*.platformsh.site https://*.platformsh.site https://www.*.platformsh.site";
     #alias /usr/share/nginx/html/ir-static/new_static_sites/IR-HTML5/index.html;
     alias      /usr/share/nginx/html/ir-static/tenaris/;
     index index.html;
        }





location /tenaris/ir/{
     add_header Content-Security-Policy "frame-ancestors";
     add_header X-Content-Security-Policy "frame-ancestors";
     rewrite ^ /tenarisemberUrl/ last;
        }

#     location /tenaris/mobile/tenaris/tdwl/1320{
#     add_header Content-Security-Policy "frame-ancestors ";
#     add_header X-Content-Security-Policy "frame-ancestors ";
#     rewrite ^ /tenarisemberUrl/ last;
#        }

     location /tenarisemberUrl/{
     add_header Content-Security-Policy "frame-ancestors";
     add_header X-Content-Security-Policy "frame-ancestors";
     #alias /usr/share/nginx/html/ir-static/new_static_sites/IR-HTML5/index.html;
     alias      /usr/share/nginx/html/ir-static/tenaris/;
     index index.html;
        }

# RDS - FreeableMemory SQL Query

{
    "metrics": [
        [ { "expression": "SELECT AVG(UsedMemory) FROM SCHEMA(\"AWS/RDS\", DBInstanceIdentifier) WHERE DBInstanceIdentifier = 'tadawuly-instance-1'", "label": "Query1", "id": "q1", "visible": false } ],
        [ "AWS/RDS", "FreeableMemory", "DBInstanceIdentifier", "tadawuly-instance-1", { "label": "tadawuly-instance-1", "region": "eu-west-1", "id": "m1", "visible": false } ],
        [ ".", "UsedMemory", ".", ".", { "region": "eu-west-1", "id": "m2" } ]
    ],
    "period": 300,
    "region": "eu-west-1",
    "stat": "Average",
    "title": "Top 10 RDS clusters by writes",
    "yAxis": {
        "left": {
            "label": "Count",
            "showUnits": false
        }
    },
    "view": "timeSeries",
    "stacked": false
}


# RDS - UsedMemory SQL Query (json to paste in source section)

{
    "metrics": [
        [ "AWS/RDS", "FreeableMemory", "DBInstanceIdentifier", "tadawuly-instance-1", { "label": "FreeableMemory", "region": "eu-west-1", "id": "m1", "visible": false } ],
        [ { "expression": "21474836480 - m1", "label": "UsedMemory", "id": "m2" } ]
    ],
    "period": 300,
    "region": "eu-west-1",
    "stat": "Average",
    "title": "RDS Used Memory",
    "yAxis": {
        "left": {
            "label": "Bytes",
            "showUnits": false
        }
    },
    "view": "timeSeries",
    "stacked": false
}


===============================


version: '3.8'

services:
  rabbitmq:
    image: rabbitmq:3.13.6-management
    container_name: rabbitmq
    ports:
      - "5672:5672"
      - "15672:15672"
    environment:
      RABBITMQ_DEFAULT_USER: myuser
      RABBITMQ_DEFAULT_PASS: mypassword
    volumes:
      - rabbitmq_data:/var/lib/rabbitmq
      - rabbitmq_logs:/var/log/rabbitmq
    restart: always
volumes:
  rabbitmq_data:
  rabbitmq_logs:


  =====================



  10.200.0.56 - - [13/Feb/2025:06:06:02 +0000] "GET /dib/ibe/?UNC=0&M=1&H=1&UID=IRPORTAL&SID=IRPORTAL&UE=DFM&L=EN&RT=32&S=DFM~DIB&CIT=CP%2CSTK%2CCPCLS%2CAUD%2CFFHIST&FC=1 HTTP/1.1" 200 7471 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0" "110.93.228.117" us=10.200.0.178:8384 uct=0.000 uht=0.025 urt=0.025 req_time=0.025
10.200.0.56 - - [13/Feb/2025:06:06:03 +0000] "GET /dib/ibe/?UNC=0&M=1&H=1&UID=IRPORTAL&SID=IRPORTAL&UE=DFM&L=EN&RT=32&S=DFM~DIB&CIT=CP%2CSTK%2CCPCLS%2CAUD%2CFFHIST&FC=1 HTTP/1.1" 200 7471 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0" "110.93.228.117" us=10.200.0.178:8384 uct=0.000 uht=0.021 urt=0.021 req_time=0.020



10.200.0.56 - - [13/Feb/2025:06:06:03 +0000] "GET /dib/ibe/?UNC=0&M=1&H=1&UID=IRPORTAL&SID=IRPORTAL&UE=DFM&L=EN&RT=32&S=DFM~DIB&CIT=CP%2CSTK%2CCPCLS%2CAUD%2CFFHIST&FC=1 HTTP/1.1" 200 7471 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0" "110.93.228.117" us=10.200.0.178:8384 uct=0.000 uht=0.022 urt=0.023 req_time=0.022


10.200.0.56 - - [13/Feb/2025:06:06:04 +0000] "GET /dib/ibe/?UNC=0&M=1&H=1&UID=IRPORTAL&SID=IRPORTAL&UE=DFM&L=EN&RT=32&S=DFM~DIB&CIT=CP%2CSTK%2CCPCLS%2CAUD%2CFFHIST&FC=1 HTTP/1.1" 400 60 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0" "110.93.228.117" us=10.200.0.178:8384 uct=0.000 uht=0.012 urt=0.012 req_time=0.012




10.200.0.56 - - [13/Feb/2025:06:06:05 +0000] "GET /dib/ibe/?UNC=0&M=1&H=1&UID=IRPORTAL&SID=IRPORTAL&UE=DFM&L=EN&RT=32&S=DFM~DIB&CIT=CP%2CSTK%2CCPCLS%2CAUD%2CFFHIST&FC=1 HTTP/1.1" 200 7471 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0" "110.93.228.117" us=10.200.0.178:8384 uct=0.000 uht=0.039 urt=0.039 req_time=0.040
10.200.0.56 - - [13/Feb/2025:06:06:30 +0000] "GET /dib/ibe/?UNC=0&M=1&H=1&UID=IRPORTAL&SID=IRPORTAL&UE=DFM&L=EN&RT=32&S=DFM~DIB&CIT=CP%2CSTK%2CCPCLS%2CAUD%2CFFHIST&FC=1 HTTP/1.1" 200 7471 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0" "110.93.228.117" us=10.200.0.178:8384 uct=0.000 uht=0.036 urt=0.036 req_time=0.036







=====================================================


{
  "statusCode": 200,
  "body": [
    {
      "Instance ID": "i-072eadfaa4805e80e",
      "Instance Name": "nginx-public-pri",
      "Instance Type": "t3a.large",
      "Public IP": "52.18.66.235"
    },
    {
      "Instance ID": "i-07956a34b0ba1d718",
      "Instance Name": "ir-pri",
      "Instance Type": "m5a.2xlarge",
      "Public IP": "34.251.189.11"
    },
    {
      "Instance ID": "i-07748982da64a98bd",
      "Instance Name": "data-man-pri-private-2",
      "Instance Type": "t3.2xlarge",
      "Public IP": "54.228.53.80"
    },
    {
      "Instance ID": "i-08a6d03bfc0920d9f",
      "Instance Name": "db-man-prviate-1",
      "Instance Type": "m5a.xlarge",
      "Public IP": "No Public IP"
    },
    {
      "Instance ID": "i-02dbdc2feab66aad4",
      "Instance Name": "Prom-Grafana",
      "Instance Type": "t3.micro",
      "Public IP": "52.211.206.208"
    },
    {
      "Instance ID": "i-06e4d0f1e3e1fa86f",
      "Instance Name": "search-services-private-sec",
      "Instance Type": "r5a.2xlarge",
      "Public IP": "No Public IP"
    },
    {
      "Instance ID": "i-001cab82ef08d7ee0",
      "Instance Name": "chart-data-private-sec",
      "Instance Type": "r5a.2xlarge",
      "Public IP": "No Public IP"
    },
    {
      "Instance ID": "i-035ccf3d7d03d8c34",
      "Instance Name": "fd-private-sec",
      "Instance Type": "r5a.2xlarge",
      "Public IP": "No Public IP"
    },
    {
      "Instance ID": "i-068e8b6d7bf6e59f3",
      "Instance Name": "mix-private-sec",
      "Instance Type": "t3.2xlarge",
      "Public IP": "No Public IP"
    },
    {
      "Instance ID": "i-068a6c7359350ca0e",
      "Instance Name": "data-man-sec-private-1",
      "Instance Type": "t3.2xlarge",
      "Public IP": "No Public IP"
    },
    {
      "Instance ID": "i-00c90ad524432ca34",
      "Instance Name": "Build Server Rhel 6 ",
      "Instance Type": "t2.micro",
      "Public IP": "No Public IP"
    },
    {
      "Instance ID": "i-071d7c90986a4218d",
      "Instance Name": "Auth1-pub",
      "Instance Type": "t3a.medium",
      "Public IP": "54.217.189.205"
    },
    {
      "Instance ID": "i-0cf528c536d3623e5",
      "Instance Name": "Auth3-pub",
      "Instance Type": "t3a.medium",
      "Public IP": "52.213.43.203"
    },
    {
      "Instance ID": "i-026ef8e95ca9a52ba",
      "Instance Name": "Search-Services-Pri",
      "Instance Type": "r5a.2xlarge",
      "Public IP": "No Public IP"
    },
    {
      "Instance ID": "i-04939a39971e72961",
      "Instance Name": "chart-data-pri",
      "Instance Type": "r5a.2xlarge",
      "Public IP": "No Public IP"
    },
    {
      "Instance ID": "i-033cc195e7dd42a82",
      "Instance Name": "fd-pri-private",
      "Instance Type": "r5a.2xlarge",
      "Public IP": "No Public IP"
    },
    {
      "Instance ID": "i-0d990b61df3e8f5a9",
      "Instance Name": "mix-pri-private",
      "Instance Type": "t3a.2xlarge",
      "Public IP": "54.73.50.122"
    },
    {
      "Instance ID": "i-0f6285707b2603aa1",
      "Instance Name": "oracle-db-RW",
      "Instance Type": "m5.4xlarge",
      "Public IP": "No Public IP"
    },
    {
      "Instance ID": "i-04cdb7a6347244e5d",
      "Instance Name": "nginx-public-sec",
      "Instance Type": "t3a.micro",
      "Public IP": "52.215.39.254"
    },
    {
      "Instance ID": "i-02cff60a318392a7f",
      "Instance Name": "Auth2-pub",
      "Instance Type": "t3a.medium",
      "Public IP": "52.208.131.21"
    },
    {
      "Instance ID": "i-09a4fd5f20195e9a6",
      "Instance Name": "ir-sec-1C",
      "Instance Type": "m5a.2xlarge",
      "Public IP": "54.246.218.121"
    },
    {
      "Instance ID": "i-027483b8edd7780f8",
      "Instance Name": "DCP-Sec-PROD",
      "Instance Type": "t3.nano",
      "Public IP": "52.51.143.69"
    },
    {
      "Instance ID": "i-0f48a06497138be9a",
      "Instance Name": "Decypha-Pri-Prod",
      "Instance Type": "c5.4xlarge",
      "Public IP": "34.240.189.1"
    },
    {
      "Instance ID": "i-007d768cbe1976d2e",
      "Instance Name": "DCP-Pri-Prod",
      "Instance Type": "c5a.xlarge",
      "Public IP": "34.248.240.204"
    },
    {
      "Instance ID": "i-0836bcfef0436e5c6",
      "Instance Name": "GFM-FEED-PROD-HISTORY-SOLR-1 (Replication Services))",
      "Instance Type": "m5a.2xlarge",
      "Public IP": "34.250.190.101"
    },
    {
      "Instance ID": "i-02e13a026a5de6d11",
      "Instance Name": "GFM-FEED-PROD-SSS (Replication Services)",
      "Instance Type": "t3a.xlarge",
      "Public IP": "52.212.170.130"
    },
    {
      "Instance ID": "i-0a8c731ece13428fc",
      "Instance Name": "GFM-FEED-PROD-CCP (Replication Services)",
      "Instance Type": "r5.xlarge",
      "Public IP": "52.30.139.200"
    },
    {
      "Instance ID": "i-00caa320e4ed5f96d",
      "Instance Name": "oracle-db-RO-GFM",
      "Instance Type": "m5.4xlarge",
      "Public IP": "No Public IP"
    },
    {
      "Instance ID": "i-0990aff745ec3be03",
      "Instance Name": "FactSet-News-MED-pri",
      "Instance Type": "m5.large",
      "Public IP": "34.245.96.238"
    },
    {
      "Instance ID": "i-0568a2daf69b08391",
      "Instance Name": "JunaidTestServer",
      "Instance Type": "t3.nano",
      "Public IP": "No Public IP"
    },
    {
      "Instance ID": "i-09c74327e6e84031b",
      "Instance Name": "MiX-VPN []",
      "Instance Type": "t2.micro",
      "Public IP": "34.249.192.137"
    },
    {
      "Instance ID": "i-06be8fe7a536d73dc",
      "Instance Name": "GFM-FEED-PROD-META-SOLR - Replication Services",
      "Instance Type": "r5a.2xlarge",
      "Public IP": "63.33.138.129"
    },
    {
      "Instance ID": "i-05aa4d5ebf262aed5",
      "Instance Name": "FactSet-News-MED-sec",
      "Instance Type": "t3.nano",
      "Public IP": "No Public IP"
    },
    {
      "Instance ID": "i-0d9f3f4f91921b4e1",
      "Instance Name": "Announcement Extractor DFM",
      "Instance Type": "t2.medium",
      "Public IP": "3.253.250.34"
    },
    {
      "Instance ID": "i-03219146f60aae12e",
      "Instance Name": "nagios-server",
      "Instance Type": "c4.large",
      "Public IP": "18.203.229.100"
    },
    {
      "Instance ID": "i-0452b64a4b6bb76ce",
      "Instance Name": "IR-UAT",
      "Instance Type": "c5n.large",
      "Public IP": "No Public IP"
    },
    {
      "Instance ID": "i-0e55959ff715fe2c8",
      "Instance Name": "Nginx-Rocky",
      "Instance Type": "t3a.small",
      "Public IP": "54.73.212.187"
    },
    {
      "Instance ID": "i-0b62fafb9364115d6",
      "Instance Name": "IR-UAT-2.0",
      "Instance Type": "m5a.large",
      "Public IP": "52.49.207.32"
    }
  ]
}


===================================

root@nagios-server:/etc/apache2/sites-available# cat nagios.conf

ServerName monitoring.gfm.support
ScriptAlias /nagios/cgi-bin "/usr/local/nagios/sbin"
#DocumentRoot "/usr/local/nagios/share"


<Directory "/usr/local/nagios/sbin">
#  SSLRequireSSL
   Options ExecCGI
   AllowOverride None
   <IfVersion >= 2.3>
      <RequireAll>
         Require all granted
#        Require host 127.0.0.1

         AuthName "Nagios Access"
         AuthType Basic
         AuthUserFile /usr/local/nagios/etc/htpasswd.users
         Require valid-user
      </RequireAll>
   </IfVersion>
   <IfVersion < 2.3>
      Order allow,deny
      Allow from all
#     Order deny,allow
#     Deny from all
#     Allow from 127.0.0.1

      AuthName "Nagios Access"
      AuthType Basic
      AuthUserFile /usr/local/nagios/etc/htpasswd.users
      Require valid-user
   </IfVersion>
<IfModule mod_headers.c>
    Header set Access-Control-Allow-Origin "*"
    Header set Access-Control-Allow-Methods "GET, POST, OPTIONS"
    Header set Access-Control-Allow-Headers "Content-Type, Authorization"
</IfModule>
</Directory>

DocumentRoot "/usr/local/nagios/share"

    # Path to Nagios configuration files
    Alias /images/ /usr/local/nagios/share/images/
    Alias /css/ /usr/local/nagios/share/css/
    Alias /js/ /usr/local/nagios/share/js/

<Directory "/usr/local/nagios/share">
#  SSLRequireSSL
   Options None
   AllowOverride None
   <IfVersion >= 2.3>
      <RequireAll>
         Require all granted
#        Require host 127.0.0.1

         AuthName "Nagios Access"
         AuthType Basic
         AuthUserFile /usr/local/nagios/etc/htpasswd.users
         Require valid-user
      </RequireAll>
   </IfVersion>
   <IfVersion < 2.3>
      Order allow,deny
      Allow from all
#     Order deny,allow
#     Deny from all
#     Allow from 127.0.0.1

      AuthName "Nagios Access"
      AuthType Basic
      AuthUserFile /usr/local/nagios/etc/htpasswd.users
      Require valid-user
   </IfVersion>
<IfModule mod_headers.c>
    Header set Access-Control-Allow-Origin "*"
    Header set Access-Control-Allow-Methods "GET, POST, OPTIONS"
    Header set Access-Control-Allow-Headers "Content-Type, Authorization"
</IfModule>
</Directory>


=================================


# Security & Compliance Report  
**MubasherCapital.com**  
**Date:** February 26, 2025  

## Overview  
This report highlights the security vulnerabilities detected on MubasherCapital.com, the actions taken to mitigate them, pending issues, and associated costs where applicable.  

---

## Identified Security Issues & Fixes  

### 1. Clickjacking (X-Frame-Options Missing)  
❌ **Issue:** The site was vulnerable to Clickjacking due to missing `X-Frame-Options`.  
✅ **Fix:** `X-Frame-Options: DENY` and `frame-ancestors` added in security headers.  
⚠️ **Pending:** Cloudflare may still override headers, requiring **Pro Plan ($20/month)** to create custom rules at Cloudflare level.  

### 2. Missing Security Headers  
❌ **Issue:** Multiple security headers were missing, making the site prone to attacks.  
✅ **Fix:** Implemented key headers like `Strict-Transport-Security`, `Content-Security-Policy`, and `Referrer-Policy`.  
⚠️ **Pending:** Cloudflare is overriding headers; So need to fix it from there, creating some custom rules.

### 3. Bootstrap Version Outdated  
❌ **Issue:** The site was running an outdated Bootstrap version (4.1.0), which had security vulnerabilities.  
✅ **Fix:** Upgraded Bootstrap to version **5.3.3**.  
⚠️ **Pending:** Changes populated successfuly.  

### 4. TLS 1.0 & 1.1 Enabled  
❌ **Issue:** Older, insecure TLS versions were enabled, making the site vulnerable.  
✅ **Fix:** Disabled **TLS 1.0 & 1.1** at the server level.  
⚠️ **Pending:** Nothing pending.

### 5. WordPress Plugins Security Issues  
❌ **Issue:** Outdated WordPress plugins had security vulnerabilities.   
⚠️ **Pending:** In Process.  

---

### 6. DNS | Certificates issue
❌ **Issue:** Mubashercapital is being proxied via cloudflare and hence cloudflare is attacing its certs. 
⚠️ **Fix - Required:** If needed we can buy cert for out site and manually place them in cloudflare.  

## Cost Considerations  

| **Service**                 | **Purpose**                                         | **Cost**        |
|-----------------------------|-----------------------------------------------------|----------------|
| **Cloudflare Pro Plan**      | Required for enforcing security headers & X-Frame-Options | **$20/month**  |
| **Custom SSL Certificate**   | Alternative to Cloudflare Business for TLS enforcement | **~$100/year** |

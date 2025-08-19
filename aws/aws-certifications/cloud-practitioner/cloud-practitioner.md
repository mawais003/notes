## Cloud Practitioner

### AWS CAF Perspective and Foundational Capabilities

![AWS_CAF](image.png)

Here are capabilities of AWS-CAF:

- Business
- People
- Governace
- Platform
- Security
- Operations

(Blood Pressure Giving People Soft Opportunities)

### AWS Cloud Adoption Framework (AWS CAF)

There are 6 phases of CAF:

- Envision: Define the vision and business case for cloud adoption. Identify desired outcomes, align stakeholders, and establish success metrics.
- Align: Assess organizational readiness and identify gaps. Align strategies across business, people, governance, platform, security, and operations to create a shared understanding.
- Launch: Start with small, iterative projects (e.g., pilot workloads) to test and validate cloud approaches, building momentum and confidence.
- Scale: Expand cloud adoption across the organization. Implement broader migration strategies, optimize processes, and scale infrastructure and operations.
- Optimize: Continuously improve performance, cost, and efficiency. Leverage analytics, automation, and best practices to refine cloud environments.
- Reinvent: Innovate and transform business models using cloud-native capabilities. Explore new opportunities like AI, machine learning, or serverless architectures.

### Important AWS Migration Strategies (The 7 Rs)

- Rehost: Lift and shift to AWS with minimal changes.
- Replatform: Optimize slightly during migration (e.g., move to managed services).
- Refactor: Redesign for cloud-native (e.g., monolith to microservices).
- Repurchase: Replace with cloud-based SaaS or commercial software.
- Rebuild: Rewrite entirely using cloud-native technologies.
- Retire: Decommission obsolete or redundant applications.
- Retain: Keep applications on-premises or delay migration.

### Pillars of AWS Well-Architected Framework

This are 6 pillars namely:

1. Operational Excellence
2. Reliability
3. Security
4. Performance Efficiency
5. Cost Optimization
6. Sustainability

(ORSPCS)

### AWS Disaster Recovery strategies

The AWS Disaster Recovery strategies, often aligned with recovery objectives (RTO/RPO), are described below with precise one-liner differential descriptions:

- `Backup and Restore`: Store backups in AWS (e.g., S3, EBS snapshots) for manual restoration after a disaster. | High RTO/RPO (hours to days), suitable for non-critical systems.
- `Pilot Light`: Maintain a minimal, scaled-down environment in AWS, ready to scale up quickly. | Moderate RTO (hours), low RPO (minutes)
- `Warm Standby`: Run a fully functional, reduced-capacity system in AWS, ready to take over with minimal delay. | Low RTO (minutes to hours), low RPO (minutes)
- `Multi-Site Active/Active`: Operate fully active systems across multiple AWS Regions for near-zero downtime. | Near-zero RTO/RPO, for mission-critical systems with no downtime tolerance.


### Services

- `S3` as a destination for backup data that might be needed quickly to perform a restore.
- `Import/Export` for transferring very large data sets by shipping storage devices directly to AWS.
- `Glacier` for longer-term data storage where retrieval times of several hours are adequate.
- `Server Migration Service` for performing agentless server migrations from on-premises to AWS.
- `Database Migration Service` and Schema Conversion Tool for moving databases from on-premises to AWS and automatically converting SQL schema from one engine to another.
- `Storage Gateway`copies snapshots of your on-premises data volumes to S3 for backup. You can create local volumes or EBS volumes from these snapshots.
- `Preconfigured servers bundled` as Amazon Machine Images (AMIs).
- `Elastic Load Balancing (ELB)` for distributing traffic to multiple instances.
- `Route 53` for routing production traffic to different sites that deliver the same application or service.
- `Elastic IP` address for static IP addresses.
- `Virtual Private Cloud (Amazon VPC)` for provisioning a private, isolated section of the AWS cloud.
- `Direct Connect` for a dedicated network connection from your premises to AWS.
- `Relational Database Service (RDS)` for scale of a relational database in the cloud.
- `DynamoDB` for a fully managed NoSQL database service to store and retrieve any amount of data and serve any level of request traffic.
- `Redshift` for a petabyte-scale data warehouse service that analyzes all your data using existing business intelligence tools.
- `CloudFormation` for creating a collection of related AWS resources and provision them in an orderly and predictable fashion.
- `Elastic Beanstalk` is a service for deploying and scaling web applications and services developed.
- `OpsWorks` is an application management service for deploying and operating applications of all types and sizes.
- `AWS Snowcone` is a data transport solution like Snowball Edge, it is not suitable for moving terabytes to petabytes of data. Usable storage for Snowcone is only **8 TB** and its weight is **2.1 kg**.
- `EC2 Spot instances` can be interrupted by AWS EC2 with **two minutes of notification** when the service takes the capacity back
- ``AWS Business Plan` gives support within 1 hour incase of any production failures/issues.
- `Amazon EMR` is a web service that enables businesses, researchers, data analysts, and developers to easily and cost-effectively process vast amounts of data. It utilizes a hosted **Apache Hadoop framework** running on the web-scale infrastructure of Amazon EC2 and Amazon S3.
- `Amazon Chime` is a high-quality communications service that transforms online meetings with an easy-to-use app that works seamlessly across all your devices.
- `AWS Sumerian` is a service that lets you create and run 3D, Augmented Reality (AR), and Virtual Reality (VR) applications.
- `AWS Glue` is incorrect because this is primarily an ETL service, used for preparing and transforming data for analytics
- `Amazon Pinpoint` is AWS’s Digital User Engagement Service that enables AWS customers to effectively communicate with their end-users and measure user engagement across multiple channels including email, Text Messaging (SMS) and Mobile Push Notifications.
- `Amazon Neptune` is a Graph Database service that makes it easy for you to build and run applications that work with highly connected datasets. It is mainly used for recommendation engines, fraud detection, knowledge graphs, drug discovery.
- `AWS Step Functions` is a web service that enables you to coordinate the components of distributed applications and microservices using visual workflows. It provides auditable automation of routine deployments, upgrades, installations, and migrations.
- `Amazon MQ` is a message broker service. It supports industry-standard APIs and protocols so you can switch from any standards-based message broker to Amazon MQ without rewriting the messaging code in your applications.
- `AWS CloudHSM` is an AWS service that enables the creation and maintenance of hardware security modules (HSMs) in your AWS environment for cryptographic purposes. These HSMs are devices that process cryptographic operations and securely store cryptographic keys. By using AWS CloudHSM, you can offload SSL/TLS processing for web servers, as well as provide protection for critical data such as financial records, personally identifiable information (PII), and intellectual property.
- `AWS Personal Health Dashboard` - in all four plans of AWS

### Penetration testing over AWS Services

#### Permitted Services – You’re welcome to conduct security assessments against AWS resources that you own if they make use of the services listed below. Take note that AWS is constantly updating this list:

- Amazon EC2 instances, NAT Gateways, and Elastic Load Balancers
- Amazon RDS
- Amazon CloudFront
- Amazon Aurora
- Amazon API Gateways
- AWS Lambda and Lambda Edge functions
- Amazon Lightsail resources
- Amazon Elastic Beanstalk environments

#### Prohibited Activities – The following activities are prohibited at this time:

- DNS zone walking via Amazon Route 53 Hosted Zones
- Denial of Service (DoS), Distributed Denial of Service (DDoS), Simulated DoS, Simulated DDoS
- Port flooding
- Protocol flooding
- Request flooding (login request flooding, API request flooding)


### AWS Loadbalancers

1. Application Load Balancer (ALB)

- Layer: 7 (Application)
- Protocols: HTTP, HTTPS, WebSocket, gRPC
- Features: Content-based routing (path/host/query), SSL termination, WebSocket support, sticky sessions, AWS WAF integration, Lambda targets
- Use Cases: Web apps, microservices, APIs
- Latency: ~400 ms
- Connections/sec: ~100,000
- Algorithm: Round-robin

2. Network Load Balancer (NLB)

- Layer: 4 (Transport)
- Protocols: TCP, UDP, TLS
- Features: Ultra-low latency, static/elastic IPs, high throughput, preserves source IP, TLS termination
- Use Cases: Gaming, streaming, IoT, high-performance apps
- Latency: ~100 μs
- Connections/sec: ~3,000,000
- Algorithm: Flow hash


3. Gateway Load Balancer (GLB)

- Layer: 3 (Network)
- Protocols: IP-based (any protocol), GENEVE
- Features: Transparent packet forwarding, scales virtual appliances (e.g., firewalls, intrusion detection), single entry/exit point
- Use Cases: Firewalls, deep packet inspection, network security
- Latency: ~200 μs
- Connections/sec: ~1,000,000
- Algorithm: Routing table lookup


4. Classic Load Balancer (CLB)

- Layer: 4 & 7 (Transport & Application)
- Protocols: HTTP, HTTPS, TCP, SSL
- Features: Basic routing, sticky sessions, SSL termination, cross-zone balancing, no advanced routing
- Use Cases: Legacy apps, simple load balancing
- Latency: ~500 ms
- Connections/sec: ~40,000
- Algorithm: Round-robin

Key Notes:

- ALB excels in advanced routing for web apps.
- NLB prioritizes low latency and high throughput.
- GLB is ideal for network appliances.

====================================

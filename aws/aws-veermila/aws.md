# AWS Zero to Hero Series - Day 0: Introduction


# Lec 1 : Day 1 : start of the aws

Welcome to the AWS Zero to Hero series! This 30-day course is designed to guide you from beginner to proficient in AWS, covering essential AWS concepts, practical exercises, real-world scenarios, and interview preparation. Below is an outline of what you’ll be learning and the core concepts explained in simple terms.

## Course Overview

| Day   | Topic                            | Description                                                                                 |
|-------|----------------------------------|---------------------------------------------------------------------------------------------|
| Day 0 | **Introduction**                 | Course introduction, objectives, and learning outcomes.                                     |
| Day 1 | **AWS Fundamentals**             | Basics of AWS and cloud computing, core AWS services, and key terminology.                  |
| Day 5 | **Storage and Databases**        | Overview of AWS storage options (S3, EBS) and database services (RDS, DynamoDB).            |
| Day 10| **Networking and Security**      | AWS networking (VPC, Route 53) and security features (IAM, CloudWatch).                     |
| Day 20| **AWS DevOps Tools**             | Introduction to CI/CD in AWS, using CodePipeline, CodeBuild, and CodeDeploy.                |
| Day 30| **Project & Interview Prep**     | Building a final project, preparing for interviews with key questions and best practices.   |

---

## Key Concepts

### 1. **What is AWS?**

**Amazon Web Services (AWS)** is a comprehensive cloud computing platform provided by Amazon. AWS offers a wide variety of services, including storage, databases, compute, and networking solutions that allow organizations to build scalable, secure, and cost-effective infrastructure.

#### Key Characteristics of AWS:
- **Scalability:** Resources can be scaled up or down based on demand.
- **Cost-Efficiency:** Pay-as-you-go model reduces unnecessary expenses.
- **Reliability:** AWS offers high availability and fault tolerance across multiple data centers.

> **Example:** A startup can use AWS to deploy a web application, adding or removing servers depending on the traffic load.

---

### 2. **Core AWS Services**

| Service Category   | AWS Services                                  | Description                                                              |
|--------------------|-----------------------------------------------|--------------------------------------------------------------------------|
| **Compute**        | EC2, Lambda, ECS                              | Virtual servers, serverless computing, and container management.         |
| **Storage**        | S3, EBS, Glacier                              | Scalable object storage, block storage, and archival storage solutions.  |
| **Database**       | RDS, DynamoDB, Aurora                         | Managed relational and NoSQL databases for different use cases.          |
| **Networking**     | VPC, Route 53, CloudFront                     | Virtual networking, DNS management, and content delivery network (CDN).  |
| **Security**       | IAM, CloudWatch, CloudTrail                   | Access control, monitoring, and auditing tools to secure AWS resources.  |

### 3. **AWS Regions and Availability Zones**

AWS services are hosted across **Regions** (geographic areas) and **Availability Zones (AZs)** (isolated data centers within regions).

- **Regions** are separate geographical areas (e.g., `us-east-1` for Northern Virginia).
- **Availability Zones** are distinct locations within each region, offering redundancy.

> **Note:** AWS regions are globally distributed, allowing users to choose the best region for performance, data residency, and compliance.

---

### 4. **Fundamental AWS Concepts**

1. **Elasticity and Scalability**
   - **Elasticity:** AWS services can automatically adjust resources to meet demand.
   - **Scalability:** Users can manually or automatically increase or decrease resource capacity.

2. **Pay-As-You-Go Pricing**
   - AWS charges only for the resources used, allowing cost control.

3. **Security and Compliance**
   - **IAM (Identity and Access Management):** Controls user access and permissions.
   - **Compliance:** AWS complies with various security standards like ISO, PCI-DSS, and HIPAA.

---

### 5. **Course Objectives and Goals**

In this 30-day AWS series, you’ll:
- Gain a foundational understanding of AWS and cloud computing.
- Work on hands-on labs to practice deploying services on AWS.
- Learn to architect, secure, and optimize AWS environments.
- Build a capstone project to demonstrate your knowledge.
- Prepare for AWS-related interview questions with a strong understanding of core concepts.

---

### Concept Map: AWS Zero to Hero Journey

- **Day 1-10:** Basics of AWS, Storage, and Networking
- **Day 11-20:** Security, IAM, and DevOps Tools
- **Day 21-30:** Real-World Project, Troubleshooting, and Interview Prep

---

# Lec 2 Day-2 | AWS IAM deep dive with practicals and notes | IAM Project 
Here are the key concepts from the lecture, organized in an appropriate way:

1. Cloud Computing Basics:
   - Cloud computing involves accessing computing resources over the internet instead of a local computer or server.
   - Private cloud is used by a single organization, while public cloud is shared among multiple organizations.
   - AWS is a leading cloud provider that offers a wide range of cloud services.

2. IAM (Identity and Access Management):
   - IAM is an AWS service that handles authentication and authorization in AWS.
   - IAM users are created for authentication, allowing individuals to log in to the AWS account.
   - IAM policies are used for authorization, defining the permissions and actions a user can perform in AWS.
   - IAM groups are used to organize users and apply policies to multiple users at once.
   - IAM roles are used for temporary access, such as allowing an application to access AWS resources.

3. Authentication and Authorization:
   - Authentication is the process of verifying the identity of a user, while authorization determines what actions a user can perform.
   - When a user is created in IAM, they can authenticate to the AWS account, but they do not have any authorization to perform actions.
   - To grant authorization, IAM policies must be attached to the user, group, or role.
   - AWS provides managed policies that can be used, or custom policies can be created.

4. IAM Best Practices:
   - The root user has full access to the AWS account and should be used cautiously.
   - IAM best practices include using IAM users instead of the root user for managing the AWS account.
   - Organizing users into groups can help streamline the process of granting permissions.

5. Interview Considerations:
   - In an interview, the candidate should mention using IAM users instead of the root user for managing the AWS account.
   - The candidate should also discuss the concept of authentication and authorization, and how IAM policies and groups are used to manage permissions.

_____________________________

# Lec 3 | EC2 Deep Dive |

Here is a summary of the key concepts covered in the lecture, organized in a structured way:

Introduction to EC2 (Elastic Compute Cloud)
- EC2 stands for Elastic Compute Cloud, which is a virtual server provided by AWS.
- EC2 allows you to request and manage virtual machines (VMs) on the AWS cloud platform.
- EC2 provides the compute capacity that you can use to run your applications.

Why use EC2?
- Eliminates the need to manage physical servers yourself.
- Provides on-demand, scalable compute resources.
- AWS handles the maintenance and upgrades of the underlying hardware and virtualization.
- You pay only for the resources you use, following a "pay-as-you-go" model.
- Reduces the management overhead compared to managing your own physical servers.

Types of EC2 Instances
- General Purpose: Balanced CPU, memory, and networking resources.
- Compute Optimized: High CPU-to-memory ratio, suitable for compute-intensive workloads.
- Memory Optimized: High memory-to-CPU ratio, suitable for memory-intensive workloads.
- Storage Optimized: High storage throughput and I/O, suitable for data-intensive workloads.
- Accelerated Computing: Utilize hardware accelerators, such as GPUs, for specialized workloads.

Regions and Availability Zones
- Regions: AWS has data centers located in different geographical regions around the world.
- Availability Zones: Multiple isolated data centers within a single region, connected through low-latency networks.
- Launching EC2 instances in multiple availability zones provides high availability and fault tolerance.

Launching an EC2 Instance
1. Choose an Amazon Machine Image (AMI) - the operating system for the instance.
2. Select an instance type based on your workload requirements.
3. Configure network settings, such as VPC, subnets, and security groups.
4. Attach a key pair for secure SSH access to the instance.
5. Review and launch the instance.

Connecting to the EC2 Instance
- On Windows, use tools like PuTTY or MobaXterm to connect to the instance via SSH.
- On macOS/Linux, use the built-in terminal and the `ssh` command.
- Use the private key (`.pem` file) associated with the key pair to authenticate.

Deploying an Application (Jenkins)
1. Install Java on the instance.
2. Install Jenkins using the provided installation script.
3. Start the Jenkins service and check its status.
4. Access the Jenkins web interface using the public IP address and the default port 8080.
5. Unlock Jenkins by entering the initial admin password.

Securing the EC2 Instance
- By default, EC2 instances are not accessible from the internet.
- Configure security groups to allow inbound traffic on the required ports (e.g., port 8080 for Jenkins).
- Security groups act as virtual firewalls, controlling both inbound and outbound traffic.

Key Takeaways
- EC2 provides on-demand, scalable virtual servers in the AWS cloud.
- Instance types are optimized for different workload requirements (general purpose, compute, memory, storage, accelerated).
- Regions and availability zones provide high availability and fault tolerance.
- Secure access to EC2 instances using key pairs and security groups.
- Deploying applications on EC2 involves installing dependencies, starting services, and configuring network access.
__________________

# Day-4 | Best VPC explanation|

![alt text](image.png)
![alt text](image-1.png)
![alt text](image-2.png)
![alt text](image-3.png)
![alt text](image-4.png)

## Introduction to Virtual Private Cloud (VPC):

VPC is a secure, isolated virtual network within the AWS cloud.
It allows you to have full control over your virtual networking environment, including IP address ranges, subnets, route tables, and network gateways.

1. **VPC (Virtual Private Cloud)**:
   - Explanation: A VPC is a virtual network within the AWS cloud that you can fully control. It allows you to define your own IP address range, create subnets, and configure routing and security settings.
   - Use Case: A company wants to host its web application and backend services in the cloud, but it needs to ensure that the network is secure and isolated from other tenants.
   - Analogy: The VPC is like a gated community in the village, where the wise person (AWS) has acquired a large plot of land and divided it into smaller, secure sections (subnets) for different residents (the company's applications).

2. **Subnets**:
   - Explanation: Subnets are subdivisions of the VPC's IP address range. They can be either public (accessible from the internet) or private (accessible only within the VPC).
   - Use Case: The company wants to separate its web servers (in a public subnet) from its database servers (in a private subnet) for better security and access control.
   - Analogy: The subnets are like the different neighborhoods within the gated community, where some houses (public subnet) are accessible from the main road, while others (private subnet) are only accessible from within the community.

3. **Internet Gateway**:
   - Explanation: The Internet Gateway is the entry point for traffic from the internet to the VPC. It enables communication between resources in the VPC and the internet.
   - Use Case: Clients from the internet need to access the company's web application hosted in the VPC.
   - Analogy: The Internet Gateway is like the main gate of the gated community, which allows visitors (internet traffic) to enter the community and reach the desired houses (resources in the VPC).

4. **Route Tables**:
   - Explanation: Route tables define the routing rules for traffic within the VPC, determining how traffic should flow between subnets and the internet.
   - Use Case: The company needs to ensure that traffic from the web servers in the public subnet can reach the database servers in the private subnet, and that internet-bound traffic from the private subnet is routed through the NAT Gateway.
   - Analogy: The route tables are like the road signs and directions within the gated community, guiding the traffic (network traffic) to the right destinations (subnets and internet).

5. **Security Groups**:
   - Explanation: Security Groups act as virtual firewalls, controlling inbound and outbound traffic to resources (e.g., EC2 instances) within the VPC.
   - Use Case: The company wants to allow inbound web traffic (port 80 and 443) to the web servers, but restrict all other inbound traffic to the database servers.
   - Analogy: The Security Groups are like the security guards at the entrances of individual houses (resources) within the gated community, checking and controlling who is allowed to enter or leave.

6. **NAT Gateway**:
   - Explanation: The NAT Gateway allows resources in private subnets to access the internet while hiding their private IP addresses, providing an additional layer of security.
   - Use Case: The company's application servers in the private subnet need to download software updates from the internet, but the company doesn't want to expose the private IP addresses of these servers to the internet.
   - Analogy: The NAT Gateway is like a personal driver (or chauffeur) for the residents in the private neighborhoods of the gated community. The driver can go out to the main road (internet) to fetch things the residents need, but the residents' exact addresses (private IP addresses) are kept hidden from the outside world.

7. **VPC Flow Logs**:
   - Explanation: VPC Flow Logs capture information about the IP traffic going to and from network interfaces within the VPC, which can be useful for debugging and monitoring.
   - Use Case: The company needs to investigate a potential security breach or unusual network activity within their VPC.
   - Analogy: The VPC Flow Logs are like the security camera footage for the gated community, recording the movement and activities of visitors and residents (network traffic) for later review and analysis.

```
+-----------------------+
|       VPC            |
|  IP Range: 172.16.0.0/16 |
+-----------------------+
        |
        |
+---------------+   +---------------+
|   Public      |   |   Private     |
|   Subnet      |   |    Subnet    |
| IP Range:     |   | IP Range:     |
| 172.16.1.0/24 |   | 172.16.2.0/24 |
+---------------+   +---------------+
        |                   |
        |                   |
+---------------+   +---------------+
| EC2 Instance  |   | EC2 Instance  |
| Private IP:   |   | Private IP:   |
| 172.16.1.10   |   | 172.16.2.20   |
| Security      |   | Security      |
| Group: Web    |   | Group: DB     |
+---------------+   +---------------+
        |                   |
        |                   |
+---------------+   +---------------+
| Network ACL  |   | Network ACL  |
| Public Subnet|   | Private Subnet|
+---------------+   +---------------+


```

Sure, let me explain the IP address concepts in more detail.

1. **VPC IP Address Range**:
   - The VPC has an IP address range of `172.16.0.0/16`.
   - The `/16` in the IP address range notation means that the first 16 bits (out of the total 32 bits in an IPv4 address) are fixed.
   - This means the VPC can accommodate IP addresses from `172.16.0.0` to `172.16.255.255`, which is a total of 65,536 IP addresses (`2^16 = 65,536`).

2. **Subnet IP Address Ranges**:
   - The VPC is divided into two subnets, each with a smaller IP address range.
   - The first subnet has an IP address range of `172.16.1.0/24`.
   - The `/24` in the IP address range notation means that the first 24 bits (out of the total 32 bits in an IPv4 address) are fixed.
   - This means the first subnet can accommodate IP addresses from `172.16.1.0` to `172.16.1.255`, which is a total of 256 IP addresses (`2^8 = 256`).
   - The second subnet has an IP address range of `172.16.2.0/24`, which can accommodate another 256 IP addresses.

3. **Private IP Addresses**:
   - Each EC2 instance within the subnets is assigned a private IP address from the respective subnet's IP range.
   - Private IP addresses are only accessible within the VPC and cannot be directly accessed from the internet.
   - In the example, the first EC2 instance has a private IP address of `172.16.1.10`, and the second instance has a private IP address of `172.16.2.20`.

The key points to understand are:
- The VPC IP address range defines the total number of IP addresses available within the VPC.
- Subnets are used to divide the VPC into smaller, more manageable IP address ranges.
- Each EC2 instance within a subnet is assigned a private IP address from the subnet's IP range.
- Private IP addresses are only accessible within the VPC and cannot be directly accessed from the internet.

_______________________
# Day-5 | AWS Security Group and NACL | Theory + Practical |

NACL FOR AUTOMATION > It restics // deny irrelevent trafect at subnet level

![alt text](image-5.png)

## Security Groups
Security groups operate at the instance level, controlling the inbound and outbound traffic to your EC2 instances. We will explore the following aspects of security groups:

### Default Security Group Behavior
- By default, AWS denies all inbound traffic to your instances.
- By default, AWS allows all outbound traffic, except for port 25 (to prevent potential spam activities).

### Configuring Security Group Rules
- As a developer or DevOps engineer, you need to explicitly configure the security group rules to allow the necessary inbound and outbound traffic to your application.
- This is a crucial step, as opening unnecessary ports or allowing traffic from untrusted sources can expose your application to security risks.

## Network ACLs (NACLs)
While security groups operate at the instance level, NACLs work at the subnet level. We will explore the following aspects of NACLs:

### NACL vs. Security Groups
- The primary difference between security groups and NACLs is that NACLs have the ability to deny traffic, whereas security groups can only allow traffic.
- NACLs are designed to act as the first line of defense, while security groups are the last line of defense before traffic reaches your application.

### NACL Rule Evaluation
- NACLs have a set of inbound and outbound rules that are evaluated in a specific order (based on rule numbers).
- The first rule that matches the traffic is applied, and the remaining rules are ignored.
- This order of evaluation is crucial, as it allows you to create more granular control over the traffic flow.

## Practical Demonstration
Now, let's put these concepts into practice and explore the security group and NACL configurations:

### Step 1: Create a Custom VPC
1. In the AWS Management Console, navigate to the VPC service and click on "Create VPC".
2. Choose the "VPC with Public and Private Subnets" option.
3. Configure the VPC with an appropriate IP address range and let AWS handle the creation of public and private subnets, an internet gateway, and default route tables.

### Step 2: Create an EC2 Instance
1. In the EC2 service, launch a new instance and select the custom VPC you just created.
2. Choose to place the instance in the public subnet, as we'll be accessing it directly for this demonstration.
3. When configuring the security group, let AWS create a new one for you.

### Step 3: Explore Security Group Configuration
1. Examine the default security group created by AWS. You'll see that it only allows inbound SSH traffic (port 22) by default.
2. Add a new inbound rule to allow traffic on port 8000 (the port where we'll run our application).
3. Save the security group changes and try to access the EC2 instance on port 8000. You should now be able to see the output of the simple Python HTTP server running on the instance.

### Step 4: Explore NACL Configuration
1. In the VPC service, navigate to the "Network ACLs" section and select the NACL associated with your custom VPC.
2. By default, the NACL allows all inbound and outbound traffic.
3. Create a new NACL rule to deny traffic on port 8000.
4. Save the NACL changes and try to access the EC2 instance on port 8000 again. This time, the traffic will be blocked at the NACL level, even though the security group allows it.

### Step 5: Modify NACL Rules
1. Experiment with the order of the NACL rules by changing the rule numbers.
2. Create additional NACL rules to allow or deny traffic based on specific IP ranges or port numbers.
3. Observe how the traffic flow is affected by the NACL configuration, even when the security group rules remain the same.
___________________________

# Day-6 | Route53

1. DNS Maps Domain Names to IP Addresses:
   - When users access applications using domain names (e.g. amazon.com, flipkart.com), DNS resolves these domain names to the actual IP addresses of the underlying infrastructure.
   - This abstraction allows users to remember and use easy-to-remember domain names instead of hard-to-remember IP addresses.

2. Route 53 Provides DNS as a Service on AWS:
   - Just like AWS provides compute resources (EC2) and storage (S3) as services, Route 53 provides DNS as a service.
   - This simplifies DNS management compared to setting up and maintaining your own DNS infrastructure.

3. Key Route 53 Features:
   - Domain Registration: Route 53 allows you to purchase domain names directly from AWS.
   - Hosted Zones: Route 53 maintains "hosted zones" which contain the DNS records mapping domain names to IP addresses.
   - Health Checks: Route 53 can perform health checks on your application endpoints and route traffic accordingly.

4. Importance for Interviews:
   - Many companies use the public-private subnet architecture within a VPC, with the application hosted in the private subnet and accessed via a load balancer in the public subnet.
   - Integrating Route 53 to handle the domain name to IP address mapping is a common requirement in such architectures.
   - Interviewers often ask candidates to explain how they would implement this type of architecture using AWS services like VPC, Load Balancer, and Route 53.
______________________________

# Day-7 | AWS Project Used In Production |

![alt text](image-6.png)
![alt text](image-7.png)
![alt text](image-8.png)

# Production-Grade AWS Architecture Implementation Guide

## Architecture Overview

The architecture we'll implement is a secure, production-grade infrastructure that follows AWS best practices. Here's what we'll build:

```
Internet
   ↓
Internet Gateway
   ↓
   → Public Subnet (AZ-1)        → Public Subnet (AZ-2)
      - NAT Gateway                - NAT Gateway
      - Load Balancer              - Load Balancer
      - Bastion Host
         ↓                            ↓
   → Private Subnet (AZ-1)       → Private Subnet (AZ-2)
      - Application Instance        - Application Instance
      (Auto Scaling Group)          (Auto Scaling Group)
```

### Key Components:
- VPC with public and private subnets across two Availability Zones
- Internet Gateway for public internet access
- NAT Gateway for private subnet internet access
- Application Load Balancer in public subnets
- Auto Scaling Group managing application instances in private subnets
- Bastion Host for secure SSH access to private instances
- Security Groups controlling access

## Step-by-Step Implementation

### 1. VPC Creation

1. Navigate to VPC Dashboard
2. Click "Create VPC"
3. Select "VPC and More" option
4. Configure:
   - Name: `AWS-Prod-Example`
   - IPv4 CIDR: Auto-generated (10.0.0.0/16)
   - Number of AZs: 2
   - Number of public subnets: 2
   - Number of private subnets: 2
   - NAT Gateways: 1 per AZ
   - VPC endpoints: None

This creates:
- VPC
- 2 public subnets (one per AZ)
- 2 private subnets (one per AZ)
- Internet Gateway
- NAT Gateways
- Route tables for both public and private subnets

### 2. Auto Scaling Group Setup

1. Create Launch Template:
   ```
   Name: AWS-Prod-Example
   AMI: Ubuntu Server LTS
   Instance Type: t2.micro
   Key pair: Select existing
   Security Group: 
     - Allow SSH (Port 22)
     - Allow Custom TCP (Port 8000)
   Network: Select created VPC
   ```

2. Create Auto Scaling Group:
   ```
   Name: AWS-Prod-Example
   Launch Template: Use created template
   VPC: Select created VPC
   Subnets: Select both private subnets
   Desired capacity: 2
   Minimum: 2
   Maximum: 4
   ```

### 3. Bastion Host Setup

1. Launch EC2 Instance:
   ```
   Name: Bastion-Host
   AMI: Ubuntu Server LTS
   Instance Type: t2.micro
   Network: Created VPC
   Subnet: Public subnet
   Auto-assign Public IP: Enable
   Security Group: Allow SSH (Port 22)
   ```

2. Copy SSH Key to Bastion:
   ```bash
   scp -i path/to/key.pem path/to/key.pem ubuntu@bastion-public-ip:~/.ssh/
   ```

### 4. Application Deployment

1. SSH to Bastion:
   ```bash
   ssh -i key.pem ubuntu@bastion-public-ip
   ```

2. SSH to Private Instance:
   ```bash
   ssh -i ~/.ssh/key.pem ubuntu@private-instance-ip
   ```

3. Deploy Sample Application:
   ```bash
   # Create HTML file
   cat << EOF > index.html
   <!DOCTYPE html>
   <html>
   <head>
   <title>AWS Private Subnet Demo</title>
   </head>
   <body>
   <h1>My First AWS Project</h1>
   <p>Demonstrating apps in private subnet</p>
   </body>
   </html>
   EOF

   # Start Python server
   python3 -m http.server 8000
   ```

### 5. Load Balancer Configuration

1. Create Target Group:
   ```
   Name: AWS-Prod-Example
   Target type: EC2 instances
   Protocol: HTTP
   Port: 8000
   VPC: Created VPC
   Health check: HTTP on port 8000
   Register targets: Select both EC2 instances
   ```

2. Create Application Load Balancer:
   ```
   Name: AWS-Prod-Example
   Scheme: Internet-facing
   VPC: Created VPC
   Subnets: Both public subnets
   Security Group: Allow HTTP (Port 80)
   Listener: HTTP on port 80
   Target Group: Created group
   ```

## Security Considerations

1. Security Group Configuration:
   - Load Balancer SG: Allow HTTP (80) from anywhere
   - Application SG: Allow 8000 from Load Balancer SG
   - Bastion SG: Allow SSH (22) from your IP
   - Private Instance SG: Allow SSH from Bastion SG

2. Network Access:
   - Public subnets route to Internet Gateway
   - Private subnets route through NAT Gateway
   - No direct internet access to private instances
   - All external access through Load Balancer

## Testing

1. Access Application:
   ```
   http://<load-balancer-dns>
   ```

2. Verify Load Balancing:
   - Deploy different content to each instance
   - Refresh browser to see traffic distribution
   - Monitor target group health status

## Cleanup

To avoid ongoing charges, remember to delete resources in this order:
1. Load Balancer
2. Auto Scaling Group
3. Launch Template
4. Bastion Host
5. NAT Gateway
6. VPC and associated resources

## Best Practices

1. Always use multiple AZs for high availability
2. Keep application instances in private subnets
3. Use Bastion Host for secure SSH access
4. Implement proper security groups with least privilege
5. Use Auto Scaling for reliability and scalability
6. Monitor health checks and configure appropriate thresholds
7. Regularly patch and update all instances
8. Implement proper backup and disaster recovery procedures

![alt text](image-9.png)


 ```mermaid
graph TB
    Start[Start] --> VPC[1. Create VPC]
    
    VPC --> Subnets[1a. Configure Subnets]
    Subnets --> |Create| PublicSubnet[Public Subnets x2]
    Subnets --> |Create| PrivateSubnet[Private Subnets x2]
    
    VPC --> Gateway[1b. Configure Gateways]
    Gateway --> |Create| IGW[Internet Gateway]
    Gateway --> |Create| NGW[NAT Gateway]
    
    VPC --> Routes[1c. Configure Route Tables]
    
    Routes --> |Associate| SubnetRoutes[Associate Subnets with Routes]
    
    SubnetRoutes --> Template[2. Create Launch Template]
    Template --> |Configure| AMI[Ubuntu AMI]
    Template --> |Configure| SecGroup1[Security Group\nPorts: 22, 8000]
    
    Template --> ASG[3. Create Auto Scaling Group]
    ASG --> |Deploy in| PrivateSubnet
    ASG --> |Configure| Capacity[Set Capacity:\nDesired: 2\nMin: 2\nMax: 2]
    
    ASG --> Bastion[4. Create Bastion Host]
    Bastion --> |Deploy in| PublicSubnet
    Bastion --> |Configure| SecGroup2[Security Group\nPort: 22]
    
    Bastion --> SSH[5. Configure SSH Access]
    SSH --> |Copy| Keys[Copy .pem to Bastion]
    SSH --> |Access| PrivateEC2[Access Private EC2]
    
    PrivateEC2 --> App[6. Deploy Application]
    App --> |Install| Python[Python HTTP Server\nPort: 8000]
    
    App --> Target[7. Create Target Group]
    Target --> |Register| Instances[Register EC2 Instances]
    Target --> |Configure| Health[Health Checks]
    
    Target --> ALB[8. Create Application\nLoad Balancer]
    ALB --> |Deploy in| PublicSubnet
    ALB --> |Configure| SecGroup3[Security Group\nPort: 80]
    
    ALB --> Final[9. Final Configuration]
    Final --> |Update| Security[Update Security Rules]
    Final --> |Test| Access[Test Access]
    
    Access --> End[End]
    style Start fill:#97c2fc
    style End fill:#97c2fc
    style VPC fill:#bbf7d0
    style Template fill:#bbf7d0
    style ASG fill:#bbf7d0
    style Bastion fill:#bbf7d0
    style App fill:#bbf7d0
    style ALB fill:#bbf7d0
    style Final fill:#bbf7d0
```
____
# Day-8 |AWS Scenario Based Interview Questions on EC2, IAM and VPC 

>Q:1 You have been assigned to design a VPC architecture for a 2-tier application. The application needs to be highly available and scalable. How would you design the VPC architecture?

>> A: In this scenario, I would design a VPC architecture in the following way.
   I would create 2 subnets: public and private. The public subnet would contain the load balancers and be accessible from the internet. The private subnet would host the application servers. 
   I would distribute the subnets across multiple Availability Zones for high availability. Additionally, I would configure auto scaling groups for the application servers.

> Q2: Your organization has a VPC with multiple subnets. You want to restrict outbound internet access for resources in one subnet, but allow outbound internet access for resources in another subnet. How would you achieve this?

>>A: To restrict outbound internet access for resources in one subnet, we can modify the route table associated with that subnet. In the route table, we can remove the default route (0.0.0.0/0) that points to an internet gateway. 
   This would prevent resources in that subnet from accessing the internet. For the subnet where outbound internet access is required, we can keep the default route pointing to the internet gateway.

> Q3: You have a VPC with a public subnet and a private subnet. Instances in the private subnet need to access the internet for software updates. How would you allow internet access for instances in the private subnet?

>>A: To allow internet access for instances in the private subnet, we can use a NAT Gateway or a NAT instance. 
   We would place the NAT Gateway/instance in the public subnet and configure the private subnet route table to send outbound traffic to the NAT Gateway/instance. This way, instances in the private subnet can access the internet through the NAT Gateway/instance.

> Q4: You have launched EC2 instances in your VPC, and you want them to communicate with each other using private IP addresses. What steps would you take to enable this communication?

>> A: By default, instances within the same VPC can communicate with each other using private IP addresses. 
  To ensure this communication, we need to make sure that the instances are launched in the same VPC and are placed in the same subnet or subnets that are connected through a peering connection or a VPC peering link. 
  Additionally, we should check the security groups associated with the instances to ensure that the necessary inbound and outbound rules are configured to allow communication between them.

> Q5: You want to implement strict network access control for your VPC resources. How would you achieve this?

>> A: To implement granular network access control for VPC resources, we can use Network Access Control Lists (ACLs). 
  NACLs are stateless and operate at the subnet level. We can define inbound and outbound rules in the NACLs to allow or deny traffic based on source and destination IP addresses, ports, and protocols. 
  By carefully configuring NACL rules, we can enforce fine-grained access control for traffic entering and leaving the subnets.

> Q6: Your organization requires an isolated environment within the VPC for running sensitive workloads. How would you set up this isolated environment?

>> A: To set up an isolated environment within the VPC, we can create a subnet with no internet gateway attached. 
   This subnet, known as an "isolated subnet," will not have direct internet connectivity. We can place the sensitive workloads in this subnet, ensuring that they are protected from inbound and outbound internet traffic. 
   However, if these workloads require outbound internet access, we can set up a NAT Gateway or NAT instance in a different subnet and configure the isolated subnet's route table to send outbound traffic through the NAT Gateway/instance.

> Q7: Your application needs to access AWS services, such as S3 securely within your VPC. How would you achieve this?

>> A: To securely access AWS services within the VPC, we can use VPC endpoints. VPC endpoints allow instances in the VPC to communicate with AWS services privately, without requiring internet gateways or NAT gateways. 
  We can create VPC endpoints for specific AWS services, such as S3 and DynamoDB, and associate them with the VPC. 
  This enables secure and efficient communication between the instances in the VPC and the AWS services.

> Q8: What is the difference between NACL and Security groups ? Explain with a use case ?

>> A: For example, I want to design a security architecture, I would use a combination of NACLs and security groups. At the subnet level, I would configure NACLs to enforce inbound and outbound traffic restrictions based on source and destination IP addresses, ports, and protocols. NACLs are stateless and can provide an additional layer of defense by filtering traffic at the subnet boundary.
  At the instance level, I would leverage security groups to control inbound and outbound traffic. Security groups are stateful and operate at the instance level. By carefully defining security group rules, I can allow or deny specific traffic to and from the instances based on the application's security requirements.
  By combining NACLs and security groups, I can achieve granular security controls at both the network and instance level, providing defense-in-depth for the sensitive application.

> **Q9: What is the difference between IAM users, groups, roles and policies ?**

>> A: IAM User: An IAM user is an identity within AWS that represents an individual or application needing access to AWS resources. IAM users have permanent long-term credentials, such as a username and password, or access keys (Access Key ID and Secret Access Key). IAM users can be assigned directly to IAM policies or added to IAM groups for easier management of permissions.
   IAM Role: An IAM role is similar to an IAM user but is not associated with a specific individual. Instead, it is assumed by entities such as IAM users, applications, or services to obtain temporary security credentials. IAM roles are useful when you want to grant permissions to entities that are external to your AWS account or when you want to delegate access to AWS resources across accounts. IAM roles have policies attached to them that define the permissions granted when the role is assumed.
   IAM Group: An IAM group is a collection of IAM users. By organizing IAM users into groups, you can manage permissions collectively. IAM groups make it easier to assign permissions to multiple users simultaneously. Users within an IAM group inherit the permissions assigned to that group. For example, you can create a "Developers" group and assign appropriate policies to grant permissions required for developers across your organization.
   IAM Policy: An IAM policy is a document that defines permissions and access controls in AWS. IAM policies can be attached to IAM users, IAM roles, and IAM groups to define what actions can be performed on which AWS resources. IAM policies use JSON (JavaScript Object Notation) syntax to specify the permissions and can be created and managed independently of the users, roles, or groups. IAM policies consist of statements that include the actions allowed or denied, the resources on which the actions can be performed, and any additional conditions.

> **Q10: You have a private subnet in your VPC that contains a number of instances that should not have direct internet access. However, you still need to be able to securely access these instances for administrative purposes. How would you set up a bastion host to facilitate this access?**

>> A: To securely access the instances in the private subnet, you can set up a bastion host (also known as a jump host or jump box). The bastion host acts as a secure entry point to your private subnet. Here's how you can set up a bastion host:
      Create a new EC2 instance in a public subnet, which will serve as the bastion host. Ensure that this instance has a public IP address or is associated with an Elastic IP address for persistent access.
      Configure the security group for the bastion host to allow inbound SSH (or RDP for Windows) traffic from your IP address or a restricted range of trusted IP addresses. This limits access to the bastion host to authorized administrators only.
      Place the instances in the private subnet and configure their security groups to allow inbound SSH (or RDP) traffic from the bastion host security group.
      SSH (or RDP) into the bastion host using your private key or password. From the bastion host, you can then SSH (or RDP) into the instances in the private subnet using their private IP addresses.

__________

# Day-9 | AWS S3 Buckets Deep Dive | 2 Demo Projects with Code 


Note: This page does not save intermediate responses. Please prepare your work in a separate file to avoid losing it and to have a copy for your own records. All submissions are irreversible and final. Please make sure that you are satisfied with your answers before submitting the form.
Your Challenge

This team responds to all triggered AWS alarms across all 100+ products, understanding why the alarm fired, the actual problem with the infrastructure, and fixing the infrastructure outage (if it’s really an outage).

Many alarms have Showstopper priority P1 (they are likely symptoms of outages and require immediate action). In contrast, others are High-priority P2 (they do not require real-time response, and can be worked asynchronously).

The DevOps team is judged by the uptime of the Production environment, so the fewer outages and the smaller the outages are, the better.

Addressing an alarm involves the following aspects:
Understand the problem by identifying:
The Symptoms - recording objective measurements
The Root Cause - finding the root cause of the problem that triggered the problem.
Immediate fix - resolving the problem as soon as possible, and fixing the infrastructure. Focus on low time-to-recovery.
Permanent fix - ensure the same problem cannot repeat itself. Focus on preventing the root cause, permanently.
Question Title
* Task 1

We have an existing alarm for an ASG:
Condition: The alarm triggers if desiredCapacity > inServiceInstances for 1 datapoint within 5 minutes.
Period: 5 minutes
Datapoints to alarm: 1 out of 1 datapoint
Math expression: IF(desiredCapacity > inServiceInstances, 1, 0).
Is there anything wrong with this CloudWatch alarm? If yes, explain what and fix it.

Your Response Here:


Symptoms: The alarm triggers whenever desiredCapacity > inServiceInstances for even a single datapoint within 5 minutes. This happens frequently during normal scaling events when new EC2 instances are launching and have not yet passed health checks. As a result, the alarm produces false positives.

Root Cause: The alarm is too sensitive because it only evaluates a single datapoint (1 out of 1). It does not account for the normal delay in bringing new instances into service.

Immediate Fix: Update the alarm to require multiple consecutive datapoints (e.g., 5 out of 5 with a 1-minute period) before triggering. This way, the alarm only fires if the ASG consistently fails to bring instances in service, which is a real issue.

Permanent Fix: Align ASG alarms with scaling behavior by tuning thresholds and evaluation periods, and supplement with additional alarms (e.g., instance launch failures, health check failures). This ensures the team only gets paged for actual outages, not expected scaling activity.


==============================================================================



Task 2:

Is there anything wrong with this CloudWatch alarm? If yes, explain what and fix it.


Symptoms:

The CloudWatch alarm for certificate expiry is in “Insufficient data” state.

The alarm threshold is set to DaysToExpiry <= 25, but it never triggers because metrics are missing.

No actions are attached to notify anyone when the alarm fires.

Root Cause:

The AWS/CertificateManager metric DaysToExpiry only publishes if the certificate is managed by ACM and in use with certain AWS resources (like ELB, CloudFront, API Gateway). For uploaded/self-managed certs, no metric data is pushed, leading to “Insufficient Data”.

Missing “AlarmActions” means even if the alarm works, no team gets notified.

Immediate Fix:

Attach an SNS topic or PagerDuty/Webhook to the alarm’s actions so alerts are sent when it fires.

For this specific certificate, verify it’s ACM-managed and actually in use. If it’s imported and not emitting metrics, set up a manual Lambda job that pushes custom metrics for expiry days.

Permanent Fix:

Standardize certificate management: keep all certificates in AWS ACM where metrics are available.

For exceptions (e.g., self-managed certs), implement a Lambda scheduled job to check expiration via DescribeCertificate and push custom CloudWatch metrics.

Add a company-wide alarm template so all certificate alarms automatically include actions (SNS → on-call).

Add monitoring tests in CI/CD so no alarm is deployed without notification actions.



========================================================================================


Task 3

Is there anything wrong with this CloudWatch alarm? If yes, explain what and fix it.

{
"AlarmName": "RDSHighCPU",
"AlarmDescription": "Alarm when RDS CPU exceeds 90%",
"ActionsEnabled": true,
"AlarmActions": [],
"MetricName": "CPUUtilization",
"Namespace": "AWS/RDS",
"Statistic": "Maximum",
"Period": 60,
"EvaluationPeriods": 3,
"Threshold": 90,
"ComparisonOperator": "GreaterThanThreshold"

Your Response Here:

Symptoms

The alarm is noisy on brief CPU spikes and sometimes fails to notify anyone.

When it does trigger, it doesn’t reliably reflect sustained database pressure.

Root Cause

Uses Statistic: Maximum with a 60s period → fires on momentary spikes that aren’t outages.

AlarmActions is empty → no page/notification even if the alarm goes ALARM.

No dimension is specified → the metric isn’t scoped to a specific DBInstanceIdentifier, which can make the alarm meaningless or evaluate the wrong resource.

Immediate Fix

Use Average CPU over a longer window so we alert on sustained load: 5-minute period, 3/3 evaluation.

Add an SNS (or PagerDuty/Webhook) action.

Scope the metric to the target DBInstanceIdentifier.

Permanent Fix

Complement CPU with related RDS alarms (FreeableMemory low, FreeStorageSpace low, Read/WriteLatency high, DatabaseConnections high).

Add a runbook and dashboard; consider anomaly detection for CPU to auto-tune to baseline.


Corrected alarm (example)

{
  "AlarmName": "RDSHighCPU",
  "AlarmDescription": "RDS CPU > 90% for a sustained period",
  "ActionsEnabled": true,
  "AlarmActions": ["arn:aws:sns:us-east-1:123456789012:OnCall"],
  "MetricName": "CPUUtilization",
  "Namespace": "AWS/RDS",
  "Dimensions": [{ "Name": "DBInstanceIdentifier", "Value": "prod-mariadb-01" }],
  "Statistic": "Average",
  "Period": 300,
  "EvaluationPeriods": 3,
  "DatapointsToAlarm": 3,
  "Threshold": 90,
  "ComparisonOperator": "GreaterThanThreshold",
  "TreatMissingData": "notBreaching"
}


===========================================================

Task 4
Existing Alarm: An alarm on a Lambda function triggers when the error rate (Average) exceeds 5% over a 1-minute period.
Improvement: Someone suggests changing the statistic to Minimum and the threshold to 1%. They claim this will ensure the alarm only fires for consistent errors.
Imagine you are the manager of this team. You are being asked to push this change through. Document your argument for or against this change in 1-2 paragraphs.

Your Response Here:


I would reject the proposed change. Switching the statistic from Average to Minimum is incorrect because Minimum error rate will almost always be 0 unless every single invocation fails, meaning the alarm would almost never fire even when error rates are very high (e.g., 40% of requests failing). This creates blind spots and increases the risk of missed production outages.

The current approach (Average > 5% over 1 minute) is the correct method to capture when a significant portion of Lambda invocations fail. If the concern is false positives on short spikes, the safer fix is to increase the evaluation window (e.g., 3 datapoints over 5 minutes) or adjust the threshold slightly, not to switch to Minimum. This ensures the alarm remains a reliable P1 signal while filtering noise.


====================================================================



Task 5:

We are taking over a new product called TCI, with the following high-level architecture. The product allows customers to create and send out survey links to end-users and track their opening/completion. Create a great monitoring plan by filling out the table below with the CloudWatch alarms you would create.


* Instructions:

Please list what you would monitor, whether it is a P1 or P2 priority, the threshold, and a brief explanation of why it’s important. List one item per line

Example:
1. [Item], [P1/P2], [threshold], [explanation]
2. [Item], [P1/P2], [threshold], [explanation]


1. EKS Cluster Node CPU Utilization, P1, > 85% for 5 minutes, High CPU saturation blocks backend services from creating/sending surveys.  
2. EKS Pod CrashLoopBackOff Events, P1, > 3 failures within 10 minutes, Detects backend instability before it cascades into outages.  
3. RDS MariaDB Primary DB CPU Utilization, P1, > 80% for 5 minutes, Prevents DB overload that would disrupt survey creation, login, and analytics.  
4. RDS MariaDB Primary DB Free Storage Space, P1, < 15% free, Database running out of storage causes outages and data loss risk.  
5. RDS Replica Lag (multi-tenant), P2, > 60 seconds lag, Ensures analytics dashboards show fresh survey results instead of stale data.  
6. Data Voyager EC2 Status Check Failures, P1, > 0 for 2 consecutive periods, Data pipeline failure blocks reporting and analytics delivery.  
7. Analytics / Tableau EC2 CPU Utilization, P2, > 85% for 10 minutes, Avoids degraded performance for reporting without affecting core survey flow.  
8. Druid Storage Utilization, P1, > 85% full, Survey results ingestion halts if storage runs out.  
9. Hurricane MTA Bounce/Failure Rate, P1, > 5% over 5 minutes, Email survey links failing = customers can’t reach users.  
10. SMS Delivery Failures (Tyntec), P1, > 5% errors over 5 minutes, SMS surveys failing blocks customer outreach.  
11. API Gateway 5XX Error Rate (SOAP/REST), P1, > 2% errors for 2 minutes, API outage stops integrators/customers from creating or sending surveys.  
12. Survey Website Latency (p95), P1, > 3s response time for 5 minutes, High latency frustrates users and reduces survey completion rates.  
13. Admin/Portal Login Failures, P2, > 10% failed logins in 10 minutes, Detects authentication failures or brute-force attack attempts.  


===============================================================
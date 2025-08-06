# Teleport

Teleport is open-source tool that give sso like features and help is achieve RBAC for our environments.

- It gives us steps on the way of installing it to configure admin user/password and MFA.
- we can later add as many resources as needed (ssh, db, aws cli, etc)
- if any issue in enrollment of new resources, try syncing the timezones (go for nrpe/ntp/chrony, etc)

## Enrolling ssh resource

- Go to "Add New" > "Resource" > then select relavent OS
- give unique labels (os:centos/ubuntu/rocky, <project-name>:dev/uat/staging/prod, server:<hostname>)
- give users to authenticate for ssh logins
- it will generate a curl command > run it inside on remote ssh host which you want to add/enroll (there we may get some errors, so resolve accordingly)
- host will be fetched in teleport web console > "Test Connection" using one or two users and you're DONE.

## Enrolling postgres db host (self-hosted) in teleport

steps:

- start from teleport gui *(always take backup of configs before editing them)*
  - "add a resource" > select "postgres (self-hosted)" > add lables > give db (public) ip address and port > run the provided command on target host > 
  - if target host is already added as ssh resource then update already present teleport.yaml to include this db-service (take example from tadawuly uat host) with the auth-join token updated from the command provided for db host enrollement
  - generate the teleport signed cert files (3 files) on db host and point them in postgresql.conf of running db -----------> tested
  OR  
  - you can also add the (already being used) cert file here in teleport console for teleport validation
  - add the given pg_hba.conf entries (add both enteries on the top of rules as the rules apply from top to bottom here in pg_hba.conf) --- with required users/database
  - reload/restart postgresql.conf
  - give the db user and database names to access
  - "Test Connection" and save.

## Managing RBAC/HBAC

- We need to create roles (by default there are access, auditor, editor, etc) | "editor" + "access" > make you have admin pervileges.
- For RBAC/HBAC, we need to create specific roles:
    - we can define the extent of permissions/previleges
    - we can restrict this role to specific hosts using host/resource specific labels (in "resources" field while creating it)
- later we will create users and can add specfic role/roles to that user to give him desired priveleges.

## Audits

- It also have by default session recording features and it stores the video recordings in proxy server as binary files.


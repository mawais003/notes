# Nagios

- open-source 
- monitoring of systems, networks and infrastructures
- it does passive monitoring (itself scraps data/ok-signal from clients)
- default ports are 5666. 5667 and 5668 but these can be changed

## Nagios Architecture

- Client-Server architecture
- nagios monitors its plugins running on remotes hosts (clients)
- main configuration file `/usr/local/nagios/etc/nagios-cfg`
- Daemon read those details and uses NRPE plugin to collect data from its nodes and store in its own (time-series) database.

## How does nagios work?




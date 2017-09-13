# mq_scan
Scans an IBM MQ instance for unauthenticated access to admin channels.

## Usage
```
python mq_scan.py <IP> <PORT>
```

## Exploiting MQ

1. Connect to the queue manager using MQ explorer and the details found by the scanner.
2. Create a service with the desired command and arguments.
3. Start the service.

## Requirements

This script requires the pymqi library to be installed.

## Issues

False positives are sometime observed on the SYSTEM.AUTO.SVRCONN channel.

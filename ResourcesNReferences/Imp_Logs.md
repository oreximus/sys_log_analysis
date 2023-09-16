# Checking System Logs for Compromize

## Source: ChatGPT

1. **Access Logs**: cheking login attempts, SSH connections, and other network activities.
2. **Event Logs**: checking unexpected system reboots, services crashes, or unusual error messages that may indicate an intrusion or compromize.
3. **Network Traffic**: Looking for unusual or unauthorized network connections, unusual traffic patterns, or signs of data exfiltration.
4. **File Integrity**: Use tools like Tripwire or AIDE to monitor changes to critical system files and directories. If there are unexpected modifications, it could be a sign of compromize.
5. **User Account Activity**: Review user account logs for any unusual activities, such as changes to user privileges, the creation of new user accountsm or unauthorized access to sensitive files.
6. **Firewall Logs**: Analyze firewall logs for any unauthorized incoming or outgoing traffic. Look for patterns of communication with known malicious IP addresses.
7. **Web Server Logs**: If there is a web-server running, then review web server logs for signs of unusual or suspicious request. Pay attention to patterns that might indicate a web application attack or attempts to exploit vulnerabilities.
8. **Authentication Logs**: Check authentication logs for any anomalies in user login behaviour, such as multiple failed login attempts or successful logins from unexpected locations.
9. **Process Monitoring**: Use tools like `ps` and `top` to monitor running processes and their resources utilization. Look for any unfamilier or suspicious processes running on the system.
10. **Malware Scans**: Run malware scanning tools to check for the presence of known malicious software or malware signatures on your system.
11. **HIDS/HIPS**: Consider using Host-based Intrusion Detection System (HIDS) or Host-based Intrusion Prevention System (HIPS) to actively monitor and alert you to suspicious activities.
12. **Logs Consolidation**: If possible, use centralized logging solutions or SIEM (Security Information and Event Management) system to aggregate and correlate logs from multiple sources, making it easier to detect anomalies.
13. **Syslogs**: Examine the syslog or equivalent logs on your system. These logs often contain important information about system activities and can help you identify suspicious events. Pay attention to any anomalies or errors that stand out.
14. **Regular Auditing**: Perform regular log analysis and auditing as part of your security best practices, even when you don't suspect a compromize. This helps establish a baseline of normal behaviour for you system.
16. **Incident Response Plan**: Have an incident response plan in place so that if you do detect a compromize, you can respond quickly and effectively to contain the threat and mitigate damage.

# 🧪 SCADA Vulnerability Analysis – CIP Perspective

This file provides a breakdown of common vulnerabilities within SCADA systems often found in critical infrastructure environments (e.g., energy, water treatment, transportation).

---

## 🔍 Typical Weaknesses

| Vulnerability Type      | Description                                             | Impact           |
|-------------------------|---------------------------------------------------------|------------------|
| Plaintext Protocols     | Protocols like Modbus/TCP lack encryption/authentication | Data exposure, command injection |
| Insecure Remote Access  | Open VPN ports, default credentials                    | Unauthorized access |
| Legacy Systems          | Unpatched Windows 7 SCADA stations                     | Exploitable RCE vulnerabilities |
| Flat Network Topology   | Lack of segmentation between IT and OT                 | Lateral movement |
| USB Autorun             | SCADA workstations allow autorun from USB              | Malware injection |

---

## 🔧 Sample Simulated Discovery (Lab)

1. `nmap -sV -p502 192.168.88.0/24`  
   ➜ Detects Modbus protocol on PLC devices

2. `wireshark` filter: `modbus`  
   ➜ Observe cleartext commands (`write coil`, `read holding register`)

3. `shodan.io` query: `port:502 country:"VN"`  
   ➜ Public exposure of Modbus endpoints

---

## 🛡️ Mitigation Recommendations

- Apply encrypted tunnels for legacy protocol traffic
- Disable unused USB ports or enforce endpoint protection
- Configure strict ACLs between IT and OT VLANs
- Patch legacy systems and restrict internet-facing OT systems

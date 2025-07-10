# 🌐 Network Segmentation in Industrial Control Systems

This lab simulates basic segmentation between IT and OT networks, demonstrating why segmentation is crucial in Critical Infrastructure Protection (CIP) strategy.

---

## 🛠️ 1. Lab Topology

[Internet]
|
[Router + Firewall]
|
[IT VLAN] [OT VLAN]
| |
[Admin PC] [SCADA PLC + HMI]


- IT VLAN: General enterprise network
- OT VLAN: Industrial equipment (SCADA, HMI, RTU)
- Segmentation enforced via `iptables` or L3 switch ACLs

---

## 🔧 2. Configuration (Linux Simulation)

### Set up VLAN interfaces (on virtualized environment):

```bash
ip link add link eth0 name eth0.10 type vlan id 10  # IT VLAN
ip link add link eth0 name eth0.20 type vlan id 20  # OT VLAN
ip addr add 192.168.10.1/24 dev eth0.10
ip addr add 192.168.20.1/24 dev eth0.20
ip link set up eth0.10
ip link set up eth0.20
```


## 🔒 3. Enforce Isolation with iptables

```bash
# Allow IT to access Internet
iptables -A FORWARD -i eth0.10 -o eth0 -j ACCEPT

# Block OT-to-IT access by default
iptables -A FORWARD -i eth0.20 -o eth0.10 -j DROP
```

## 🧪 4. Testing Scenarios

✅ Ping from Admin PC → Internet: should work

✅ Ping from Admin PC → PLC: only if explicitly allowed

❌ Ping from PLC → Admin PC: should be blocked

📌 Key Lessons

- Flat networks allow easy pivoting from IT to OT

- VLANs are not security boundaries alone — require firewall/ACL rules

- SCADA systems should never be directly reachable from corporate IT

🔗 Real-World Reference

[NIST SP 800-82 Rev.2](https://csrc.nist.gov/pubs/sp/800/82/r2/final) – Guide to Industrial Control Systems Security


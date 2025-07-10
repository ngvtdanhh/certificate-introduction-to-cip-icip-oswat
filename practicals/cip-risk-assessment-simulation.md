# 🧪 CIP Risk Assessment Simulation – OT Environment

This practical outlines a simulated risk assessment for a **water treatment facility** using ICS/SCADA systems, incorporating threat modeling and security posture evaluation.

---

## 🏭 Scenario Overview

### 🎯 Target Environment:
- Water treatment plant (Municipal scale)
- ICS setup includes:
  - **PLC** controlling water pumps & valves
  - **SCADA** system managing chemical dosing
  - **HMI** for real-time monitoring
  - Remote access enabled via VPN

---

## 📌 Step 1: Asset Identification

| Asset                   | Type     | Criticality |
|------------------------|----------|-------------|
| Pump Controller (PLC)  | Hardware | High        |
| SCADA Workstation      | Software | High        |
| Operator HMI           | Software | Medium      |
| Remote VPN Appliance   | Network  | High        |
| Engineering Laptop     | Host     | Medium      |

---

## 📌 Step 2: Threat Modeling (STRIDE)

| Threat Category | Description                        | Affected Asset      |
|-----------------|------------------------------------|---------------------|
| Spoofing        | Fake credentials over VPN          | VPN Appliance       |
| Tampering       | Alter chemical dosing via PLC      | SCADA/PLC           |
| Repudiation     | Lack of audit trail in HMI         | HMI                 |
| Information     | Packet sniffing (Modbus insecure)  | SCADA ↔ PLC         |
| Denial          | DDoS on remote access              | VPN Appliance       |
| Elevation       | Privilege escalation via USB drop  | Engineering Laptop  |

---

## ⚠️ Step 3: Vulnerability Discovery

### ✅ Findings:

- 🔓 **Modbus Protocol** – Unencrypted & unauthenticated
- 💻 **Default Credentials** – Found on HMI interface
- 🧪 **USB Port Active** – No endpoint security on engineering laptop
- 🌍 **Public VPN Exposure** – No geo-IP restrictions

---

## 🔐 Step 4: Recommendations

| Area               | Recommendation |
|--------------------|----------------|
| SCADA ↔ PLC Comm.  | Implement secure Modbus proxy or VPN tunneling |
| Authentication     | Enforce MFA for remote VPN users |
| Logging & Auditing | Centralized syslog for HMI and SCADA |
| USB Protection     | Disable USB ports or use device control agent |
| Network Segmentation | Apply DMZ between IT and OT networks |

---

## 📘 Tools Simulated

- `GRASSMARLIN` for ICS network mapping
- `Wireshark` to identify Modbus packets
- `Nmap` with NSE scripts for PLC fingerprinting
- Basic STRIDE modeling using Microsoft Threat Modeling Tool

---

## 📊 Risk Score Summary (FAIR-based)

| Threat                         | Likelihood | Impact | Risk Level |
|--------------------------------|------------|--------|------------|
| PLC Overwrite (Modbus)         | High       | High   | 🔴 Critical |
| VPN Brute Force (No MFA)       | Medium     | High   | 🟠 High     |
| USB Malware (Insider Vector)   | Medium     | Medium | 🟡 Medium   |

---

## 🎓 Learning Outcome

This simulation demonstrates how even **legacy, low-complexity ICS networks** can be exposed to **modern cyber threats** if basic segmentation, logging, and protocol hardening aren’t implemented.

---

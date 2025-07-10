# 🏭 Introduction to Critical Infrastructure Protection (CIP) – ICIP OSWAT

![Course](https://img.shields.io/badge/OSWAT-ICIP%20Certified-brightgreen?style=flat-square&logo=fortinet)
![Status](https://img.shields.io/badge/Status-Completed-blue?style=flat-square&logo=verizon)
![Focus](https://img.shields.io/badge/Focus-ICS%20Security-orange?style=flat-square&logo=siemens)
![Type](https://img.shields.io/badge/Type-Self--Study-informational?style=flat-square&logo=openaccess)
![Author](https://img.shields.io/badge/Maintainer-Thành%20Danh-blueviolet?style=flat-square&logo=github)

This repository contains all my learning notes, demo labs, practicals, screenshots, and certificate for the course **"Introduction to CIP (Critical Infrastructure Protection)"** by ICIP – OSWAT.

---

## 📚 Course Notes

All notes are written in Markdown, covering technical and policy-based aspects of ICS and CIP:

- 🧭 [`cip-overview.md`](./notes/cip-overview.md) – Introduction, scope, and sectors of CIP  
- ⚙️ [`ics-components.md`](./notes/ics-components.md) – PLCs, RTUs, HMIs, and control hierarchy  
- 🚨 [`threat-landscape.md`](./notes/threat-landscape.md) – Real-world ICS threat actors and APTs  
- 🛡️ [`policy-and-compliance.md`](./notes/policy-and-compliance.md) – NERC CIP, ISO 27019, and legal mandates  
- 🎯 [`attack-scenarios.md`](./notes/attack-scenarios.md) – Example attacks on ICS: logic bombs, ransomware, DNP3 spoofing  

---

## 💻 Demo Labs

These simulated hands-on exercises help reinforce understanding:

- 🌐 [`network-segmentation-lab.md`](./demo/network-segmentation-lab.md) – IT/OT segmentation using `iptables` and subnets  
- 🧪 [`scada-vuln-analysis.md`](./demo/scada-vuln-analysis.md) – Assessing SCADA exposures (weak auth, default creds, cleartext)

---

## 🧠 Practicals

- 📊 [`cip-risk-assessment-simulation.md`](./practicals/cip-risk-assessment-simulation.md) – Impact-based risk rating on ICS targets  
- 🐍 [`scada_log_anomaly.py`](./practicals/scada_log_anomaly.py) – Basic anomaly detection using SCADA log patterns

---

## 📸 Screenshots

| Section                | Screenshot                                |
|------------------------|-------------------------------------------|
| 🧱 Course Introduction  | ![](./screenshots/IcIp-course-1.png)      |
| ⚙️ ICS Foundations      | ![](./screenshots/IcIp-course-2.png)      |
| 📘 Course Completion    | ![](./screenshots/IcIp-course-review.png) |

---

## 🎓 Certificate

- 📜 [`cert/introduction_to_cip.png`](./cert/cert/introduction_to_cip.png)

---

## 📝 Course Review: ICIP OSWAT – Introduction to CIP

This course delivers a robust introduction to securing critical infrastructure systems (ICS/SCADA/OT) through practical and policy-focused content.

✅ **What I Liked**  
- Realistic ICS examples (RTUs, PLCs, attack paths)  
- Legal + governance integration (NERC, ISA, ISO)  
- Clear demos and modular approach

📌 **Suggestions**  
- Expand more on OT ransomware case studies  
- Include mini CTF or hands-on tool use (e.g., Snort, Wireshark)

---

## 🤝 Code of Conduct

We strive to foster an inclusive and respectful learning environment.  
See [`CODE_OF_CONDUCT.md`](./CODE_OF_CONDUCT.md)

---

## ✍️ Author

**Thành Danh** – Pentester & Cybersecurity Researcher  
GitHub: [@ngvtdanhh](https://github.com/ngvtdanhh)  
Email: ngvu.thdanh@gmail.com

---

## 📄 License

This project is licensed under the **GNU AGPL v3.0**.  
See [`LICENSE`](./LICENSE) for details.

© 2025 ngvtdanhh. All rights reserved.
ork.md`](./notes/cip-controls-framework.md) – NERC CIP, ISO, and other frameworks

---

## 🧪 Demo Labs

- ⚙️ [`asset-inventory-lab.md`](./demo/asset-inventory-lab.md) – Simulated ICS asset discovery
- 🌐 [`network-segmentation-lab.md`](./demo/network-segmentation-lab.md) – IT/OT VLAN segmentation with `iptables`

---

## 💻 Practicals

- 🧠 [`scada_log_anomaly.py`](./practicals/scada_log_anomaly.py) – Anomaly detection in simulated SCADA logs

---

## 🧭 Security Operations Strategy

- 🚨 [`incident-escalation-framework.md`](./strategy/incident-escalation-framework.md) – Response ladder for ICS/CIP environment
- 🛡️ [`ics-hardening-principles.md`](./strategy/ics-hardening-principles.md) – System hardening, patching, and physical security
- 🔄 [`redundancy-and-resilience.md`](./strategy/redundancy-and-resilience.md) – Fault tolerance & industrial backups

---

## 📸 Screenshots

| Description             | Screenshot                                      |
|-------------------------|-------------------------------------------------|
| 🧩 Course Modules        | ![](./screenshots/IcIp-course-1.png)            |
| 🏗️ CIP Foundations       | ![](./screenshots/IcIp-course-2.png)            |
| ✅ Course Conclusion     | ![](./screenshots/IcIp-course-review.png)       |

---

## 🎓 Certificate

- 📜 [`certificate-introduction-to-cip.pdf`](./cert/certificate-introduction-to-cip.pdf)

---

## 📝 Course Review: Introduction to CIP – ICIP OSWAT

This course serves as a strong primer for anyone interested in the **protection of industrial control systems**. It blends policy, governance, and technical models into a well-structured format.

✅ **What I Liked**:
- Clear separation between IT and OT threat models
- Focus on real-world ICS examples (PLC, HMI, SCADA)
- Hands-on examples encouraged contextual thinking

📌 **To Improve**:
- Would benefit from lab challenges (e.g., identifying misconfigurations)
- Could include more modern threats like ransomware in OT

---

## 🚧 Ongoing Work

Additional deep-dive demos and strategy docs (e.g., `ICS Forensics`) are in progress.

---

## 🤝 Code of Conduct

We commit to respectful, inclusive communication.  
See [`CODE_OF_CONDUCT.md`](./CODE_OF_CONDUCT.md)

---

## ✍️ Author

**Thành Danh** – Pentester & Cybersecurity Research  

- GitHub: [@ngvtdanhh](https://github.com/ngvtdanhh)  
- Email: ngvu.thdanh@gmail.com

---

## 📄 License

This project is licensed under the **GNU AGPL v3.0**.  
See [`LICENSE`](./LICENSE) for details.

© 2025 ngvtdanhh. All rights reserved.

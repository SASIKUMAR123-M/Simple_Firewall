🛡️ Simple Firewall (Rule-Based)

This project is a **simple firewall simulation** implemented in Python.  
It checks **incoming traffic (IP + Port)** against a predefined list of rules and decides whether to **block** or **allow** the packet.  

---

## 🚀 Features
- Block traffic from specific **IP addresses**.
- Block traffic on specific **ports** (e.g., SSH, Telnet).
- Allow all other traffic by default.
- Simple **command-line based simulation** (no root/admin needed).
- Beginner-friendly project to understand firewall rule checking.

---

## 📖 How It Works
The program:
1. Defines lists of **blocked IPs** and **blocked ports**.
2. Accepts user input for a packet’s IP address and port number.
3. Checks if the packet matches blocked rules.
4. Prints whether the traffic is **Blocked** or **Allowed**.

---

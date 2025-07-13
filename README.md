COMPANY: CODTECH IT SOLUTIONS

NAME: SACHINDORE P

INTERN ID: CT06DG1111

DOMAIN: CYBER SECURITY AND ETHICAL HACKING

DURATION: 6 WEEKS

MENTOR: NEELA SANTHOSH


# 🔐 Task 1: File Integrity Checker

## 📄 Description
This Python script detects file tampering by calculating and comparing the **SHA-256 hash values** of a file before and after any potential modification.

It's a simple but powerful tool to ensure **file integrity**—especially useful in cybersecurity to verify that critical files haven’t been altered by attackers or corrupted in transit.

---

## 📂 Folder Structure

**├── task1_file_integrity_checker/**
   **├── checker.py**
   **├── test_files/**
     **├── sample.txt**
   **└── README.md**

---

## 🧑‍💻 Prerequisites

- ✅ Python 3.x installed
- ✅ No external libraries required (uses built-in `hashlib`)

---

## ▶️ How to Run the Script

1. Open a terminal or command prompt.
2. Navigate to the folder:
   ```bash
   cd task1_file_integrity_checker

---   

## ⚙️ How It Works

* The script calculates and stores the SHA-256 hash of sample.txt.

* can manually modify the file (e.g., change its content in a text editor).

* then re-calculates the hash and compares the two.

* they match ➡️ file is intact.

* they don’t ➡️ file has been modified or tampered with.

---

## 🧪 Sample Output

```
Original Hash: d7a8fbb307d7809469ca9abcb0082e4f...
🔄 Modify the file (if you want) and press Enter to recheck...
New Hash: d7a8fbb307d7809469ca9abcb0082e4f...
✅ File is intact.

```

<img width="1050" height="260" alt="Image" src="https://github.com/user-attachments/assets/ea63e44a-a1e0-4236-824d-bc3469898096" />

## OR if modified: 

```
Original Hash: d7a8fbb307d7809469ca9abcb0082e4f...
New Hash: b26bc43c05f849a5cd03fe4aa760c244...
⚠️ File has been modified!
```

---

## 📘 Notes

* You can test with any file by changing the **file_path** variable in **checker.py.**

* Consider adding logging or GUI in future versions.

* SHA-256 is cryptographically strong and ideal for integrity checks.

---


## 📌 Credits

Internship: CODTECH – Cyber Security Internship
Developer: Sachin Dore P
Task: File Integrity Monitoring using Hashing (Task 1/4)

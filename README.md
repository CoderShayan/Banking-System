# Banking System

A simple interactive banking demo implemented in Python. The single script for the project is:
- [Banking-Sys.py](Banking-Sys.py)

Features
- Create new accounts with minimum opening balance and a 4-digit PIN.
- Show account details.
- Deposit and withdraw funds with basic validation.
- Transfer funds between accounts requiring PIN and recipient name match.
- In-memory account storage via a dictionary (no persistence).

Quick start

Requirements:
- Python 3.10+ (uses `match` statement)

Run:
```sh
python3 Banking-Sys.py
```

Usage
- Follow on-screen menu prompts.
- Options correspond to these functions in the script:
  - Open account: [`Banking-Sys.createAccount`](Banking-Sys.py)
  - Show details: [`Banking-Sys.showAccountDetails`](Banking-Sys.py)
  - Deposit: [`Banking-Sys.depositAmount`](Banking-Sys.py)
  - Withdraw: [`Banking-Sys.withDrawAmount`](Banking-Sys.py)
  - Transfer: [`Banking-Sys.amountTransfer`](Banking-Sys.py)

Notes & limitations
- Accounts are stored in memory only (`account_list`), so all data is lost when the program exits.
- No input sanitization beyond basic checks; use with caution.
- PINs and account data are not encrypted.
- Intended as a learning/demo project, not production-ready.

Developer pointers
- Core data structure: `account_list` in [Banking-Sys.py](Banking-Sys.py).
- Helper functions: [`Banking-Sys.getAccountDetail`](Banking-Sys.py), [`Banking-Sys.updateBal`](Banking-Sys.py), [`Banking-Sys.saveAccountDetail`](Banking-Sys.py).

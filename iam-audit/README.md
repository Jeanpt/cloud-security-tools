# IAM Misconfiguration Audit

This script checks IAM users in an AWS account for:

- ❌ Missing MFA
- ⚠️ Old or unused access keys
- ⚠️ Admin permissions via attached policies

## 🛠️ Usage
```bash
pip install boto3
aws configure
python iam_audit.py

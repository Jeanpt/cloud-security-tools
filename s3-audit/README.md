# 🪣 S3 Misconfiguration Scanner

This tool audits AWS S3 buckets for common misconfigurations:

- ❌ Public access via bucket policy
- ❌ Missing default encryption
- ❌ Logging not enabled

## ✅ Usage

```bash
pip install boto3
aws configure
python s3_audit.py

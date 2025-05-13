import boto3
from datetime import datetime, timezone

def check_users():
    iam = boto3.client('iam')
    users = iam.list_users()['Users']
    print(f"\nFound {len(users)} IAM users.\n")

    for user in users:
        username = user['UserName']
        print(f"User: {username}")

        # Check for MFA
        mfa_devices = iam.list_mfa_devices(UserName=username)['MFADevices']
        if not mfa_devices:
            print("  ❌ No MFA")

        # Check for access keys
        keys = iam.list_access_keys(UserName=username)['AccessKeyMetadata']
        for key in keys:
            key_age = (datetime.now(timezone.utc) - key['CreateDate']).days
            if key_age > 90:
                print(f"  ⚠️ Access key {key['AccessKeyId']} is {key_age} days old")

        # Check for admin privileges
        attached_policies = iam.list_attached_user_policies(UserName=username)['AttachedPolicies']
        for policy in attached_policies:
            if "Admin" in policy['PolicyName']:
                print(f"  ⚠️ Attached admin policy: {policy['PolicyName']}")

        print()

if __name__ == "__main__":
    print("🔍 Auditing AWS IAM users...")
    check_users()

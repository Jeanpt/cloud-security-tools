import boto3

# Define dangerous ports to flag
DANGEROUS_PORTS = [22, 3389, 3306, 5432, 80, 443]

def check_sg():
    ec2 = boto3.client('ec2')
    sgs = ec2.describe_security_groups()['SecurityGroups']

    for sg in sgs:
        print(f"\n🔍 Security Group: {sg['GroupName']} ({sg['GroupId']})")
        for rule in sg.get('IpPermissions', []):
            from_port = rule.get('FromPort')
            to_port = rule.get('ToPort')
            ip_ranges = rule.get('IpRanges', [])

            for ip_range in ip_ranges:
                cidr = ip_range.get('CidrIp')
                if cidr == '0.0.0.0/0':
                    if from_port in DANGEROUS_PORTS:
                        print(f"  ❌ Open port {from_port} to 0.0.0.0/0")
                    else:
                        print(f"  ⚠️ Open port {from_port} to 0.0.0.0/0 (non-standard)")

if __name__ == "__main__":
    print("🌐 Scanning AWS Security Groups for open ports...")
    check_sg()

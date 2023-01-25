import dns.resolver
import argparse
import os
import time
import datetime

# Our DNS Lookup Function
def dns_lookup(hostname, duration, substring):
    while True:
        try:
            answers_list = [dns_record.to_text() for dns_record in dns.resolver.resolve(hostname, "TXT").rrset]
            for answer in answers_list:
                if substring in answer:
                    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), answer)
        except:
            pass
        time.sleep(duration)

# Allowing For Duration To Be Argument
parser = argparse.ArgumentParser()
parser.add_argument("--duration", type=int, help="how many X seconds to check for record",
                    nargs='?', default=5, const=5)
parser.add_argument("--hostname",type=str, help="what hostname to check?",
                    nargs='?', default=os.environ.get('DNS_HOSTNAME'))
parser.add_argument("--substring",type=str, help="what subtring to check?",
                    nargs='?', default=os.environ.get('DNS_SUBSTRING'))
args = parser.parse_args()

# Bring in env vars
hostname = args.hostname
duration = args.duration
substring = args.substring

if not all([hostname, substring]):
    print("Missing hostname or substring, please add as env var or as args to the script.")
else:
    dns_lookup(hostname, duration, substring)
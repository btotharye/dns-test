# dns-test
This is a repo to outline a resolution for a test given for the following information below.

## Problem
Imagine that we need to monitor a domain name for the presence of a special DNS
TXT record and use that information to trigger printing a message to STDOUT. The
requirements specify that the solution will have to run on an existing EC2 instance.

## Task
Implement a script/process/service that can:
1. Monitor DNS TXT records of a specified $hostname every $d seconds.
2. Print date and time every time $substring is detected in any TXT record.
3. Feel free to use whatever tools, languages, libraries, frameworks, etc that
you think are needed / you are most comfortable with.
4. Create a git repo including all required files plus a README.md which
documents the commands needed to run (hypothetically) deploy your
project.
5. Test variable values:
a. $hostname = devopswithbrian.com”
b. $d = 5 seconds
c. $substring = “google-site”

# Using This Repo
So this is a pretty basic setup, it uses Poetry to set everything up and manage dependencies.

1. Install the package with `pip install .` from the root dir.
3. Please note this script expects either `DNS_HOSTNAME` and `DNS_SUBSTRING` to be setup as env vars before hand in your shell, etc where you are running this or you can add them to the below command via adding in `--hostname whatever.com` and `--substring google-site`.  It uses the env var if nothing is supplied from the cli.  

    You can also supply a different duration via `--duration 10` if you want a shorter or longer seconds check, by default it will use 5 seconds.

4. To run the script `python3 dns_test/dns_query.py` from the root of the project.  As stated above if you don't already have the env vars setup you would run `poetry run python3 dns_test/dns_query.py --hostname whatever.com --substring google-site` for the check with the default 5 second duration.

In future development of this, this would be best served even as a python package then can just be installed that way and not have to be cloned down, etc.


# Ways of Running This
So there are a few ways you could actually run this, I would recommend the best way would be as a AWS Lambda or even Kubernetes cron job potentially.  If you went the AWS Lambda route you could also write the data/events to a cloudwatch event or logs.  

Otherwise if you wanted to say run this on a ec2 box for some reason then you would want to pip install it on the bring up of the ec2 instance and could set this up as a supervisor job or cron job, etc.
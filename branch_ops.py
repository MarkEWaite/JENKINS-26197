#! /usr/bin/python

import subprocess

#----------------------------------------------------------------------------

def checkout_master_branch():
    subprocess.check_call(["git", "checkout", "-f", "master"])

#----------------------------------------------------------------------------

def list_a_branch():
    "List one existing remote branch name that starts with 'branch', return None otherwise"
    branch_ref = subprocess.check_output(["git", "ls-remote", "--heads", "origin", "branch*"]).split()
    prefix = "refs/heads/"
    if len(branch_ref) > 1:
        if branch_ref[1].startswith(prefix):
            return branch_ref[1][len(prefix):]
    return None

#----------------------------------------------------------------------------

def remove_a_branch():
    branch_name = list_a_branch()
    if not branch_name:
        return
    subprocess.check_call(["git", "branch", "-D", branch_name])
    subprocess.check_call(["git", "push", "origin", ":" + branch_name])

#----------------------------------------------------------------------------

def create_and_push_a_branch():
    import time
    import random
    import string
    suffix = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for i in range(2))
    branch_name = "branch-" + time.strftime("%Y-%m-%d-%H-%M-%S") + "-" + suffix
    print "Branch", branch_name

#----------------------------------------------------------------------------

def branch_ops():
    # checkout_master_branch()
    # remove_a_branch()
    create_and_push_a_branch()

#----------------------------------------------------------------------------

if __name__ == "__main__":
    branch_ops()
    exit(0)

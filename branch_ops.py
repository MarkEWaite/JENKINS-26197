#! /usr/bin/python

import random
import string
import subprocess
import time

#----------------------------------------------------------------------------

def checkout_master_branch():
    "Checkout master branch (force) and clean working directory"
    subprocess.check_call(["git", "checkout", "-f", "master"])
    subprocess.check_call(["git", "clean", "-xffd"])

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
    "Remove one remote branch"
    branch_name = list_a_branch()
    if not branch_name:
        return
    subprocess.check_call(["git", "branch", "-D", branch_name])
    subprocess.check_call(["git", "push", "origin", ":" + branch_name])

#----------------------------------------------------------------------------

def create_and_push_a_branch():
    "Create a branch and push it to origin"
    suffix = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for i in range(2))
    branch_name = "branch-" + time.strftime("%Y-%m-%d-%H-%M-%S") + "-" + suffix
    subprocess.check_call(["git", "checkout", "-b", branch_name, "origin/master"])
    with open(branch_name, "w") as branch_file:
        branch_file.write("Created on branch " + branch_name)
    subprocess.check_call(["git", "add", branch_name])
    subprocess.check_call(["git", "commit", "-m", "Added " + branch_name + " file"])
    subprocess.check_call(["git", "push", "origin", "--set-upstream", branch_name])

#----------------------------------------------------------------------------

def branch_ops():
    checkout_master_branch()
    remove_a_branch()
    create_and_push_a_branch()
    checkout_master_branch()

#----------------------------------------------------------------------------

if __name__ == "__main__":
    branch_ops()
    exit(0)

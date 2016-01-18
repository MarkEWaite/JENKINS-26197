[JENKINS-32435](https://issues.jenkins-ci.org/browse/JENKINS-32435) - Env vars unusable in "Branches to Build"

This change is intentionally on the branch named "jenkins".  That is
assumed to be the value of the environment variable "LOGNAME" in many
Jenkins installations (default on Debian and Ubuntu and Red Hat).

When a test job clones this repo and reads this README.md, it will expect
to find the string JENKINS-32435 in the file.

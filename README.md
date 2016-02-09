[JENKINS-32840](https://issues.jenkins-ci.org/browse/JENKINS-32840) - subdir fails to push

The bug report claims that tags don't push if a checkout is done to
a subdirectory.

This test uses the JENKINS-32840 branch for verification.  Verification
tests run on different Jenkins servers, all monitoring the same GitHub
repository.

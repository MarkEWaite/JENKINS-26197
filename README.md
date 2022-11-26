## [JENKINS-70158](https://issues.jenkins.io/browse/JENKINS-70158) - Ignore committer strategy is not honored in git plugin 4.14.0

The "Ignore committer" strategy is not honored in git plugin 4.14.0 when it was honored in git plugin 4.13.0.

Steps to reproduce:

* Install git plugin 4.13.0
* Create a new multibranch Pipeline with the repository URL: https://github.com/MarkEWaite/JENKINS-26197.git
* Commit to a branch in the repository and confirm the branch is detected and built successfully
* Add the strategy "Ignore committer" strategy to the multibranch Pipeline with your own git email address ignored
* Commit to the branch again and confirm that the change is detected for the branch but the job is not built (git plugin 4.13.0)
* Install git plugin 4.14.0
* Commit to the branch again and confirm that the change is detected for the branch and the job is built (git plugin 4.14.0)

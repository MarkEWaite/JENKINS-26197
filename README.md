[JENKINS-42971](https://issues.jenkins-ci.org/browse/JENKINS-42971) - Lightweight checkout does not expand environment variables

Pipeline from SCM does not expand parameters or environment variables 

Steps to reproduce:

* Create a new Pipeline with a String Parameter  `PIPELINE_BRANCH`
* In the pipeline definition ; Select "Pipeline Script from SCM"
* Enter the repository URL: https://github.com/MarkEWaite/JENKINS-26197.git
* In branch to build, enter the parameter  : `${PIPELINE_BRANCH}` with a default value `ENKINS-42971`
* Run the job with the default value of the `PIPELINE_BRANCH` parameter
 
An error is thrown :
```
hudson.plugins.git.GitException: Command "git fetch --tags --progress origin 
  +refs/heads/${PIPELINE_BRANCH}:refs/remotes/origin/${PIPELINE_BRANCH} --prune" 
  returned status code 128:
```

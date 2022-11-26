#!groovy

/* Only keep the 10 most recent builds. */
// properties([[$class: 'BuildDiscarderProperty',
//                 strategy: [$class: 'LogRotator', numToKeepStr: '10']]])

def branch='JENKINS-70158'

node('!windows && !cloud') {
  stage('Checkout') {
    checkout([$class: 'GitSCM',
        branches: [[name: branch]],
        extensions: [
            [$class: 'CloneOption', honorRefspec: true, noTags: true],
            [$class: 'LocalBranch', localBranch: branch]],
        gitTool: scm.gitTool,
        userRemoteConfigs: [[refspec: "+refs/heads/${branch}:refs/remotes/origin/${branch}",
                             url: 'https://github.com/MarkEWaite/JENKINS-26197']]]
    )
  }
  stage('Verify') {
    sh "ant info"
    status = sh returnStatus: true, script: "ant info | grep -q No.automatic.build.triggered.for.${branch}"
    if (status != 0) {
        if ( currentBuild.getBuildCauses('jenkins.branch.BranchIndexingCause') ) {
            echo '**** Build was triggered  by branch indexing ****'
            currentBuild.description = "Triggered by branch indexing"
        } else if (! currentBuild.getBuildCauses('hudson.model.Cause$UserIdCause') ) {
            unstable('**** Build was triggered ****')
            currentBuild.description = 'Triggered and not started by a user'
        }
        print "User cause is ${currentBuild.getBuildCauses('hudson.model.Cause$UserIdCause')}"
        print "SCM trigger cause is ${currentBuild.getBuildCauses('hudson.triggers.SCMTrigger$SCMTriggerCause')}"
        print "SCM trigger cause is ${currentBuild.getBuildCauses('hudson.triggers.SCMTrigger$SCMTriggerCause')}"
        print "Branch indexing trigger cause is ${currentBuild.getBuildCauses('jenkins.branch.BranchIndexingCause')}"
    }
  }
}

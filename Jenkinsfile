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
    sh "ant info | grep Scheduled.build.for.branch:.${branch}'
  }
}

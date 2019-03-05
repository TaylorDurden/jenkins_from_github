pipeline {
  agent {
    node {
      label 'dev'
    }

  }
  stages {
    stage('git') {
      steps {
        dir(path: '/home/wolverine/jenkins_from_github') {
          git(url: 'git@github.com:TaylorDurden/jenkins_from_github.git', credentialsId: '3118a854497d64e27f38cbdb1a4ec2b268ef97fd')
        }

      }
    }
    stage('build') {
      steps {
        sh 'sudo -H pip install -r requirements.txt'
      }
    }
    stage('run') {
      steps {
        sh 'python app.py'
      }
    }
  }
}
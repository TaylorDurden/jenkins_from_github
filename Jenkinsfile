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
          git(url: 'git@github.com:TaylorDurden/jenkins_from_github.git', credentialsId: 'eb7f056e3c72325e233d8db271053cae82f36de6')
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
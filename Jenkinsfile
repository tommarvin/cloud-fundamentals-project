pipeline{
        agent any
        stages{
            stage('Make Directory'){
                steps{
                    sh "mkdir ~/jenkins-cloud-fundamentals"
                }
            }
            stage('Make Files'){
                steps{
                    sh "touch ~/jenkins-cloudfundamentals1/file1 ~/jenkins-cloudfundamentals2/file2"
                }
            }
        }
}

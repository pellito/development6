node {
	stage ('Build') {
	
	}
	stage ('Test') {
        sh "python3 Dev6BDjango/siteMain/manage.py test crime1.tests"
	}
	stage ('Deploy') {
	    echo "${JENKINS_HOME}"
        if (currentBuild.result == 'SUCCESS') {
            sh "cp ${JENKINS_HOME} /var/www/dev66"
        }
    }
}

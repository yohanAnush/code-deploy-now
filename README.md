DeployNow: Integrated AWS CodeDeploy Module.
============================================

What is DeployNow?
------------------
DeployNow is a Python module designed to make deployments with AWS CodeDeploy easy. By providing a couple of parameters, you can be on your way to deploy an application via CodeDeploy.

How to install DeployNow
------------------------
DeployNow is compatible both Python 2 and Python3.
```sh
# For Python 2
$ cd /tmp
$ git clone https://github.com/AnushkaYohan/code-deploy-now.git
$ cd code-deploy-now
$ python setup.py install

# For Python 3, only the last line changes.
$ python3 setup.py install
```

How to use DeployNow
--------------------
DeployNow expects a couple of parameters to identify attributes related to a CodeDeploy application.

| Commandline Argument | Shortform Argument | Description |
| --------------------- |--- | ------------------------------------------------------ |
| --application-name | -a | Name of the CodeDeploy application |
| --deployment-group | -d | Deployment group to which the deployment will be pushed |
| --deployment-config | -c | Deployment configuration name |
| --source | -s | Path to source directory |
| --bucket | -b | Name of the S3 bucket to store the artifact |
| --prefix | -p | Additional S3 prefix to structure the artifact storage |
| --region | -r | AWS region code |
| --ignore-progress | Not available in short form | Setting this flag will make the application quit after deployment is created |

Running DeployNow to create a revision and deploy it using AWS CodeDeploy.
```sh
$ deploynow -a 'sample-app-codedeploy' 
            -s '/etc/usr/sampleapp' 
            -b 'packages-bucket' 
            -p 'path/to/package/' 
            -d 'sample-app-deployment-group' 
            -c 'CodeDeployDefault.AllAtOnce'
            -r 'eu-west-1'
```

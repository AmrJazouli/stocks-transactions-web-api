# Stocks Transactions API Web Application

## Notes

I have chosen to create a Flask web application in Python and use a MongoDB as database (develop reasons) 

The goal of this repository is to showcase a uniform way to deploy a Flask API in Python using IaC (Infrastructure as Code) and different deployment approaches such as:

1. Web App in Azure
2. Virtual Machines with Vagrant and Ansible
3. Docker-Compose
4. Kubernetes/Minikube

## Structure

Here is the structure of the repository:

```

.github/
api/
  templates/
  app.py
  Dockerfile
  README.md
  requirements.txt
  test_functionalities.py
docker-compose/
  docker-compose.yml
  README.md
iac-vargrant-ansible/
  main.yml
  README.md
  Vagrantfile
images/
k8s/
  deployment.yml
  README.md
  service.yml
README.md

```




    
  










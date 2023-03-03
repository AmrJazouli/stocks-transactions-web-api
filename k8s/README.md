## Docker orchestration using Kubernetes:

For Kubernetes, I used minikube cluster to run kubernetes locally and configured kubectl.

Below is screenshot of installation and set up of Minikube and kubectl:

![Web Page18](../images/Kubernetes/MinikubeSetup.png)

Then, I deployed the application and exposed the service with the following commands as shown below:

![Web Page19](../images/Kubernetes/ServiceRunning.png)

```
kubectl apply -f deployment.yml
```

```
kubectl apply -f service.yml
```

The web server is running on :

![Web Page20](../images/Kubernetes/ServiceRunningPort64164.png)

To check the deployment and pods on the Kubernetes dashboard, I typed the following:

```
minikube dashboard
```

![Web Page21](../images/Kubernetes/minikubedashboard_1.png)

![Web Page22](../images/Kubernetes/minikubedashboard_3.png)

Then, we connect to the pod of mongodb, to query the database and check simultaneously if insertion, update and delete operations are performed successfully while we interact with the api through the browser webpage.

![Web Page23](../images/Kubernetes/New/dboperations.png)
# django-postgresql-kubernetes
This is a Django, with database PostgreSQL Docker/ Kubernetes cluster
# django_kubernetes
Django application deployed with [Kubernetes](https://kubernetes.io)
## To run the web app locally
<p>First install the dependencies</p>

```
    pip install -r requirements.txt
```

<p> To start the django app locally </p>

```python
  python manage.py runserver
```
<p>Go to url</p>

http://localhost:8000
  
Django-app deployment in kubernetes
## To start the docker-container use command>

```docker
docker-compose up
```
<p>The app starts at port number 8020</p>

http://localhost:8020

## Use Kubernetes to deploy enviornmental variables used by web-app
```kubernetes
kubectl apply -f ./kubernetes/secret.yml
kubectl create -f ./kubernetes/config_map.yml
```
## Use Kubernetes to create persistan-volume, persistant-volume-claim deployment and service resources for database
```kubernetes
kubectl apply -f ./kubernetes/postgre/component_postgre.yml
```

## To check the status of pods:
```kubernetes
kubectl get pod
```
## To check the service
```kubernetes
kubectl get service
```
## Use Kubernetes to create deployment and service resources for django app
```kubernetes
kubectl apply -f ./kubernetes/django/component_postgre.yml
```
## Running the app using an external ip address
```kubernetes
minikube get service django-rest-service --url
```
## Running the app using ingress
<p>start the ingress controller</p>

```kubernetes
minikube addons enable ingress
```
## To view the ingress resources

```kubernetes
minikube get pods -n ingress-nginx
```
<p>makesure to map the host name to minikube IP in /etc/host file</p>
<p>In this case that shall be</p>
<p>minikube_IP django.postgre.com</p>
    
## Use Kubernetes to create ingress resources for django app
```kubernetes
kubectl apply -f ./kubernetes/ingress_service.yml
```

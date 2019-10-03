### Kubernetes

Website			kubernetes.io
Type			Cluster management software and container orchestration
Repository	 	https://github.com/kubernetes/kubernetes 



-What is Kubernetes 

- Kubernetes (commonly stylized as K8s)
- Kubernetes is an open-source system for automating deployment, scaling, and management of containerized applications.
- It groups containers that make up an application into logical units for easy management and discovery.
- Platform for automating deployment, scaling, and operations of application containers across clusters of hosts
- Originally developed by Google in 2014, now maintained by Cloud Native Computing Foundation(CNCF)
- Implemented in Go.
- Works with a range of container tools, including Docker.
- help to shape the evolution of technologies that are container-packaged, dynamically-scheduled and microservices-oriented



# Architecture 

sites : 
1. https://thenewstack.io/kubernetes-an-overview/
2. https://x-team.com/blog/introduction-kubernetes-architecture/
3. https://medium.com/@abhaydiwan/kubernetes-introduction-and-twelve-key-features-cdfe8a1f2d21
4. https://medium.com/jorgeacetozi/kubernetes-master-components-etcd-api-server-controller-manager-and-scheduler-3a0179fc8186

- Kubernetes follows the master-slave architecture

I] Kubernetes Master
	- Kubernetes Masters act as the control unit for a cluster.
	- Manages its workload and directs communication across the system.
	- A cluster needs 1 or more Masters to run

- API Server
	- The API server provides endpoints for developers and operators to interact with the cluster
	- Key component and serves the Kubernetes API using JSON over HTTP, provides both the internal and external
	  interface to Kubernetes.
	- Processes and validates REST requests and updates state of the API objects in etcd

- Controller Manager
	- Controller Manager manages controllers that work to bring Kubernetes to the desired state.
	- This include scheduling controllers and Replication controllers. 
	- Is the process in which the core Kubernetes controllers like DaemonSet Controller and Replication Controller 	 run.
	- It communicate with the API server to create, update and delete the resources they manage (pods, service
	  endpoints, etc.)

- Scheduler
	- Scheduler is responsible for actually doing the resource management of pods based.
	- Process that actually assigns workloads to specifc nodes in the cluster is the scheduler.
	- It manages on which node an unscheduled pod should run on based on resource availability

- etcd
	- To store confguration data that can be accessed by each of the nodes in cluster.
	- Stores cluster state and confguration in the form of key-value

-----------

# II] Kubernetes Nodes
	- The Node, also known as Worker or Minion
	- Kubernetes Nodes actually run the workloads(containers).
	- Kubernetes needs at least 1 node to run.
	- In small setups, the node and the master can be the same.

- Kubelet
	- Kubelet is an agent that runs on each node that receives the instructions from the Master about what to do 
	  on the node.
	- Is responsible for the running state of each node.
	- Ensures all containers on the node are healthy.
	- Takes cares of Containers(POD) lifecycle management.

- cAdvisor
	- cAdvisor collects telemetry about the pods running on the nodes such as network, CPU and RAM usage.
	- Is the agent that monitors and gathers resource usage and performance metrics of containers on each node.

- Kube-Proxy
	- Is an implementation of a network proxy and a load balancer for the pods running on the node
	- It supports the service abstraction along with other networking operation.
	- It is responsible for routing trafc to the appropriate container based on IP and port number of the incoming request.
	- It uses linux ip tables in backend to perform its operation.
 
- POD
	- POD is collection of one or more container(s).
	- smallest deplyable unit
	- Small group of tightly coupled containers
	- shared network and data volumes
	- routable IP address
	- The containers in the pod share resources such as storage, CPU and RAM
	- Network resources are connected to the pod
	- Containers is the lowest level of microservice which holds the running application, libs or their dependancies.

- Plugin Network
	- Plugin Network uses a driver to create an overlay network between Kubernetes Nodes.
	- This allows pods to communicate seamlessly between nodes on a Kubernetes Cluster.
	- eg. Flannel (Flannel is a very simple overlay network that satisfies the Kubernetes requirements. Many people have reported success with Flannel and Kubernetes.) or weave-net or calico.


# Services 

https://medium.com/google-cloud/kubernetes-nodeport-vs-loadbalancer-vs-ingress-when-should-i-use-what-922f010849e0

- services provide permanent virtual IP and DNS name
- It is an exposure of pods, replica set, controllers etc. on a port through kube-proxy
- Types of Services:
	- ClusterIP
	- NodePort
	- ExternalIP
	- ExternalName

1. ClusterIP
	- A ClusterIP service is the default Kubernetes service.
	- Service gets virtual IP which only used to communicate within the cluster.
	- It gives you a service inside your cluster that other apps inside your cluster can access. There is no external access.

2. NodePort
	- Derives properties of ClusterIP.
	- Makes a service accessible from outside the cluster
	- In addition, it gets port from range 30000-32767 mapped with all nodes in cluster 




# Tools 

1. Kubeadm
	- A administration tool for setting up and managing kubernetes clusters.  Kubeadm runs on the Kubernetes host.

2. Kubectl
	- The command line interface for interacting with a Kubernetes clusters




# Kubernetes Features 

1. Automatic binpacking
Automatically places containers based on their resource requirements and other constraints, while not sacrificing availability. Mix critical and best-effort workloads in order to drive up utilization and save even more resources.

2. Horizontal scaling
Scale your application up and down with a simple command, with a UI, or automatically based on CPU usage.

3. Automated rollouts and rollbacks
Kubernetes progressively rolls out changes to your application or its configuration, while monitoring application health to ensure it doesn't kill all your instances at the same time. If something goes wrong, Kubernetes will rollback the change for you. Take advantage of a growing ecosystem of deployment solutions.

4. Storage orchestration
Automatically mount the storage system of your choice, whether from local storage, a public cloud provider such as GCP or AWS, or a network storage system such as NFS, iSCSI, Gluster, Ceph, Cinder, or Flocker.

5. Self-healing
Restarts containers that fail, replaces and reschedules containers when nodes die, kills containers that don't respond to your user-defined health check, and doesn't advertise them to clients until they are ready to serve.

6. Service discovery and load balancing
No need to modify your application to use an unfamiliar service discovery mechanism. Kubernetes gives containers their own IP addresses and a single DNS name for a set of containers, and can load-balance across them.

7. Secret and configuration management
Deploy and update secrets and application configuration without rebuilding your image and without exposing secrets in your stack configuration.

8. Batch execution
In addition to services, Kubernetes can manage your batch and CI workloads, replacing containers that fail, if desired.




# Creating a single master cluster with kubeadm 

Sites : 
1. https://kubernetes.io/docs/setup/independent/create-cluster-kubeadm/
2. https://kubernetes.io/docs/tasks/tools/install-kubeadm/

# Steps : 

- Installing kubeadm, kubelet and kubectl

1. vim /etc/yum.repos.d/kubernetes.repo
	- Add this
	[kubernetes]
	name=Kubernetes
	baseurl=https://packages.cloud.google.com/yum/repos/kubernetes-el7-x86_64
	enabled=1
	gpgcheck=1
	repo_gpgcheck=1
	gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg

2. setenforce 0
3. yum install -y kubelet kubeadm kubectl
4. systemctl enable kubelet && systemctl start kubelet

5.  vim /etc/sysctl.d/k8s.conf
	- Add this
	net.bridge.bridge-nf-call-ip6tables = 1
	net.bridge.bridge-nf-call-iptables = 1

6. sysctl --system


# Demo Using Ansible


- /etc/hosts  on both master and node
1.  10.10.X.X 	Master
2.  10.10.X.X	Node

- Set Hostname

```
	- hostnamectl set-hostname Master
	- hostnamectl set-hostname Node
```

- Using Ansible

1. yum install ansible
2. git clone https://github.com/kairen/kubeadm-ansible.git
3. cd kubeadm-ansible/
4. vim hosts.ini
	- Edit Master and Node IP address
5. ansible-playbook site.yaml 
6. ansible-playbook site.yaml --limit @/root/kubeadm-ansible/site.retry

- Master 

1. To set up the kubernetes master.
```
    - kubeadm init --service-cidr 10.96.0.0/12 --kubernetes-version v1.11.0 --pod-network-cidr "10.244.0.0/16"  --token b0f7b8.8d1767876297d85c --apiserver-advertise-address 10.10.121.222
```
2. mkdir -p $HOME/.kube
3. sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
4. sudo chown $(id -u):$(id -g) $HOME/.kube/config
5. Deploy a pod network to the cluster (flannel)
	- kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml

- Node

1. You can now join any number of machines by running the following on each node
```
	- kubeadm join 10.10.X.222:6443 --token b0f7b8.8d1767876297d85c --discovery-token-ca-cert-hash sha256:f4a0f891e5e5afde7c273d38b8762c2915e29a8ee807fadeea5382bc8c90407b
```
								OR
```
	- kubeadm join 10.10.X.222:6443 --token b0f7b8.8d1767876297d85c --discovery-token-unsafe-skip-ca-verification
```


 Demo Using Manual Commands 


-- Kubernetes Installation on both Master and Node

1. Configure Hosts
	- vim /etc/hosts
		10.0.15.10      k8s-master
		10.0.15.21      node01
		10.0.15.22      node02

2. Disable SELinux
	- setenforce 0
	- sed -i --follow-symlinks 's/SELINUX=enforcing/SELINUX=disabled/g' /etc/sysconfig/selinux

3.  Enable br_netfilter Kernel Module
	- modprobe br_netfilter
	- echo '1' > /proc/sys/net/bridge/bridge-nf-call-iptables

4. Disable SWAP
	- swapoff -a
	- edit vim /etc/fstab
		Comment the swap line UUID

5. Install Docker CE
	- yum install -y yum-utils device-mapper-persistent-data lvm2
	- yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
	- yum install -y docker-ce

6. Install Kubernetes
	- cat <<EOF > /etc/yum.repos.d/kubernetes.repo
	  [kubernetes]
	  name=Kubernetes
	  baseurl=https://packages.cloud.google.com/yum/repos/kubernetes-el7-x86_64
	  enabled=1
	  gpgcheck=1
	  repo_gpgcheck=1
	  gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg
	          https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
	  EOF

	- yum install -y kubelet kubeadm kubectl
	- sudo reboot
	- systemctl start docker && systemctl enable docker
	- systemctl start kubelet && systemctl enable kubelet

7. Change the cgroup-driver
	- Check docker cgroup using the docker info command.
		- docker info | grep -i cgroup
	- sed -i 's/cgroup-driver=systemd/cgroup-driver=cgroupfs/g' /etc/systemd/system/kubelet.service.d/10-kubeadm.conf
	- systemctl daemon-reload
	- systemctl restart kubelet


-------


1. Creating Kubernetes Cluster 

	1. To set up the kubernetes master
		- kubeadm init --apiserver-advertise-address=10.0.15.10 --pod-network-cidr=10.244.0.0/16

Note : 
	--apiserver-advertise-address = determines which IP address Kubernetes should advertise its API server on.
	--pod-network-cidr = specify the range of IP addresses for the pod network. 
						 We're using the 'flannel' virtual network. 
						 If you want to use another pod network such as weave-net or calico, change the range IP address.

	2. Now in order to use Kubernetes
		- mkdir -p $HOME/.kube
		- sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
		- sudo chown $(id -u):$(id -g) $HOME/.kube/config

	3. Deploy the flannel network to the kubernetes cluster
		- kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml

	- kubectl cluster-info
	- kubectl get nodes 
	- kubectl get pods --all-namespaces
	- kubectl delete node name




2. Joining Node to Cluster 

	1. This command is used to get join node information if u missed
	```
		- kubeadm token create --print-join-command
	```
	2. You can now join any number of machines by running the following on each node
	```
	   - kubeadm join 10.10.121.222:6443 --token b0f7b8.8d1767876297d85c --discovery-token-ca-cert-hash sha256:f4a0f891e5e5afde7c273d38b8762c2915e29a8ee807fadeea5382bc8c90407b
	```

								OR
```
	- kubeadm join 10.10.121.222:6443 --token b0f7b8.8d1767876297d85c --discovery-token-unsafe-skip-ca-verification

	
	- kubectl get nodes 
	- kubectl delete node name
```
?4zQc}syHy5XN[he


3. Creating Deployment 

sites :
	1. https://www.howtoforge.com/tutorial/centos-kubernetes-docker-cluster/  (command) 
	2. https://kubernetes.io/docs/concepts/workloads/controllers/deployment/  (file)

Steps : 

	1. Login to the 'k8s-master' server and create new deployment named 'nginx' 
```
		- kubectl create deployment nginx --image=nginx
						OR
		- kubectl create -f <file-name>  					

		file-name = nginx-deployment.yaml		

			apiVersion: apps/v1
			kind: Deployment
			metadata:
			  name: nginx-deployment
			  labels:
			    app: nginx
			spec:
			  replicas: 3
			  selector:
			    matchLabels:
			      app: nginx
			  template:
			    metadata:
			      labels:
			        app: nginx
			    spec:
			      containers:
			      - name: nginx
			        image: nginx:1.7.9
			        ports:
			        - containerPort: 80
```

	2. To see details of the 'nginx' deployment sepcification
```
	-  kubectl describe deployment nginx
	- kubectl get deployments
	- kubectl get deployment <deployment-name> -o yaml
	- kubectl delete deployment <deployment_name>

	- kubectl get pods
	- kubectl get pods --all-namespaces
	- kubectl get pods -o wide (along with IP address)
	- kubectl delete pod <pod_name>

```
			
4. Creating Service 

sites : 
	1. https://www.howtoforge.com/tutorial/centos-kubernetes-docker-cluster/	(command) 
	2. https://kubernetes.io/docs/concepts/services-networking/service/			(file)

Steps :

	1. Next, expose the nginx pod accessible via the internet. And we need to create new service NodePort for this.
```
		- kubectl create service nodeport nginx --tcp=80:80
```

	2. From the 'k8s-master' server run the curl command below.
```
		- curl node-name : service-port
```

	3. The Nginx Pod has now been deployed under the Kubernetes cluster and it's accessible via the internet.
		http://node-ip:service-port/
```
	- kubectl get svc
	- kubectl describe services/<service-name>
```



5. Scaling Current Deployment

sites : 
	1. https://kubernetes.io/docs/tutorials/kubernetes-basics/scale/scale-interactive/
	2. https://cloud.google.com/kubernetes-engine/docs/how-to/scaling-apps

Steps :
	
	1. scale the Deployment to 4 replicas. Followed by the deployment type, name and desired number of instances:
```
		- kubectl scale deployments/<deployment-name> --replicas=4
```
	2. Scale Down
```
		- kubectl scale deployments/<deployment-name> --replicas=2
```

	3. check docker container scaling or not. Remove 1 docker container and it will get scaled
```
	- docker rm container-id
	- kubectl get deployments
	- kubectl get pods -o wide
	- kubectl describe deployments/<deployment-name>
```
	


6. Autoscaling Deployments

sites : 
	1. https://cloud.google.com/kubernetes-engine/docs/how-to/scaling-apps

steps : 
	
	1. autoscale Deployments based on CPU utilization of Pods using kubectl autoscale
		- kubectl autoscale deployment <deployment-name> --max 6 --min 4 --cpu-percent 50
	
	2. To see a specific HorizontalPodAutoscaler object in your cluster
		- kubectl get hpa [HPA_NAME]
	
	3. To see the HorizontalPodAutoscaler configuration
		- kubectl get hpa [HPA_NAME] -o yaml
	
	4. To see a detailed description of a specific HorizontalPodAutoscaler object in the cluster
		- kubectl describe hpa [HPA_NAME]

	5. To delete a HorizontalPodAutoscaler object
		- kubectl delete hpa [HPA_NAME]


7. Web UI (Dashboard)

sites : 
	
	1. https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/#deploying-the-dashboard-ui
	2. https://github.com/kubernetes/dashboard/wiki/Accessing-Dashboard---1.7.X-and-above
	3. https://stackoverflow.com/questions/46664104/how-to-sign-in-kubernetes-dashboard

steps :

	1. Deploying the Dashboard UI
		- kubectl create -f https://raw.githubusercontent.com/kubernetes/dashboard/master/src/deploy/recommended/kubernetes-dashboard.yaml

	2. Accessing the Dashboard UI
		- kubectl proxy
OR

	3. Edit kubernetes-dashboard service.
		- kubectl -n kube-system get service kubernetes-dashboard
		- kubectl -n kube-system edit service kubernetes-dashboard
			- Change type: ClusterIP to type: NodePort and save file

	4. Create kube-dashboard-access.yaml file
		- vim kube-dashboard-access.yaml
		
			apiVersion: rbac.authorization.k8s.io/v1beta1
			kind: ClusterRoleBinding
			metadata:
			  name: kubernetes-dashboard
			  labels:
			    k8s-app: kubernetes-dashboard
			roleRef:
			  apiGroup: rbac.authorization.k8s.io
			  kind: ClusterRole
			  name: cluster-admin
			subjects:
			- kind: ServiceAccount
			  name: kubernetes-dashboard
			  namespace: kube-system

		- kubectl create -f kube-dashboard-access.yaml
	
	5. Run on
		- kubectl -n kube-system get service kubernetes-dashboard 
		- https://<master-ip>:<service-port>
	
	6, Sign in with Token 
```
	- kubectl -n kube-system get secret
 	- kubectl -n kube-system describe secret <name>  			(kubernetes-dashboard-token-7vwwp)
```




-- CaaS --

Sites : 
1. https://www.1and1.com/digitalguide/server/know-how/caas-container-as-a-service-service-comparison/
2. https://www.gartner.com/doc/3666417/container-services-public-cloud
3. https://blog.docker.com/2016/02/containers-as-a-service-caas/

- Containers as a service (CaaS) is a cloud service that allows software developers to upload, organize, run, scale, manage and stop containers by using a provider's API calls or a web portal interface. As is the case with most cloud services, users pay only for the CaaS resources – such as compute instances, load balancing and scheduling capabilities -- that they use.Containers as a service (CaaS) is a cloud service that allows software developers to upload, organize, run, scale, manage and stop containers by using a provider's API calls or a web portal interface. As is the case with most cloud services, users pay only for the CaaS resources – such as compute instances, load balancing and scheduling capabilities -- that they use.

- Containers as a service (CaaS) is a cloud service model that allows users to manage and deploy containers, applications and clusters through container-based virtualization. CaaS is highly useful to IT departments and developers in building secure and scalable containerized applications.

- Containers are more specifcally used when your application architecture is more or less inspired by Micro-Services. With more services, comes more containers and to manage them all you need an orchestrate, Container Orchestator.

- At the heart of a Containers-as-a-Service system is the container orchestration platform, which is designed to handle operations such as container deployment and cluster management. 

- CaaS provides an easy way to set up a container cluster. Orchestration, which essentially automates key IT functions, is an essential quality of CaaS technology. 

- Container as a Service (CaaS): Is a form of container-based virtualization in which container engines, orchestration and the underlying compute resources are delivered to users as a service from a cloud provider.

- Google Container Engine(GKE), AWS (ECS), Azure (ACS) and Pivotal (PKS) are some examples of CaaS.

- Which orchestrator is used within the CaaS framework has a direct influence on the functions made available to cloud service users. The market for container-based virtualization is currently dominated by three orchestration tools: Docker Swarm, Kubernetes, and Mesosphere DC/OS.

-  Important Features of CIaaS
1. Image Registry
2. Scheduling, Orchestration and Cluster Management
3. Autoscaling
4. API, CLI and GUI
5. Stateful Application Support
6. Monitoring and Log Management

- CaaS doesn’t force a workflow on you – but instead gives you a framework to better manage your application delivery. That means the CaaS requirements need to be flexible enough to cover the environment and the one you’ll have tomorrow:
1. Provide tooling for both dev and IT ops
2. Provide tooling across the entire app lifecycle
3. Any operating system
4. Any language stack and tooling
5. Any infrastructure
6. Open APIs and extensibility
7. Broad ecosystem support

- When choosing a CaaS service for use in enterprise, users should take the following questions into consideration:
1. Which orchestration tools are available?
2. Which file formats do container applications support?
3. Is it possible to operate multi-container applications?
4. How are the clusters managed when operating a container?
5. What networks and storage functions are supported?
6. Does the provider issue a private registry for container images?
7. How well is the container runtime environment integrated with other cloud services?
8. Which billing models are available?
--------


kubeadm join 10.10.121.222:6443 --token b0f7b8.8d1767876297d85c --discovery-token-ca-cert-hash sha256:17ccb41872fb3a405df498b3d10acdd2fc47787ee541b58f87e8e71933134c65


kubeadm join 10.10.121.222:6443 --token b0f7b8.8d1767876297d85c --discovery-token-ca-cert-hash sha256:90bec7aa30b4b0fe5709bbb2cc46f49fa356b18eb381e52726b89d2ea59358b1




kubeadm join 10.10.121.222:6443 --token b0f7b8.8d1767876297d85c --discovery-token-ca-cert-hash sha256:bdc0c2d38048641916d9b49bc5795eaa9129ebe704722c23832c9d8edb147a1c




https://www.server-world.info/en/note?os=CentOS_7&p=kubernetes
https://www.server-world.info/en/note?os=CentOS_7&p=kubernetes&f=3
https://www.server-world.info/en/note?os=CentOS_7&p=docker&f=1
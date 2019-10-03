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


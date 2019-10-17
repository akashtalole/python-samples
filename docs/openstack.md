## Opensatck

- What is OpenStack?
OpenStack is a cloud management system that controls large pools of compute, storage, and networking resources throughout a datacenter, all managed through a dashboard that gives administrators control while empowering their users to provision resources through a web interface.


What is Neutron?
- Networking project in Openstack
- Setup virtual network infrastructure
- Switching and Routing
- Also specialised virtual network functions like VPNaaS, FWaaS, LBaaS
- Flexibility through plugins, drivers andd agents

Openstack Networking Components
- neutron server(neutron-server and neutron-*-plugin)
- plugin agent(neutron-*-agent)
- DHCP agent(neutron-dhcp-agent)
- L3 agent(neutron-l3-agent)


VLAN is a logical slice of physical network.
OS nw is also broadcast domain
os nw provides logical space isolation 

segmenatation
separation of virtual network is known as segmenatation

Segmenatation method includes
- VLANs
- VXLAN
- GRE
- Network Namespaces
- Openflow Rules

https://docs.openstack.org/liberty/networking-guide/intro-os-networking-overview.html#openstack-networking-concepts

## OpenStack Networking concepts

To configure rich network topologies, you can create and configure networks and subnets and instruct other OpenStack services like Compute to attach virtual devices to ports on these networks. OpenStack Compute is a prominent consumer of OpenStack Networking to provide connectivity for its instances. In particular, OpenStack Networking supports each tenant having multiple private networks and enables tenants to choose their own IP addressing scheme, even if those IP addresses overlap with those that other tenants use. There are two types of network, tenant and provider networks. It is possible to share any of these types of networks among tenants as part of the network creation process.

- Tenant networks
Users create tenant networks for connectivity within projects. By default, they are fully isolated and are not shared with other projects. OpenStack Networking supports the following types of network isolation and overlay technologies.

- Flat
All instances reside on the same network, which can also be shared with the hosts. No VLAN tagging or other network segregation takes place.

- VLAN
Networking allows users to create multiple provider or tenant networks using VLAN IDs (802.1Q tagged) that correspond to VLANs present in the physical network. This allows instances to communicate with each other across the environment. They can also communicate with dedicated servers, firewalls, load balancers, and other networking infrastructure on the same layer 2 VLAN.

- GRE and VXLAN
VXLAN and GRE are encapsulation protocols that create overlay networks to activate and control communication between compute instances. A Networking router is required to allow traffic to flow outside of the GRE or VXLAN tenant network. A router is also required to connect directly-connected tenant networks with external networks, including the Internet. The router provides the ability to connect to instances directly from an external network using floating IP addresses.

- Provider networks
The OpenStack administrator creates provider networks. These networks map to existing physical networks in the data center. Useful network types in this category are flat (untagged) and VLAN (802.1Q tagged).

To configure rich network topologies, you can create and configure networks and subnets and other OpenStack services like Compute will request to be connected to these networks by requesting virtual ports. In particular, Networking supports each tenant having multiple private networks and enables tenants to choose their own IP addressing scheme, even if those IP addresses overlap with those that other tenants use.

- Subnets
A block of IP addresses and associated configuration state. This is also known as the native IPAM (IP Address Management) provided by the networking service for both tenant and provider networks. Subnets are used to allocate IP addresses when new ports are created on a network.

- Ports
A port is a connection point for attaching a single device, such as the NIC of a virtual server, to a virtual network. The port also describes the associated network configuration, such as the MAC and IP addresses to be used on that port.

- Routers
This is a logical component that forwards data packets between networks. It also provides L3 and NAT forwarding to provide external network access for VMs on tenant networks. Required by certain plug-ins only.

- Security groups
A security group acts as a virtual firewall for your compute instances to control inbound and outbound traffic. Security groups act at the port level, not the subnet level. Therefore, each port in a subnet could be assigned to a different set of security groups. If you don’t specify a particular group at launch time, the instance is automatically assigned to the default security group for that network.

Security groups and security group rules give administrators and tenants the ability to specify the type of traffic and direction (ingress/egress) that is allowed to pass through a port. A security group is a container for security group rules. When a port is created, it is associated with a security group. If a security group is not specified, the port is associated with a ‘default’ security group. By default, this group drops all ingress traffic and allows all egress. Rules can be added to this group in order to change the behavior.

- Extensions
The OpenStack Networking service is extensible. Extensions serve two purposes: they allow the introduction of new features in the API without requiring a version change and they allow the introduction of vendor specific niche functionality. Applications can programmatically list available extensions by performing a GET on the /extensions URI. Note that this is a versioned request; that is, an extension available in one API version might not be available in another.


Service and component hierarchy
Server
Overview and concepts
Provides API, manages database, etc.
Plug-ins
Overview and concepts
Manages agents
Agents
Overview and concepts
Provides layer 2/3 connectivity to instances
Handles physical-virtual network transition
Handles metadata, etc.
Layer 2 (Ethernet and Switching)
Linux Bridge
Overview and concepts
OVS
Overview and concepts
Layer 3 (IP and Routing)
L3
Overview and concepts
DHCP
Overview and concepts
Miscellaneous
Metadata
Overview and concepts

Services
Routing services
- VPNaaS
The Virtual Private Network-as-a-Service (VPNaaS) is a neutron extension that introduces the VPN feature set.

- LbaaS
The Load-Balancer-as-a-Service (LBaaS) API provisions and configures load balancers. The reference implementation is based on the HAProxy software load balancer.

- FwaaS
The Firewall-as-a-Service (FWaaS) API is an experimental API that enables early adopters and vendors to test their networking implementations.


## QA

2. Describe OpenStack.
Most multinational organizations define OpenStack as the future of Cloud Computing. The Internet and large volumes of data together have instigated the purpose of cloud computing, and OpenStack is one such platform to create and handle massive groups of virtual machines through a Graphical User Interface. It is a set of efficient software tools to manage private and public cloud computing platforms.
Openstack is free, open-source software and works similar to Linux.

3. Explain the benefits of using OpenStack Cloud.
Openstack is useful in developing any software-as-a-service (SAAS) applications, for new developments or to improve existing solutions.

Can serve as a strong foundation to deliver self-service storage to IT users.
Can deliver on-demand objective or block storage with higher scalability and easy-to-handle storage at lower costs.
Most enterprises can save bigger on licensing fees by switching virtual machines running on VMware to OpenStack.

4. What are the key components of OpenStack?
- Horizon: the only GUI in OpenStack; the first component administrators see and get an idea of the current operations in the cloud.

- Nova: chief computing engine to handle multiple virtual machines and computing tasks

- Swift: reliable and robust storage system for files and objects helping developers to refer to a unique identifier and Openstack decides where to store the info.

- Cinder: similar to traditional computer storage system, it is a block storage system in OpenStack for accessing files at faster speed.

- Neutron: ensures efficient connectivity between components during deployment.

- Keystone: a central identity list of all OpenStack cloud users and provides various mapping techniques to access methods against Keystone.

- Glance: image service provider where images are the virtual copies of hard disks. Allows using the images as templates during deployment of new instances.

- Ceilometer: component providing billings services and other telemetry services to cloud users. Maintains an account of component system usage by each user.

- Heat (Orchestration Engine): Allows developers to orchestrate/illustrate and store the cloud application requirements and resources needed in a file, thereby maintaining the cloud infrastructure.

5. What storage types are allowed by OpenStack Compute?
OpenStack Cloud Operating system supports two types of storage:
Persistent Storage: Persistent and independent of any particular instance, created by users. This further includes three storages:

- Object storage: to access binary objects through the REST API.
- Block storage: offers access-to-block storage devices by affixing volumes their current VM instances.
- Shared File System storage: provides a set of services to manage multiple files together for storage and exchange with multiple users at one time.
- Ephemeral Storage: Referring to a single instance. As the name suggests, these storage options are temporary and short-lived and disappear once the VM is terminated.Interested in a high-paying career in Cloud Computing?

6. Define ‘users,’ ‘role’ and ‘tenant’ in OpenStack.
Users can be members of multiple projects
Tenant is a group of users and an alternative term for Project/accounts where projects are organizational units in cloud processing
Role is the position to which a user is mapped (the authorization level). Roles are usually assigned to project-user duos.

7. Define Identity Service in OpenStack.
Keystone is the most important and preferred Identity Service in OpenStack and executes the complete OpenStack Identity API. The Keystone Identity Service is responsible for user management and service catalog. In user management, it tracks users and their permissions while Service Catalog offers a list of services available with their API. The former provides authentication credential details of users, tenants and roles.
Internal services like Token and Policy are also part of Keystone Identity

8. Define the Networking Managers in OpenStack Cloud.
Flat Network Manager: This places all VMs on a single network utilizing the same subnet and bridge as created by the administrator. Thus, all VMs share the same network that can be interconnected and are known to have Flat Network Manager.

Flat DHCP Network Manager: Much similar to the above except that the IP addresses to VM are assigned via DHCP (Dynamic Host Configuration Protocol).
VLAN: Unlike the single network concept, VLAN facilitates more secure and separate network to VMs. It has a physical switch to offer separate virtual network and separate IP range and bridge for each tenant. This is indeed most preferable choice for multi-tenant/project environment.

9. Name the commands used to pause and un-pause(resume) an instance
$ novaunpause INSTANCE_NAME
$ nova pause INSTANCE_NAME

10. List the storage locations for VM images in OpenStack
• OpenStack Object Storage
• Filesystem
• S3
• HTTP
• RBD or Rados Block Device
• GridFSMaster Openstack  from industry experts.

11. What is Token?
Token is a type of authentication similar to password-based validation. A token gets generated once the user inserts the credentials and authenticates as a Keystone user. The token can then be used to access OpenStack services without any revalidation. It is interesting to note that a token is active for a limited period and must be renewed after regular intervals.
To create a token, users first need to authenticate their Keystone credentials.

12. What is OpenStack Python SDK?
Python SDK (Software Development Kit) helps users to write applications for performing automation tasks in Python by calling Python objects. It provides a platform to work with multiple OpenStack services at one place. It consists of language bindings to access OpenStack clouds, complete API reference, easy interaction with REST API and sample code for initial applications.

13. Describe the function of Filter Scheduler.
The Filter Scheduler facilitates filtering and weighting to notify where a new instance can be created. It supports working with Compute Nodes. Filter Scheduler firstly creates an unfiltered dictionary of hosts and then filter them using related properties and makes the final selection of hosts for the number of instances as needed.

14. Define the Networking option in OpenStack.
AvalabilityZoneFilter: filters hosts by their availability zone.
CapacityFilter: filtering based on volume host’s capacity consumption
DifferentBackendFilter: Scheduling volumes to a different back-end
DriverFilter: filters based on ‘filter function’ and ‘metrics’
InstanceLocalityFilter
JSONFIlter
RetryFilter: Filter the previously attempted hosts
SameBackendFilterMost in-depth, industry-led curriculum in Openstack.
Check the Openstack Course Details now!

15. List down the Networking hardware in OpenStack.
Networks
Routers
Subnets
Ports Vendor Plugins

16. Define Hypervisor
For all cloud computing paltforms, Hypervisor is a term to define virtual machine monitor (VMM) including hardware, software and firmware components running on a virtual machine. Host machine is the one having hypervisor with one or more virtual machines.
OpenStack Compute allows multiple hypervisors. There are functionalities to choose one among them for a specific purpose.

17. List down the type of Hypervisors supported by OpenStack.
KVM (Kernel-based Virtual machine)
LXC: Linux Containers having Linux-based VMs
QEMU: Quick EMUlator used for development purposes
UML: User Mode Linux used for development purposes
VMware vSphere: VMware-based Linux and Windows via vCenter server connection.
Hyper-V: Server virtualization with Microsoft’s Hyper-V

18. Explain in brief the modular architecture of OpenStack.
The three important components of OpenStack modular architecture are:

OpenStack Compute: For managing large networks on the virtual machine
Image Service: The delivery service provides discovery and registration for virtual disk images
OpenStack Object Storage: A storage system that provides support for both block storage and object storage

19. What command manages floating IP addresses in OpenStack
nova floating-ip-*

20. Define bare-metal node.
Bare-metal node grants access to control bare-metal driver that handles the provisioning of OpenStack Compute physical hardware utilizing the standard cloud APIs and tools like Heat. It is generally used for single tenant clouds like high-performance cluster computing. For using the bare-metal driver, a network interface must be created with the bare-metal node inserted into it. Afterwards, users can launch an instance from the node. Users can also list and delete bare-metal nodes by removing the associated network instances

21. List down the components of OpenStack Compute
Nova (Compute) Cloud comprises following components:

- API server
- Message Queue (Rabbit-MQ Server)
- Compute Workers (Nova-Compute)
- Network controller (Nova-Network)
- Volume Worker
- Scheduler

22. Define the role of API Server.
It provides an interface for the external world to interact with the cloud infrastructure.

23. List the commands to generate Key pairs.
ssh-keygen
cd .ssh
nova keypair-add –pub_key id_rsa.pub mykey

24. Define Flavor
Flavors are virtual hardware templates present in OpenStack, which define the memory sizes of RAM, hard disk, etc. Flavors illustrate a number of parameters like ID, Name, Memory_MB, Disk and others, giving a choice of Virtual Machine to the user just like having a physical server. OpenStack dashboard also allows users to modify a flavor by deleting the existing one and creating a new with the similar name and parameters.

25. How to create a user in OpenStack?
sudo nova-manage user create user-name

26. How to assign a project/tenant to a user?
By using the command sudo nova-manage user create user-name

27. Can we see the list of roles and associated IDs in OpenStack environment?
Yes, by using keystone role-list

https://assafmuller.com/2015/04/15/distributed-virtual-routing-overview-and-eastwest-routing/
https://assafmuller.com/2014/05/02/introduction-to-neutron/
https://assafmuller.files.wordpress.com/2014/05/neutron.pdf

## OVS vs Linux Bridge: What Are They?

- OVS
Open vSwitch (OVS) is an open source multilayer virtual switch. It usually operates as a software-based network switch or as the control stack for dedicated switching hardware. Designed to enable effective network automation via programmatic extensions, OVS also supports standard management interfaces and protocols, including NetFlow, sFlow, CLI, IPFIX, RSPAN, LACP, 802.1ag. In addition, Open vSwitch can support transparent distribution across multiple physical servers. This function is similar to the proprietary virtual switch solutions such as the VMware vSphere Distributed Switch (vDS). In short, OVS is used with hypervisors to interconnect virtual machines within a host and virtual machines between different hosts across networks.

- Linux Bridge
As mentioned above, the Open vSwitch is a multilayer virtual switch, which can work as a Layer 2 or Layer 3 switch. While the Linux bridge only behaves like a Layer 2 switch. Usually, Linux bridge is placed between two separate groups of computers that communicate with each other, but it communicates much more with one of the computer groups. It consists of four major components, including a set of network ports, a control plane, a forwarding plane, and MAS learning database. With these components, Linux bridge can be used for forwarding packets on routers, on gateways, or between VMs and network namespaces on a host. What’s more, it also supports STP, VLAN filter, and multicast snooping.


## OVS vs Linux Bridge: Advantages And Disadvantages of OVS

* Compared to Linux Bridge, there are several advantages of Open vSwitch:

Easier for network management – With the Open vSwitch, it is convenient for the administrator to manage and monitor the network status and data flow in the cloud environment.
Support more tunnel protocols – OVS supports GRE, VXLAN, IPsec, etc. However, Linux Bridge only supports GRE tunnel.
Incorporated in SDN – Open vSwitch is incorporated in software-defined networking (SDN) that it can be driven by using an OpenStack plug-in or directly from an SDN Controller, such as OpenDaylight.

* Despite these advantages, Open vSwitch have some challenges:

Lacks stability – Open vSwitch has some stability problems such as Kernetl panics, ovs-switched segfaults, and data corruption.
Complex operation – Open vSwitch itself is a complex solution, which owns so many functions. It is hard to learn, install and operate.
OVS vs Linux Bridge: Strengths And Limitations of Linux Bridge

* Linux Bridge is still popular mainly for the following reasons:

Stable and reliable – Linux Bridge has been used for years, its stability and reliability are approved.
Easy for installation – Linux Bridge is a part of standard Linux installation and there are no additional packages to install or learn.
Convenient for troubleshooting – Linux Bridge itself is a simple solution that its operation is simpler than that of Open vSwitch. It is convenient for troubleshooting.

* However, there are some limitations:

Fewer functions – Linux Bridge doesn’t support the Neutron DVR, the newer and more scalable VXLAN model, and some other functions.
Fewer supporters – Many enterprises wanted to ensure that there was an open model for integrating their services into OpenStack. However, Linux Bridge can’t ensure the demand, so it has fewer users than that of Open vSwitch.

* OVS vs Linux Bridge: Who’s the Winner?
OVS vs Linux Bridge: who’s the winner? Actually, both of them are good network solutions and each has its appropriate usage scenarios. OVS has more functions in centralized management and control. Linux Bridge has good stability that is suitable for Large-scale network deployments. All in all, The winner is the right one that meets your demands.


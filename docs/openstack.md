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
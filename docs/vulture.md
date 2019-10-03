Product Sheet
A new generation WAF to protect Web applications

*An Innovative architecture
Vulture speeds up and protects your web applications. Based on a FreeBSD operating system and an optimized version of Apache, its clustered architecture offers unique scalability.
Control access and block attacks before they reach your web applications
Manage user authentication with SSO and identity federation
High-performance Redis cache and HTTP/2 support provide Vulture with unparalleled performance

*Big Data and machine learning
Vulture is based on a MongoDB engine.
No need to invest in a SIEM to benefit from real-time log analysis, alerting or anomaly detection capabilities
Vulture enriches logs in real time: Geolocation, IP address reputation and identification of malicious users
Need to increase the treatment capacity? Add nodes in the cluster! Vulture works natively in active/active, supports the virtual addresses CARP as well as the distribution of load

*Authentication and Web SSO
Vulture can authenticate users based on SQL, MongoDB, LDAP/Active Directory directories, Kerberos ... It supports Kerberos seamless authentication and spreads Kerberos tickets to protected applications. Vulture can also distribute OAuth2 tokens.
Web SSO has never been easier: Vulture scans the protected application and automatically identifies the necessary fields for the SSO Web.

Virtual Patching
Vulture relies on the modSecurity engine to block Web attacks through positive and negative security models. Integrate Acunetix, QualysGuard or Zed Attack Proxy vulnerability scans reports and automatically generate a protection profile that eliminates discovered vulnerabilities!

Anomaly Detection & Behavioral Analysis
Vulture learns the classic behavior of users during a learning period. Using "Support Vector Machines" (SVM-RBF) algorithms, Vulture creates its own anomaly detection model. Any attempt to intrude deviating from the usual behavior will be detected by these innovative algorithms.

New Interface, Behavioral Analysis, Virtual Patching, Web SSO
New HTTP/2.0 protocols Oauth2 Kerberos
Improved performance High availability Load balancing Cache, QoS, SSL acceleration


=============
Tech details
=============
=============
Introduction
=============
▪ Main risks according to OWASP
	> A1: Injection of commands
	> A2: Incorrect management of authentication and sessions
	> A3: Cross Site Scripting
	> A4: Unsafe direct references
	> A5: Incorrect security configuration
	> A6: Exposure of sensitive data
	> A7: Lack of access control at the functional level
	> A8: Cross Site Request Forgery
	> A9: Use of vulnerable components
	> A10: Redirection and forwarding not validated


▪ WAF does not replace developer's zeal
▪ ... but can reduce the risks of Top 10 OWASP
	> Encryption of communications
	> Validation of incoming requests
	> Control of outgoing data
	> Blocking known attacks (blacklist)
	> Blocking suspicious flows
		- Geolocation,
		- Reputation of the source IP
	> Blocking behavioral anomalies and zero days
		- whitelisting,
		- Machine learning

▪The Vulture project
	> Created in 2003, 14 years of application security expertise> Open Source
		- Licensed GPLv3: Management Interface
		- Licensed Apache2: Filtering Engine and Machine Learning Algorithms
▪ International deployments
	> More than 10 countries> 1,500 deployments in version 3 identified as of March 1, 2017
▪ Professional services operated by aDvens
	> Integration, Training> Support and Managed Services> Cloud Protection Services

=================
Network features
=================
Load-balancer Web
	• Vulture can spread the load across multiple web servers and maintain application sessions
Load-balancing IPv4/IPv6 network
	• Inbound traffic is distributed to all nodes in the cluster 
Virtual IPv4/IPv6 virtual addresses
	• If one node fails, the others take over
Firewall IPv4/IPv6 network 
	• Malicious IPs are blocked before they reach applications

▪ Vulture locates source IPs and analyzes their reputation
▪ It is possible to make filtering policies on these criteria
	> The blocking is done before processing the HTTP request

▪ Network logs can be viewed from the management interface
	> Quick and intuitive interface, possibility to save your search filters
	> Logs available: Firewall, WAF, access to applications, internal logs (API, system of
diagnostic, ...)
▪ Connectors for sending logs to a SIEM or external databases:
	Syslog, MongoDB and Elastic

=========================
Web Application Firewall
=========================
▪ Vulture uses an improved version of modSecurity
	> This version is more efficient and works in a cluster on all Nodes: The filtering decisions of a node are shared with the other nodes

▪ Vulture simplifies the use of a WAF
> Qualified and ready-to-use rules are integrated by default
	- Protection against protocol anomalies
	- Protection against session interception
	- Protection against Cross Site Request Forgery
	- Cookies security
> Automated integration of OWASP CRS rules (Open Source) and SLR (Commercial)
	- Automatic import and versioning of rule sets
	- Graphical interface to edit the rules
	- Assistant for writing rules

▪ Machine learning: In addition to rule-based filtering and reputation of the sources, Vulture proposes an approach based on pure mathematics:
	1. Learning and modeling of typical traffic
	2. Detection of "abnormal" requests

▪ In the end, the decision to block a request follows a process based on
multiple factors:
	> If suspicious geolocation => Increased risk score
	> If the reputation of the doubtful IP => Increase in the risk score
	> If Suspicious User-Agent => Increased Risk Score
	> If a WAF rule "match" => Increase in the risk score
	> If the machine learning "matche" => Increase in the risk score

▪ Vulture makes the decision to block when the risk score exceeds the tolerated threshold. The administrator decides on the sensitivity of the blocking.

Virtual Patching
▪ Helps protect only the fallible
	> Upload a vulnerability scan report Qualys, Acunetix or ZAP
	> Vulture generates the rules to correct the identified faults

========
Web SSO
========
▪Authenticate the user before they access the application
	> Digital certificate authentication
		- Via integrated PKI or thanks to existing certificates in the company
	> Authentication by login / password
		- LDAP, Active Directory, Kerberos, Radius, MongoDB, SQL ...
	> Transparent authentication
		- HTTP basic and Kerberos
	> Double factor authentication
		- Sending a token by SMS (authy.com) or email
	> Captcha system, responder OAuth2, ...
	> Self-service portal for loss and change of password

▪Spread identity to protected apps
	> HTML forms support, Javascript authentication, AJAX
	> Support of transparent methods "Basic" and Kerberos with spread of tokens
▪SSO Forward
	> Vulture "scans" protected applications and detects the information needed to propagate authentication


DISTRIBUTION MODES
PACKAGING AND SUPPORT

Packaging
▪Vulture is available free of charge as ISO
	> Registration required during installation
	> Support provided by the community or professional support aDvens

▪Vulture is available for sale
	> Physical appliances with guaranteed performances
	> Support provided by aDvens
▪Vulture is available "as-a-service"
	> Cloud secured by aDvens
	> Optional anti-DDOS protection
	> Customized service contract


=====================================================

AUTHENTICATION
Authenticate users and propagate their identity on web applications. Take advantage of Vulture features to set up an SSO without modifying your existing applications

SECURITY
Enable TLS, control user reputation, set up access control and block attacks (XSS, SQL Injection, Malware ...) before they reach your web applications

HIGH AVAILABILITY
Need to increase the treatment capacity? Add nodes to the cluster: Vulture runs natively as active / active and supports the CARP virtual addresses.

LOAD DISTRIBUTION
With HA-Proxy, vulture distributes incoming traffic to all nodes in the cluster. Vulture can then dispatch the traffic to a farm of Web servers.

CONTENT REWRITING
Vulture works in reverse-proxy, based on Apache. You can rewrite links, headers, content, compress pages, ...

ANOMALY DETECTION
Vulture integrates anomaly detection algorithms allowing the administrator to identify risky behaviors and create effective filtering policies


*Monitoring
	- General services status monitoring
	- system mon
	- network mon
	- users

*Diagnostic
	 to detect any problem inside a Vulture cluster

*Self-service portal

*OAuth2 responder
	can be used with any authentication backend of type MongoDB, SQL, and LDAP.

*Anomaly detection

Reporting 
	- Map

	    Application: Filter results by application (empty will use all applications).
	    Status code: Filter by request status code.
	    Reputation : Filter by reputation tags.

	- Access

	    Number of hits by status code (line chart)
	    HTTP code (pie chart)
	    HTTP methods (pie chart)
	    Browsers (pie chart)
	    Operating systems (pie chart)
	    Traffic per URL (data table)
	    Average bytes received per request (line chart)
	    Average bytes sent per request (line chart)
	    Average time elasped per request (line chart)

	- Security

	    Number of hits by status code (line chart)
	    Average score by status code (pie chart)
	    Distribution of blocked requests (radar chart)
	    Number of blocked requests (bar chart)
	    OWASP Top 10 requests (bar chart)
	    Reputation tags (pie chart)
	    IP list reputation (bar chart)

	- Packet Filter

	    Number of hits (line chart)
	    Source IP (pie chart)
	    Destination IP (radar chart)
	    Firewall actions (pie chart)
	    Requests per destination port (bar chart)

Cluster Management
	
    Add or remove nodes
    Switch a node from master to slave

Service Management
	
    ModSecurity URL settings
    Vulture global settings
    Log global settings
    Location settings
    DNS
    NTP
    SMTP
    SSH
    FAIL2BAN

PKI Management
	
    One self-signed ROOT CA
    One certificate associated to mongoDB and GUI apache httpd listeners

Users management

	Administrator 
	Application Manager 
	Security Manager 	
	System Manager

Reputation

	By default Vulture will download 55 databases from Internet and ingest them into Redis. This process runs every night in background (crontab).
	You can  add custom database
	A Vulture system process, loganalyzer, check in Vulture logs if any source IP address is known to have a bad reputation. This process will query redis for that. If a match is found, Vulture will modify the log entries to add the corresponding tags.
	Can block traffic based on IP source reputation.

Log Viewer
	
    Internal Vulture logs (GUI, Portal, process...).
    Internal Vulture diagnostic logs (updated every minute), see diagnostic.
    Packet filter logs, see pf.
    Apache Worker logs, see application.

    Query builder for Logs

    Available actions when you "right click" on a line of log
		Add IP to blacklist"
		Add whitelist/blacklist
		can build some ModSecurity Rules with data all the data of the selected log line
		Find related rules -find all rules related to the log entry. This way you can edit / delete it.

Repositories
	A Data Repository is used to store logs and alerts
		internal MongoDB Engine, MongoDB, Elasticsearch, SYSLOG

	An Authentication Repository is used to authenticate users
		 internal MongoDB Engine, MongoDB, MySQL, PostgreSQL, LDAP, Active Directory, Kerberos.

    Two-factor authentication repository
    	email or SMS

 Network

 	Listener
 		 can manage listeners to add/remove IP addresses to Vulture nodes. Once created, you will be able to bind Vulture processes onto these IP Addresses. 
 		 MAIN Listener, ALIAS Listener

 	Load Balancer
 		uses ha-proxy to provide high-performance load-balancing features on incoming request.

 	URL Rewriting
 		When Vulture receives an HTTP request, you can modify the requested URL before processing it.
		You can create rules that apply on all applications or only to the specified ones.
		Rewriting policy

	Proxy Balancer
		
	Topology

Configuration profiles
	
    Logs profiles
    	Logs profiles are used to define custom logging policy: Where to store logs, log format
    TLS profiles
    	Create a TLS profile to implement TLS and encrypt communication between clients and Vulture.
		This profile will be associated to a listener in the application's listener panel.
    Worker profiles
    	Worker profiles are used to tune the number of process and thread Vuture will allocate for applications.
    ACLs profiles
    	Vulture can perform access control before accepting to serve a request.
		Here you can create ACLs to allow or deny requests based on several criteria:

	    HTTP method,
	    Client IP address,
	    Apache Expression,
	    Apache environment variable, ...

	    ACL policy

	    Users & Groups ACL

Web Application Firewall
	Vulture allows you to filter incoming and outgoing web trafic and block threats like injection, cross site scriping... and other attacks of the OWASP Top10.
	It is relying on mod_security, mod_defender (fork of Naxsi), and mod_svm (Machine learning based on Support Vector Machines) to filter HTTP traffic.

	WAF Ruleset
		Vulture gives you the possibility to edit security rules based on modules mod_security and mod_defender. When you create whitelist / blacklist from logs, related rules appear here.

		Vulture RS
			Anti Session Hijacking
			CSRF Token
			User-Agent checking
			Content-type whitelist
			Protocol whitelist
			File extension whitelist
			Headers whitelist

		WAF Policy
			This menu lists the custom policies in effect by mod_security.
			It allows you to create new one on the fly, and you can fine tune them.

			Main settings
			Scoring
			HTTP Policy
			DOS & BF Protection
			Advanced
			Custom directives

		Virtual Patching
			Virtual patching can understand Acunetix, Qualysguqrd WAS and OWASP ZAP Proxy

		Machine learning Datasets
			SVM
			Learning

		Packet Filter
			Firewall settings
			Firewall Status
			Configuration
			Blacklist
			SSH Protection
			Advanced configuration

Applications settings
	From this menu you can manage all your Vulture's applications. You can change their configurations and start / stop / reload Apache listeners.

	Internet settings
		Global settings
		Public URL mapping
		HTTP features and performance

	Backend settingsRequest header settings
		Application backend settings
		Advanced settings

	Network settings
		From this menu you can manage settings relative to the listeners on which your application should be available.

	Security settings
		From this menu you can manage the security settings of your application.
		Global settings
		Source IP Reputation analysis
		WAF policy settings
		Machine Learning Protection (SVM: Support Vector Machines)

	Logs settings
		From this menu you can manage the logs settings of your application.
		Logs settings

	Request header settings
		From this menu you can manage the requested headers, sent from client's web browser to Vulture. 

		Request Headers
		Basically you can do here everything you can do with Apache "RequestHeader" directive.

	Response header settings
		From this menu you can manage the response headers, sent from the Web application to client's web browser.

		Response Headers
		Basically you can do here everything you can do with Apache "Header" directive.

	Content Rewriting
		From this menu you can manage the content rewriting rules.
		GZIP Management
		Content rewriting

	Authentication
		Authentication settings
		HTML Form authentication
		Kerberos authentication
		OAuth2 authentication

	SSO Forward
		SSO Forward settings

		SSO Forward using Basic authentication
		SSO Forward using HTML Form
		SSO Forward using Kerberos authentication

Portal Template



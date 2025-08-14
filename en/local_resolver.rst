**************
Local resolver
**************

Deploying the Whalebone |product| as a **local resolver** brings the advantage of visibility of local IP addresses that send the actual requests. If deploying locally is not a suitable option for you, 
check out the :ref:`Cloud deployment<Cloud deployment>`.

Whalebone resolver is based on the implementation of `Knot Resolver <https://www.knot-resolver.cz/>`_ developed in the CZ.NIC labs.

Local resolver system requirements
==================================

Hardware and software requirements
----------------------------------

Local resolver is supported on **solely dedicated** physical or virtual machine running a supported operating system and Docker engine. Running resolver on unsupported versions of operating system and/or Docker or with other services might lead to incorrect behavior or issues with service or resolution. Please be aware that not-compliance of these requirements makes troubleshooting more complicated in case of issues with the product.

Please perform regular checks and maintain the resolver's operating system and Docker engine versions up-to-date to ensure stability of the service.

* **Operating system**

  * The operating system must support the amd64-bit architecture.
  * Whalebone requires an actively maintained operating system distributed by one of the following operating system publishers:

    * `Red Hat Enterprise Linux (Full support) <https://access.redhat.com/product-life-cycles?product=Red%20Hat%20Enterprise%20Linux>`_
    * `CentOS Stream (Active support) <https://endoflife.date/centos-stream>`_
    * `Debian (Supported by LTS team) <https://wiki.debian.org/LTS/>`_
    * `Ubuntu (Standard support) <https://ubuntu.com/about/release-cycle>`_

* **Docker**

  * Whalebone supports and is tested on versions of Docker that are supported by the community. See the supported versions `here <https://endoflife.date/docker-engine>`_.

* **File systems** 

  * ext4
  * xfs only with d_type support (ftype=1)

* **Minimum hardware sizing**

  * 2 CPU cores

  * The CPU supports the amd64-bit architecture and the x86-64-v2 instruction set. See below for instructions on how to verify if x86-64-v2 is supported:

    * Ubuntu, Debian:

      * Execute ``/lib64/ld-linux-x86-64.so.2 --help``.
      * Check if you see ``x86-64-v2 (supported, searched)`` in the terminal.

    * Red Hat Enterprise Linux, CentOS Stream:

      * Execute ``/lib/ld-linux-x86-64.so.2 --help``.
      * Check if you see ``x86-64-v2 (supported, searched)`` in the terminal.

  * 4 GB RAM
  * 80 GB HDD with at least 70 GB in /var partition

.. warning:: Please note that Whalebone only supports deloyments without desktop environments such as GNOME, KDE or Xfce as those can impact available memory and DNS processing on the server.

Network requirements
--------------------

  * Local resolver needs the following egress ports opened:
  
  =========== =========== ======= =================================== ======================
  Direction   Protocol(s) Port    Destination IP/Domain               Description         
  =========== =========== ======= =================================== ======================
  Outbound    TCP+UDP     53      Any                                 DNS resolution        
  Outbound    TCP         443     resolverapi.whalebone.io            Database updates
  Outbound    TCP         443     resolverapi.eu-01.whalebone.io      Database updates
  Outbound    TCP         443     resolverapi.apac-01.whalebone.io    Database updates
  Outbound    TCP         443     resolverapi.am-01.whalebone.io      Database updates
  Outbound    TCP         443     resolverapi.uae-01.whalebone.io     Database updates
  Outbound    TCP         443     stream.whalebone.io                 Realtime Database updates
  Outbound    TCP         443     stream.eu-01.whalebone.io           Realtime Database updates
  Outbound    TCP         443     stream.apac-01.whalebone.io         Realtime Database updates
  Outbound    TCP         443     stream.am-01.whalebone.io           Realtime Database updates
  Outbound    TCP         443     stream.uae-01.whalebone.io          Realtime Database updates
  Outbound    TCP         443     logger.whalebone.io                 Logging stream
  Outbound    TCP         443     logger.eu-01.whalebone.io           Logging stream
  Outbound    TCP         443     logger.apac-01.whalebone.io         Logging stream
  Outbound    TCP         443     logger.am-01.whalebone.io           Logging stream
  Outbound    TCP         443     logger.uae-01.whalebone.io          Logging stream
  Outbound    TCP         443     agentapi.whalebone.io               Resolver management
  Outbound    TCP         443     agentapi.eu-01.whalebone.io         Resolver management
  Outbound    TCP         443     agentapi.apac-01.whalebone.io       Resolver management
  Outbound    TCP         443     agentapi.am-01.whalebone.io         Resolver management
  Outbound    TCP         443     agentapi.uae-01.whalebone.io        Resolver management
  Outbound    TCP         443     transfer.whalebone.io               Support Log collection
  Outbound    TCP         443     portal.whalebone.io                 Admin portal
  Outbound    TCP         443     portal.eu-01.whalebone.io           Admin portal
  Outbound    TCP         443     portal.apac-01.whalebone.io         Admin portal
  Outbound    TCP         443     portal.am-01.whalebone.io           Admin portal
  Outbound    TCP         443     portal.uae-01.whalebone.io          Admin portal
  Outbound    TCP         443     harbor.whalebone.io                 Resolver updates
  Outbound    TCP         443     download.docker.com                 Installation Process
  Outbound    TCP         443     data.iana.org                       DNSSEC keys       
  =========== =========== ======= =================================== ======================
  
  .. warning:: Without communication on port 443 to the domains listed above, the resolver won't be installed at all and the installation script will abort.

  
  The main function of the resolver to get queries from the customers and answer back to them the answer requires certain ports to be opened on the resolver for the traffic originating from the client subnet or coming to the customer interface.
  
  ============ ========= ======= =========================== =========================
  Direction    Protocol  Port    Source IP/Domain            Description              
  ============ ========= ======= =========================== =========================
  Inbound      TCP+UDP   53      Customer's subnet range(s)  DNS
  Inbound      TCP       853     Customer's subnet range(s)  DNS over TLS (if used)
  Inbound      TCP       443     Customer's subnet range(s)  DNS over HTTPS (if used)
  ============ ========= ======= =========================== =========================
  
  The Blocking Pages are being hosted **directly** on the Resolvers so the IP addresses that are advertised to the clients must be used. The clients will then be redirected to the IP address of the resolver upon blocking. It is advised to allow only subnet(s) assigned to customers or trusted networks, otherwise it can be misused for various attacks or unauthorized users.
  
  ============ ========= ======= =========================== =========================
  Direction    Protocol  Port    Source IP/Domain            Description              
  ============ ========= ======= =========================== =========================
  Inbound      TCP       80      Customer's subnet range(s)  Redirection/Blocking page
  Inbound      TCP       443     Customer's subnet range(s)  Redirection/Blocking page
  ============ ========= ======= =========================== =========================

  The resolver's processes need to communicate on localhost. In case some firewall is in place please make sure that the traffic is allowed, i.e. ``iptables -A INPUT -s 127.0.0.1 -j ACCEPT``

  ============ ========= ======= =========================== ===================================
  Direction    Protocol  Port    Source IP/Domain            Description                        
  ============ ========= ======= =========================== ===================================
  Inbound      TCP       ANY     127.0.0.1                   Resolver's processes communication 
  ============ ========= ======= =========================== ===================================

.. note:: For hardware sizing estimation of large ISP or Enterprise networks feel free to contact Whalebone. Whalebone local resolver will need approx. twice the RAM and CPU than usual resolver BIND or Unbound. 

Installation of a new local resolver
====================================

You can watch step-by-step video guide about the installation procedure :ref:`here<Deployment video>`.

In menu **Resolvers** press the button **Create new**. Choose a name (identifier) for your new resolver. The input is purely informative and won't affect the functionality.
Once you've entered the name, click **Add resolver** button.
After clicking the button an informative window will pop up with list of supported platforms and the one-line command for the installation. Copy the command and run on the machine dedicated for the local resolver.
The command will run the installation script and will pass the one time token used for the resolver activation. The same command can't be used repeatedly.

.. image:: ./img/lrv2-create.gif
	:align: center
  

Once the command is run the operating system is being checked and requirements installed. Script will inform you about the progress and it creates a detailed log named ``wb_install.log`` in current directory.
Successful run of the installation script is ended with the notification ```Final tuning of the OS``` with value ``[ OK ]``. Right after the installation also the initialization takes place and it could take several minutes before the resolver starts the services.

.. image:: ./img/lrv2-install.gif
   :align: center


.. warning:: Local resolver is configured as an open resolver. It will respond to any request sent. This is quite comfortable in terms of availability of the services, but also could be a risk if the service is available from the outside networks. Please make sure you limit the access to the local resolver on port UDP/53 and TCP/53 from the trusted networks only, otherwise it can be misused for various DoS attacks.

.. important:: The resolver's processes need to communicate on localhost. In case some firewall is in place please make sure that the traffic is allowed, i.e. ``iptables -A INPUT -s 127.0.0.1 -j ACCEPT``

Verifying the installation
--------------------------

Whalebone resolvers come with a set of testing domains for the verification of the installation and the Security filtering.
These domains can be used in order to ensure that you are effectively using a Whalebone resolver:

* ``http://malware.test.attacker.online``
* ``http://c2server.test.attacker.online``
* ``http://spam.test.attacker.online``
* ``http://phishing.test.attacker.online``
* ``http://coinminer.test.attacker.online``

Upon visiting these domains a blocking page similar to the following should be presented:

.. figure:: ./img/blocking-page-default.png
   :alt: Blocking Pages (Default)
   :align: center
   
   Blocking Page - Whalebone Resolver is being used.

In case you come across the page below, it means that the request was not blocked and thus a Whalebone resolver is not being used. 
Please review your settings and if the issue persists, please contact support.

.. figure:: ./img/testing-page.png
   :alt: Blocking Pages (Target)
   :align: center
   
   Blocking Page - Whalebone Resolver is not being used.



Securing your resolver
----------------------

Upon initial installation, the resolver is configured as an open resolver. It will respond to any request sent to it regardless of where the request originated from. This is quite 
comfortable in terms of availability of the services, but could also be a risk if the service is available from the outside networks. Please make sure you limit the access 
to the local resolver on port UDP/53 and TCP/53 from the trusted networks only, otherwise it can be misused for various DoS attacks.


System requirements
===================

Local resolver is supported on dedicated (hardware or virtual) machine running a supported operating system.

* **Supported operating system** (64-bit, server editions of following distributions):

  * Red Hat Enterprise Linux 7, 8
  * CentOS 7, 8
  * Debian 9, 10
  * Ubuntu 16.04, 18.04, 20.04

* **Supported filesystems** 

  * ext4
  * xfs only with d_type support (ftype=1)

* **Minimum hardware sizing** (physical or virtual):

  * 2 CPU cores
  * 4 GB RAM
  * 40 GB HDD (at least 30 GB in /var partition)

.. warning:: Please note that Whalebone only supports deloyments without desktop environments such as GNOME, KDE or Xfce as those can impact available memory and DNS processing on the server.

* **Network setup requirements** (local resolver needs the following ports opened):
  
  =========== =========== ======= ======================== ======================
  Direction   Protocol(s)  Port    Destination IP/Domain    Description         
  =========== =========== ======= ======================== ======================
  Outbound    TCP+UDP     53      Any                      DNS resolution        
  Outbound    TCP         443     resolverapi.whalebone.io Threat Database updates
  Outbound    TCP         443     stream.whalebone.io      Threat Database updates     
  Outbound    TCP         443     logger.whalebone.io      Logging stream   
  Outbound    TCP         443     agentapi.whalebone.io    Resolver management
  Outbound    TCP         443     transfer.whalebone.io    Support Log collection
  Outbound    TCP         443     portal.whalebone.io      Admin portal
  Outbound    TCP         443     harbor.whalebone.io      Resolver updates
  Outbound    TCP         443     download.docker.com      Installation Process
  Outbound    TCP         443     data.iana.org            DNSSEC keys       
  =========== =========== ======= ======================== ======================
  
  .. warning:: Without communication on port 443 to the domains listed above the resolver won't be installed at all (the installation script will abort).

  
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

.. note:: Should you need sizing estimation for large ISP or Enterprise network contact Whalebone. Whalebone local resolver will need approx. twice the RAM and CPU than usual resolver (BIND, Unbound). 

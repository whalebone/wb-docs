*********
Changelog
*********

Steady
==========

2022.09.23
----------
**Improvements**

* Update to Knot Resolver version 5.5.3
	- Fix for CVE-2022-40188. A malicious attacker could perform Denial of Service attack by performing CPU-expensive requests towards specially crafted DNS zones. https://www.knot-resolver.cz/2022-09-21-knot-resolver-5.5.3.html

2022.08.25
----------
**Improvements**

* DNS Resolver update to Knot Resolver version 5.5.0
    - One of the most significant changes is an improved algorithm of nameserver selection for recursive resolution. The updated algorithm ensures a faster and more reliable process.
    - Fixed issue with QName minimization affecting resolution of console.aws.amazon.com subdomains
* Real-time Threat Intelligence synchronization
    - Whenever Whalebone finds a new threat, the resolver immediately receives the information and starts behaving accordingly.
    - For this purpose, the resolver stays connected to the service stream.whalebone.io on TCP/433.
* Blocking of a new type of DNS requests (TYPE65/HTTPS)
    - At this point, this type of request is most commonly used by Apple devices accessing services hosted on Cloudflare.
* New categories of content filtering
    - Peer To Peer (P2P)
    - DNS over HTTPS (DoH)
    - Child abuse
* New categories of legal blocking requirements in different countries: 
    - United Kingdom, Serbia and Philippines
    - Observability: new network and disk operations metrics are available from the portal
    
**Bugfixes**

* Higher precision of reporting of the available memory on the resolver machine 
* Optimization of memory usage of the service which manages the threat database and the local blocking page
* Fixed minor issues during update process in the local orchestration agent (will be put to work after the update is finished) 
* Adjusted DNSSEC log gathering format to comply with changes in Knot Resolver
* Fixed memory leak causing occasional swap issues on some of the resolvers
* Improvements in specific scenarios for threat evaluation of specific subdomains, which are included in content categories and at the same time under legal requirements of countries

2021.07.21
------
**Bugfixes**

* Fixed Knot resolver version to 5.2.1 (fixed ocassional slow resolution issue and issues with particular domains)



Latest
======

2022.05.04
----------

**New features**

* Completely reworked DNS logging (passivedns service is replaced by dnstag service)
* Ability to log even encrypted traffic (DNS over HTTPS / TLS)
* New DNS query types supported
* Under heavy load does not overload single CPU core but distributes the load evenly
* New network and disk operations metrics will be available from the portal
* Based on up-to-date Knot Resolver version (5.5.0)

**Bugfixes**

* Fixed memory leak causing occasional swap issues on some of the resolvers
* Higher precision of reporting of the available memory on the resolver machine
* Fixed minor issues during update process in the agent (will be put to work after the update is finished)
* Set memory limit for real-time Threat Intelligence updates as we have observed occasional overconsumption
* Adjusted DNSSEC log gathering format to comply with changes in Knot Resolver



2021.12.14
----------

**Bugfixes**

* fixed issue with QName minization affecting resolution of `console.aws.amazon.com` subdomains
* small fixes on real time threat intelligence updates


2020.10.12
----------

**Important! Before upgrade, make sure that the service systemd-resolved is running (in case it is installed):**
sudo systemctl enable systemd-resolved
sudo systemctl start systemd-resolved

**Changes**

- Software update source for Whalebone resolver is now https://harbor.whalebone.io (please check your firewall rules)
- Based on DNS Flag Day 2020 recommendation that EDNS buffer size is adjusted to 1232 bytes

**New features**

* Blocking page is reworked from the scratch (originally referred to as "Sinkhole")
  - You can find the configuration in Configuration -> Blocking pages and the activation can be done in the resolver details in Policy assignment
  - It is hosted directly on the resolver (ports TCP/80,443 has to be reachable from clients)
  - Full access to html code editor
  - Feature "Continue anyway" - user can decide to continue to the destination malicious website on his own
  - Different blocking pages per IP or subnet - could be used to customize the blocking page for a specific customer (school, government office, etc.)
  - Definition of supported languages and a default language (for browsers that do not tell which language they prefer if any)
  - Knot resolver updated to version 5.1.3 (from version 5.1.1)
* Management Agent for cloud communication is now independently monitored and if there are any issues, it is automatically restarted (no impact on DNS resolution)

2021.08.10
----------

**New features**

- Knot Resolver update from version 5.2.1 to version 5.3.2
  - Various new features and fixed issues
  - One of the most significant changes is an improved algorithm of nameserver selection for recursive resolution. The updated algorithm ensures a faster and more reliable process.
- Real-time threat intelligence synchronization
  - Whenever Whalebone finds a new threat, the resolver immediately receives the information and starts behaving accordingly.
  - For this purpose, the resolver stays connected to the service stream.whalebone.io on the TCP/433 port.
- Blocking of a new type of DNS requests (Type 65/HTTPS)
  - At this point, this type of request is most commonly used by Apple devices accessing services hosted on Cloudflare.
- New categories of content filtering
  - P2P
  - DoH (DNS over HTTPS)
  - Child abuse
- New categories of legal blocking requirements in different countries
  - United Kingdom
  - Serbia
  - Philippines

**Fixed issues**

- Improvements in specific scenarios for threat evaluation of specific subdomains, which are included in content categories and at the same time under legal requirements of countries
- Optimization of memory usage of the service which manages the threat database and the local blocking page
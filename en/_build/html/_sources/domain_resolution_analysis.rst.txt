.. _header-n233:

Domain resolution analysis
==========================

Sooner or later every administrator will encounter a situation, when DNS resolution is not successful. Most of the time it is not connected with Whalebone's resolver but there is an issue with an authoritative server. 


ISPs often face complaints that users cannot access the domain, in many cases it is not the ISP's fault, but Whalebone solution provides you with information so you can identify the issue. These steps needs to be done:

* **Examine domain in Threats page.**  Check whether domain was block by security feature.

* **Examine domain in DNS traffic** If it was not blocked because of threats, go to DNS Traffic and check whether it reached the resolver. Often users rewrites resolver with public ones and if that resolver faces a issue ISP is blamed to as source of problem, which is not true 

  You can face three cases:
      * domain was translated correctly
      * NXDOMAIN was returned - it means that the authoritative server responded, but the domain or subdomain does not exist.
      * SERVFAIL - no response came from the configured authoritative server. This can mean an outage of server or link issue.


* **Examine domain in DNSVIZ** Under each domain there is an arrow where you can be redirected to DNSVIZ of a particular domain. It shows full resolution process in a human readable way. It can show that the DNSSEC validation process was unsuccessful or the authoritative DNS server was not reachable.

You can watch step-by-step video guide below:

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/sV2Ql8erWwY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

|

Whalebone administration portal provides ability to trace the domain. This feature is available in ``Resolvers`` under each resolver three dots. This feature shows what information is passed to resolver when resolving particular domain.

You can watch step-by-step video guide below:

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/WD6RawjWGqo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

|
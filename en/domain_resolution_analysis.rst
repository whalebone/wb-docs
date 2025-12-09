Domain resolution analysis
==========================

There is always a chance that an administrator will encounter a situation where DNS resolution fails. Most of the time, it is not related to Whalebone's resolver, but there is probably an issue with an authoritative server. 

ISPs often face complaints that users cannot access the domain. In many cases, it is not the ISP's fault. The Whalebone Admin Portal provides administrators with the information you need to identify the issue.

Troubleshooting consists of four steps:

**Step 1: Examine if on-premises Whalebone resolvers block the domain**

  * If you have on-premises resolvers, use the "Is this domain blocked?" button in the resolver menu, under the three dots icon. The test result will tell you whether the resolver blocks the domain.

    .. image:: ./img/domain-resolution-analysis-1.png
      :align: center

**Step 2: Examine the domain in the Threats page**

  * Try to find the affected domain among blocked threats.

**Step 3: Examine the domain in the DNS traffic**

  * If the threat protection feature did not block the domain, go to **DNS Traffic** and check whether the request reached the resolver.
  * If you did not find any requests from the user's IP address in the DNS Traffic overview, the user changed the DNS server configuration on their PC or home router to use public DNS servers. In that case, DNS requests are not sent to Whalebone, and Whalebone does not cause the issue with accessing the domain.
  * If you found the request in the DNS Traffic overview, you can face three cases:
    
    * The domain was translated correctly, and the issue is not caused by Whalebone.
    * NXDOMAIN was returned. It means that the authoritative server responded, but the domain or subdomain does not exist.
    * SERVFAIL was returned. It means no response was received from the configured authoritative server, or the authoritative DNS server does not have valid DNSSEC records for the domain. If this happens, proceed to Step 4.

**Step 4: Examine the domain using the DNSVIZ tool**

  * There is an arrow next to each domain that opens a menu where you can be redirected to DNSVIZ for that domain. DNSVIZ allows you to analyze the entire resolution process, including DNSSEC validation.
    
    .. image:: ./img/domain-resolution-analysis-2.png
      :align: center

  * It can show that the DNSSEC validation process was unsuccessful or the authoritative DNS server was not reachable.

You can watch a step-by-step video guide :ref:`here <domain-resolution-troubleshooting>`.

The Whalebone administration portal provides the ability to trace the domain. This feature is available in **Resolvers** under each resolver's three dots. This feature shows what information is passed to the resolver when resolving a particular domain.

You can watch a step-by-step video guide :ref:`here <domain-tracing>`.
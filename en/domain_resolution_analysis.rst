Domain resolution analysis
==========================

There is always chance that every administrator will encounter a situation, when DNS resolution is not successful. Most of the time it is not related to Whalebone's resolver but there is probably an issue with an authoritative server. 


ISPs often face complaints that users cannot access the domain, in many cases it is not the ISP's fault. Whalebone |product| provides you with information so you can identify the issue. 

**Steps to be done:**

**Step 1.: Examine domain in the Threats page**

  * Check whether domain was blocked by a security feature.
  * For analysis you can use the **Is this domain blocked?**, which is located directly in the resolver menu under the three dots icon. The result of the test will tell you if the domain is blocked or not. 

**Step 2.: Examine domain in the DNS traffic**

  * If it was not blocked because of **threats**, go to **DNS Traffic** and check whether it reached the resolver.
  * Users often rewrites resolver with public ones and if that resolver faces a issue ISP is blamed to as source of problem, which is not true 

  **You can face three cases:**
    * Domain was translated correctly.
    * NXDOMAIN was returned - it means that the authoritative server responded, but the domain or subdomain does not exist.
    * SERVFAIL - no response came from the configured authoritative server. This can mean an outage of server or link issue.

**Step 3.: Examine domain using DNSVIZ tool**
  * Under each domain there is an arrow where you can be redirected to DNSVIZ of a particular domain. 
  * It shows full resolution process in a human readable way.
  * It can show that the DNSSEC validation process was unsuccessful or the authoritative DNS server was not reachable.

.. only:: Immunity
  You can watch step-by-step video guide `here`__.
  __ https://docs.whalebone.io/en/immunity/video_guides.html#domain-resolution-troubleshooting
.. only:: Peacemaker
  You can watch step-by-step video guide `here`__.
  __ https://docs.whalebone.io/en/master/video_guides.html#domain-resolution-troubleshooting

Whalebone administration portal provides ability to trace the domain. This feature is available in **Resolvers** under each resolver's three dots. This feature shows what information is passed to resolver when resolving particular domain.

.. only:: Immunity
  You can watch step-by-step video guide `here`__.
  __ https://docs.whalebone.io/en/immunity/video_guides.html#domain-tracing
.. only:: Peacemaker
  You can watch step-by-step video guide `here`__.
  __ https://docs.whalebone.io/en/master/video_guides.html#domain-tracing

.. only:: Immunity
  `Immunity Support Page <https://Immunity.example.com/support>`_
.. only:: Peacemaker
  `Peacemaker Support Page <https://Peacemaker.example.com/support>`_
.. _Deployment video:

Deployment
==========

On-premise resolver deployment
------------------------------
Unlike other similar services, Whalebone can be deployed as a full-fledged local DNS resolver. This is the type of deployment we encourage.
The installation is fairly simple. All you need is access to Whalebone Portal and a virtual or physical server, which is rather undemanding in terms of hardware.
First, let's take a look at system requirements. Whalebone suports the latest versions of the most popular Linux distributions Debian, Ubuntu, CentOS, and Red hat Enterprise Linux.
The minimum hardware sizing is 2 CPU cores, 4 GB RAM, and a 40 GB HDD. Such a machine can handle up to 20,000 users. 

Before setting up your server, make sure you don't fall short of the network requirements and prevent the machine from being reachable from outside your network. Once the server is ready, go to the Whalebone Portal and create a new resolver.
Come up with a fitting name, which can be changed later on. Once you initiate the addition of the new resolver, you'll see the installation script one-liner command. Copy it to the clipboard.
At this point, access the terminal of the server created for this resolver. All that's left to do is to run the installation script previously copied to the clipboard.
The installation shouldn't take more than a couple of minutes. The script will inform you about the progress. If the installation wasn't successful, send us the installation log and we'll look into it.
Before long, the status of the resolver changes. As soon as the resolver becomes Active, you can route the traffic to it and start protecting your network.

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/W_sWor-Wg-U" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

|
|
|

.. _Cloud resolvers video:

Cloud resolvers
---------------
Whalebone also offers cloud resolvers with malware protection and content blocking. Their addresses are to be found in the Whalebone Portal in the Cloud resolver tab.
You can use them directly as primary or secondary resolvers or as a backup to your existing local resolver. It's not rocket science to use them.

First of all, type in your public IP ranges you want to direct to the cloud resolvers. Afterward, all you need to do is set the Whalebone cloud resolver address as the DNS server address in your network.
As with the local resolvers, you can create different policies and assign them to individual IP addresses or ranges. This allows you to offer Whalebone to institutions such as schools,
which don't necessarily get their connectivity from you, but you administer their network. After having saved and directed the traffic, you're good to go. Just wait for the changes to be propagated to your clients.

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/kdpjCenhTVg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

|
|
|

Configuration
=============

.. _Basic configuration video:

Basic configuration
-------------------
Every network has its own specific needs. Whalebone can and will adapt to every single one of them. One of the key components that need to be configured when implementing Whalebone is setting up your "Security Policies."
This part of the configuration allows you to adjust the default settings. You can for example lower the blocking threshold or deactivate blocking entirely which leaves you with the audit mode.
In this mode, Whalebone monitors the incidents without preventing them from happening. The core of the configuration of audit and blocking is a so-called "score", which is assigned to individual domains by our algorithm. 
The higher the score, the more dangerous the domain. It's up to you to choose from the preset levels of sensitivity or decide to adjust the threshold manually. We advise ISP networks to "block carefully". 
The lower the threshold, the more sensitive the blocking. Keep in mind, though, that setting a low threshold increases the risk of false positives.

You can also choose different types of threats to be blocked. If needed, you can easily create your own blocking lists or define domains that should always be accessible. Our customers love that Whalebone can meet the legal blocking requirements
of their government for them. If you don't find your country our list, let us know and we'll make sure it gets there.
If you activated the content filtering add-on, you can configure it here as well. Create as many unique security policies as you want.
Afterward, you can go into the configuration of a given resolver and assign these policies to different IP addresses or ranges. All you need to do is to go to the "Policy Assignment" section in the resolver details
and assign a policy to a particular IP address or range. Make sure to save the settings.

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/sUqVXKaPuIc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

|
|
|

.. _Security policies video:

Security policies
-----------------
One of the key components that need to be configured when implementing Whalebone is setting up your "Security Policies. This part of the configuration allows you to adjust the default settings. You can for example lower the blocking threshold or deactivate blocking entirel
which leaves you with the audit mode. In this mode, Whalebone monitors the incidents without preventing them from happening. The core of the configuration of audit and blocking is a so-called "score"
which is assigned to individual domains by our algorithm. The higher the score, the more dangerous the domain. It's up to you to choose from the preset levels of sensitivity or decide to adjust the threshold manually.

We advise ISP networks to **block carefully** The lower the threshold, the more sensitive the blocking. Keep in mind, though, that setting a low threshold increases the risk of false positives. 
You can also choose different types of threats to be blocked.

If needed, you can easily create your own blocking list or define domains that should always be accessible.  Our customers love that Whalebone can meet the legal blocking requirement of their government for them.
If you don't find your country our list, let us know and we'll make sure it gets there.

If you activated the content filtering add-on, you can configure it here as well. Create as many unique security policies as you want.
Afterward, you can go into the configuration of a given resolve and assign these policies to different IP addresses or ranges. All you need to do is to go to the **Policy Assignment** section in the resolver detail
and assign a policy to a particular IP address or rangeMake sure to save the settings.

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/vjzOeHAYi4A" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

|
|
|

.. _Blocking page configuration video:

Blocking page configuration
---------------------------
With Whalebone, you can fully customize blocking pages, which appear in case someone attempts to access a dangerous website in their browser. This tool needs a local resolver, where you can switch the blocking page from cloud to on-premise. 
In order to configure blocking pages, go to **Configuration** and then **Blocking pages**. You can adjust the existing ones or create a brand-new one. When creating a new blocking page, you can define its name, the domain, and the language of the page.
Afterward, fill in all the necessary data including the name of the company, its logo and contact information. Naturally, you can change the information later on. If you want to do so, use the magic stick or edit directly in the HTML code. You can modify the design as well as the content of the blocking page as you choose. All you need to do is to preserve the necessary variables shown over the blocking field.

Once you have saved the modified blocking page, go to **Resolvers** and select the resolver to which you would like to apply the blocking page. Go to "Policy assignment" and apply the blocking page to a given resolver.
Alternatively, you can assign it to a specific IP address or range. While you're at it, you can also activate a **bypass**, which will alow the user to access the blocked domain nonetheless.

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/K0p2l-qxHtk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

|
|
|

.. _Alerts video:

Alerts
------
Set up Whalebone alerts and get live updates about what's going on with your resolvers, how secure your network is, and how well your DNS resolution works. 
The basic setup is simple: just choose what type of information you want to get and how often you want to be alerted. You can get alerts via E-mail or Slack.
You can also integrate Whalebone alerts into your systems through webhooks or syslog. For the status of the resolver, resolution, and server it runs on. We would argue that everyone should at least create alerts.

Make sure to start by setting up alerts for resolution failures. Afterward, set up alerts for hardware resources failure, such as insufficiencies concerning the HDD, RAM, or CPU capacity.
You can also monitor failures in communication between the resolver and the Whalebone cloud when the resolution works just fine, but the resolver isn't in sync with Whalebone data centers.

You can even create advanced alerts for DNS traffic and security incidents. We will gladly give you a hand with setting advanced alerts, no matter if it's during the introductory technical consultation,
at the end of the trial or any time you decide to contact Whalebone support.

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/GXUkPICav-o" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

|
|
|

Analysis
========

.. _Domain analysis video:

Domain analysis
----------------
There are two ways to manually perform an analysis of a domain against the Whalebone database. One way to open the **Domain Analysis** tool is from the user's menu.
The other option is to check a specific domain from the context menu in **Threats** or **DNS traffic** overviews directly. Afterward, you will see all the information 
that Whalebone has collected about the domain. We used **kidos-bank.ru** as an example. We can see that there are different types of threats associated with the domain.
Its score is 95-100 and it was labeled as dangerous in November 2019. In the following graphs, you can see the development of the detections, or rather the DNS 
resolution requests of the domain in your network. The outcome of the analysis also shows that the domain is not assigned a content category and its blocking wasn't 
ordered by law. You can inquire into any domain like that. Just enter it into the **top field**. We can see that **facebook.com** is not considered a security threat, 
there's quite some traffic going on and Whalebone categorizes it as a **social network**. If we type in **porn.com**, we can see that the category has changed into **Sexual content**.

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/WJzsGvBiF80" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

|
|
|

.. _DNS traffic video:

DNS traffic
-----------
You can see the timeline of the DNS requests and answers of the last 1, 7, 14, or 30 days in the "DNS traffic" log. The log shows the first resolution of the domain by a given IP address in the last 24 hours,
the type of query, the outcome of the resolution, the source and destination IP address. It also enables you to do a full-text filtration using wild card operators.

The summarizing logarithmic graphs under the main timeline display an overview of the most common answers, second-level domains, and IP addresses with the heaviest traffic. All the data is accessible in a table format, too, and you can even export them to a CSV file
with a maximum of 1,000,000 lines. The DNS traffic logs are temporarily stored on the resolver's server. You can access them from there for your own processing. One of the biggest advantages of the DNS traffic log is the possibility of filtering errors in responses such as NXDOMAIN and SERVFAIL.
This allows you to see the malicious traffic on devices connected to the network. This video shows a hashed IP address with almost 240,000 resolutions of different domains leading to NXDOMAIN and SERVFAIL errors. Here, you can see both public and private IP addresses.

This display is particularly useful especially if you add other queries to the filter, such as MX. Such as setting of the filter shows you IP addresses in your network, which send spam and are therefore in danger of being blacklisted and consequently endangering other customers as well, in case they're behind NAT.
Similarly, you can choose for example A queries. We specialize in the detection of DGA malware communication. Clients, who are infected in this way, connect to quasi-randomly generated domains that try to communicate with the command center of the malware.

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/Qgj-fUHS5qg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

|
|
|

.. _Threats video:

Threats
-------
Whalebone is all about protecting your network. That's why you can access a complete overview of incidents that have happened in the last three months.
Not only does the overview offer information, but it also provides you with the possibility of filtration and data analysis. The results are divided into three categories; events that have been blocked, audited, and allowed. 
The audited domains represent domains, which are somewhat suspicious. Their score is high enough to be listed in the log but lower that the blocking threshold. When it comes to blocked domains, the resolver returns a fully-customized blocking page with an optional bypass button.

You can also filter the data by the type of incident. Let's take a look at the example of communication with the command center of the malware. We can see specific blocked domains as well as local or public IPs that tried to access them.
This is an example of active intensive traffic from a specific IP address and communication with malware called Necurs. Such an infected client would affect the quality of other client's connections as well.
For every single record, you can choose different types of domain checks in the context menu. It's very practical to start the analysis by googling the domain. More often than not, though, the results will only tell you that the domain is dangerous.

Another way of checking the domain is by using various security sources. An example of such a service is a very useful website Virustotal. If you aren't convinced that there was a good reason for the blocking even after the analysis,
feel free to report such a domain to us. We will examine the case and get back to you. In case it truly turns out to be a false positive blocking, we will globally allow access to the domain for all Whalebone customers.

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/GVZoMOEUWzM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

|
|
|

.. _Data Analysis video:

Data Analysis
-------------
The Whalebone Portal allows detail full-text filtration and associated data analysis. The thorough manual is to be found in the technical documentation available at docs.whalebone.io.
You will find a list of different operators, examples of their usage, and references to the potential difference between the DNS traffic and threats overview. You can use wildcard or logical operators. When using full-text filtration,
all the parameters are to be type directly into the URL address. This way, you can easily create filters for future use.

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/TVhyQP_AG-Y" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

|
|
|

.. _API video:

API
---
With Whalebone API, you can integrate Whalebone into your own systems. This allows you to make use of all the advantages of Whalebone. First of all, you need to create a new key.
Go to the API keys configuration from the context menu. After a new API key is created, you will see all the necessary details. The secret for the API key will never be 
displayed again, so make sure you really copied it. You can always invalidate the API key. Just click the corresponding icon. We have a detailed interactive documentation 
for Whalebone API. Just click the icon in the API keys overview or go directly to apidocs.whalebone.io/public. The documentation will take you through different categories 
of information and settings with specific examples. The "Event" section contains all the information about threats such as types of threats and domains. You can even model 
API calls directly in the documentation and use them right away. On top of that, the API contains certain information that isn't available in the Whalebone Portal yet, 
such as the DNSSEC validation details. Naturally, you can access information about resolvers, such as latency, the health of the resolvers, or the usage of system resources. 
Before you start modeling API calls in the documentation, we recommend authorizing it with your API keys. This will allow you to directly work with your account in the documentation.

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/9SsxMVR6ino" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


|
|
|

.. _domain-resolution-troubleshooting:

Domain resolution troubleshooting
---------------------------------
When internet users can't access a domain, they often think it's the ISP's fault. More often than not, you're not the one to blame, it's the domain itself.
No matter what, you still have to answer the customer and explain the situation. Let's take a look at how Whalebone improve this process.

First of all, examine the potential domain blocking by searching the domain in "Threats". We recommend using search operators and querying for subdomains.
It turns out that the domain "sufr.cz" has not been blocked as a threat. The second steap is to go to "DNS traffic" and check if the domain was even accessed by anyone. If so, take a look at how Whalebone deal with the resolution.
It turns out there have been attempts to access the domain. In that case, we have to check the results. We can see that the response for this domain was SERVFAIL. To further the troubleshooting process, we can analyze the domain through the context menu. 

We recommend using the DNS Viz tool. DNS Viz is designed to fully inspect the DNS resolution behavior. A direct click-through leads to the DNSSEC validation results. It turns out that the problem of this particular domain is that it has issues with expired cryptographic signatures.
If you feel like you still don't really know what's going on with the domain, feel free to contact us via E-mail at support@whalebone.io. We will gladly look into your issue.

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/sV2Ql8erWwY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

|
|
|

.. _domain-tracing:

Domain Tracing
--------------
A well-working DNS resolution is essential for a functional internet connection. That's why you can make sure that the individual resolvers are functioning all right in the administration portal.
All you need to do is choose the corresponding local resolver, open the context menu and click "Trace domain". At this point, type in the domain you want to examine. Let's say it's whalebone.io.

Choose one of the query types, for example, "A" and trace the domain. You can see the outcome of the resolution here. The upper part shows the result of the query. The green color tells you there's nothing wrong with the DNS resolution. 
If there's an issue, there will be some information about the particular problem in orange or red. For example, if the domain doesn't exist, the result will be NXDOMAIN. In case there's an issue with the resolution, you will see the "SERVFAIL" response.
If you encounter any issues, send the log to support@whalebone.io and we'll look into it.

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/WD6RawjWGqo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>




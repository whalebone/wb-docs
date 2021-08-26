On-premise resolver deployment
------------------------------
Unlike other similar services, Whalebone can be deployed as a full-fledged local DNS resolver. This is the type of deployment we encourage.
The installation is fairly simple. All you need is access to Whalebone Portal and a virtual or physical server, which is rather undemanding in terms of hardware.
First, let's take a look at system requirements. Whalebone suports the latest versions of the most popular Linux distributions Debian, Ubuntu, CentOS, and Red hat Enterprise Linux.
The minimum hardware sizing is 2 CPU cores, 4 GB RAM, and a 40 GB HDD. Such a machine can handle up to 20,000 users. Before setting up your server, make sure you don't fall short
of the network requirements and prevent the machine from being reachable from outside your network. Once the server is ready, go to the Whalebone Portal and create a new resolver.
Come up with a fitting name, which can be changed later on. Once you initiate the addition of the new resolver, you'll see the installation script one-liner command. Copy it to the clipboard.
At this point, access the terminal of the server created for this resolver. All that's left to do is to run the installation script previously copied to the clipboard.
The installation shouldn't take more than a couple of minutes. The script will inform you about the progress. If the installation wasn't successful, send us the installation log and we'll look into it.
Before long, the status of the resolver changes. As soon as the resolver becomes Active, you can route the traffic to it and start protecting your network.
.. raw:: html
    <iframe width="560" height="315" src="https://www.youtube.com/watch?v=W_sWor-Wg-U&list=PLqtoGboy8K8lTmzl0nJwi4WOz4_Xck-08&index=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>






Cloud resolvers
---------------------------
Whalebone also offers cloud resolvers with malware protection and content blocking. Their addresses are to be found in the Whalebone Portal in the Cloud resolver tab.
You can use them directly as primary or secondary resolvers or as a backup to your existing local resolver. It's not rocket science to use them.
First of all, type in your public IP ranges you want to direct to the cloud resolvers. Afterward, all you need to do is set the Whalebone cloud resolver address as the DNS server address in your network.
As with the local resolvers, you can create different policies and assign them to individual IP addresses or ranges. This allows you to offer Whalebone to institutions such as schools,
which don't necessarily get their connectivity from you, but you administer their network. After having saved and directed the traffic, you're good to go. Just wait for the changes to be propagated to your clients.
.. raw:: html
    <iframe width="560" height="315" src="https://www.youtube.com/watch?v=kdpjCenhTVg&list=PLqtoGboy8K8lTmzl0nJwi4WOz4_Xck-08&index=2" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>






Basic configuration
-------------------
Every network has its own specific needs. Whalebone can and will adapt to every single one of them. One of the key components that need to be configured when implementing Whalebone is setting up your “Security Policies.”
This part of the configuration allows you to adjust the default settings. You can for example lower the blocking threshold or deactivate blocking entirely which leaves you with the audit mode.
In this mode, Whalebone monitors the incidents without preventing them from happening. The core of the configuration of audit and blocking is a so-called "score", which is assigned to individual domains by our algorithm. The higher the score, the more dangerous the domain. It's up to you to choose from the preset levels of sensitivity
or decide to adjust the threshold manually. We advise ISP networks to "block carefully". The lower the threshold, the more sensitive the blocking. Keep in mind, though, that setting a low threshold increases the risk of false positives.
You can also choose different types of threats to be blocked. If needed, you can easily create your own blocking lists or define domains that should always be accessible. Our customers love that Whalebone can meet the legal blocking requirements
of their government for them. If you don't find your country our list, let us know and we'll make sure it gets there.
If you activated the content filtering add-on, you can configure it here as well. Create as many unique security policies as you want.
Afterward, you can go into the configuration of a given resolver and assign these policies to different IP addresses or ranges. All you need to do is to go to the "Policy Assignment" section in the resolver details
and assign a policy to a particular IP address or range. Make sure to save the settings.
.. raw:: html
    <iframe width="560" height="315" src="https://www.youtube.com/watch?v=sUqVXKaPuIc&list=PLqtoGboy8K8lTmzl0nJwi4WOz4_Xck-08&index=3" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>





Security policies
-----------------
.. raw:: html
    <iframe width="560" height="315" src="https://www.youtube.com/watch?v=vjzOeHAYi4A&list=PLqtoGboy8K8lTmzl0nJwi4WOz4_Xck-08&index=4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


Blocking page configuration
---------------------------
.. raw:: html
    <iframe width="560" height="315" src="" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>



Alerts
------
.. raw:: html
    <iframe width="560" height="315" src="" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


DNS traffic
------------
.. raw:: html
    <iframe width="560" height="315" src="" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>



Threats
---------
.. raw:: html
    <iframe width="560" height="315" src="" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


Data Analysis
---------------


.. raw:: html
    <iframe width="560" height="315" src="https://www.youtube.com/watch?v=TVhyQP_AG-Y&list=PLqtoGboy8K8lTmzl0nJwi4WOz4_Xck-08&index=9" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


API
----

With Whalebone API, you can integrate Whalebone into your own systems. This allows you to make use of all the advantages of Whalebone. First of all, you need to create a new key.
Go to the API keys configuration from the context menu. After a new API key is created, you will see all the necessary details. The secret for the API key will never be 
displayed again, so make sure you really copied it. You can always invalidate the API key. Just click the corresponding icon. We have a detailed interactive documentation 
for Whalebone API. Just click the icon in the API keys overview or go directly to apidocs.whalebone.io/public. The documentation will take you through different categories 
of information and settings with specific examples. The "Event" section contains all the information about threats such as types of threats and domains. You can even model 
API calls directly in the documentation and use them right away. On top of that, the API contains certain information that isn't available in the Whalebone Portal yet, 
such as the DNSSEC validation details. Naturally, you can access information about resolvers, such as latency, the health of the resolvers, or the usage of system resources. 
Before you start modeling API calls in the documentation, we recommend authorizing it with your API keys. This will allow you to directly work with your account in the documentation.

.. raw:: html
    <iframe width="560" height="315" src="https://www.youtube.com/watch?v=9SsxMVR6ino&list=PLqtoGboy8K8lTmzl0nJwi4WOz4_Xck-08&index=10" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


Domain analysis
----------------

There are two ways to manually perform an analysis of a domain against the Whalebone database. One way to open the "Domain Analysis" tool is from the user's menu.
The other option is to check a specific domain from the context menu in "Threats" or "DNS traffic" overviews directly. Afterward, you will see all the information 
that Whalebone has collected about the domain. We used kidos-bank.ru as an example. We can see that there are different types of threats associated with the domain.
Its score is 95-100 and it was labeled as dangerous in November 2019. In the following graphs, you can see the development of the detections, or rather the DNS 
resolution requests of the domain in your network. The outcome of the analysis also shows that the domain is not assigned a content category and its blocking wasn't 
ordered by law. You can inquire into any domain like that. Just enter it into the top field. We can see that facebook.com is not considered a security threat, 
there's quite some traffic going on and Whalebone categorizes it as a social network. If we type in porn.com, we can see that the category has changed into "Sexual content".

.. raw:: html
    <iframe width="560" height="315" src="https://www.youtube.com/embed/WJzsGvBiF80" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
 

Domain resolution troubleshooting
----------------------------------
.. raw:: html
    <iframe width="560" height="315" src="https://www.youtube.com/embed/sV2Ql8erWwY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


Domain Tracing
-----------------
.. raw:: html
    <iframe width="560" height="315" src="https://www.youtube.com/embed/WD6RawjWGqo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>




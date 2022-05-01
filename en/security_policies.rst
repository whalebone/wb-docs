Security policies
=================

You can watch step-by-step video guide of basic security policy configuration below:

.. raw:: html

	<iframe width="560" height="315" src="https://www.youtube.com/embed/sUqVXKaPuIc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

|

You can watch step-by-step video guide with deeper exxplanation of security policy tuning below:

.. raw:: html

	<iframe width="560" height="315" src="https://www.youtube.com/embed/vjzOeHAYi4A" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

|

The behavior of DNS filtering on the resolvers could be defined in the menu item **Configuration** and tab **Security policies**. In the default state there is only the **Default policy**, which is automatically assigned to any new resolver.
In any policy there are several options to be defined:

* **Malicious domains filtering**

  * Allows to apply actions Audit (logging) or Block (redirect to blocking page) on resolution of malicious domains
  * Individual actions could be turned off - e.g. turn off the blocking for testing purposes
  * The slider values define the probability that the particular domain is malicious on the scale from 0 to 100 (0 is a safe domain, 100 is malicious)
  * There are available preconfigured policies that cover the most usual cases. These cases are: `Don't Block`, `Block carefully` and `Block strictly`.

.. tip:: The default threshold for blocking is set to ``80`` which is safe even for larger network with liberal policy towards the users. For more restrictive policy we suggest setting threshold for blocking to ``70-75``, in very restrictive networks even down to ``60``. Audit is purely informative, however setting the threshold too low can result in too many logged incidents.

* **Types of threats**

  * The default behavior is to include all types of threats
  * The drop-down menu allows the user to choose a more granular category of the threats they would like to audit or block. The available categories are: `blacklist`, `c&c`, `coinminer`, `compromised`, `malware`, `phishing` and `spam`.

A full list of what each category includes can be found below: 

* **C&C (Command and Control)**:  domains that facilitate botnet communication to coordinate its activity. A botnet is a network of infected computers, which are controlled as a group. 
* **Malware**: domains that host and distribute any kind of malicious code
* **Phishing**: domains aiming to trick users and extract sensitive information such as credit card details, login credentials, etc.
* **Blacklist**: domains that are known to serve multiple nefarious purposes at the same time or over a period of time
* **Spam**: domains that are linked to spreading spam emails and scam schemes.
* **Compromised**: otherwise legitimate domains that have been hacked and are temporarily used for malicious purposes
* **Coinminer**: domains that hijack processing and energy resources for unsolicited cryptocurrency mining


.. image:: ./img/security-policies.gif
   :align: center

* **Allow List**

  * Domains that won't be blocked at any time (higher priority has only **Blacklist**)
  * The allow list is applied to the domain and all of the subdomains, e.g.: allowed domain ``whalebone.io`` will also allow ``docs.whalebone.io``, but not vice versa
  * The list can be configured on the `Allow / Deny List` tab

* **Deny List**

  * Domains that will be blocked at all times 
  * The deny list is applied to the domain and all of the subdomains, e.g.: denied domain ``malware.ninja`` will also deny ``super.malware.ninja``, but not vice versa 
  * The list can be configured on the `Allow / Deny List` tab.

.. image:: ./img/whitelist.gif
   :align: center

.. warning:: After creating an allow or deny list, it should be assigned to the specific security policy, or else the changes will not take effect.

.. note:: Changes will be applied to the resolvers in approx. 2-3 minutes. Saved configuration is used during preparation of the threat data package for the resolvers that download and apply those packages at regular intervals.

* **Regulatory Restrictions**

  * Integrated list of domains that must be applied in order to conform to Regulatory Restrictions of a country.
  * Examples of these domains include cases of illegal gambling or child pornograpy. 

.. warning:: Each country has different Regulatory lists. In case of multi-country deployments different policies can be used in order to apply the proper Regulatory Restrictions. 

* **Content Filtering** 

  Particular Content categories can be applied on a per-policy level. This is useful in case different segments of the networks come with different requirements. For example, in case of a School environment all the **Adult** categories can be enabled and access to relevant content can be restricted.

  A diverse set of content filtering categories are available:

*	**Sexual content**: sexual and pornographic material
*	**Gambling**: games and activities involving betting money
*	**Weapons**: guns and weapon-related sites
*   **Audio-video**: audio and video streaming services
*	**Games**: online games and gaming websites
*	**Chat**: instant messaging and chatting applications
*	**Social-networks**: social networking sites and applications
*	**Child abuse**: websites related to child abuse dissemination of child pornography
*	**Drugs**: drug related websites including alcohol and tobacco
*	**Racism**: content linked to racism and xenophobia
*	**Violence**: explicit violence and gore
*	**Terrorism**: domains linked to terrorism support
*	**Advertisement**: banners, context advertisements and other advertisements systems
*	**Crypto-mining**: domains connected to crypto-currency mining activities
*	**DoH**: DNS over HTTPS. These are domains that provide obfuscation of the DNS requests in HTTP traffic 
*	**P2P**: domains linked to peer to peer networks where multimedia content is shared by the users
*	**Tracking**: web and email tracking systems




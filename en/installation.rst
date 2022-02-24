Installation of a new resolver
==============================

You can watch step-by-step video guide about installation procedure below:

.. raw:: html

	<iframe width="560" height="315" src="https://www.youtube.com/embed/W_sWor-Wg-U" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen>
	</iframe>

|

In menu **Resolvers** press the button **Create new**. Choose a name (identifier) for your new resolver. The input is purely informative and won't affect the functionality.
Once you've entered the name, click **Add resolver** button
After clicking the button an informative window will pop up with list of supported platforms and the one-line command for the installation. Copy the command and run on the machine dedicated for the local resolver.
The command will run the installation script and will pass the one time token used for the resolver activation (the same command can not be used repeatedly).

.. image:: ./img/lrv2-create.gif
	:align: center

Once the command is run the operating system is being checked and requirements installed. Script will inform you about the progress and it creates a detailed log named ``wb_install.log`` in current directory.
Successful run of the installation script is ended with the notification ```Final tuning of the OS``` with value ``[ OK ]``. Right after the installation also the initialization takes place and it could take several minutes before the resolver starts the services.

.. image:: ./img/lrv2-install.gif
   :align: center

.. warning:: Local resolver is configured as an open resolver. It will respond to any request sent. This is quite comfortable in terms of availability of the services, but also could be a risk if the service is available from the outside networks. Please make sure you limit the access to the local resolver on port 53 (UDP and TCP) from the trusted networks only, otherwise it can be misused for various DoS attacks.

.. important:: The resolver's processes need to communicate on localhost. In case some firewall is in place please make sure that the traffic is allowed, i.e. ``iptables -A INPUT -s 127.0.0.1 -j ACCEPT``

Verifying the installation
--------------------------

Whalebone resolvers come with a set of testing domains for the verification of the installation and the Security filtering.
These domains can be used in order to ensure that you are effectively using a Whalebone resolver:

* ``http://malware.test.whalebone.io``
* ``http://c2server.test.whalebone.io``
* ``http://spam.test.whalebone.io``
* ``http://phishing.test.whalebone.io``
* ``http://coinminer.test.whalebone.io``

Upon visiting these domains a blocking page similar to the following should be presented:

.. figure:: ./img/blocking-page-default.png
   :alt: Blocking Pages (Default)
   :align: center
   
   Blocking Page - Whalebone Resolver is being used

In case you come across the page below, it means that the request was not blocked and thus a Whalebone resolver is not being used. 
Please review your settings and if the issue persists, please contact support.

.. figure:: ./img/testing-page.png
   :alt: Blocking Pages (Target)
   :align: center
   
   Blocking Page - Whalebone Resolver is not being used




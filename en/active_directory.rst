============================
Active Directory Integration
============================

In order to get the **device name visibility** in the logs Whalebone Immunity can be easily integrated with Active Directory. Visibility to device name speeds up the analysis and troubleshooting since the administrator does not have to look up for the device name in the DHCP logs.

How it works?
-------------
Once configured, Whalebone resolver asks the authoritative name server for the device name using PTR record. A **PTR (Pointer) record** is a type of DNS record used to map an IP address to a domain name, essentially performing a reverse DNS lookup. Unlike A or AAAA records, which resolve domain names to IP addresses, a PTR record provides the human-readable domain name associated with a given IP address.


DNS lookup integration can be simply done in a few steps.
Head to the Whalebone portal -> Resolvers

.. image:: ./img/ad-integration-1.png
   :align: center

Click on the resolver you would like to integrate and then head to the Integrations tab on the left of the page.

.. image:: ./img/ad-integration-2.png
   :align: center
   

Turn the Log device names in your network slider to the On position.

.. image:: ./img/ad-integration-3.png
   :align: center
   

Add  your Authoritative nameservers

.. image:: ./img/ad-integration-4.png
   :align: center
   

If you have multiple controllers you can press on the + sign and add a secondary.

.. image:: ./img/ad-integration-5.png
   :align: center
   

If your network is segmented and each IP range or network segment is associated with a different name server, you can leverage the Network segmentation feature.

.. image:: ./img/ad-integration-6.png
   :align: center
   

By enabling this option, resolver starts to query itself for the PTR records (in order to enrich the logs for the device hostname). Association of IP ranges with the particular name server is then set up in the DNS resolution settings.

*Note: Do not forget that PTR records are entered in the reverse way. See the screenshots below for examples.*

You can set these up under DNS resolution settings.

Click on the Go to the DNS resolution settings and set up your desired forwarding rules.

.. image:: ./img/ad-integration-6.png
   :align: center
   

.. image:: ./img/ad-integration-7.png
   :align: center
   
In the Advanced setup you can configure specific behaviors.

.. image:: ./img/ad-integration-8.png
   :align: center

Defaults are the recommended values, but they can be adjusted to your specific needs.
Once satisfied with the settings you can click on the Save button on the bottom of the page to save the configuration.
The settings **need to be applied to the resolver** as indicated by the message that will pop up at the top of the page.

.. image:: ./img/ad-integration-9.png
   :align: center


Head back to the Resolvers page and apply the configuration on the resolver by pressing the apply configuration button next to your resolver.

.. image:: ./img/ad-integration-10.png
   :align: center

*Note: PTR records are not visible in DNS traffic logs. The resolver performs reverse lookups **separately** from the actual DNS queries made by clients.*


.. toctree::
   :maxdepth: 1

   active_directory_secondary

Whalebone Immunity
===================

Local DNS forwarder
-------------------

Very similar deployment scenario as the local resolver, however Whalebone just forwards the requests to preconfigured resolvers. This scenario is very useful in case there are local DNS zones that has to be available for the clients (e.g. Active Directory) or cases when the recent resolver configuration is very specific and has to be preserved.
This deployment has also lower hardware requirements, roughly half of the CPU and RAM recommended.

.. warning:: We don't recommend to forward the requests from the local resolver to Whalebone cloud resolvers. Such configuration would result in duplicit incident detection, no added security and unnecesary latency for the clients.

.. image:: ./img/deployment_forwardeer.png
   :align: center


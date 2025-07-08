#####################
Whalebone admin guide
#####################

Whalebone is a service for security filtering of DNS traffic. It uses logic on top of own DNS resolvers. 
Such resolvers could be either cloud ones maintained directly by Whalebone, or on-premise software resolvers using cloud just for threat intelligence updates and reporting. 
For threat prevention Whalebone relies on external intelligence sources as well as on own methods.
More information about the product and company is available on the official `Whalebone website. <https://whalebone.io>`_

.. toctree::
   :maxdepth: 2
   :caption: Deployment Options

   deployment_cloud

.. toctree::
   :caption: Quickstart

   quickstart

.. toctree::
   :caption: Configuration

   security_policies
   cloud_resolver

.. toctree::
   :caption: Analysis and reporting
   
   data_analysis
   domain_resolution_analysis
   reporting
   api_integration

.. toctree::
   :caption: About
   
   licence_disclaimer
   
.. toctree::
   :maxdepth: 3
   :hidden:

   active_directory
   blocking_pages
   deployment_immunity
   deployment_peacemaker
   dns_resolution
   hos_installation
   hos_operation
   hos_overview
   idp_overview
   knot_tips_tricks
   local_resolver
   resolver_agent
   resolvers
   snmp_monitoring
   uninstalling
   user
   video_guides
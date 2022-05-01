#####################
Whalebone admin guide
#####################

Whalebone is a service for security filtering of DNS traffic. It uses logic on top of own DNS resolvers. 
Such resolvers could be either cloud ones maintained directly by Whalebone, or on-premise software resolvers using cloud just for threat intelligence updates and reporting. 
For threat prevention Whalebone relies on external intelligence sources as well as on own methods.
More information about the product and company is available on the official `Whalebone website <https://whalebone.io>`_

.. toctree::
   :maxdepth: 3
   :caption: Getting started

   deployment
   quickstart

.. toctree::
   :caption: Configuration

   local_resolver
   resolvers
   security_policies
   dns_resolution
   knot_tips_tricks
   blocking_pages
   resolver_agent
   cloud_resolver
   uninstalling

.. toctree::
   :caption: Analysis and reporting
   
   data_analysis
   domain_resolution_analysis
   reporting
   integration


.. toctree::
   :caption: Organization Settings
   
   user

.. toctree::
   :caption: Step-by-Step Video Guides

   video_guides

.. toctree::
   :caption: About
   
   licence_disclaimer


.. toctree::
   :caption: Home Office Security

   hos







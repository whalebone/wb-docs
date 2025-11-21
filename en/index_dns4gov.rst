#####################
Whalebone admin guide
#####################

Whalebone DNS is a service for security filtering of DNS traffic. It uses logic on top of own DNS resolvers. 
Such resolvers could be either cloud ones maintained directly by Whalebone, or on-premise software resolvers using cloud just for threat intelligence updates and reporting. 
For threat prevention Whalebone relies on external intelligence sources as well as on own methods.
More information about the product and company is available on the official `Whalebone website. <https://whalebone.io>`_

.. toctree::
   :maxdepth: 1
   :caption: Deployment Options

   deployment_immunity
   deployment_cloud

.. toctree::
   :maxdepth: 1
   :caption: Quickstart

   quickstart

.. toctree::
   :maxdepth: 1
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
   :maxdepth: 1
   :caption: Analysis and reporting

   data_analysis
   domain_resolution_analysis
   reporting
   api_integration
   syslog_integration
   active_directory
   snmp_monitoring

.. toctree::
   :maxdepth: 1
   :caption: Organization Settings
   
   user
   multitenancy

.. toctree::
   :maxdepth: 1
   :caption: Home Office Security
   
   hos_overview
   hos_installation
   hos_operation
   hos_troubleshooting

.. toctree::
   :maxdepth: 1
   :caption: Step-by-Step Video Guides

   video_guides

.. toctree::
   :maxdepth: 1
   :caption: About
   
   licence_disclaimer

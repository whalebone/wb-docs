#####################
Whalebone admin guide
#####################

Whalebone je služba pro bezpečnostní filtrování provozu DNS. Využívá logiku nad vlastními DNS resolvery. 
Tyto resolvery mohou být buď cloudové, které jsou pod správou Whalebone, nebo lokální softwarové resolvery využívající cloud pouze pro aktualizace a hlášení informací o hrozbách. 
Při prevenci hrozeb se Whalebone spoléhá na externí zpravodajské zdroje i na vlastní metody.
Další informace o produktu a společnosti jsou k dispozici na oficiálních stránkách `Whalebone. <https://whalebone.io>`_

.. toctree::
   :maxdepth: 1
   :caption: Možnosti nasazení

   deployment_immunity
   deployment_cloud

.. toctree::
   :maxdepth: 1
   :caption: Quickstart

   quickstart

.. toctree::
   :maxdepth: 1
   :caption: Konfigurace

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
   :caption: Analýza dat

   data_analysis_overview
   data_analysis_content
   data_analysis_dns_traffic
   data_analysis_threats
   domain_resolution_analysis

.. toctree::
   :maxdepth: 1
   :caption: Upozornění a reportování

   reporting
   alerts

.. toctree::
   :maxdepth: 1
   :caption: Integrace

   api_integration
   syslog_integration
   active_directory
   snmp_monitoring

.. toctree::
   :maxdepth: 1
   :caption: Nastavení ogranizace
   
   user_management
   organization_settings
   multitenancy

.. toctree::
   :maxdepth: 1
   :caption: Home Office Security
   
   hos_overview
   hos_installation
   hos_operation

.. toctree::
   :maxdepth: 1
   :caption: Identity protection

   idp_overview

.. toctree::
   :maxdepth: 1
   :caption: Videonávody krok za krokem

   video_guides

.. toctree::
   :maxdepth: 1
   :caption: Další informace
   
   licence_disclaimer

#####################
Whalebone admin guide
#####################

Whalebone je služba pro bezpečnostní filtrování provozu DNS. Využívá logiku nad vlastními DNS resolvery. 
Tyto resolvery mohou být buď cloudové, které jsou pod správou Whalebone, nebo lokální softwarové resolvery využívající cloud pouze pro aktualizace a hlášení informací o hrozbách. 
Při prevenci hrozeb se Whalebone spoléhá na externí zpravodajské zdroje i na vlastní metody.
Další informace o produktu a společnosti jsou k dispozici na oficiálních stránkách `Whalebone. <https://whalebone.io>`_

.. toctree::
   :maxdepth: 3
   :caption: Možnosti nasazení

   deployment_peacemaker
   deployment immunity
   deployment_cloud


.. toctree::
   :caption: Quickstart

   quickstart


.. toctree::
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
   :caption: Analýza a reporting
   
   data_analysis
   domain_resolution_analysis
   reporting
   api_integration
   active_directory
   snmp_monitoring


.. toctree::
   :caption: Nastavení ogranizace
   
   user


.. toctree::
   :caption: Home Office Security
   
   hos_overview
   hos_installation
   hos_operation

.. toctree::
   :caption: Videonávody krok za krokem

   video_guides


.. toctree::
   :caption: Další informace
   
   licence_disclaimer
   changelog









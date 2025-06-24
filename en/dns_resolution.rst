DNS resolution configuration
============================

You can find the options to configure the resolver in the menu **Configuration** and tab **DNS resolution**. This page allows you to do the basic configuration without the knowledge of configuration syntax. Furthermore there is a text area allowing you to define any configuration to the underlying `Knot Resolver <https://www.knot-resolver.cz/>`_.

Available configuration options:

* **Enable IPv6**

  * If the system has IPv6 configured properly its is possible to enable IPv6.
  * Otherwise the activation of IPv6 could have negative effects on the performance and latency of the resolver.

* **Forward queries to**

  * This option allows to redirect all or chosen queries to upstream resolvers or authoritative DNS servers (suitable e.g. for forwarding to domain controllers of Active Directory).
  * **Disable DNSSEC**

    * If checked, the answers from the forwarded queries won't be DNSSEC validated. 
    * We recommend to check this option in case the upstream server don't have DNSSEC configured properly.

  * **All queries to**

    * Option to forward all queries to one or more resolver.
    * This option keeps caching all responses!

  * **Following domains**
    * Option to choose particular domains that should be forwarded to on more resolvers.
    * Different resolvers could be defined for different domains.
    * Caching for the selected domains will be turned off!.

* **Static records**

  * Predefined answers that should be returned for particular domains.
  * Could serve for special purposes such as monitoring or very simple substition of records on authoritative server.

* **Advanced DNS configuration**

  * Text area for advanced configuration.
  * Used for direct configuration of Knot Resolver.
  * `Complete Knot Resolver configuration <https://knot-resolver.readthedocs.io/en/stable/config-overview.html>`_
  * Supports Lua scripting.

.. image:: ./img/resolution_en.gif
   :align: center

.. warning:: Faulty configuration can impact stability, performance or security functions of the resolver. In case of wrong syntax the **Deploy Configuration** will result in error code.



.. note:: Once the **Save** button is pressed changes in DNS resolution are saved and prepared to be deployed to target resolvers. The deployment itself has to be done from the **Resolvers** page. It is possible to do multiple changes and apply all of them at once to minimize the number of deployments to the resolver.


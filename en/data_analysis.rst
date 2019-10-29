.. _header-n152:

Data Analysis
=============

Whalebone Portal (graphical user interface) gives the user number of
possibilities how to analyze what is happening on the DNS resolvers and
the network.

.. _header-n155:

Threats
-------

Threats are special events where there is a DNS request for a domain
that is present within the reputation database. There are two types of
actions when a threat is detected. The first is to audit the event while
the second is to block it.

The action that is to be implemented depends on the policies that are
assigned to the specific resolver. For more on that please refer to
`Security
Policies <http://docs.whalebone.io/cs/latest/local_resolver.html#bezpecnostni-politiky>`__.

There are some pre-configured filters that can be applied on the data on
the portal. Some sample queries can be found below. These queries depict
the majority of the use cases but there is no hard limit as the
available search engine is **full-text** and *any* query can be compiled
impromptu.

.. _header-n159:

How to search for audit/block events.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| There are two options in order to filter the different types of
  events. 
| In the first option a visual filter can be applied where the type that
  a user clicks is disabled from the graph. This can aid the process of
  having a basic overview of the traffic's qualities.

.. figure:: .img/block_graph.gif
   :alt: 

For more advanced usage a query can be issued:

-  ``action: block`` in order to filter the blocking events

-  ``action: audit`` in order to filter the auditing events

-  ``action: whitelist`` in order to view the Block page redirects

This query updates the content of the whole dashboard.

.. figure:: .img/request_ip.gif
   :alt: 

.. _header-n173:

How to search for events based on specific IP address.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A filtering of an IP address is possible by clicking on the specific
``Source IP`` bar and in this way filtering the content of the whole
portal.

A more advanced use case could be to directly insert the IP address in
the search field.

**In the following example the data are animized so a reader could
consider that instead of the previewed hash value, an IP address is
used**.

.. figure:: .img/request_ip.gif
   :alt: 

.. _header-n178:

How to search for events based on specific threat category.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are multiple threat categories available.

To name a few: ``legal`` , ``malware``, ``c&c``, ``blacklist``,
``phishing`` and ``exploit``.

A *simple* alternative could be to click on the bar that matches the
detected threat and filter only the specific type.

.. figure:: .img/phising.gif
   :alt: 

Another approach could be to click on the filter icon and in this way
specify the desired category, as can be seen in the next image.

.. figure:: .img/cc.gif
   :alt: 

.. _header-n186:

How to change the range of the available data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| The range of the dates that can be preview in the portal can change in
  multiple ways.
| The following image show three of the available ways. These can be
  summarized as simply by clicking on the current date that
  automatically transcribes to the current time, by inserting the date
  in text in the ``YYYY.MM.DD HH:mm:ss`` format or by using the builtin
  tool that provides quick suggestions.

.. figure:: .img/date_range.gif
   :alt:

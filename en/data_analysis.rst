Data Analysis
=============

Whalebone Portal (graphical user interface) gives the user number of
possibilities how to analyze what is happening on the DNS resolvers and
the network.


Threats
-------

Threats are special events where there is a DNS request for a domain
that is present within the reputation database. There are two types of
actions when a threat is detected. The first is to audit the event while
the second is to block it.

The action that is to be implemented depends on the policies that are
assigned to the specific resolver. For more on that please refer to
`Security Policies <http://docs.whalebone.io/cs/latest/local_resolver.html#security-policies>`__.

There are some pre-configured filters that can be applied on the data on
the portal. Some sample queries can be found below. These queries depict
the majority of the use cases but there is no hard limit as the
available search engine is **full-text** and *any* query can be compiled
impromptu.

You can watch step-by-step video guide `here. <https://docs.whalebone.io/en/latest/video_guides.html#threats>`__


How to search for audit/block events.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| There are two options in order to filter the different types of
  events. 
| In the first option a visual filter can be applied where the type that
  a user clicks is disabled from the graph. This can aid the process of
  having a basic overview of the traffic's qualities.

.. figure:: ./img/block_graph.gif
   :alt: 

How to search for a domain
~~~~~~~~~~~~~~~~~~~~~~~~~~

In order to search for a domain's instances in the events, the easiest way
is to click on it in the provided log history. Alternatively a query
could be issued in the search engine with the term: ``domain:<domain>``


How to search for events based on specific IP address.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A filtering of an IP address is possible by clicking on the specific
Source IP bar and in this way filtering the content of the whole
portal.

A more advanced use case could be to directly search for IP address in
the search field and use the operator ``client_ip`` such as: ``client_ip:<IP address>``.

.. figure:: ./img/requestip.gif
   :alt: 
   
How to search for events based on specific threat category.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are multiple threat categories available.

To name a few: ``malware``, ``c&c``, ``blacklist``,
``phishing``, ``coinminer``, ``spam``, and ``compromised``.

A *simple* alternative could be to click on the bar that matches the
detected threat and filter only the specific type.

.. figure:: ./img/phising.gif
   :alt: 

Another approach could be to click on the filter icon and in this way
specify the desired category, as can be seen in the next image.

.. figure:: ./img/cc.gif
   :alt: 

How to change the date range of the available data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| The date range of the data that can be previewed in the portal can
  change in multiple ways.
| The following image shows three of the available ways. These can be
  summarized as simply by clicking on the current date that
  automatically transcribes to the current time, by inserting the date
  in text in the ``YYYY.MM.DD HH:mm:ss`` format or by using the builtin
  tool that provides quick suggestions.

.. figure:: ./img/date_range.gif
   :alt: 

How to analyze a domain
~~~~~~~~~~~~~~~~~~~~~~~

In case to know further information about domain, especially what score 
Whalebone assigns to particular domain, when was first seen and categorized 
as malicious, if it falls under regulatory category or what external sources 
know about it, then watch step-by-step video `here. <https://docs.whalebone.io/en/latest/video_guides.html#domain-analysis>`__


DNS Traffic
-----------

The ``DNS Traffic`` tab contains an overview of the traffic that has
been logged on the resolver. It contains all the queries along with some
additional information such as the type, the answer and the TTL (time to
live) of the answer.

.. tip:: The data are subject to de-duplication. This means that the resolver
   logs only unique combinations of query, query type and answer per 24
   hour time frame. For this reason, a query might not be available on
   the portal even though it has been resolved.

You can watch step-by-step video guide `here. <https://docs.whalebone.io/en/latest/video_guides.html#dns-traffic>`__

Below are some of the most useful filtering options of the available data will be described.


How to view all queries of a specific type
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In order to view all queries of a specific type the most straight
forward way is to click on the filter icon and select the desired value.

.. figure:: ./img/query_type.gif
   :alt: 

Another option is to insert a query in the search field. This query
could be in the form ``query_type:<type>.`` The possible types are:
``A``,\ ``AAAA``, ``CNAME``, ``MX``, ``NS``, ``PTR``, ``RRSIG``,
``SPF``, ``SRV`` and\ ``TXT``.


How to view all answers of a specific type 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The answers can be filtered by selecting the specific bar in the
respective ``Answers`` field. Additionally, the answers can be viewed by
issuing a query in the form ``answer:<answer_type>``.
Useful answer types are ``NXDOMAIN`` or ``SERVFAIL``.

.. figure:: ./img/answer.gif
   :alt: 


How to search for a domain
~~~~~~~~~~~~~~~~~~~~~~~~~~

In order to search for a domain's instances in the logs, the easiest way
is to click on it in the provided l  og history. Alternatively a query
could be issued in the search engine with a fully qualified domain: ``query:<domain>.``
Please note the ``.`` at the end of the query.

A more fine-grained search can b e performed by searching for more
specific domain based on the available domain levels. The acceptable
search fields are ``domain_l1:<domain_l1>`` and
``domain_l2:<domain_l2>``.


How to change the date range of the available data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Please refer to `How to change the date range of the available
data <http://docs.whalebone.io/en/latest/data_analysis.html#how-to-change-the-date-range-of-the-available-data>`__
of the Threats section.


How to view DGA (Domain Generation Algorithm) indications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Whalebone provides a view of indicators of DGA instances. These
indications can be accessed by using the filter icon and selecting DGA
as can be seen below. Alternatively the query ``dga.class:1`` can be issued.

.. figure:: ./img/dga.gif
   :alt:

Fulltext filtering
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For more advanced usage, a fulltext filter can be applied to construct a composite query. You can filter for many fields however not all of them are searchable in all dashboards. 
Below you can find an overview of fields that are applicable for each dashboard:

- ``action`` - The action the resolver took with regards to the query. Possible values are "audit", "block" or "allow".
- ``accu`` -   The score of the queried domain at the time of the event. 
- ``client_ip``- The source IP of the DNS request.
- ``device_id`` - The internal identifier of the device (the Offnet app or the HOS agent)
- ``domain``    - The domain in the DNS query
- ``timestamp`` - The time of the event. The format is: 2022-10-07T18:14:39.000Z
- ``matched_iocs.classification.type`` - The type of the treat.
- ``geoip.continent_code``- The continent code of the IP in the DNS response. Fot example "AS" for Asia.
- ``geoip.country_code3`` - The country code of the IP in the DNS response. For example "CZ" for the Czech Republic.
- ``geoip.country_name``  - The name of the country of the IP in the DNS response. For example "United States".
- ``ip``                  - The IP in the DNS response that would be returned if the action was not "block".
- ``resolver_id``         - The id of the resolver which registered that event.

These fields can be concatenated using logical operators. ``AND, OR, NOT, <, >`` and the wildcard character ``*`` are supported. Strings do not have to be wrapped with quotes. An example of the syntax is as follows:
``action: block AND accu:>70 AND (client_ip: 10.20.30.41 OR 10.20.30.40 OR 192.168.*) AND NOT geoip.country_name: Germany AND matched_iocs.classification.type: malware AND NOT phishing`` 
When you run a fulltext query, it updates the content of the entire dashboard.

+--------------------------------------------------+---------------------------------------------------+----------------------------------------------+-------------------------------------------------------------------+
| DNS Traffic                                      | Threats                                           | Content                                      | Example value                                                     |
+==================================================+===================================================+==============================================+===================================================================+
| ``timestamp``                                    | ``timestamp``                                     | ``timestamp``                                |``2022-10-14T12:28:01.000Z``                                       |
+--------------------------------------------------+---------------------------------------------------+----------------------------------------------+-------------------------------------------------------------------+
| ``client``                                       | ``client_ip``                                     | ````                                         |``192.168.2.3``                                                    |
+--------------------------------------------------+---------------------------------------------------+----------------------------------------------+-------------------------------------------------------------------+
| ``domain``                                       | ``client_ip``                                     | ``request_ip``                               |``whalebone.io`` OR ``whale*one.io``                               |
+--------------------------------------------------+---------------------------------------------------+----------------------------------------------+-------------------------------------------------------------------+ 
| ``resolver_id``                                  | ``resolver_id``                                   | ``resolver_id``                              |``2404``                                                           |
+--------------------------------------------------+---------------------------------------------------+----------------------------------------------+-------------------------------------------------------------------+ 
| ``device_id``                                    | ``device_id``                                     | ``device_id``                                |``MB2A1b4OTDin3Xz6DgftAip72v57e``                                  |
+--------------------------------------------------+---------------------------------------------------+----------------------------------------------+-------------------------------------------------------------------+ 
| ``geoip.continent_code``                         | ``geoip.continent_code``                          | ````                                         |``EU``                                                             |
+--------------------------------------------------+---------------------------------------------------+----------------------------------------------+-------------------------------------------------------------------+ 
| ``geoip.country_code3``                          | ``geoip.country_code3``                           | ````                                         |``RU``                                                             |   
+--------------------------------------------------+---------------------------------------------------+----------------------------------------------+-------------------------------------------------------------------+ 
| ``geoip.country_name``                           | ``geoip.country_name``                            | ````                                         |``Russia``                                                         |      
+--------------------------------------------------+---------------------------------------------------+----------------------------------------------+-------------------------------------------------------------------+ 
| ``query_type``                                   | \-\-                                              | \-\-                                         |``A\|AAAA\|CNAME\|MX\|NS\|PTR\|RRSIG\|SPF\|SRV\|TXT``              |      
+--------------------------------------------------+---------------------------------------------------+----------------------------------------------+-------------------------------------------------------------------+ 
| ``answer_ip``                                    | ``ip``                                            | \-\-                                         |``174.85.249.36`` OR ``SERVFAIL`` OR ``NXDOMAIN``                  |      
+--------------------------------------------------+---------------------------------------------------+----------------------------------------------+-------------------------------------------------------------------+ 
| ``dga.class``                                    | \-\-                                              | \-\-                                         |``1\|0``                                                           |
+--------------------------------------------------+---------------------------------------------------+----------------------------------------------+-------------------------------------------------------------------+ 
| ``tunnel.class``                                 | \-\-                                              | \-\-                                         |``1\|0``                                                           |
+--------------------------------------------------+---------------------------------------------------+----------------------------------------------+-------------------------------------------------------------------+ 
| \-\-                                             | ``action``                                        | \-\-                                         |``block`` OR ``allow`` OR ``audit``                                |
+--------------------------------------------------+---------------------------------------------------+----------------------------------------------+-------------------------------------------------------------------+ 
| \-\-                                             | ``accu``                                          | \-\-                                         | from ``0`` to ``100``. < and > operators can be used too          |
+--------------------------------------------------+---------------------------------------------------+----------------------------------------------+-------------------------------------------------------------------+ 
| \-\-                                             | ``matched_iocs.classification.type``              | \-\-                                         |``malware\|c&c\|phishing\|coinminer\|spam\|compromised\|blacklist``|
+--------------------------------------------------+---------------------------------------------------+----------------------------------------------+-------------------------------------------------------------------+ 
| \-\-                                             | \-\-                                              | ``category``                                 |``porn``                                                           |
+--------------------------------------------------+---------------------------------------------------+----------------------------------------------+-------------------------------------------------------------------+ 
| \-\-                                             | \-\-                                              | ````                                         |````                                                               |
+--------------------------------------------------+---------------------------------------------------+----------------------------------------------+-------------------------------------------------------------------+ 
| \-\-                                             | \-\-                                              | ````                                         |````                                                               |
+--------------------------------------------------+---------------------------------------------------+----------------------------------------------+-------------------------------------------------------------------+ 
| \-\-                                             | \-\-                                              | ````                                         |````                                                               |
+--------------------------------------------------+---------------------------------------------------+----------------------------------------------+-------------------------------------------------------------------+ 


.. tip:: Filtering operators are placed statically to the URL address. Therefore, you can create your set of
	filters in advance (such as view on individual IPs) and to use them when necessary. Afterwards, you
	can place them to your CRM for the specific user’s account and to access the filtered view immediately. It
	will help saving your time when customer asks for the support as you can immediately open their
	details.

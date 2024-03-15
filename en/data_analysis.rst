Data Analysis
=============

Whalebone Portal (graphical user interface) gives the user number of
possibilities how to analyze what is happening on the DNS resolvers and
the network.

Content
-------

The **content** tab shows an overview of logged traffic subject to content filtering settings. If you do not have the content filter enabled or are not using it, nothing will be logged in this tab.

How to view all queries of a specific type:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The easiest way to select queries of a certain type is by clicking the **filter** icon and selecting the desired query type. There are several options to choose from, including ``Sexual Content``, ``Gambling``, ``Audio/video``, ``Games`` and other 13 categories out of 17 total. Alternatively you can click on of categories displayed on the pie graph under the **Category** section or directly in the plot showing all the data.


ow to search for a domain:
~~~~~~~~~~~~~~~~~~~~~~~~~~~

To search for domains, you can use the **Result Filter** text box to enter the name of the domain you are looking for. Other ways to search for a domain is by clicking the domain in the **Domain** section or directly in the log list in the same column.

How to change the date range of the available data:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The range of data that can be displayed in the portal preview can be changed in several ways. The basic selection method includes selecting predefined time windows (1,7, 14 or 30 days) from the drop-down list located next to the **results filter**. If desired, a specific time range can be specified using the **Start Date and Time** and **End Date and Time** windows.


By clicking on the pie graphs you can also filter out the **Client IP** and **Resolver**.




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

You can watch step-by-step video guide `here <https://docs.whalebone.io/en/latest/video_guides.html#dns-traffic>`__.

Below are some of the most useful filtering options of the available data will be described.


How to view all queries of a specific type:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The easiest way to select queries of a certain type is by clicking the **filter** icon and selecting the desired query type. There are several options to choose from, including ``A``, ``AAA``, ``CNAME``, ``MX``, ``NS``, ``PTR``, ``RRSIG``,
``SPF``, ``SRV`` and ``TXT``.


How to view all answers of a specific type:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the **Answers** window, you can select the desired answer, or in the log list in the **Answer** column, or click the desired answer.

How to search for a domain:
~~~~~~~~~~~~~~~~~~~~~~~~~~~

To search for domains, you can use the **Result Filter** text box to enter the name of the domain you are looking for. Other ways to search for a domain is by clicking the domain in the **Tier 2 Domains** section or directly in the log list in the same column.

How to change the date range of the available data:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The range of data that can be displayed in the portal preview can be changed in several ways. The basic selection method includes selecting predefined time windows (1,7, 14 or 30 days) from the drop-down list located next to the **results filter**. If desired, a specific time range can be specified using the **Start Date and Time** and **End Date and Time** windows.

How to view DGA (Domain Generation Algorithm) indications:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

DGA indications can be filtered in a similar way as in the case of displaying queries of a certain type, in this case just select the last record in the list - **DGA**


Threats
-------

Threats are special events where there is a DNS request for a domain
that is present within the reputation database. There are two types of
actions when a threat is detected. The first is to **audit** the event while
the second is to **block** it. **Audit** option only logs the domain but acces is possible.

The action that is to be implemented depends on the policies that are
assigned to the specific resolver. For more on that please refer to
`Security Policies <http://docs.whalebone.io/en/latest/security_policies.html>`__.

There are some pre-configured filters that can be applied on the data on
the portal. Some sample queries can be found below. These queries depict
the majority of the use cases but there is no hard limit as the
available search engine is **full-text** and *any* query can be compiled
impromptu.

You can watch step-by-step video guide `here. <https://docs.whalebone.io/en/latest/video_guides.html#threats>`__


How to search for audit/block events:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are two options for filtering different types of events. The first option, a visual filter can be used. Within the graph, you can click one of the actions (audit, block, allow) to filter it and display only the cases in which the event occurred. Second one is to click next to the **Result's filter** field on the **Filter button** and choose desired filtering option.

How to search for a domain:
~~~~~~~~~~~~~~~~~~~~~~~~~~

The easiest way to search for a domain is by clicking on a specific domain in the log hostory. The second way is by typing the domain name into the **Result Filter** field.


How to search for events based on specific IP address:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Filtering logs from a specific IP address is possible by selecting a specific source IP address in the log history. The second option is by entering the domain name in the **Result Filter** field.

How to search for events based on specific threat category:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There is a large number of threat categories.

Some of them are: *malware*, *c&c*, *blacklist*,
*phishing*, *coinminer*, *spam*, and *compromised*.

A simple way to find attacks is by selecting a specific category from the pie charts or in the log list under the **Threat Categories** column. Another option is to click the **Filter result** button next to the **Filter** field and select the desired filtering option.


How to change the date range of the available data:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The range of data that can be displayed in the portal preview can be changed in several ways.
The basic selection method includes choosing predefined time windows (1,7, 14 or 30 days) in the drop-down list next to the **results filter**. If necessary, a specific time range can be specified using the **Start Date and Time** and **End Date and Time** windows.

How to analyze a domain:
~~~~~~~~~~~~~~~~~~~~~~~~

In case to know further information about domain, especially what score 
Whalebone assigns to particular domain, when was first seen and categorized 
as malicious, if it falls under regulatory category or what external sources 
know about it, then watch step-by-step video `here <https://docs.whalebone.io/en/latest/video_guides.html#domain-analysis>`__.


Fulltext filtering
~~~~~~~~~~~~~~~~~~

For more advanced use, you can use the full-text filter and build a compound query.
These fields can be concatenated using logical operators. ``AND, OR, NOT, <, >`` and the wildcard character ``*`` are supported. Strings do not have to be wrapped with quotes. An example of the syntax is as follows:
``action: block AND accu:>70 AND (client_ip: 10.20.30.41 OR 10.20.30.40 OR 192.168.*)``
``AND NOT geoip.country_name: Germany AND matched_iocs.classification.type: malware AND NOT phishing`` 
When you run a fulltext query, it updates the content of the entire dashboard.

+--------------------------------------+-------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| Threats                              | Description                                                                               |  Example value                                                           |
+======================================+===========================================================================================+==========================================================================+
| ``timestamp``                        | The exact time when the resolver registered the DNS request / incident                    | ``2022-10-14T12:28:01.000Z``                                             |
+--------------------------------------+-------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| ``client_ip``                        | The source IP address which made the DNS request / incident                               | ``192.168.2.3``                                                          |
+--------------------------------------+-------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| ``domain``                           | The domain in the DNS query                                                               | ``whalebone.io`` OR ``whale*one.io``                                     |
+--------------------------------------+-------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| ``resolver_id``                      | The id of ther resolver which handled the event                                           | ``2404``                                                                 |
+--------------------------------------+-------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| ``device_id``                        | The device_id of the HOS agent                                                            | ``MB2A1b4OTDin3Xz6DgftAip72v57e``                                        |
+--------------------------------------+-------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| ``geoip.continent_code``             | The code of the continent from the php geoIP library                                      | ``AF | AN | AS | EU | NA | OC | SA``                                     |
+--------------------------------------+-------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| ``geoip.country_code3``              | The code of the country from the php geoIP library                                        | ``RU | CZ | US | CN | DE | ...``                                         |
+--------------------------------------+-------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| ``geoip.country_name``               | The name of the country from the php geoIP library                                        | ``Russia``                                                               |
+--------------------------------------+-------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| ``ip``                               | The IP in the DNS answer or the IP that would the resolver answer if it didn't block      | ``174.85.249.36`` OR ``SERVFAIL`` OR ``NXDOMAIN``                        |
+--------------------------------------+-------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| ``action``                           | The action that the resolver took with that specific query                                | ``block | allow | audit``                                                |
+--------------------------------------+-------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| ``accu``                             | The score of the domainat the time of the event                                           |  ``0..100`` < and > operators can be used too                            |
+--------------------------------------+-------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| ``matched_iocs.classification.type`` | The type of threat                                                                        | ``malware | c&c | phishing | coinminer | spam | compromised | blacklist``|
+--------------------------------------+-------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+

.. tip:: Filtering operators are placed statically to the URL address. Therefore, you can create your set of
	Filters in advance (such as view on individual IPs) and to use them when necessary. Afterwards, you
	can place them to your CRM for the specific user's account and to access the filtered view immediately. It
	will help saving your time when customer asks for the support as you can immediately open their
	details.

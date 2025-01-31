Data Analysis
=============

This section provides guidance on analyzing DNS traffic and leveraging insights within the Whalebone platform. Effective data analysis helps identify trends, optimize performance, and detect threats.

Tutorial: Accessing Data Analysis Tools
----------------------------------------

1. **Navigate to the DNS traffic section of the portal:**
   - Log in to the Whalebone portal.
   - Click on the **DNS traffic** tab under the main menu.

   .. image:: ./img/data_analysis_access.png
      :align: center

2. **Filter and View Data:**
   - Use predefined filters or create custom filters to analyze specific DNS queries or traffic patterns.

   .. image:: ./img/analytics_filters.png
      :align: center

3. **Export Data Reports:**
   - Select the desired time range and export data in CSV or other supported formats for offline analysis.

   .. image:: ./img/export_data_reports.png
      :align: center

How-To Guide: Advanced Data Analysis
-------------------------------------

### Threat Detection and Analysis

1. Open the **Threat Analysis** section under Analytics.
2. Identify blocked domains and their associated threat categories.
3. Review trends over time to detect potential anomalies or targeted attacks.

   .. image:: ./img/threat_analysis.png
      :align: center

Reference: Data Analysis Features
----------------------------------

- **Custom Filters:** Tailor data views to focus on specific domains, IP ranges, or query types.
- **Export Options:** Export reports for deeper offline analysis or compliance purposes.
- **Threat Intelligence:** Leverage categorized threat data for proactive network protection.

Threat Categories and Examples
Fulltext filtering
~~~~~~~~~~~~~~~~~~

For more advanced use, you can use the full-text filter and build a compound query. Fulltext filtering only works in the **Threats** panel.
.. warning::
   The **content** and **DNS trafic** dashboards does not support fulltext filtering at the moment. Only the clickable elements will result in filtering the data in the content dashboard.

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

Data Analysis
=============

Whalebone Portal differentiates among three data types: **Content**, **DNS Traffic**, and **Threats**. Each of these categories has its own tab in the portal, allowing users to easily navigate and analyze the data. All three views share the same structure and use the same filtering options, as described in the following sections.

The page structure is as follows:

* **Filters**: Located at the top of the page, allowing users to filter the data based on various criteria.
* **A graph with a traffic overview in time**: Located below the filters, providing visual representations of the data in time.
* **Pie charts**: Located below the graph, showing the distribution of data based on different categories.
* **Raw data**: Located at the bottom of the page, displaying the raw data in a tabular format.

All graphs and tables are interactive, allowing users to click specific elements to filter the data. For example, clicking on a specific category in the pie chart will filter the data and update all charts to show only entries that belong to that category.

More detailed filtering options are available at the top of the page, where users can select specific criteria to filter the data. These filters include options such as date range, content type, query type, and more. The filters apply to all charts and tables on the page, enabling users to analyze data based on their specific needs.

The row with filters contains the following options:

1. **Filter**: Opens a drop-down menu with various filtering options based on the type of data being analyzed.
2. **Saved filters**: Allows users to access their saved filter settings for future use, making it easier to apply the same filters again without having to set them up each time.
3. **Describe the filters you want to apply...**: A text box that allows users to enter specific criteria for filtering the data. This can include domain names, IP addresses, or other relevant information. The field supports full-text search and the AI mode, allowing users to build queries using natural language.
4. **Quick date range selection**: Provides predefined time windows (e.g., 1 day, 7 days) for quick filtering of data based on common time frames.
5. **From date selection**: Allows users to select a specific date and time to filter the data starting from that point.
6. **To date selection**: To date selection: Allows users to filter data up to a specific date and time.

.. figure:: ./img/data-analysis-1.png
   :alt: Filters
   :align: center

   Data analysis filters

.. tip:: Date selection can be performed in the graph, which shows the traffic overview over time. By clicking and dragging on the graph, users can select a time range, which automatically updates the filters and displays data for that period.

   .. figure:: ./img/data-analysis-2.gif
      :alt: Date selection in the graph
      :align: center

      Date selection in the graph

The **Describe the filters you want to apply...** search field supports natural language queries, allowing users to build complex filters using simple language. For example, users can enter queries like "Show me all blocked domains related to gambling in the last 7 days" or "Find all DNS requests from IP address 192.168.1.1". The AI mode will interpret the query and apply the appropriate filters to display the relevant data.

Apart from the AI mode, the search field also supports full-text search, allowing users to enter specific keywords or phrases to filter the data. For example, entering a specific domain name or IP address will filter the data to show only entries that match the search criteria. It also supports wildcard characters, enabling users to search for patterns in the data. For instance, entering "example.*" will filter the data to show all entries that contain domains starting with "example.".

The "Add to filter" buttons in the pie charts with top 10 clients and domains allow users to quickly add all items from the chart to the filters. For example, if a user clicks "Add to filter" in the top 10 clients pie chart, all client IP addresses listed in that chart will be added to the filters, allowing the user to analyze data specifically for those clients.

.. figure:: ./img/data-analysis-5.png
   :alt: Add to filter
   :align: center

   Add to filter button in pie charts

All filters are saved in the user's session and will be applied when the user returns to the portal. This means that if a user applies specific filters and then leaves the portal or switches to a different part of the portal, those filters will still be in place when they return, allowing for a seamless experience without the need to reapply filters each time.

Raw DNS data can be exported to a CSV file using the button at the top of the table. The exported data will include all data currently filtered on the portal. Please note that the export is limited to 1,000,000 records. If you need to export more data, it is recommended to apply additional filters to narrow the results before exporting or to use the API to retrieve data.

Content
-------

The **Content** tab shows an overview of blocked domains subject to content filtering settings. If you do not have the content filter enabled or are not using it, nothing will be logged in this tab. There are 18 categories to choose from, including ``Sexual Content``, ``Gambling``, ``Audio/video``, or ``Games``.

Filtering Options
~~~~~~~~~~~~~~~~~

The Filter button contains different options based on the type of data being analyzed. Here are the available options for each data type:

* **Client IP**: Filter the data based on specific client IP addresses.
* **Device ID**: Filter the data based on specific device IDs.
* **Domain**: Filter the data based on specific domain names.
* **Content category**: Filter the data based on specific content categories (e.g., Sexual Content, Gambling, Audio/video, Games).
* **Legal**: Filter the domains blocked by regulatory restrictions.
* **Resolver ID**: Filter the data received by specific resolvers.

Domain Categorization Change
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In case of a domain categorized incorectly you can check which categories a domain falls into by using the **Domain Analysis** tool located in the user menu. After entering a domain, the **Content Categorization** section will appear, showing the categories the domain falls into and also offering a **Suggest Category Change** button to suggest a change in categorization. It is also possible to report a domain as a false negative using the **Report as malicious** button.

CSV Export
~~~~~~~~~~

The raw data contains the following details:

* date
* client's IP address
* device name
* domain
* content category type
 
DNS Traffic
-----------

The ``DNS Traffic`` tab provides an overview of traffic logged on resolvers. It contains all queries, along with additional information such as the query type, the answer, and the TTL (Time To Live).

.. tip:: The data is subject to de-duplication. This means the resolver logs only unique combinations of query, query type, and answer within a 24-hour time frame. For this reason, a query might not appear on the portal even if it has been resolved.

You can watch a step-by-step video guide :ref:`here<DNS traffic video>`.

Filtering Options
~~~~~~~~~~~~~~~~~

The Filter button contains different options based on the type of data being analyzed. Here are the available options for each data type:

* **Client IP**: Filter the data based on specific client IP addresses.
* **Device ID**: Filter the data based on specific device IDs.
* **Domain**: Filter the data based on specific domain names.
* **Query Type**: Filter the data based on specific query types (e.g., A, AAAA, CNAME).
* **Query**: Filter the data based on specific DNS queries.
* **DNS Tunnel**: Filter out domains associated with DNS tunneling in DNS traffic.
* **DGA**: Filter out data clasified as DGA (Domain Generation Algorithm) in DNS traffic.
* **Country code**: Filter the data based on specific country codes.
* **Segment**: Filter the data based on specific segments.
* **Brand**: Filter the data based on specific brands.
* **Resolver ID**: Filter the data received by specific resolvers.
* **Answer**: Filter the data based on specific DNS answers.
* **Protocol**: Filter the data based on specific protocols used in DNS traffic (e.g., UDP, TCP, DoH, or DoT).
* **EDE code**: Filter the data based on specific Extended DNS Error (EDE) codes in DNS traffic.

How to Report "False Negative"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In some cases, the score classification of a domain may not be correct. If you believe a domain should be blocked but is not, you can report it as malicious using the **Report as Malicious** button to initiate a domain review request. This option is located in the log table under the arrow icon for each query.

.. figure:: ./img/data-analysis-3.png
   :alt: Report false negative
   :align: center

   Report false negative

CSV Export
~~~~~~~~~~

The CSV export contains the following details:

* date
* client's IP address
* device name
* query type
* query
* second-level domain
* country
* answer
* TTL (Time to Live)
* class

Threats
-------

Threats are special events in which a DNS request for a domain is present in the reputation database. There are two types of actions when a threat is detected. The first is to **audit** the event, which only logs the domain; however, access is still possible. The second action is a **block** that prevents requests to the malicious site and redirects the user to the blocking page.

You can watch a step-by-step video guide :ref:`here<Threats video>`.

Threats are categorized by their types. The categories are:

* Blacklist
* C&C
* Coinminer
* Compromised
* Malware
* Phishing
* Spam

How to Search for Events Blocked by a Deny List
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tip:: The Deny list category is a custom list maintained by the customer's administrators to block domains on demand. Blacklist is part of the Whalebone threat intelligence data for known domains that host multiple threats, or when the exact category could not be determined.

You can select the deny list category in the pie charts or in the log list under the **Threat Categories** column. Another option is to click the **Filter** button and set the **Deny list** filter to **Yes**.

How to Analyze a Domain
~~~~~~~~~~~~~~~~~~~~~~~

To learn more about domain analysis, scoring of malicious domains, domain categories, or what external sources know about them, watch the step-by-step video :ref:`here<Domain analysis video>`.

How to Report "False Positive"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In some cases, the score of a domain may be wrong. If you believe a domain should not be blocked but is, you can report it as misclassified using the **Report False Positive** button to initiate a domain review request.

.. figure:: ./img/data-analysis-4.png
   :alt: Report false positive
   :align: center

   Report false positive

Filtering Options
~~~~~~~~~~~~~~~~~

* **Client IP**: The source IP address that made the DNS request or incident
* **Device ID**: The unique identifier of the device that made the DNS request or was involved in the incident
* **Domain**: The domain in the DNS query
* **Action**: The action that the resolver took with that specific query, such as ``block``, ``allow``, and ``audit``
* **Threat category**: The category of the threat, such as ``malware``, ``phishing``, or ``c&c`` (command and control)
* **Threat name**: The specific name of the threat, which may provide more detailed information about the nature of the threat
* **Deny list**: Enable or disable the filter for domains that are present in deny lists
* **Country code**: The country code associated with the client's IP address, which can provide insights into the geographic location of the source of the DNS request or incident
* **Resolver ID**: The unique identifier of the resolver that processed the DNS request or was involved in the incident, which can help identify patterns or specific resolvers that may be associated with certain types of threats       

CSV Export
~~~~~~~~~~

The CSV export contains the following details:

* date
* action
* client's IP address
* device name
* country
* domain
* score
* threat category
* threat name
* resolver's name

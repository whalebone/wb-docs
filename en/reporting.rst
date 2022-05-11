.. _header-n233:

Reporting
=============

Whalebone Portal provides the tools in order to configure various reporting options and manage the access to Whalebone API.

.. _header-n236:

Reports
-------

Reporting capabilities can be configured from the drop-down menu under a user's account.
The properties that can be customized, include the frequency that the reports are being delivered, the preferred day of the week, the language and the recipients.

.. note:: The default recipient is the owner of the account and the reports are delivered to their respective registered email address.

.. image:: ./img/report-configuration.gif
   :align: center


Alerts
-------
Whalebone alerting provides live updates about key information such as resolver's health, resolution status, hardware usage and it also informs about crucial security incidents and many more.
All of these information can be passed through multiple channels e.g. email, slack, syslog or webhook. You can create new alert from predefined templates and alerts can be then customized by editing their parameters.
You can watch step-by-step video guide `here <https://docs.whalebone.io/en/latest/video_guides.html#alerts>`


.. note:: In order to turn on an alert, you first need to assign a destination for it. Click the alert name to expand it in detail and select the destination from the box. Multiple destinations may be selected by shift-clicking the addresses.

DNS traffic - count of unique requests from IP
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This alert is triggered when a single source IP reaches the limit of unique requests with defined attributes
   Parameters:
   * MINUTES: time window in minutes (Default=15)
   * TRESHOLD: number of events in timeframe to trigger alert (Default=100)
   * QUERY_TYPE: Filter by DNS query type (Default=*)
   * RESPONSE_TYPE: Filter by DNS response (Default=*)
   * IP_WILDCARD: Include only these these comma-separated IP addresses in the alert (Default=*)
   * IP_WILDCARD_IGNORE: Ignore these comma separated domains in the alert (Default=none)
   * DOMAIN_WILDCARD: Include only these comma separated domains in the alert(Default=*)
   * DOMAIN_WILDCARD_IGNORE: Ignore these comma separated domains in the alert (Default=none)
   * DGA: Filter by domain generation algorithm - Only DGA, Without DGA or both (Default=*)
   

DNS traffic - increased percentage of queries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This Alert will be sent when number of DNS traffic logs is percentually greater over configured time period.
   Parameters:
   * MINUTES: Timeframe - time window (Default=15)
   * PERCENT: Percentage increase (e.g. 200%) - difference between two intervals (Default=50)
   * QUERY_TYPE: Filter by DNS query type (Default=*)
   * RESPONSE_TYPE: Filter by DNS response (Default=*)


DNS traffic - possible homograph attack
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This Alert is sent when a possible homograph attack for a specified domain is detected
   Parameters:
   * DOMAIN: Domain to monitor for possible homograph attacks (One alert can monitor only one domain)
   * DISTANCE: Number of characters that can differ in the phishing domain (Default=1)
   * DOMAIN_WILDCARD_IGNORE: Ignore this list of comma separated domains in the alert. 
   In case DISTANCE is larger than 1, there will be a detection on domains that support both a global and regional top level formats. 
   It is recommended to add the legitimate domains in the whitelists in order to avoid unnecessary alarms. (Default=none)


DNS traffic - treshold for unique queries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This Alert is sent when threshold for filtered unique DNS logs is reached
   Parameters:
   * MINUTES: Timeframe - time window (Default=15)
   * TRESHOLD: Threshold - number of events in timeframe to trigger alert (Default=100)
   * QUERY_TYPE: Filter by DNS query type (Default=*)
   * RESPONSE_TYPE: Filter by DNS response (Default=*)


Resolver - Cloud communication failure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Resolver - Insufficient hardware resources
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Resolver - Resolution service failure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Threats - count during intervals
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Threats - event detection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Threats - newly blocked domain
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note:: When the alerting channel is syslog, by default TCP or TLS is supported as the transport layer protocol.

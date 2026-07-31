======================
Logmanager Integration
======================

Logmanager is a log management and SIEM platform that enables organizations to centrally collect, store, and analyze logs from across their IT environment.

Whalebone supports integration with Logmanager through Syslog export. This allows organizations to stream security and operational data from Whalebone to Logmanager, where events can be centralized, analyzed, and correlated with other data sources. Logmanager provides built-in support for processing Whalebone logs and includes detailed instructions for configuring the integration. Its documentation covers the required Logmanager configuration, supported log sources, and parser details.

* For step-by-step instructions on configuring Logmanager, refer to: `Logmanager documentation <https://doc.logmanager.com/3.12.0/log-source-devices/whalebone/>`_

* To configure Syslog export in Whalebone, follow the :doc:`syslog_integration` guide.

Once Syslog export is enabled in Whalebone and Logmanager is configured to receive the logs, Whalebone events are automatically processed by the Logmanager parser and are ready for further analysis and monitoring.
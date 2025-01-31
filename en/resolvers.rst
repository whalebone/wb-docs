Resolver Management
===================

This section provides guidance on managing DNS resolvers using the Whalebone portal, focusing on resolver states, deploying configurations, managing network segments, customizing blocking pages, and upgrading or rolling back resolvers.

Overview of Resolver States
----------------------------

The **Resolvers** section in the Whalebone portal provides a comprehensive overview of all configured resolvers, including:

- **Active Resolvers:** Displayed with real-time status and query volume.
- **Unavailalbe Resolvers:** Indicated by the status of Unavailable.
- **Resolver Details:** Name, interfaces, and operating status.

   .. image:: ./img/resolver_overview.png
      :align: center

Deploying Configurations
-------------------------

1. **Access Resolver Settings:**
   - Navigate to the **Resolvers** tab in the Whalebone portal.
   - Select a resolver to view or modify its configuration.

   .. image:: ./img/resolver_settings.png
      :align: center

2. **Apply Configuration Changes:**
   - In the Policy assignment a selection of options can be made.
   - Update parameters such as blocking page and policy assignment selection.
   - Save the changes to automatically deploy the updated configuration.

   .. image:: ./img/resolver_policy_settings.png
      :align: center

3. **Advanced configuration:**
   - In this section you can select the DNS resolution configuration for the resolver.
   - Expert settings are also available
   - Disable DNS logging
   - Adjusting the size of the logs on the resolver
   - Configuration of the syslog destinations for exporting logs directly to SIEM

   .. image:: ./img/resolver_advanced_configuration.png
      :align: center


Why Resolver Management is Essential
-------------------------------------

- **Reliability:** Real-time visibility ensures prompt issue detection and resolution.
- **Customization:** Tailor configurations to meet network-specific needs.
- **Control:** Manage DNS behavior for each network segment with precision.
- **Scalability:** Easily upgrade or rollback resolvers to adapt to evolving requirements.
- **User Experience:** Provide informative and branded blocking pages for end users.

Using the Whalebone portal for resolver management simplifies DNS configuration, enhances visibility, and provides granular control over your network.

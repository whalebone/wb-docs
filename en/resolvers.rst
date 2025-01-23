Resolver Management
===================

This section provides guidance on managing DNS resolvers using the Whalebone portal, focusing on resolver states, deploying configurations, managing network segments, customizing blocking pages, and upgrading or rolling back resolvers.

Overview of Resolver States
----------------------------

The **Resolvers** section in the Whalebone portal provides a comprehensive overview of all configured resolvers, including:

- **Active Resolvers:** Displayed with real-time status and query volume.
- **Offline Resolvers:** Highlighted for immediate attention.
- **Resolver Details:** Including type (cloud or local), location, and configured settings.

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
   - Update parameters such as upstream DNS servers, caching policies, or logging preferences.
   - Save the changes to automatically deploy the updated configuration.

3. **Verify Deployment:**
   - Use the **Activity** tab to confirm that the resolver is functioning as expected.

   .. image:: ./img/config_verification.png
      :align: center

Managing Configurations Per Network Segment
-------------------------------------------

1. **Define Network Segments:**
   - Use the **Network Segments** feature in the portal to divide your network into logical sections based on IP ranges.

   .. image:: ./img/network_segments.png
      :align: center

2. **Assign Resolver Configurations:**
   - Apply specific resolver settings or policies to individual network segments.
   - This ensures granular control over DNS resolution and filtering for different parts of your network.

   .. image:: ./img/segment_config.png
      :align: center

3. **Monitor Segment-Specific Traffic:**
   - Use traffic analytics to review query volume and trends per network segment.

Customizing Blocking Pages
--------------------------

1. **Access Blocking Page Settings:**
   - In the portal, navigate to the **Blocking Pages** section under resolver settings.

   .. image:: ./img/blocking_pages_settings.png
      :align: center

2. **Customize Appearance and Messaging:**
   - Modify the layout, branding, and message displayed on DNS blocking pages.

   .. image:: ./img/blocking_page_customization.png
      :align: center

3. **Test Blocking Pages:**
   - Simulate a DNS query that triggers a blocking page to ensure the customization appears as intended.

   .. image:: ./img/blocking_page_test.png
      :align: center

Upgrading or Rolling Back Resolvers
------------------------------------

1. **Access Upgrade Options:**
   - Navigate to the **Resolvers** tab in the Whalebone portal.
   - Select the resolver you want to upgrade or rollback.

   .. image:: ./img/resolver_upgrade_access.png
      :align: center

2. **Perform an Upgrade:**
   - In the **Upgrade** section, select the desired version and click **Upgrade**.
   - Monitor the progress in the portal to ensure a successful update.

   .. image:: ./img/resolver_upgrade_progress.png
      :align: center

3. **Rollback to a Previous Version:**
   - If issues occur after an upgrade, use the **Rollback** option to revert to the previous stable version.
   - Confirm the rollback and verify resolver functionality.

   .. image:: ./img/resolver_rollback.png
      :align: center

Why Resolver Management is Essential
-------------------------------------

- **Reliability:** Real-time visibility ensures prompt issue detection and resolution.
- **Customization:** Tailor configurations to meet network-specific needs.
- **Control:** Manage DNS behavior for each network segment with precision.
- **Scalability:** Easily upgrade or rollback resolvers to adapt to evolving requirements.
- **User Experience:** Provide informative and branded blocking pages for end users.

Using the Whalebone portal for resolver management simplifies DNS configuration, enhances visibility, and provides granular control over your network.

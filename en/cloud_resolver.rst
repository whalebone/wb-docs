Cloud Resolver Configuration
============================

This section provides guidance on configuring and managing cloud resolvers within the Whalebone platform. Cloud resolvers offer scalability and simplicity for DNS management.

Tutorial: Setting Up a Cloud Resolver
-------------------------------------

1. **Access the Cloud Resolver Section:**
   - Log in to the Whalebone portal.
   - Navigate to the **Cloud Resolvers** tab in the main menu.

   .. image:: ./img/cloud_resolver_access.png
      :align: center

2. **Add a New Cloud Resolver:**
   - Click on **Add Resolver** and specify a name and description.
   - Select the region closest to your network for optimal performance.

   .. image:: ./img/add_cloud_resolver.png
      :align: center

3. **Configure DNS Forwarding:**
   - Update your network’s DNS settings to forward queries to the Whalebone cloud resolver IP addresses.
   - Ensure that firewalls or security systems allow communication with these IPs.

   .. image:: ./img/cloud_dns_forwarding.png
      :align: center

4. **Verify Resolver Activity:**
   - Monitor the **Activity Logs** in the portal to confirm that queries are being forwarded and resolved correctly.

   .. image:: ./img/cloud_resolver_activity.png
      :align: center

How-To Guide: Managing Cloud Resolvers
--------------------------------------

### Monitoring Resolver Performance

1. Navigate to the **Analytics** tab under the Cloud Resolvers section.
2. Review metrics such as query volume, resolution times, and blocked threats.

   .. image:: ./img/cloud_resolver_analytics.png
      :align: center

### Updating Cloud Resolver Settings

1. Access the **Settings** tab for the specific resolver.
2. Modify configuration options such as logging preferences, response policies, or custom DNS rules.
3. Save changes and monitor activity to ensure proper functionality.

   .. image:: ./img/cloud_resolver_settings.png
      :align: center

Reference: Cloud Resolver Features
----------------------------------

- **Scalability:** Automatically adjusts to handle increased query volume.
- **Redundancy:** Built-in failover to ensure continuous availability.
- **Security:** Protects against DNS-based threats with real-time filtering.
- **Customization:** Allows tailored DNS rules and policies.

Explanation: Benefits of Cloud Resolvers
----------------------------------------

- **Ease of Use:** Simplifies DNS management with minimal configuration.
- **High Availability:** Ensures reliable DNS resolution with redundant infrastructure.
- **Real-Time Analytics:** Provides insights into DNS traffic and threat activity.

Cloud resolvers are ideal for organizations looking for a scalable and low-maintenance DNS solution that offers robust performance and security.

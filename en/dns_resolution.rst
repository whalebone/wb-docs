DNS Resolution Configuration
============================

This section provides a detailed guide to configuring DNS resolution within the Whalebone system. It covers setup steps, troubleshooting tips, and advanced configurations to optimize DNS performance.

Tutorial: Setting Up DNS Resolution
------------------------------------

1. **Access the Configuration Settings:**
   - Log in to the Whalebone portal.
   - Navigate to the **Configuration** section.
   - Navigate to the **DNS resolution** section.

   .. image:: ./img/DNS_resolution_section.png
      :align: center

2. **Configure Upstream Resolvers:**
   - Define upstream DNS servers for the resolver to query.
   - Click on Forward queries to -> Following domains
   - Define your internal domains and the corresponding internal DNS resolver IP address to handle them
   

   .. image:: ./img/upstream_resolvers_configuration.png
      :align: center


How-To Guide: Advanced DNS Configuration
-----------------------------------------

Reference: DNS Resolution Parameters
-------------------------------------

- **Upstream Resolvers:** Specify DNS servers to handle external queries.

Explanation: Why DNS Resolution Configuration Matters
-----------------------------------------------------

- **Flexibility:** Conditional forwarding allows granular control over domain-specific DNS behavior.

Proper DNS resolution configuration is essential to ensure reliable, secure, and efficient DNS operations within your network.

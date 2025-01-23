Deployment: Cloud
=================

Whalebone’s cloud deployment option offers a scalable and maintenance-free solution for DNS protection. This section guides you through setting up and managing a cloud-based deployment.

Tutorial: Setting Up Cloud Deployment
-------------------------------------

1. **Access the Cloud Portal:**
   - Log in to the Whalebone cloud portal using your credentials.
   - Navigate to the **Deployment** section.

   .. image:: ./img/cloud_portal_access.png
      :align: center

2. **Configure Your Network:**
   - Obtain the IP addresses of the Whalebone cloud resolvers.
   - Update your network’s DNS settings to forward traffic to these resolvers.

   .. image:: ./img/cloud_resolver_settings.png
      :align: center

3. **Verify DNS Traffic:**
   - Check the **DNS Traffic** section in the portal to confirm traffic is being forwarded correctly.

   .. image:: ./img/cloud_traffic_verification.png
      :align: center

4. **Enable Advanced Features:**
   - Use the portal to configure policies, filtering rules, and advanced security features.

   .. image:: ./img/cloud_advanced_settings.png
      :align: center

How-To Guide: Managing Cloud Deployment
----------------------------------------

### Monitoring DNS Traffic

1. Navigate to the **Traffic Analytics** section in the portal.
2. Review real-time and historical DNS traffic logs.

   .. image:: ./img/cloud_traffic_analytics.png
      :align: center

### Updating Policies and Rules

1. Go to the **Policies** tab in the cloud portal.
2. Add, edit, or remove DNS filtering rules as needed.

   .. image:: ./img/cloud_policy_update.png
      :align: center

Reference: Cloud Deployment Details
------------------------------------

- **Resolver IPs:** IP addresses are provided during setup and must be configured in your network.
- **Supported Features:** Advanced DNS filtering, threat detection, and traffic analytics.
- **Accessibility:** Managed entirely through the Whalebone cloud portal.

Explanation: Why Choose Cloud Deployment
----------------------------------------

- **Scalability:** Automatically handles increasing traffic with no hardware limitations.
- **Maintenance-Free:** Updates and patches are managed by Whalebone.
- **Accessibility:** Manage and monitor DNS traffic from anywhere via the cloud portal.

Cloud deployment is an ideal solution for organizations seeking a hassle-free and scalable approach to DNS protection.

Deployment: Whalebone Immunity
=============================

Whalebone Immunity provides advanced security features tailored to protect your network against threats. This section explains how to deploy and configure Whalebone Immunity.

Tutorial: Setting Up Whalebone Immunity
---------------------------------------

1. **Prepare Your Environment:**
   - Ensure that your infrastructure meets the system requirements for Whalebone Immunity.
   - Verify administrative access to the systems.

2. **Install Whalebone Immunity:**
   - Download the installation package from the portal.
   - Run the installation command in your terminal

   - Follow the on-screen prompts to complete the installation.

   .. image:: ./img/immunity_installation.png
      :align: center

3. **Activate Your License:**
   - Access the Whalebone Immunity portal.
   - Enter your license key to activate the service.

   .. image:: ./img/license_activation.png
      :align: center

4. **Verify Deployment:**
   - Test the setup by resolving DNS traffic through Whalebone Immunity.
   - Check traffic visibility in the dashboard.

   .. image:: ./img/immunity_dashboard.png
      :align: center

How-To Guide: Managing Whalebone Immunity
-----------------------------------------

### Updating the Immunity System

1. Use the package manager to update the system:
   ```bash
   sudo apt update && sudo apt upgrade whalebone-immunity
   ```
2. Verify that the update is successfully applied.

### Configuring Advanced Features

1. Enable advanced threat protection via the portal settings.
2. Configure custom rules for DNS filtering.

   .. image:: ./img/advanced_settings.png
      :align: center

Reference: System Requirements
-------------------------------

- **Operating System:** Ubuntu 20.04+, CentOS 8+, or Debian 10+.
- **Hardware:** Minimum 4 CPU cores, 8GB RAM, and 50GB storage.
- **Network:** Stable internet connection for real-time updates.

Explanation: Benefits of Whalebone Immunity
-------------------------------------------

- **Enhanced Security:** Advanced threat detection and DNS filtering to protect against malicious activity.
- **Customizable Rules:** Tailor DNS filtering to your organization’s specific needs.
- **Real-Time Updates:** Stay protected with automatic updates against emerging threats.

By deploying Whalebone Immunity, you ensure robust protection for your network while maintaining flexibility and control.

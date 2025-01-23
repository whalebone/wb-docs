Quickstart
==========

This guide will help you set up your Whalebone account and verify that DNS traffic is being forwarded correctly. It is structured to follow the Diátaxis framework for clarity and usability.

Tutorial: Setting Up Whalebone
------------------------------

1. **Create Your Portal Account:**
   - Access the URL from your activation email.
   - Set up your account password. While no complexity is enforced, it is highly recommended to use a unique and non-trivial password to prevent unauthorized access.

   .. image:: ./img/password_setup.png
      :align: center

   - Log in with your username and newly created password.

   .. image:: ./img/login.png
      :align: center

2. **Verify DNS Traffic:**
   - Forward DNS traffic to Whalebone resolvers (cloud or local).
   - Check the **DNS traffic** section in the portal to view individual requests and responses. Traffic should appear within a few minutes after setup.

   .. image:: ./img/dns_traffic.png
      :align: center

   - If no traffic is visible after several hours, contact Whalebone support for assistance in troubleshooting your configuration.

How-To Guide: Checking DNS Resolution
--------------------------------------

To manually verify that DNS traffic is being resolved through Whalebone:

1. Use the `nslookup` tool on a Windows or Linux machine.
2. Set the Whalebone resolver IP and resolve a domain name. For example:

   .. sourcecode:: bash
      
      localhost:~$ nslookup whalebone.io
      Server:         193.32.92.32
      Address:        193.32.92.32#53

      Non-authoritative answer:
      Name:   whalebone.io
      Address: 75.2.70.75
      Name:   whalebone.io
      Address: 99.83.190.102

Reference: Whalebone Resolvers
------------------------------

- **Resolver IPs:** Ensure the correct Whalebone resolver IPs are configured on your network.
- **Supported Tools:** The `nslookup` tool is recommended for manual checks, but alternatives like `dig` or `host` can also be used.

Explanation: Importance of DNS Traffic Visibility
--------------------------------------------------

- **Privacy and Security:** Unauthorized access can jeopardize user privacy and misuse DNS configuration to harm your network.
- **Troubleshooting:** Visibility into DNS traffic helps identify misconfigurations or network issues quickly.

For more detailed instructions or troubleshooting, refer to other sections of this documentation or contact Whalebone support.

Deployment Options
==================

Whalebone offers a variety of deployment options tailored to different environments and use cases. This section will help you understand the available deployment methods and choose the best one for your needs.

Tutorial: Choosing a Deployment Method
--------------------------------------

1. **Evaluate Your Environment:**
   - Determine whether your infrastructure is on-premises, cloud-based, or hybrid.
   - Identify your network size and specific DNS filtering needs.

2. **Review Deployment Options:**
   - On-Premises Deployment: Install Whalebone DNS resolvers locally on your infrastructure.
   - Cloud Deployment: Use Whalebone’s managed cloud resolvers for minimal setup and maintenance.
   - Hybrid Deployment: Combine on-premises and cloud-based resolvers for flexibility.

3. **Select the Best Option:**
   - Based on your environment, select the appropriate deployment option.
   - For guidance, refer to the corresponding sections in this documentation.

How-To Guide: Deploying Whalebone
---------------------------------

### On-Premises Deployment

1. Install the Whalebone Resolver package on a supported Linux distribution.
   
2. Configure the resolver from the Whalebone portal.
3. Test the setup to ensure proper DNS resolution.

### Cloud Deployment

1. Access the Whalebone cloud portal.
2. Claim your public IP ranges and select the policies for them.
3. Configure your network to forward DNS traffic to the provided cloud resolver IPs.
4. Verify traffic visibility in the portal.

### Hybrid Deployment

1. Deploy on-premises resolvers for internal network traffic.
2. Configure fallback or primary forwarding to Whalebone’s cloud resolvers.
3. Test traffic resolution in both environments.

Reference: Supported Platforms and Requirements
-----------------------------------------------

- **On-Premises:**
  - Supported OS: Ubuntu 20.04+, Debian 10+.
  - Hardware: Minimum 2 CPU cores, 4GB RAM, and 40GB storage.

- **Cloud:**
  - Whalebone cloud resolvers are pre-configured and do not require hardware or software installation.

- **Hybrid:**
  - Combine the requirements for on-premises and cloud setups.

Explanation: Why Deployment Method Matters
-------------------------------------------

- **On-Premises Benefits:** Full control over DNS resolution and internal traffic privacy.
- **Cloud Benefits:** Minimal maintenance, automatic updates, and scalability.
- **Hybrid Benefits:** Balances control and flexibility, ideal for diverse environments.

Choosing the right deployment option ensures optimal performance, security, and adaptability for your network.

Security Policies
=================

Whalebone allows administrators to define and manage security policies to control DNS behavior and protect against threats. This section provides comprehensive details on malicious filtering thresholds, threat types, allow and deny lists, regulatory restrictions, content filtering, and threat categories.

Tutorial: Creating and Deploying a Security Policy
--------------------------------------------------

1. **Access the Security Policies Section:**
   - Log in to the Whalebone portal.
   - Navigate to the **Security Policies** tab under the main menu.

   .. image:: ./img/security_policies_access.png
      :align: center

2. **Create a New Policy:**
   - Click on **Add Policy** and provide a name and description for the policy.
   
3. **Configure Policy Rules:**
   - Add rules to block, allow, or log specific domains or categories (e.g., malware, phishing).
   - Customize the content filtering options.
   - Select the Regulatory restrictions for your location.

4. **Set Malicious Filtering Thresholds:**
   - Define thresholds for identifying malicious domains based on threat scores.
   - Adjust sensitivity to balance security with user accessibility.

   .. image:: ./img/malicious_thresholds.png
      :align: center

5. **Save the Policy:**
   - Save the policy.


Threat Types and Categories
---------------------------

Whalebone security policies address a variety of threats by categorizing them into distinct groups to facilitate effective filtering and response. The primary categories include:

1. **Malware Domains:**
   - Domains hosting malicious software or facilitating downloads of harmful content.
   - Includes domains used for command and control (C2) communications.

2. **Phishing Sites:**
   - Fraudulent domains designed to steal sensitive information, including credentials and payment data.

3. **Spyware and Adware:**
   - Domains associated with unwanted software that tracks user activity or delivers intrusive advertisements.

4. **Botnet Activity:**
   - Domains linked to botnet operations, including data exfiltration and distributed denial-of-service (DDoS) attacks.

5. **Content-Based Threats:**
   - Categories of non-malicious but restricted content, such as adult content, gambling, or streaming services, configurable per organizational policy.

6. **Cryptojacking:**
   - Domains that hijack computational resources for cryptocurrency mining without user consent.

   .. image:: ./img/threat_categories.png
      :align: center

Reference: Comprehensive Policy Options
----------------------------------------

- **Policy Categories:**
  - Block specific categories like phishing, malware, and adult content.
  - Allow domains critical for business operations.

- **Custom Rules:**
  - Build allowlists or blocklists to meet organizational needs.
  - Define query logging preferences for better visibility.

- **Policy Scope:**
  - Apply globally or restrict to specific resolvers or segments.

Explanation: The Role of Security Policies
------------------------------------------

- **Enhanced Protection:** Blocks harmful DNS queries to prevent security threats.
- **Operational Compliance:** Ensures adherence to organizational and regulatory requirements.
- **Granular Control:** Allows precise DNS traffic management through targeted policies.

By effectively using security policies, administrators can strengthen network defenses, ensure smooth operations, and meet compliance goals with ease.

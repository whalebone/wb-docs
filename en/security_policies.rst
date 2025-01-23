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
   - Define the scope, specifying whether the policy applies to all resolvers or specific network segments.

   .. image:: ./img/add_security_policy.png
      :align: center

3. **Configure Policy Rules:**
   - Add rules to block, allow, or log specific domains or categories (e.g., malware, phishing).
   - Customize response messages and define blocking behavior (e.g., blocking pages or redirects).

   .. image:: ./img/configure_policy_rules.png
      :align: center

4. **Set Malicious Filtering Thresholds:**
   - Define thresholds for identifying malicious domains based on threat scores.
   - Adjust sensitivity to balance security with user accessibility.

   .. image:: ./img/malicious_thresholds.png
      :align: center

5. **Deploy the Policy:**
   - Save the policy and assign it to resolvers or network segments.
   - Confirm that the policy is active in the **Policies Overview** section.

   .. image:: ./img/policies_overview.png
      :align: center

How-To Guide: Managing Security Policies
-----------------------------------------

### Editing an Existing Policy

1. Navigate to the **Security Policies** tab in the portal.
2. Select the policy to be edited and adjust its rules, scope, or other settings.
3. Save the changes to update the active policy.

   .. image:: ./img/edit_security_policy.png
      :align: center

### Monitoring Policy Effectiveness

1. Open the **Analytics** tab to review the impact of the policy.
2. Analyze metrics such as the number of blocked, allowed, or logged queries.

   .. image:: ./img/policy_analytics.png
      :align: center

3. Identify patterns or anomalies that may require policy adjustments.

### Configuring Allow and Deny Lists

1. **Allow Lists:**
   - Add domains to the allow list to bypass all filtering.
   - Useful for business-critical services.

   .. image:: ./img/allow_list.png
      :align: center

2. **Deny Lists:**
   - Add domains to the deny list to block them regardless of category filtering.

   .. image:: ./img/deny_list.png
      :align: center

### Regulatory Restrictions

1. Enable country-specific restrictions to comply with local regulations.
2. Restrict access to content based on geographic location or legal requirements.

   .. image:: ./img/regulatory_restrictions.png
      :align: center

### Applying Policy Changes Globally

1. Use the **Bulk Apply** feature to deploy updates across multiple resolvers or network segments.
2. Verify changes using the **Activity Logs** section.

Content Filtering
------------------

1. **Enable Content Categories:**
   - Activate predefined content categories such as adult content, gambling, or social media.
   - Customize filtering levels for each category based on organizational requirements.

   .. image:: ./img/content_filtering.png
      :align: center

2. **Refine Content Filtering:**
   - Use analytics to evaluate blocked content and optimize filtering.
   - Apply exceptions or adjust categories as necessary to balance user experience and security.

   .. image:: ./img/content_filtering_analytics.png
      :align: center

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

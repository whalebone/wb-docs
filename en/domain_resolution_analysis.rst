Domain Resolution Analysis
===========================

This section provides guidance on analyzing domain resolution patterns and troubleshooting issues within the Whalebone platform. By understanding domain resolution behavior, administrators can optimize DNS configurations and identify anomalies.

Tutorial: Analyzing Domain Resolution
-------------------------------------

1. **Access Domain Analytics:**
   - Log in to the Whalebone portal.
   - Navigate to the **Domain Analytics** section under the **Analytics** menu.

   .. image:: ./img/domain_analytics_access.png
      :align: center

2. **Search for a Specific Domain:**
   - Use the search bar to locate resolution data for a specific domain.
   - View detailed metrics such as query volume, resolver activity, and policy actions.

   .. image:: ./img/domain_search.png
      :align: center

3. **Export Data for Offline Analysis:**
   - Select the time range and export domain-specific resolution data in supported formats (e.g., CSV).

   .. image:: ./img/domain_data_export.png
      :align: center

4. **Utilize DNSViz for Detailed Insights:**
   - Use the DNSViz tool to visualize DNS resolution paths.
   - DNSViz helps identify misconfigurations or issues in the DNS chain of trust.
   - Upload DNS query data or analyze live queries directly.

   .. image:: ./img/dnsviz_tool.png
      :align: center

How-To Guide: Troubleshooting Resolution Issues
-----------------------------------------------

### Identifying Resolution Failures

1. Access the **Resolution Logs** for the domain in question.
2. Review query details to identify patterns such as high latency or timeouts.

   .. image:: ./img/resolution_logs.png
      :align: center

### Analyzing Policy Actions

1. Check the **Policy Logs** to determine if a blocking policy or allowlist rule affected the domain.
2. Adjust the policy configuration if necessary to resolve conflicts.

   .. image:: ./img/policy_logs.png
      :align: center

### Cross-Referencing Threat Data

1. Use the **Threat Analysis** section to verify if the domain is associated with any malicious activity.
2. Reassess blocking thresholds or allowlisting decisions based on threat intelligence.

   .. image:: ./img/threat_data_check.png
      :align: center

Reference: Domain Analytics Features
-------------------------------------

- **Query Metrics:** Provides insights into query volume and resolution times.
- **Policy Impact:** Highlights how policies influence domain resolution.
- **Threat Correlation:** Links domain resolution data with threat intelligence.
- **Export Options:** Enables offline analysis of resolution trends.
- **DNSViz Tool:** Visualizes DNS resolution paths and identifies chain-of-trust issues.

Explanation: Importance of Domain Resolution Analysis
------------------------------------------------------

- **Performance Optimization:** Identifies areas where DNS performance can be improved.
- **Threat Detection:** Correlates resolution patterns with potential security risks.
- **Policy Refinement:** Ensures policies are correctly configured to support business needs.
- **Chain-of-Trust Verification:** Validates DNS resolution paths using DNSViz for enhanced reliability.

Domain resolution analysis is essential for maintaining a secure, efficient, and optimized DNS infrastructure within your organization.

Blocking Pages
==============

This section provides a detailed guide for configuring and customizing DNS blocking pages within the Whalebone system. Blocking pages inform users when access to a specific domain has been denied based on security or content filtering policies.

Tutorial: Setting Up Blocking Pages
-----------------------------------

1. **Access the Blocking Pages Section:**
   - Log in to the Whalebone portal.
   - Navigate to the **Blocking Pages** tab under the **Configuration** menu.

   .. image:: ./img/blocking_pages_access.png
      :align: center

2. **Choose a Default Template:**
   - Select one of the pre-defined templates for blocking pages.
   - Preview the template to ensure it matches your organizational branding and message.

   .. image:: ./img/blocking_page_templates.png
      :align: center

3. **Customize the Page Content:**
   - Edit the title, description, and contact details.
   - Add a company logo or other branding elements.

   .. image:: ./img/blocking_page_customization.png
      :align: center

4. **Test the Blocking Page:**
   - Use a test domain that triggers a blocking page to verify that the configuration works as expected.

   .. image:: ./img/blocking_page_test.png
      :align: center

How-To Guide: Advanced Blocking Page Configurations
---------------------------------------------------

### Multi-Language Support

1. Enable multi-language options in the blocking page settings.
2. Add translations for all text fields, including title and description.

   .. image:: ./img/multi_language_blocking_pages.png
      :align: center

### Redirect Options

1. Set up custom redirect URLs for users attempting to access blocked domains.
2. Use this option to show a different url in he browser page.
Note that this will require setting up also a static record in the DNS configuration pointing the redirect domain to the IP address of your resolver.

   .. image:: ./img/redirect_options.png
      :align: center

Reference: Blocking Page Configuration Options
----------------------------------------------

- **Templates:** Pre-designed layouts for ease of setup.
- **Custom Branding:** Upload logos and modify colors to align with corporate identity.
- **Multi-Language Support:** Ensure accessibility for users in different regions.
- **Signed Pages:** Enhance security by using a signed certificate for blocking pages.

Explanation: The Importance of Blocking Pages
---------------------------------------------

- **Transparency:** Provides clear communication to users about why access to a domain was denied.
- **Branding:** Reinforces organizational identity through customized messaging.
- **Compliance:** Ensures adherence to regulatory and internal policy requirements.

Blocking pages are a critical component of a secure and user-friendly DNS filtering system, offering both transparency and functionality.

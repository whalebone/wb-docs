Troubleshooting
===============

If you encounter issues with Single Sign-On, here are some common troubleshooting steps.

404 Page not Found
------------------

If you receive a 404 error when trying to access the SSO URL, it may indicate that the SSO endpoints have not been created yet. Please allow up to 3 hours after saving your SSO configuration for the endpoints to be set up. If the issue persists after this time, please contact Whalebone support for assistance.

404 Page not Found Even After 3 Hours
-------------------------------------

If you continue to receive a 404 error after waiting for the SSO endpoints to be created, it may indicate an issue with the SSO configuration. Please check that the Metadata URL is correct and accessible from the internet, and that the metadata content is valid. If you are still experiencing issues, please contact Whalebone support for further assistance.

Missing Identity Attribute
--------------------------

If you receive an error indicating that a required identity attribute is missing, it may indicate that the Name ID claim provided by your identity provider does not match the expected format or is missing. Please visit the test URL to check the IdP response and ensure that Name ID is present and has the expected format. If the Name ID is missing or does not match the expected format, please check your IdP configuration to ensure that it is correctly set up to provide the necessary claims.

Missing Roles Value Attribute
-----------------------------

If you receive an error indicating that a required roles attribute is missing, it may indicate that the Role key claim provided by your identity provider does not match the expected format or is missing. Please visit the test URL to check the IdP response and ensure that the Role key claim is present and has the expected format. If the Role key claim is missing or does not match the expected format, please check your IdP configuration to ensure that it is correctly set up to provide the necessary claims.

Here is an example of an output from the test URL:

.. code-block:: json

  {
    "aud": "https://login.whalebone.io/sso/12345678-90ab-cdef-1234-567890abcdef/",
    "exp": 1771579797,
    "iat": 1771576197,
    "iss": "https://login.whalebone.io/sso/12345678-90ab-cdef-1234-567890abcdef/",
    "nbf": 1771576197,
    "sub": "user@test.intra",
    "attr": {
      "SessionIndex": [
        "_c3148bb6-4b6a-40e3-b0b3-88ba4b99da32"
      ],
      "http://schemas.microsoft.com/ws/2008/06/identity/claims/role": [
        "Domain Admins",
        "Domain Users"
      ]
    },
    "saml-session": true
  }

In this example, the Role key claim is `http://schemas.microsoft.com/ws/2008/06/identity/claims/role`, and it contains the values "Domain Admins" and "Domain Users". The whole claim name should be used in the Role key field of the SSO configuration to ensure that the roles are correctly recognized and assigned in the Admin Portal.

Low-Level Troubleshooting
-------------------------

Sometimes, it may be necessary to analyze the SAML request and response in more detail to identify the root cause of SSO issues. You can use the developer tools in a web browser to inspect the network traffic during the SSO authentication process. The troubleshooting process typically involves the following steps:

1. Open the developer tools in your web browser (usually by pressing F12 or right-clicking and selecting "Inspect").
2. Navigate to the "Network" tab to monitor the network requests and responses.
3. Initiate the SSO authentication process by accessing the authentication URL.
4. It is easier to find the SAML response because it is sent to the `https://login.whalebone.io/sso/<ssoid>/saml/acs` URL. The SAML response is in the Payload of the POST request to this URL.
5. The SAML request is usually in the request proceeded to the SAML response, and it is sent to the IdP's SSO URL. You can find it by looking for a request that contains a SAMLRequest parameter in the URL or in the request body.
6. The SAML request and response are typically encoded in Base64, so you may need to decode them to analyze their contents. You can use online tools or command-line utilities to decode the Base64-encoded SAML messages.

.. warning:: Be cautious when sharing SAML requests and responses or pasting them to online tools, as they may contain sensitive information. If you would like to use online tools for decoding, it is recommended to use a testing environment. Always ensure that any shared data is properly sanitized to remove any personally identifiable information or sensitive attributes before sharing it with support teams or in public forums.
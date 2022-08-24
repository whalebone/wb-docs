Blocking Pages
============================
You can watch step-by-step video guide `here <https://docs.whalebone.io/en/latest/video_guides.html#blocking-page-configuration>`__
In case of blocking access to a domain (due to security, content or regulatory reasons), the resolvers are answering to the clients with a specific IP address that leads to one of the Blocking pages. Should the clients initiate the HTTP(S) connections towards the blocked domain, they are presented with a custom Blocking page with different content based on the reason of the blocking. 
Whalebone provides sample template pages for the Blocking Pages, however, they do not have to be followed and virtually every modification, branding and copywriting is possible. The template code is written to be compatible with the widest range of browsers to avoid problems with older versions.

Different versions of the Blocking Pages can be assigned to different segments of the networks.


.. figure:: ./img/blocking-pages-overview.png
   :alt: Blocking Pages Overview
   :align: center
   
   Blocking Pages Overview

For each version, based on the deployment details, there are four variants of the Blocking Pages that are available and can be configured:

* **Security**: displayed when access is blocked due to security reasons
* **Blacklist**: displayed when access is blocked by the Administrators
* **Regulatory**: displayed when access is regulated due to law or court order
* **Content**: displayed when access is blocked due to the content of the domain

Furthermore, each version can have different localization options. The language that is going to be presented to the user is infered from the language of the browser that is visiting the Blocking Page. New locales can be seamlessly added as an option.

.. figure:: ./img/blocking-pages.png
   :alt: Blocking Pages Menu
   :align: center
   
   Blocking Pages Menu

For each Locale several options are available. In the example above, the English version has the following options:

**1) Use Template**

  When using the template option, the information that is provided as input to the following form are injected in the template code. This is the fastest and easiest way to customize the blocking pages.

.. figure:: ./img/template.png
   :alt: Template Customization
   :align: center
   
   Template Customization

**2) Set as default locale**

  This option can customize the default language of the Blocking Pages. In case some browser does not declare its preferred language, the "Default" language acts as a fallback mechanism.

**3) Delete the locale**

  In case the locale is no longer needed, it can be deleted.


Each of the Versions of the Blocking Page (Security, Blacklist, Regulatory, Content) can be customized in more detail by modifying the HTML code. Upon clicking on each version an editor is presented that allows for any required changes.

The editor also exposes a "Verification" interface which parses the final HTML code and checks for the enabled functionalities. The check is based on the ``id`` of the specific elements. More information and requirements for each functionality can be found by clicking the respective labels.

.. note:: Each Version of the Blocking Page has unique characteristics that can be selected. For example, the Security Blocking Page can include a "Bypass" button which is not available in the respective Regulatory and Blacklist versions.


After editing and saving the changes to the Blocking Pages it is important that they are applied to the individual resolvers. More information can be found at the :ref:`Configure Blocking Pages Section<Configure Blocking Pages>`


.. tip:: The Blocking Pages are served from a web server directly on the Resolver. The pages are expected to be a single file so any additional resources (CSS, images, scripts) must be either embedded directly in the HTML code or served from a publicly accessible web server. The resolver does not provide any option to serve other content.

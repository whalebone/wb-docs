Home Office Security Overview
=============================

Why DNS-level protection matters
--------------------------------

Over 90 % of cyberattacks originate from DNS queries. By inspecting and filtering these requests, Home Office Security (HOS) blocks threats before they are opened in browsers, accessed by applications, or triggered by malicious email links. Unlike traditional VPN-based protection, HOS works continuously, without slowing users down or requiring manual logins.

Whalebone Home Office Security protects company devices even when they operate outside the corporate network. It provides DNS-level protection for remote and hybrid employees, eliminating the need for an active VPN connection. The HOS client continuously monitors and filters DNS traffic to block threats before they reach users, securing every connection, regardless of where employees work.

Key features
------------

* **Always-on protection**: DNS filtering continues even off the corporate network.

* **Multi-region support**: automatic selection of the nearest Whalebone resolver using the built-in resolver discovery mechanism.

* **Full DNS-type coverage**: protects HTTPS, SVCB, and future record types out of the box.

* **VPN awareness**: The service automatically pauses when a VPN connection is detected, preventing conflicts with internal routing. Officially tested and supported VPNs:

    * Barracuda Secure Edge
    * Cisco AnyConnect VPN
    * Fortinet FortiGate
    * Palo Alto Networks Prisma Access
    * Check Point Remote Access VPN
    * OpenVPN 11.31

* **Automatic internal resolver switch**: once the device joins the corporate network, HOS switches to the internal resolver for seamless access to internal systems and domains.

* **Prioritised connectivity**: ensures Internet access even when discovering the nearest resolver, using anycast as a fallback.

* **Clean UI**: a lightweight interface with minimal user interaction required.

Supported operating systems
---------------------------

=============== =============================
Platform        Minimum version
=============== =============================
Windows Desktop Windows 10 (64-bit) or higher
Android         Android 5 or higher
iOS             iOS 15.0 (SDK ≥ 13.4)
Linux           Not supported
macOS X         On the product roadmap
=============== =============================

System requirements
-------------------

* Internet access on TCP 443 (HTTPS) to `hos.whalebone.io <http://hos.whalebone.io>`_ and all cloud resolvers. The list of resolvers can be obtained by running the following command:

    .. code-block:: bash

        dig hos.whalebone.io TXT

    .. warning::

        The list of servers is likely to change because new resolvers may be added to the pool. Therefore, it is necessary to check regularly whether the firewall rules allow all of them.

* The Home Office Security client must be excluded from antivirus network protection to ensure its correct functioning.

* Windows: 64-bit CPU architecture

* Windows: Local administrator rights are required for installation

Known limitations
-----------------

* Security-policy propagation can take up to 4 hours to reach all devices.
* IPv6 networks may experience incorrect resolutions.
* 64-bit only – x86 Windows not supported.
* HOS may experience compatibility issues with different antivirus engines, leading to inconsistent threat detection.
* Some antivirus software may classify the Home Office Security client as a DNS hijacking or ARP cache poisoning threat. However, the client protects users by redirecting their DNS traffic to Whalebone cloud DNS servers, which is a legitimate activity.
* The GUI application does not start when the Home Office Security client is deployed using an MDM or Active Directory Group Policies. DNS traffic protection is not affected.
* The Home Office Security app is not compatible with the Private DNS feature on Android devices.

Changelog
---------

The changelog is available at `https://github.com/whalebone/home-office-security/releases <https://github.com/whalebone/home-office-security/releases>`_.

Glossary
--------

* **DNS-over-HTTPS (DoH)**: A secure protocol that encrypts DNS queries over HTTPS.
* **Resolver**: Whalebone Cloud infrastructure handling DNS requests safely.
* **Device Group**: A logical set of endpoints managed under one policy.
* **Internal Domain**: DNS pattern used to detect the corporate network.
* **Policy**: Configuration of security and content rules defining blocked or allowed domains.
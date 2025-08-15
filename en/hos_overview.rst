******************************
Home Office Security Overview
******************************

Whalebone Home Office Security (HOS) provides off‑network DNS filtering for
desktop and mobile devices. It intercepts DNS traffic and inspects it before
sending packets to the Internet. Currently Windows, Android and iOS are
supported. For detailed OS versions, see *Supported OS* below.

.. image:: ./img/hos-overview.png
   :align: center

Whalebone HOS • v2.20.4 at a glance
------------------------------------

* **Multi‑region support** – automatic selection of the nearest resolver
  using the *REGION* installer switch.
* **Full DNS‑type coverage** – protects HTTPS, SVCB and future record
  types out‑of‑the‑box.
* **Prioritised connectivity** – client keeps Internet access while
  discovering the best resolver; automatic Anycast fallback on failure.
* **Smarter shielding** – service auto‑pauses when a VPN is detected.
* **Cleaner UI** – main window starts hidden; tray and UI ports auto‑retry
  if defaults are in use.
* **64‑bit only** – x86 Windows is no longer supported.

HOS is deployed via a Windows MSI installer that requires a ``TOKEN``.
The default installation paths are:

``C:\Program Files (x86)\Whalebone\Home Office Security\`` (Windows)  
``/storage/emulated/0/Android/io.whalebone.securedns.corp/`` (Android)

Supported OS
============

+-----------------+----------------------------------+
| Windows Desktop | Windows 10 (64‑bit) or higher    |
+-----------------+----------------------------------+
| Android         | Android 5 or higher              |
+-----------------+----------------------------------+
| iOS             | iOS 15.0 (SDK ≥ 13.4)            |
+-----------------+----------------------------------+
| Linux           | Not supported                    |
+-----------------+----------------------------------+

.. note:: 32‑bit Windows builds (x86) are no longer supported from v2.20.4.

Windows 10 systems must be up‑to‑date.  
Windows Server 2016 systems must have Secure Boot disabled.

.. _known-limitations:

Known limitations (v 2.20.4)
============================

* **Security‑policy propagation:** changes can take *up to 4 hours* to reach
  devices. Real‑time sync is in development (target Q3–Q4 2025).
* **DNS‑over‑TCP:** TCP queries (e.g. from Microsoft Edge or very long
  questions) are not yet routed to Whalebone resolvers. A fix is in
  progress.
* **IPv6 networks:** with IPv6 enabled, some queries resolve incorrectly.
  Patch scheduled **by end of August 2025**.

.. _hos-roadmap:

Roadmap / Ongoing development
=============================

We continue to enhance the Home Office Security agent, focusing on:

* Real‑time policy updates.
* Full DNS‑over‑TCP handling.
* Complete IPv6 support.
* Unified UI across Windows, iOS and Android.
* Easier troubleshooting tools and performance optimisations.

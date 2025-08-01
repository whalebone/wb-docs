******************************
Home Office Security Overview
******************************

Whalebone HOS • v 2.20.4 at a glance
----------------------------------

* **Multi‑region support** – automatic selection of the nearest resolver
  using the new *REGION* installer switch.
* **Full DNS‑type coverage** – protects HTTPS, SVCB and future record
  types out‑of‑the‑box.
* **Prioritised connectivity** – client maintains internet access while
  discovering the best resolver; automatic Anycast fallback on failure.
* **Smarter shielding** – service auto‑pauses when a VPN is detected.
* **Cleaner UI** – main window starts hidden; tray and UI ports auto‑retry
  if defaults are in use.
* **64‑bit only** – x86 Windows is no longer supported.

Whalebone Home Office Security (HOS) provides an off-network DNS filtering functionality for desktop and mobile devices. It intercepts DNS traffic and inspects it before sending network packets to the wild. 
It protects the device from network threat by scanning every DNS packet. At the moment, Windows, Android and iOS devices are supported. For detailed OS version support, see below.

.. image:: ./img/hos-overview.png
    :align: center

HOS comes with Windows Installer for the deployment. No user interaction is required to perform the installation, however the installer requires a ``token``. 

The default target directory is:

``C:\Program Files (x86)\Whalebone\Home Office Security\``

For Android the default install location is:

``/storage/emulated/0/Android/io.whalebone.securedns.corp/``

Supported OS
====================


+-----------------+-------------------------------+
| Windows Desktop | Windows 7 SP1 (64‑bit)        |
+=================+===============================+
| Android         | Android 5 or higher           |
+-----------------+-------------------------------+
| iOS             | All versions                  |
+-----------------+-------------------------------+
| Linux           | Not supported                 |
+-----------------+-------------------------------+

.. note:: 32‑bit Windows builds (x86) are no longer supported from v 2.20.4.

Windows 7 systems must be up-to-date or at least have KB3033929 installed.

Windows Server 2016 systems must have secure boot disabled.



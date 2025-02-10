************************
Operation
************************


Devices
========================
Your organization may divide devices into single or multiple groups. Every device may belong exactly to a single group only. Each must be a member of **Device group** before they get monitored. Each group provides a security **Policy** which is later conditionally applied to them. Whether the device is present on the **internal** or **external** network makes it **active** or **inactive**.

It separates the network location into **internal** or **external** and the biggest role here has the **Internal domain** setting which must be defined in the **Device group**. If HOS detects the **Internal domain** the network location is decided as **internal**. Detection is performed by running DNS query for the configured internal domain and receiving the configured answer.

States
========================
HOS is constantly monitoring changes on the network interfaces and based on the conditions it changes its states. 

``Active`` 
    All DNS traffic is diverted to DoH server. HOS becomes **Active** when it is connected to the public network, but the **Internal domain** is unreachable. This state is used for the danger zones such as public wifi.

``Inactive`` 
    DNS trafic is left intact. This state is used when device can't connect to the Internet or when it is connected through internal network.


Security
========================
In the background HOS uses **DNS-over-HTTPs** or **DoH**. The **Hostname** of the **Resolveru** is never diverted and is cached. The identification and authenticity is left to the TLS protocol. When device belongs to any **Domain**, then all domain names and their subdomains are allowed to reach the DNS servers they route to. HOS uses ``Win32_NetworkAdapterConfiguration`` WMI table to get the information.



Service requirements
====================

Windows
-------

Because HOS must intecept network traffic it requres to run as **SYSTEM** account. You can query the service by name **hos** to see if it started properly. When none or invalid installation token is supplied the service it will stop.

.. code-block:: shell

    C:\Users\admin>sc query "Whalebone Home Office Security"

    SERVICE_NAME: HOS
            TYPE               : 10  WIN32_OWN_PROCESS
            STATE              : 4  RUNNING
                                    (STOPPABLE, PAUSABLE, ACCEPTS_SHUTDOWN)
            WIN32_EXIT_CODE    : 0  (0x0)
            SERVICE_EXIT_CODE  : 0  (0x0)
            CHECKPOINT         : 0x0
            WAIT_HINT          : 0x0


On first run HOS also installs ``windivert`` system driver. 

.. code-block:: shell

    C:\Users\admin>sc query windivert type=kernel

    SERVICE_NAME: windivert
            TYPE               : 1  KERNEL_DRIVER
            STATE              : 4  RUNNING
                                    (STOPPABLE, NOT_PAUSABLE, IGNORES_SHUTDOWN)
            WIN32_EXIT_CODE    : 0  (0x0)
            SERVICE_EXIT_CODE  : 0  (0x0)
            CHECKPOINT         : 0x0
            WAIT_HINT          : 0x0

Service is configured to recover after crash three times and then stay stopped.

Android
-------

The Android app has access to:

- Location

    - precise location (GPS and network-based)

- Camera

    - take pictures and videos (to scan QR code of the Device group from the portal)

- Wi-Fi connection information

    - view Wi-Fi connections

- Other 

    - view network connections

    - connect and disconnect from Wi-Fi

    - full network access (to create a VPN tunnel to Whalebone Cloud resolvers) 

    - run at startup



Application Firewall Settings
=============================

Enable TCP port 443 for the **Whalebone Home Office Security.exe** in the application firewall. To enable it for all network profiles in Windows, adjust following command to let HOS connect to your DoH server (e.g. 185.150.10.71):

If HOS service does not work please ensure that HOS service can connect to **hos.whalebone.io** and **mobileapi.whalebone.io**.

.. code-block:: shell

    netsh advfirewall firewall add rule name="Whalebone Home Office Security" dir=out action=allow program="C:\Program Files (x86)\Whalebone\Home Office Security\Whalebone Home Office Security.exe" enable=yes remoteip=185.150.10.71,LocalSubnet


It is not necessary for the service to listen on port 53, thus there is no requirement for the application firewall to follow.

Additionally, service is listening on **TCP endpoint localhost:9000** to provide data endpoint for UI app, and UI app server ``whosui.exe`` listens on *TCP endpoint localhost:55221* to render graphical components. Even though these ports are not critical for HOS operation they are relevant for UI app ``AdminUI.exe``. Please ensure that services are allowed to listen on those local ports as this allows user to have insight into app operation.


Application Logs
================

Service logs can be found at ``c:\ProgramData\Whalebone\Home Office Security\Logs\``, which contain detailed information about application states and operation. In case you encounther unexpected service behaviour please include this Log folder and/or Config folder along inside your support ticket. Application provides additional information for operation trace, in AdminUI.exe app, Events tab may give you better insight in HOS operation.


Uninstalling the app
================

To completely remove the app, uninstall the service and delete all contents from ``c:\ProgramData\Whalebone\Home Office Security\``
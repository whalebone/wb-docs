============================
Active Directory Integration
============================

**************************
Installation prerequisites
**************************

Before you install and Event Log Forwarer (ELF) on one or more of your devices, please ensure that you have enabled audit of events. 

On each of your Domain Controllers (DC) go to:
``Windows Administrative Tools`` > ``Local Security Policy``, and then
``Security Settings`` > ``Local Policies`` > ``Audit Policy``, and there find
``Audit account logon events``, ``Audit account sign-in events`` and  ``Audit logon events``. 

Some settings may differ in name or be missing, based on your Windows version.

.. image:: ./img/ad_integration_1.png
   :align: center

Check both Success and Failure boxes.

.. image:: ./img/ad_integration_2.png
   :align: center

You may need to reload configured policy. To reload policy, please run following command:

.. code-block:: shell

   gpupdate /force


*******************************
Domain Controller Configuration
*******************************

DC Firewall on Windows
======================

Ensure that Event Log can be accessed through your Firewall configuration using WMI.

On each of your Domain Controllers go to:
``Windows Defender Firewall`` > ``Windows Defender Firewall with Advanced Security on Local Computer`` 
``Inbound Rules`` > ``Windows Management Instrumentation (WMI-In)``

ensure the rule allows connections

.. image:: ./img/ad_integration_3.png
   :align: center

set up a scope of allowed addresses that may connect. In this example a remote address 192.168.1.0/24 is allowed.

.. image:: ./img/ad_integration_4.png
   :align: center

Or, alternatively you can use command line:
   
.. code-block:: shell

   netsh firewall set service RemoteAdmin enable


DC Firewall Rules
=================

====== ========= =========== ==== ========= ===========================
Source Direction Destination Port Protoocol Reason
====== ========= =========== ==== ========= ===========================
DC     --->      local netwk 135  TCP/UDP   Microsoft RPC	
DC     --->      local netwk 445  TCP       Microsoft MQ	
DC     --->      local netwk      ICMP      	
====== ========= =========== ==== ========= ===========================


Windows Service
===============

Please ensure that ``Windows Management Instrumentation`` service is running.

.. code-block:: shell

   C:\Users\Administrator>sc query Winmgmt

   SERVICE_NAME: Winmgmt
         TYPE               : 30  WIN32
         STATE              : 4  RUNNING
                                 (STOPPABLE, PAUSABLE, ACCEPTS_SHUTDOWN)
         WIN32_EXIT_CODE    : 0  (0x0)
         SERVICE_EXIT_CODE  : 0  (0x0)
         CHECKPOINT         : 0x0
         WAIT_HINT          : 0x0

.. image:: ./img/ad_integration_5.png
   :align: center


WMI Remote Configuration
========================

If you chose to install ELF on another Windows PC, ensure that it can use WMI remotely. To enable Remote WMI for the account which will be used to connect to Domain Controller, go to:
``Computer Management`` > ``Services and Applications`` > ``WMI Control```
Right click on it and selet ``Properties``

.. image:: ./img/ad_integration_6.png
   :align: center

Select ``Security`` tab, then choose the ``Root`` namespace and hit ``Security`` button.

.. image:: ./img/ad_integration_7.png
   :align: center

Add user to the list or select a group it belongs to, check ``Remote Enable`` permission.

.. image:: ./img/ad_integration_8.png
   :align: center

*******************
Event Log Forwarder 
*******************

You can install ELF locally on the DC or on another Windows PC. ELF uses following connections:


ELF Firewall Rules
==================

====== ========= =========== ==== ========= ===========================
Source Direction Destination Port Protoocol Reason
====== ========= =========== ==== ========= ===========================
ELF    --->      DC          135  TCP/UDP 
ELF    --->      resolver    4222 TCP	     NATS Message Queue
====== ========= =========== ==== ========= ===========================


Install Instructions
=====================

Install or Update:

.. code-block:: shell

   msiexec /i "Whalebone.Event.Log.Forwarder.Installer.msi" ui="true"

Uninstall:

.. code-block:: shell

   msiexec /x "Whalebone.Event.Log.Forwarder.Installer.msi

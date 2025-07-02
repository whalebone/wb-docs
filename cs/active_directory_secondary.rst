============================
Secondary method
============================

**************************
Požadavky pro instalaci
**************************

Před instalací Event Log Forwarderu (ELF) na jedno nebo více vašich zařízení se ujistěte, že máte povolený audit událostí.

Na každém vašem řadiči domény (DC) přejděte do:
``Windows Administrative Tools`` → ``Local Security Policy``, poté do
``Security Settings`` → ``Local Policies`` → ``Audit Policy``, a zde najdete
``Audit account logon events``, ``Audit account sign-in events`` a  ``Audit logon events``. 

Některá nastavení se mohou lišit názvem nebo mohou chybět, v závislosti na verzi Windows.

.. image:: ./img/ad-integration-1.png
   :align: center

Zaškrtněte **Úspěch** a **Selhání**.

.. image:: ./img/ad-integration-2.png
   :align: center

Možná bude potřeba znovu načíst nakonfigurovanou politiku. Pro znovunačtení politiky, prosím, spusťte následující příkaz:

.. code-block:: shell

   gpupdate /force


*********************************************
Konfigurace řadiče domény (Domain Controller)
*********************************************

DC Firewall pro Windows
=======================

Ujistěte se, že Event Log lze přistupovat skrze konfiguraci Firewallu pomocí WMI.

Na každém vašem řadiči domény přejděte do:
``Windows Defender Firewall`` → ``Windows Defender Firewall with Advanced Security on Local Computer`` 
``Inbound Rules`` → ``Windows Management Instrumentation (WMI-In)``


Ujistěte se, že pravidlo umožňuje připojení.

.. image:: ./img/ad-integration-3.png
   :align: center

Nastavte rozsah povolených adres, které se mohou připojit. V tomto příkladu je povolena vzdálená adresa **192.168.1.0/24.**

.. image:: ./img/ad-integration-4.png
   :align: center

Nebo, alternativně, můžete použít příkazový řádek:
   
.. code-block:: shell

   netsh firewall set service RemoteAdmin enable


DC Firewall Rules
=================

====== ========= =========== ==== ========= ===========================
Zdroj  Směr      Cíl         Port Protokol  Důvod
====== ========= =========== ==== ========= ===========================
DC     --->      local netwk 135  TCP/UDP   Microsoft RPC	
DC     --->      local netwk 445  TCP       Microsoft MQ	
DC     --->      local netwk      ICMP      	
====== ========= =========== ==== ========= ===========================


Služba Windows
===============

Ujistěte se, že služba ``Windows Management Instrumentation`` běží.

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

.. image:: ./img/ad-integration-5.png
   :align: center


Vzdálená konfigurace WMI
========================

Pokud se rozhodnete nainstalovat ELF na jiném počítači s Windows, ujistěte se, že může používat WMI na dálku. Pro povolení vzdáleného WMI pro účet, který bude použit pro připojení k řadiči domény, přejděte do:
``Computer Management`` → ``Services and Applications`` → ``WMI Control``
Klikněte pravým tlačítkem a vyberte ``Properties``.

.. image:: ./img/ad-integration-6.png
   :align: center

Vyberte kartu ``Security``, poté vyberte jmenný prostor ``Root`` a klikněte na tlačítko ``Security``.

.. image:: ./img/ad-integration-7.png
   :align: center

Přidejte uživatele do seznamu nebo vyberte skupinu, ke které patří, zaškrtněte povolení ``Remote Enable``.

.. image:: ./img/ad-integration-8.png
   :align: center

*******************
Event Log Forwarder 
*******************

ELF můžete nainstalovat lokálně na DC nebo na jiném počítači s Windows. ELF využívá následující spojení:


ELF Firewall Rules
==================

====== ========= =========== ==== ========= ===========================
Zdroj  Směr      Cíl         Port Protokol  Důvod
====== ========= =========== ==== ========= ===========================
ELF    --->      DC          135  TCP/UDP 
ELF    --->      resolver    4222 TCP	     NATS Message Queue
====== ========= =========== ==== ========= ===========================


Instrukce pro instalaci
=======================

Instalace nebo aktualizace:

.. code-block:: shell

   msiexec /i "Whalebone.Event.Log.Forwarder.Installer.msi" ui="true"

Odinstalace:

.. code-block:: shell

   msiexec /x "Whalebone.Event.Log.Forwarder.Installer.msi

Konfigurace
===========

Instalátor by měl automaticky otevřít okno konfigurace. Konfiguraci můžete přistupovat z oblíbeného webového prohlížeče pomocí příkazu:

.. code-block:: shell

   start http://localhost:55225/Configure/AD

.. image:: ./img/ad-integration-9.png
   :align: center

Logy služby
===========

Protokoly služby lze najít v ``c:\ProgramData\Whalebone\Event Log Forwarder\``, které obsahují podrobné informace o stavu služby. V případě, že narazíte na neočekávané chování služby, prosím, zahrňte obsah této složky k požadavku na podporu.
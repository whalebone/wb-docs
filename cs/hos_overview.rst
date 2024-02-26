****************************
Přehled Home Office Security
****************************

Whalebone Home Office Security (HOS) poskytuje funkci filtrování DNS mimo síť pro stolní počítače a mobilní zařízení. Zachycuje provoz DNS a mění adresu DNS serveru. 
Chrání zařízení před síťovými hrozbami tím, že kontroluje každý paket DNS. V současné době jsou podporována zařízení se systémy Windows, Android a iOS. Podrobné informace o podpoře verzí operačních systémů naleznete níže.

.. image:: ./img/hos-overview.png
    :align: center

HOS se dodává s instalátorem systému Windows pro nasazení. K provedení instalace není nutná žádná interakce uživatele, instalační program však vyžaduje ``token``.

Výchozí cílový adresář je:

``C:\Program Files (x86)\Whalebone\Home Office Security\``

Pro Android, výchozí cílový adresář je:

``/storage/emulated/0/Android/io.whalebone.securedns.corp/``

Porporované operační systémy
============================

| Windows Desktop      | Windows Server                 | Android              | iOS           | MacOS           | Linux           |
|----------------------|--------------------------------|----------------------|---------------|-----------------|-----------------|
| Windows 7 nebo vyšší | Windows Server 2012 nebo vyšší | Android 5 nebo vyšší | Všechny verze | Není podporován | Není podporován |

Systémy se operačním systémem Windows 7 musí být aktuální nebo musí mít nainstalovanou alespoň verzi KB3033929.

Systémy se operačním systémem Windows Server 2016 musí mít vypnuté zabezpečené spouštění (secure boot).



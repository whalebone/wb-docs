***********
Operace HOS
***********

Zařízení
========
Vaše organizace může zařízení rozdělit do jedné nebo více skupin. Každé zařízení může patřit pouze do jedné z nich. Každé zařízení musí být členem **skupiny zařízení**, aby mohlo být monitorováno. Každá skupina poskytuje  **Bezpečnostní politiku**, které jsou na ně později podmíněně aplikovány. Podle toho, zda je zařízení přítomno v **interní** nebo **externí** síti, je **aktivní** nebo **neaktivní**.

Rozděluje umístění v síti na **interní** nebo **externí** a největší roli zde má nastavení **interní domény**, které musí být definováno ve **Skupině Zařízení**. Pokud HOS detekuje správnou odpověď na **Interní doménu**, je síťové umístění určeno jako **interní**. Detekce se provádí spuštěním dotazu DNS na nakonfigurovanou interní doménu a obdržením nakonfigurované odpovědi.

Stavy
=====
HOS neustále sleduje změny na síťových rozhraních a na základě podmínek mění své stavy. 

``Aktivní`` 
    Veškerý provoz DNS je přesměrován na server DoH. HOS se stává **Aktivním**, když je připojen k veřejné síti, ale **Interní doména** je nedostupná. Tento stav se používá pro nebezpečné zóny, jako je veřejná wi-fi.

``Neaktivní`` 
    DNS trafic zůstává nedotčen. Tento stav se používá, když se zařízení nemůže připojit k internetu nebo když je připojeno přes vnitřní síť.

Bezpečnost
==========
Na pozadí HOS používá **DNS-over-HTTPs** neboli **DoH**. Název **Hostname** z **Resolveru** není nikdy přesměrován a je uložen v mezipaměti. Identifikace a autentizace je ponechána na protokolu TLS. Pokud zařízení patří k libovolné **Doméně**, pak je všem doménovým jménům a jejich subdoménám umožněno přistoupit k serverům DNS, na které jsou směrovány. HOS používá k získání informací tabulku ``Win32_NetworkAdapterConfiguration`` WMI.


Systémové požadavky
===================

Windows
-------

Protože služba HOS musí zachytávat síťový provoz, musí být spuštěna jako **SYSTEM**. Můžete se dotázat na služby podle názvu **hos** a zjistit, zda se správně spustila. Pokud není zadán žádný nebo je zadán neplatný instalační token, služba se zastaví.

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


Při prvním spuštění HOS nainstaluje také systémový ovladač ``windivert``. 

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

Služba je nakonfigurována tak, aby se po pádu třikrát pokusila o opětovné spuštění a poté zůstala zastavena.


Android
-------

Aplikace pro systém Android má přístup k:

- Poloha

    - K přesné poloze (GPS a síťové)

- Fotoaparát

    - K pořizování snímků a videí (skenování QR kódu skupiny zařízení z portálu)

- Informace o připojení Wi-Fi

    - Zobrazení připojení Wi-Fi

- Ostatní 

    - Zobrazení síťových připojení

    - Připojení a odpojení od sítě Wi-Fi

    - Úplný přístup k síti (pro vytvoření tunelu VPN k resolverům Whalebone Cloud) 

    - Spustit při spuštění




Nastavení brány firewall pro aplikace
=====================================

V aplikační bráně firewall povolte port TCP 443 pro **Whalebone Home Office Security.exe**. Chcete-li jej povolit pro všechny síťové profily v systému Windows, upravte následující příkaz tak, aby se služba HOS mohla připojit k vašemu serveru DoH (např. 185.150.10.71):

Pokud služba HOS nefunguje, zajistěte, aby se služba HOS mohla připojit k **hos.whalebone.io** a **mobileapi.whalebone.io**.


.. code-block:: shell

    netsh advfirewall firewall add rule name="Whalebone Home Office Security" dir=out action=allow program="C:\Program Files (x86)\Whalebone\Home Office Security\Whalebone Home Office Security.exe" enable=yes remoteip=185.150.10.71,LocalSubnet


Není nutné, aby služba naslouchala na portu 53. Kromě toho služba naslouchá na **TCP endpointu localhost:9000**, aby poskytla datový endpoint pro aplikaci UI, a server aplikace UI **whosui.exe** naslouchá na **TCP endpointu localhost:55221**, aby vykresloval grafické komponenty. I když tyto porty nejsou pro provoz HOS kritické, jsou důležité pro aplikaci UI **AdminUI.exe**. Zajistěte, aby služby měly povoleno naslouchat na těchto místních portech, protože to umožňuje uživateli nahlédnout do provozu aplikace.

Aplikační Logy
==============

Nacházejí se na adrese ``c:\ProgramData\Whalebone\Home Office Security\Logs\``, obsahují podrobné informace o stavech a provozu aplikace. V případě, že se setkáte s neočekávaným chováním služby, zašlete obsah složky Log a/nebo složly Config spolu se svým dotazem na podporu. Aplikace poskytuje další informace pro sledování provozu, v aplikaci AdminUI.exe, karta Události vám může poskytnout lepší přehled o provozu HOS.


Odinstalování aplikace
======================

Chcete-li aplikaci zcela odstranit, odinstalujte službu a odstraňte veškerý obsah z ``c:\ProgramData\Whalebone\Home Office Security\``.
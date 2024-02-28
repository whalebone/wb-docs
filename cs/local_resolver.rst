******************
Lokální resolver
******************

Nasazení řešení Whalebone nasazeného jako **lokální resolver** přináší výhodu viditelnosti místních IP adres, které odesílají skutečné požadavky. Pokud pro vás nasazení lokálního řešení není vhodnou volbou, 
podívejte se na další :ref:`Možnosti nasazení.<Možnosti nasazení>`

Whalebone resolver je založen na implementaci `Knot Resolveru <https://www.knot-resolver.cz/>`_ vyvinutého CZ.NIC.



Systémové požadavky na lokální resolver
=======================================

Instalace lokálního resolveru je podporována na vyhrazeném (hardwarovém nebo virtuálním) stroji s jedním z níže uvedených operačních systémů.

* **Podporovaný operační systém** (64bitový, serverové edice následujících distribucí):

  * Red Hat Enterprise Linux 7, 8, 9
  * CentOS Linux 7, 8 
  * CentOS Stream 8, 9
  * Debian 9, 10, 11, 12
  * Ubuntu 16.04, 18.04, 20.04, 22.04

* **Podporované souborové systémy** 

  * ext4
  * xfs pouze s podporou d_type (ftype=1)

* **Minimální požadavky na hardware** (fyzického nebo virtuálního):

  * 2 jádra procesoru
  * 4 GB RAM
  * 40 GB HDD (alespoň 30 GB v oddílu /var)

.. warning:: Pozor, Whalebone podporuje pouze nasazení bez desktopových prostředí, jako je GNOME, KDE nebo Xfce, protože ty mohou ovlivnit dostupnou paměť a zpracování DNS na serveru.

* **Požadavky na nastavení sítě** (místní resolver potřebuje otevřené následující výstupní porty):

  =========== =========== ======= ========================== ================================
  Směr        Protokol(y) Port    Cílová IP/Doména           Popis         
  =========== =========== ======= ========================== ================================
  Odchozí     TCP+UDP     53      Jakákoli                   DNS rekurze        
  Odchozí     TCP         443     resolverapi.whalebone.io   Aktualizace databáze hrozeb
  Odchozí     TCP         443     stream.whalebone.io        Aktualizace databáze hrozeb     
  Odchozí     TCP         443     logger.whalebone.io        Logovací stream   
  Odchozí     TCP         443     agentapi.whalebone.io      Správa resolveru
  Odchozí     TCP         443     transfer.whalebone.io      Sběr podpůrných protokolů
  Odchozí     TCP         443     portal.whalebone.io        Portál správce
  Odchozí     TCP         443     harbor.whalebone.io        Aktualizace resolveru
  Odchozí     TCP         443     download.docker.com        Instalační proces
  Odchozí     TCP         443     data.iana.org              DNSSEC klíče   
  =========== =========== ======= ========================== ================================
  
  .. warning:: Bez povolené komunikace na portu 443 s výše uvedenými doménami nebude resolver vůbec nainstalován (instalační skript se přeruší).

  
  Hlavní funkcí resolveru je přijímat dotazy od uživatelů a odpovídat jim na ně, což vyžaduje, aby byly na resolveru otevřeny určité porty pro provoz pocházející z klientské podsítě nebo přicházející do zákaznického rozhraní.
 
 
 
  =========== =========== ======= ============================ ==========================================
  Směr        Protokol(y) Port    Cílová IP/Doména             Popis         
  =========== =========== ======= ============================ ==========================================
  Příchozí    TCP+UDP     53      Rozsah(y) podsítě zákazníka  DNS
  Příchozí    TCP         853     Rozsah(y) podsítě zákazníka  DNS přes TLS (pokud se používá)
  Příchozí    TCP         443     Rozsah(y) podsítě zákazníka  DNS přes HTTPS (pokud se používá)
  =========== =========== ======= ============================ ==========================================

  Blokační stránky jsou hostovány **přímo** na resolverech, takže musí být použity IP adresy, které jsou přístupné klientům. Klienti pak budou při blokování přesměrováni na IP adresu resolveru. Doporučujeme povolit pouze podsítě přidělené zákazníkům nebo důvěryhodným sítím, jinak by mohly být zneužity k různým útokům nebo neoprávněným uživatelům.

  =========== =========== ======= ============================ ==========================================
  Směr        Protokol(y) Port    Cílová IP/Doména             Popis         
  =========== =========== ======= ============================ ==========================================
  Příchozí    TCP         80      Rozsah(y) podsítě zákazníka  Stránka přesměrování/blokování
  Příchozí    TCP         443     Rozsah(y) podsítě zákazníka  Stránka přesměrování/blokování
  =========== =========== ======= ============================ ==========================================
  
  Procesy resolveru musí komunikovat na localhostu. V případě, že je v provozu nějaký firewall, ujistěte se, že je provoz povolen, tj. ``iptables -A INPUT -s 127.0.0.1 -j ACCEPT``

  =========== =========== ======= ============================ ==========================================
  Směr        Protokol(y) Port    Cílová IP/Doména             Popis         
  =========== =========== ======= ============================ ===========================================
  Příchozí    TCP         ANY     127.0.0.1                    Procesy řešitele
    =========== =========== ======= ============================ ===========================================

.. note:: Pro odhad HW požadavků u nasazení vr velkých sítích ISP nebo podnikových sítích se neváhejte obrátit na společnost Whalebone. Lokální resolver Whalebone bude potřebovat přibližně dvojnásobek paměti RAM a procesoru než běžný resolver (BIND, Unbound).

Instalace nového lokálního resolveru
====================================

Můžete se podívat na videonávod krok za krokem o postupu instalace :ref:`zde.<Deployment>`

V záložce **Resolvery** stiskněte tlačítko **Vytvořit nový**. Zvolte název (identifikátor) nového resolveru. Zadání je čistě informativní a nebude mít vliv na funkčnost.
Po zadání názvu klikněte na tlačítko **Přidat resolver**.
Po kliknutí na tlačítko se zobrazí informativní okno se seznamem podporovaných platforem a **jednořádkovým příkazem pro instalaci**. Příkaz zkopírujte a spusťte na stroji (VM) určeném pro místní resolver.
Příkaz spustí instalační skript a předá jednorázový token použitý pro aktivaci resolveru (stejný příkaz nelze použít opakovaně).

.. image:: ./img/lrv2-create.gif
	:align: center


Po spuštění příkazu probíhá kontrola operačního systému a instalace požadavků. Skript vás bude informovat o průběhu a vytvoří podrobný protokol s názvem ``wb_install.log`` v aktuálním adresáři.
Úspěšné spuštění instalačního skriptu je ukončeno oznámením ```Finální ladění operačního systému```` s hodnotou ``[ OK ]```. Hned po instalaci proběhne také inicializace a může trvat několik minut, než resolver spustí služby.


.. image:: ./img/lrv2-install.gif
   :align: center


.. warning:: Lokální resolver je nakonfigurován jako otevřený resolver. Odpoví na jakýkoli zaslaný požadavek. To je poměrně pohodlné z hlediska dostupnosti služeb, ale také to může představovat riziko, pokud je služba dostupná z vnějších sítí. Ujistěte se, že jste omezili přístup k místnímu resolveru na port 53 (UDP a TCP) pouze z důvěryhodných sítí, jinak může být zneužit k různým DoS útokům.
.. important:: The resolver's processes need to communicate on localhost. In case some firewall is in place please make sure that the traffic is allowed, i.e. ``iptables -A INPUT -s 127.0.0.1 -j ACCEPT``

Ověření správnosti instalace
----------------------------

Whalebone diponuje řadou neškodných testovacích domén, které jsou interně klasifikovány jako testovací domény pro ověření funkčnosti resolveru.
Pomocí těchto domén se můžete ujistit, že Whalebone resolver pracuje správně:

* ``http://malware.test.attacker.online``
* ``http://c2server.test.attacker.online``
* ``http://spam.test.attacker.online``
* ``http://phishing.test.attacker.online``
* ``http://coinminer.test.attacker.online``

Při přístupu na tyto domény by se měla zobrazit podobná blokační stránka podobná s následující:

.. figure:: ./img/blocking-page-default.png
   :alt: Blocking Pages (Default)
   :align: center
   
   Blokační stránka - správná funkce resolveru.

V případě, že narazíte na níže uvedenou stránku, znamená to, že požadavek nebyl zablokován, a tedy není použit resolver Whalebone. 
Zkontrolujte prosím své nastavení a pokud problém přetrvává, kontaktujte prosím podporu.

.. figure:: ./img/testing-page.png
   :alt: Blocking Pages (Target)
   :align: center
   
   Blokační stránka - resolver nefunguje správně.



Zabezpečení resolveru
---------------------

Při první instalaci je resolver nakonfigurován jako otevřený resolver. Odpoví na jakýkoli požadavek, který je mu zaslán, bez ohledu na to, odkud požadavek pochází. To je poměrně 
pohodlné z hlediska dostupnosti služeb, ale může být také rizikem, pokud je služba dostupná z vnějších sítí. Ujistěte se, že jste omezili přístup 
k místnímu resolveru na portu 53 (UDP a TCP) pouze z důvěryhodných sítí, jinak může být zneužit k různým DoS útokům.
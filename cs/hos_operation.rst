Provoz a monitoring
===================

Aktivita zařízení v Administračním portálu
------------------------------------------

Administrační portál uvádí, zda zařízení komunikovalo s backendem Whalebone během posledních 24 hodin. Tento stav aktivity je nezávislý na stavu ochrany v klientovi Home Office Security: aktivní zařízení nemusí v danou chvíli filtrovat DNS provoz.

========= ====================================================================================================
Stav          Popis
========= ====================================================================================================
Aktivní   Zařízení kontaktovalo backend Whalebone alespoň jednou za posledních 24 hodin.
Neaktivní Zařízení nekontaktovalo backend Whalebone během posledních 24 hodin.
========= ====================================================================================================

.. _hos-client-states:

Stavy ochrany klienta
---------------------

Klient Home Office Security zobrazuje konkrétní stavy ochrany a důvody selhání na hlavní obrazovce. Každý stav má nadpis a podnadpis. Níže jsou uvedeny anglické texty rozhraní pro snadné rozpoznání hlášení.

.. list-table:: Stavy na hlavní obrazovce
   :class: hos-state-table
   :header-rows: 1
   :widths: 25 35 40

   * - Stav
     - Nadpis
     - Podnadpis
   * - Spouštění (Starting)
     - Just a second …
     - Connecting to the protection service
   * - Aktivní ochrana (Active)
     - Protection is active
     - Malicious websites are being filtered
   * - Pozastaveno uživatelem (Paused by user)
     - Protection paused
     - Turn protection back on using the toggle
   * - Důvěryhodná síť (Trusted network)
     - You are on a trusted network
     - Your protection is enabled at the network level
   * - Detekována VPN (VPN detected)
     - VPN detected
     - Protection is on standby
   * - Nekompatibilní software (Incompatible software)
     - VPN detected
     - Protection is on standby
   * - Bez internetu (No internet)
     - You are not connected to the internet
     - Protection will start when the connection is restored

Stav důvěryhodné sítě se použije, pokud je povolena funkce **Vypnout home office zabezpečení uvnitř podnikové sítě** a nakonfigurovaný interní DNS záznam odpovídá očekávané hodnotě. HOS pozastaví místní filtrování a ochrana je zajištěna na úrovni sítě. Detekce VPN a nekompatibilního softwaru také uvede ochranu do pohotovostního režimu; oba stavy zobrazují stejnou zprávu na hlavní obrazovce.

.. _hos-error-states:

Chybové stavy ochrany
---------------------

Následující stavy vysvětlují, proč se ochranu nepodařilo zapnout.

.. list-table:: Chybové zprávy na hlavní obrazovce
   :class: hos-state-table
   :header-rows: 1
   :widths: 25 35 40

   * - Stav
     - Nadpis
     - Podnadpis
   * - Nedostupné DoH resolvery (DoH unreachable)
     - Protective DNS resolvers cannot be reached
     - Protective DNS servers cannot be reached. Contact your IT administrator.
   * - Selhání DoH resolveru (DoH failed)
     - Protective DNS resolvers cannot be reached
     - Protective resolvers failed. Contact your IT administrator.
   * - Blokování proxy serverem (Proxy blocked)
     - Network proxy is blocking protection
     - Network proxy is blocking protection. Contact your IT administrator.
   * - Zastavená služba ochrany (Protection service stopped)
     - Protection service is not running
     - Contact your IT administrator
   * - Nedostupné servery Whalebone (Whalebone servers unavailable)
     - Protection could not be enabled
     - Whalebone servers cannot be reached. Contact your IT administrator.
   * - Nedostupná služba Windows (Windows service unavailable)
     - Protection could not be enabled
     - Windows service cannot be started. Restart your computer or contact your IT administrator.

**DoH unreachable** znamená, že se klient nemůže připojit k žádnému vhodnému DNS-over-HTTPS resolveru. **DoH failed** znamená, že vybraný resolver neodpověděl v časovém limitu na 10 po sobě jdoucích požadavků. Oba stavy mají stejný nadpis, ale podnadpis rozlišuje příčinu selhání.

Doporučený postup a sběr logů popisuje část :doc:`hos_troubleshooting`.

Oznámení v systémové liště Windows
----------------------------------

Klient Home Office Security uvádí důvod selhání také v oznámeních v systémové liště Windows.

.. list-table:: Zprávy v systémové liště Windows
   :class: hos-state-table
   :header-rows: 1
   :widths: 30 70

   * - Situace
     - Oznámení
   * - DoH unreachable nebo DoH failed
     - Protection could not be enabled since protective resolvers cannot be reached. Please contact your IT administrator.
   * - Proxy blocked
     - Protection could not be enabled due to incorrect network proxy settings. Please contact your IT administrator.
   * - Protection service stopped
     - Protection could not be enabled since the protection service is not running. Restart your computer or contact your IT administrator.
   * - Whalebone servers unavailable
     - Protection could not be enabled since cloud services cannot be reached. Please contact your IT or security administrator.
   * - Windows service unavailable
     - Protection could not be enabled since the protection service is not responding. Restart your computer or contact your IT administrator.
   * - Vyřešeno (Resolved)
     - All issues have been resolved.

Automatický výběr resolveru
---------------------------

Klient HOS se automaticky připojuje k **nejbližšímu cloudovému DNS resolveru Whalebone** pro co nejrychlejší dobu odezvy. Jakmile je detekována interní doména, HOS se plynule přepne na interní resolver, čímž zajistí přístup k firemním zdrojům bez ruční konfigurace.

Monitoring
----------

* V portálu lze zobrazit skupinu každého zařízení, politiku, čas poslední aktivity a stav připojení.
* Kontroly dostupnosti internetu používají nativní Windows API, což minimalizuje falešné stavy, kdy je počítač bez internetu.

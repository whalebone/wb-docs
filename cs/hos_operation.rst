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

Klient Home Office Security zobrazuje konkrétní stavy ochrany a důvody selhání na hlavní obrazovce. Každý stav má nadpis a podnadpis. Níže jsou uvedeny české texty rozhraní klienta pro Windows.

.. list-table:: Stavy na hlavní obrazovce
   :class: hos-state-table
   :header-rows: 1
   :widths: 25 35 40

   * - Stav
     - Nadpis
     - Podnadpis
   * - Spouštění
     - Ještě chvíli …
     - Připojování k zabezpečené službě
   * - Aktivní ochrana
     - Jste v bezpečí
     - Škodlivé webové stránky jsou filtrovány
   * - Pozastaveno uživatelem
     - Ochrana pozastavena
     - Ochranu obnovíte přepnutím tlačítka
   * - Důvěryhodná síť
     - Jste na důvěryhodné síti
     - Interní síť: Ochrana na úrovni sítě
   * - Detekována VPN
     - Detekována VPN
     - Ochrana je v pohotovostním režimu
   * - Nekompatibilní software
     - Detekována VPN
     - Ochrana je v pohotovostním režimu
   * - Bez internetu
     - Nejste připojeni k internetu
     - Ochrana se spustí po obnovení internetového připojení

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
   * - Nedostupné DoH resolvery
     - Ochranné DNS resolvery jsou nedostupné
     - Ochranné resolvery jsou nedostupné: Kontaktujte svého správce IT
   * - Selhání DoH resolveru
     - Ochranné DNS resolvery jsou nedostupné
     - Ochranné resolvery selhaly: Kontaktujte svého správce IT
   * - Blokování proxy serverem
     - Síťová proxy blokuje ochranu
     - Síťová proxy blokuje ochranu. Kontaktujte svého správce IT.
   * - Zastavená služba ochrany
     - Ochranná služba neběží
     - Pro vyřešení problému kontaktujte naši podporu
   * - Nedostupné servery Whalebone
     - Ochranu se nepodařilo aktivovat
     - Servery Whalebone jsou nedostupné. Kontaktujte svého správce IT.
   * - Nedostupná služba Windows
     - Ochranu se nepodařilo aktivovat
     - Windows službu se nepodařilo spustit. Restartujte počítač nebo kontaktujte svého správce IT.

Stav **Nedostupné DoH resolvery** znamená, že se klient nemůže připojit k žádnému vhodnému DNS-over-HTTPS resolveru. Stav **Selhání DoH resolveru** znamená, že vybraný resolver neodpověděl v časovém limitu na 10 po sobě jdoucích požadavků. Oba stavy mají stejný nadpis, ale podnadpis rozlišuje příčinu selhání.

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
   * - Nedostupné DoH resolvery nebo selhání DoH resolveru
     - Ochranné resolvery nejsou dostupné. Pro vyřešení situace kontaktujte IT či bezpečnostního administrátora.
   * - Blokování proxy serverem
     - Ochrana nemohla být spuštěna kvůli nesprávnému nastavení síťového proxy serveru. Kontaktujte prosím svého správce IT.
   * - Zastavená služba ochrany
     - Ochrana nemohla být spuštěna, protože služba ochrany není spuštěna. Restartujte počítač nebo kontaktujte svého správce IT.
   * - Nedostupné servery Whalebone
     - Ochrana nemohla být spuštěna, protože se nelze připojit ke cloudovým službám. Kontaktujte prosím svého správce IT.
   * - Nedostupná služba Windows
     - Ochrana nemohla být spuštěna, protože služba ochrany neodpovídá. Restartujte počítač nebo kontaktujte svého správce IT.
   * - Vyřešeno
     - Všechny problémy byly vyřešeny.

Automatický výběr resolveru
---------------------------

Klient HOS se automaticky připojuje k **nejbližšímu cloudovému DNS resolveru Whalebone** pro co nejrychlejší dobu odezvy. Jakmile je detekována interní doména, HOS se plynule přepne na interní resolver, čímž zajistí přístup k firemním zdrojům bez ruční konfigurace.

Monitoring
----------

* V portálu lze zobrazit skupinu každého zařízení, politiku, čas poslední aktivity a stav připojení.
* Kontroly dostupnosti internetu používají nativní Windows API, což minimalizuje falešné stavy, kdy je počítač bez internetu.

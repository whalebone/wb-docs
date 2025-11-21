Provoz a monitoring
===================

Stavy zařízení
--------------

========= ====================================================================================================
Stav          Popis
========= ====================================================================================================
Aktivní   Zařízení bylo aktivní a kontaktovalo s backendem Whalebone alespoň jednou za posledních 24 hodin.
Neaktivní Zařízení nebylo aktivní nebo nekontaktovalo backend Whalebone alespoň jednou za posledních 24 hodin.
========= ====================================================================================================

Automatický výběr resolveru
---------------------------

Klient HOS se automaticky připojuje k **nejbližšímu cloudovému DNS resolveru Whalebone** pro co nejrychlejší dobu odezvy. Jakmile je detekována interní doména, HOS se plynule přepne na interní resolver, čímž zajistí přístup k firemním zdrojům bez ruční konfigurace.

Chování ochrany
---------------

* Využívá **DNS-over-HTTPS** k šifrování a validaci dotazů.
* Lokální domény jsou překládány DNS resolverem nastaveným v operačním systému, pokud je povolena a správně nakonfigurována funkce "Vypnout home office zabezpečení uvnitř podnikové sítě".
* Agent monitoruje změny sítě a automaticky upravuje stav.

Monitoring
----------

* V portálu lze zobrazit skupinu každého zařízení, politiku, čas poslední aktivity a stav připojení.
* Kontroly dostupnosti internetu používají nativní Windows API, což minimalizuje falešné stavy, kdy je počítač bez internetu.
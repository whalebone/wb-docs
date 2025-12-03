Přehled Home Office Security
============================

Proč je ochrana na úrovni DNS důležitá
--------------------------------------

Více než 90 % kybernetických útoků pochází z DNS dotazů. Klient Home Office Security (HOS) kontroluje a filtruje tyto požadavky, čímž blokuje hrozby dříve, než je zobrazí webový prohlížeč, přistoupí k nim aplikace nebo jsou spuštěny škodlivými odkazy v e-mailech. Na rozdíl od tradiční ochrany založené na VPN, HOS funguje nepřetržitě, aniž by uživatele zpomaloval nebo vyžadoval ruční přihlašování.

Whalebone Home Office Security chrání firemní zařízení, i když fungují mimo firemní síť. Poskytuje ochranu na úrovni DNS pro zaměstnance pracující z domu nebo na služební cestě, čímž eliminuje potřebu aktivního připojení k VPN. Klient HOS nepřetržitě monitoruje a filtruje DNS provoz, aby zablokoval hrozby dříve, než se dostanou k uživatelům, a zabezpečuje každé připojení bez ohledu na to, kde zaměstnanci pracují.

Klíčové vlastnosti
------------------

* **Stále aktivní ochrana**: Filtrování DNS i mimo firemní síť.

* **Podpora více regionů**: automatický výběr nejbližšího resolveru Whalebone pomocí vestavěného mechanismu pro vyhledávání resolverů.

* **Plné pokrytí DNS**: chrání HTTPS, SVCB a budoucí typy záznamů.

* **Kompatibilita s VPN**: Služba se automaticky pozastaví, když je detekováno připojení VPN, čímž zabraňuje konfliktům s interním směrováním. Oficiálně testované a podporované sítě VPN:

    * Barracuda Secure Edge
    * Cisco AnyConnect VPN
    * Fortinet FortiGate
    * Palo Alto Networks Prisma Access
    * Check Point Remote Access VPN
    * OpenVPN 11.31

* **Automatické přepnutí interního resolveru**: Jakmile se zařízení připojí k firemní síti, HOS se přepne na interní resolver pro bezproblémový přístup k interním systémům a doménám.

* **Prioritní konektivita**: Zajišťuje přístup k internetu i při zjišťování nejbližšího resolveru, přičemž jako záložní řešení používá anycast.

* **Přehledné uživatelské rozhraní**: odlehčené rozhraní s minimální požadovanou interakcí uživatele.

Podporované operační systémy
----------------------------

=============== ===========================================
Platforma       Minimální verze
=============== ===========================================
Windows Desktop Windows 10 (64-bit) nebo vyšší
Android         Android 5 nebo vyšší
iOS             iOS 15.0 (SDK ≥ 13.4)
Linux           Nepodporováno
macOS X         Nyní nepodporováno, ale s vývojem se počítá
=============== ===========================================

Systémové požadavky
-------------------

* Přístup k internetu na TCP 443 (HTTPS) k `hos.whalebone.io <http://hos.whalebone.io>`_ a všem cloudovým resolverům. Seznam resolverů lze získat spuštěním následujícího příkazu:

    .. code-block:: bash

        dig hos.whalebone.io TXT

    .. warning::

        Seznam serverů se může změnit, protože mohou být přidány nové resolvery. Proto je nutné pravidelně kontrolovat, zda pravidla firewallu povolují všechny z nich.

* Klient Home Office Security musí být vyloučen z antivirové síťové ochrany, aby byla zajištěna jeho správná funkce.

* Windows: 64bitová architektura CPU

* Windows: Pro instalaci jsou vyžadována práva lokálního administrátora

Známá omezení
-------------

* Šíření bezpečnostních politik může trvat až 4 hodiny, než se dostane na všechna zařízení.
* Sítě IPv6 mohou zaznamenat problémy s DNS překladem.
* Pouze 64-bit – x86 Windows nejsou podporovány.
* HOS může mít problémy s kompatibilitou s různými antivirovými programy, což vede k nekonzistentní detekci hrozeb.
* Některý antivirový software může klienta Home Office Security klasifikovat jako hrozbu přesměrování DNS nebo ARP cache poisoning. Přesměrováním DNS provozu na cloudové DNS servery Whalebone je ovšem žádoucí a legitimní aktivita HOS klienta.
* Aplikace GUI se nespustí, pokud je klient Home Office Security nasazen pomocí MDM nebo Zásad skupiny Active Directory (Active Directory Group Policies). Ochrana DNS provozu tím není dotčena.
* Aplikace Home Office Security není kompatibilní s funkcí Private DNS v zařízeních s operačním systémem Android a funkcí Private Relay v zařízeních s operačním systémem iOS.

Změny
-----

Seznam změn je k dispozici na `https://github.com/whalebone/home-office-security/releases <https://github.com/whalebone/home-office-security/releases>`_.

Slovníček pojmů
---------------

* **DNS-over-HTTPS (DoH)**: Zabezpečený protokol, který šifruje dotazy DNS přes HTTPS.
* **Resolver**: Cloudová infrastruktura Whalebone, která bezpečně zpracovává požadavky DNS.
* **Skupina zařízení**: Logická sada koncových bodů spravovaná podle jedné politiky.
* **Interní doména**: Vzor DNS používaný k detekci firemní sítě.
* **Politika**: Konfigurace bezpečnostních a obsahových pravidel definujících blokované nebo povolené domény.
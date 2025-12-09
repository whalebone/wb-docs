Analýza překladu domén
======================

Může se stát, že se správce setká se situací, kdy překlad DNS není úspěšný. Většinou to nesouvisí s resolverem Whalebone, ale pravděpodobně se jedná o problém s autoritativním serverem. 

Poskytovatelé internetových služeb se často setkávají se stížnostmi, že uživatelé nemohou přistoupit k doméně. V mnoha případech to není chyba poskytovatele. Portál Whalebone správcům poskytne informace pro identifikaci problému.

Analýza se skládá ze čtyř kroků:

**1. krok: Ověřte, zda lokální resolvery Whalebone blokují doménu**

  * Pokud máte lokální resolvery Whalebone, využijte nástroj **Debug překladu domény**, který se nachází přímo v nabídce resolveru pod ikonkou tří teček. Výsledek testu oznámí, jestli je doména blokována, či nikoliv. 

    .. image:: ./img/domain-resolution-analysis-1.png
      :align: center

**2. krok: Prozkoumejte doménu v záložce Hrozby**

  * Zkuste najít postiženou doménu mezi zablokovanými hrozbami.

**3. krok: Prozkoumejte doménu v záložce DNS provoz**

  * Pokud nebyla zablokována jako hrozba, přejděte na stránku **DNS provoz** a zkontrolujte, zda se dotaz dostal až k resolveru.
  * Pokud jste v přehledu provozu DNS nenalezli žádné dotazy z IP adresy uživatele, pak uživatel změnil konfiguraci DNS serveru na svém PC nebo domácím routeru tak, aby používal veřejné DNS servery. V takovém případě nejsou DNS dotazy odesílány do Whalebone a Whalebone nezpůsobuje problém s přístupem k doméně.
  * Pokud jste dotaz v přehledu provozu DNS nalezli, můžete se setkat se třemi případy:

    * Doména byla přeložena správně a problémy s přístupem k doméně nejsou způsobeny Whalebone.
    * Byla vrácena odpověď NXDOMAIN. Znamená to, že autoritativní server odpověděl, ale doména nebo subdoména neexistuje.
    * Byla vrácena odpověď SERVFAIL. Znamená to, že nebyla přijata žádná odpověď od nakonfigurovaného autoritativního serveru, nebo autoritativní DNS server nemá pro doménu platné záznamy DNSSEC. Pokud k tomu dojde, přejděte ke Kroku 4.

**4. krok: Prozkoumejte doménu pomocí DNSVIZ**

  * V seznamu domén lze pomocí šipky otevřít seznam nástrojů pro investigaci. Pomocí tohoto seznamu se můžete přesměrovat do nástroje DNSVIZ pro danou doménu, kde můžete analyzovat celý proces překladu včetně validace záznamů DNSSEC.
    
    .. image:: ./img/domain-resolution-analysis-2.png
      :align: center

  * Nástroj DNSVIZ znázorní v grafické podobně, jestli byla DNSSEC validace úspěšná, nebo, že autoritativní server nebyl dosažitelný

Videoprůvodce krok za krokem si můžete prohlédnout :ref:`zde <domain-resolution-troubleshooting>`.

Portál Whalebone poskytuje možnost trasovat doménu. Tato funkce je k dispozici v části **Resolvery** pod třemi tečkami každého resolveru. Tato funkce ukazuje, jaké informace jsou předávány resolveru při překladu konkrétní domény.

Videoprůvodce krok za krokem si můžete prohlédnout :ref:`zde <domain-tracing>`.
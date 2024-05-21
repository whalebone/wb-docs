Analýza překladu domén
======================

Může se stát, že se správce setká se situací, kdy překlad DNS není úspěšný. Většinou to nesouvisí s resolverem Whalebone, ale pravděpodobně se jedná o problém s autoritativním serverem. 


Poskytovatelé internetových služeb se často setkávají se stížnostmi, že uživatelé nemohou přistoupit k doméně, v mnoha případech to není chyba poskytovatele. Whalebone vám poskytne informace pro identifikaci problému.

Jednotlivé kroky k provedení analýzy
------------------------------------


**1. Krok: Prozkoumejte doménu v záložce Hrozby**

  * Zkontrolujte, zda doména nebyla zablokována z důvodu bezpečnosti.

**2. Krok: Prozkoumejte doménu v záložce DNS provoz**

  * Pokud nebyla zablokována kvůli **hrozbám**, přejděte na stránku **DNS provoz** a zkontrolujte, zda se dotaz dostal až k resolveru.
  * Uživatelé často mění nastavení DNS serveru na veřejné a z nefunkčnosti viní poskytovatele připojení. 
  **Můžete se setkat s třemi možnostmi:**
    * Překlad byl správny.
    * NXDOMAIN odpověď - autoritativní server odpověděl, ale subdoména neexistuje.
    * SERVFAIL odpověď - žádná odpověď ze strany serveru. Může se jednat o výpadek serveru nebo spojení.

**3. Krok: Prozkoumejte doménu pomocí DNSVIZ**
  * V seznamu domén lze pomocí šipky otevřít seznam nástrojů pro investigaci.
  * Nástroj **DNSVIZ** může v grafické podobně nastínit jestli byla DNSSEC validace úspěšná, nebo, že autoritativní server nebyl dosažitelný

Videoprůvodce krok za krokem si můžete prohlédnout `zde <https://docs.whalebone.io/cs/latest/video_guides.html#domain-resolution-troubleshooting>`__.

Portál Whalebone poskytuje možnost trasovat doménu. Tato funkce je k dispozici v části **Resolvery** pod třemi tečkami každého resolveru. Tato funkce ukazuje, jaké informace jsou předávány resolveru při překladu konkrétní domény.

Videoprůvodce krok za krokem si můžete prohlédnout `zde <https://docs.whalebone.io/cs/latest/video_guides.html#domain-tracing>`__.
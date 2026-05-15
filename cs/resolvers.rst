Správa resolveru
================

V záložce **Resolvery** je přehled vytvořených resolverů. Správce může upravovat konfiguraci, nasazovat aktualizace, instalovat nové resolvery a sledovat detailní provozní a výkonnostní metriky každého resolveru.

Přehled resolverů
-----------------

V hlavním přehledu resolverů jsou dlaždice s podrobnostmi o resolveru. Každá dlaždice obsahuje název resolveru a jeho ID, název hostitele, používanou verzi, jednu či více IP adres, indikátor stavu operačního systému a aktuální využití zdrojů (CPU, RAM a HDD). Stav komunikačního kanálu mezi resolverem a cloudem je označen barevnou tečkou vedle popisku **Stav**.

Resolver se může nacházet v jednom z těchto stavů:

* **Aktivní**: Tento stav se očekává v produkčních prostředích a signalizuje, že vše běží správně.
* **Problém s překladem**: Resolver není schopen překládat požadavky DNS.
* **Nedostupný**: Resolver ztratil spojení se službou Whalebone Cloud. Tento stav nemá vliv na překlad DNS, nicméně resolver nemůže získávat aktualizace databáze hrozeb a nemusí reagovat na změny zásad nebo konfigurace iniciované z portálu.
* **Upgrading**: Resolveru byl vydán příkaz k aktualizaci. Tento stav by neměl přetrvávat déle než několik minut.
* **Není nainstalován**: Resolver ještě nebyl nainstalován.

Nad dlaždicemi resolverů jsou čtyři grafové záložky agregující metriky napříč všemi lokálními resolvery:

* **Časy odezvy** — rozdělení latence DNS dotazů do skupin (1 ms / 10 ms / 50 ms / 100 ms / 250 ms / 500 ms / 1000 ms / 1500 ms / pomalé).
* **Provoz** — absolutní objem dotazů v čase.
* **Provoz %** — relativní podíl na resolver.
* **Denní požadavky** — celkový denní počet požadavků.

.. note:: Pokud zatím nemáte žádný nainstalovaný resolver, na stránce se zobrazí výzva **Vytvořte si první resolver** s tlačítkem **Vytvořit nový**. Postup instalace najdete v sekci :doc:`local_resolver`.

Akce nad resolverem
~~~~~~~~~~~~~~~~~~~

Každá dlaždice resolveru má v pravém horním rohu nabídku se třemi tečkami obsahující následující akce:

* **Upravit resolver** — otevře detail resolveru (lze také kliknout na název resolveru).
* **Vymazat keš pro doménu** — vyprázdní záznamy keše resolveru pro zadanou doménu.
* **Vymazat keš resolveru** — vyprázdní celou DNS keš na resolveru.
* **Trasovat doménu** — spustí trasování překladu domény z tohoto resolveru.
* **Je tato doména blokována?** — ověří, zda by zadaná doména byla blokována stávající politikou.
* **Změnit název** — přejmenuje resolver v portálu.
* **Smazat resolver** — odstraní resolver z portálu. Tato akce neodinstaluje software na hostiteli; viz :doc:`uninstalling`.

Nahrání konfigurace
-------------------

Pokud došlo ke změnám konfigurace, které mají vliv na překlad DNS, je třeba následně **Nahrát konfiguraci**. Jinak se změny neprojeví. V případě, že jsou k dispozici nějaké změny konfigurace, které lze nasadit, bude na kartě resolveru viditelná **červená ikona** se šipkou vpravo. Po kliknutí na ni bude webová stránka požádána o potvrzení a v pravém horním rohu bude oznámeno úspěšné nasazení.

.. note:: Pokud nasazení skončilo chybou, zkuste akci zopakovat. Důvodem chyby může být krátkodobý výpadek komunikace mezi cloudem a resolverem.

Na následující animaci uvidíte nahrání konfigurace na resolver.

.. image:: ./img/lrv2-deployconfig.gif
   :align: center

Detail resolveru
----------------

Kliknutím na název resolveru (nebo na **Upravit resolver** v nabídce na dlaždici) se otevře stránka s detailem resolveru. Stránka je rozdělena do šesti sekcí v levém menu:

* :ref:`statistiky`
* :ref:`prirazeni-politik`
* :ref:`pokrocila-konfigurace`
* :ref:`aktualizace`
* :ref:`protokol-akci`
* :ref:`integrace`

Pravý sloupec zobrazuje **Název hostitele**, **Rozhraní** s přiřazenými IP adresami, **Platformu** (operační systém) a **Verzi** pro referenci.

.. _statistiky:

Statistiky
~~~~~~~~~~

Výchozí pohled při otevření detailu resolveru. Obsahuje živé provozní grafy:

* **Časy odezvy resolveru** — dotazy rozdělené podle latence (1 ms / 10 ms / 50 ms / 100 ms / 250 ms / 500 ms / 1000 ms / 1500 ms / pomalé).
* **Zdraví** — procento úspěšných kontrol zdraví v rámci pozorovaného intervalu.
* **Vytížení CPU** — využití procesoru na hostiteli resolveru.
* **Využití paměti / Swap / Disku** — metriky paměťové zátěže.
* **Počet zápisů / čtení** — diskové vstupně-výstupní operace.
* **Zapsané / přečtené bajty** — propustnost diskového I/O.
* **Přijaté / odeslané pakety** — počítadla síťových paketů.
* **Přijaté / odeslané bajty** — síťová propustnost.

.. _prirazeni-politik:

Přiřazení politik
~~~~~~~~~~~~~~~~~

Pohled **Přiřazení politik** sdružuje tři související nastavení.

Nastavení blokační stránky
""""""""""""""""""""""""""

* **Umístění blokační stránky** — výběr mezi **Whalebone Cloud** (blokační stránky obsluhované Whalebone) a **On-premise lokální resolver** (blokační stránky obsluhované z hostitele resolveru). Při volbě **On-premise lokální resolver** se zobrazí dvě další pole:

  * **IPv4 pro blokační stránku** — IPv4 adresa pro blokační stránku. Měla by být nastavena na veřejnou IP adresu resolveru.
  * **IPv6 pro blokační stránku** — IPv6 adresa pro blokační stránku. Měla by být nastavena na veřejnou IP adresu resolveru.

.. tip:: Blokační stránky jsou umístěny **přímo** na resolverech, takže je třeba použít IP adresy, které jsou inzerovány klientům. Klienti pak budou při blokování přesměrováni na IP adresu resolveru. Zajistěte, aby byly na firewallu přístupné porty 80 a 443.

Strategie přiřazování politik
"""""""""""""""""""""""""""""

Volba **Přiřadit politiku podle IP** určuje, podle čeho resolver rozhoduje, jakou politiku aplikovat na DNS dotaz:

* **Klient** — přiřazení podle IP adresy klienta. Použijte, pokud chcete politiky řízené IP rozsahy klientských zařízení (například odlišné politiky pro různé podsítě koncových uživatelů).
* **Resolver** — přiřazení podle IP adresy resolveru. Použijte, pokud se klienti dostávají k Whalebone prostřednictvím vlastního DNS serveru a politika má být určena podle IP tohoto serveru.

Tabulka přiřazení politik
"""""""""""""""""""""""""

Zásady zabezpečení a obsahu lze granulárním způsobem přiřadit různým segmentům sítě. Nastavení se vztahuje na jednotlivé resolvery a lze je nakonfigurovat v části **Resolvery** → ``Název resolveru`` → **Přiřazení politik**.

.. note:: Konfigurace se vztahuje **na každý resolver zvlášť**. V případě, že chcete konfiguraci použít pro více resolverů, upravte konfiguraci u všech resolverů.

Politiky lze aplikovat přidáním rozsahů IP ve vstupních polích:

.. image:: ./img/add-policy.PNG
   :align: center

Pro lepší pochopení uvažujme příklad s rozsahem sítě ``10.10.0.0/16``.

Vytvořili jsme 3 různé politiky:

* **Default**: Tuto politiku chceme použít pro celou síť. Jedná se o nejobecnější politiku.
* **Exception**: Politika pro konkrétní segment v síti, který bude mít vypnuté veškeré zabezpečení a filtrování obsahu.
* **Schools**: Politika pro 2 různé podsítě, které byly přiřazeny školnímu prostředí. V tomto případě jsme zvolili přísnější blokování.

.. figure:: ./img/policies-example-1.png
   :alt: Default policy
   :align: center

   Výchozí politika

.. figure:: ./img/policies-example-2.png
   :alt: Exception policy
   :align: center

   Politika s vypnutým zabezpečením a filtrováním obsahu

.. figure:: ./img/policies-example-3.png
   :alt: Schools policy
   :align: center

   Politika s přísnějším blokováním

.. note:: Výchozí politika je aplikována na všechny nedefinované rozsahy. V případě různých politik ovlivňujících stejný rozsah se použije ta granulárnější.

Shrňme požadavky do následující tabulky:

========================= ===============================
**Bezpečnostní politika** **Síťový rozsah**
========================= ===============================
Default                   10.10.0.0/16
Exception                 10.10.10.0/24
Schools                   10.10.20.0/24 a 10.10.40.0/24
========================= ===============================

Následující obrázek ukazuje proces přiřazování politik k rozsahům:

.. image:: ./img/policy_task.png
   :align: center

.. note:: Po přidání politik k rozsahům je nutné kliknout na **Uložit do resolveru**, aby se změny projevily. Poté budou změny ověřeny a vyskakovací zpráva poskytne další informace.

Pro přidání dalších položek ke stávajícímu přiřazení lze přidat nový rozsah sítě pomocí **nového řádku** jako oddělovače.

V návaznosti na předchozí příklad, kdy bychom chtěli přidat podsíť ``10.10.30.0/24`` do bezpečnostní politiky **Exception**, tuto podsíť přidáme jako nový rozsah k existující politice:

.. image:: ./img/add-range.gif
   :align: center

Pro každý přidaný rozsah IP adres je v rozevírací nabídce uvedena přiřazená blokační stránka.

.. figure:: ./img/blocking-page-assign.png
   :alt: Přiřazení blokační stránky k adresnímu rozsahu
   :align: center

   Přiřazení blokační stránky k adresnímu rozsahu

.. important:: První položka v **Přiřazení politik** je považována za výchozí. V případě, že klient přistupuje k resolveru z nedefinovaného rozsahu IP, bude spadat pod politiku a blokační stránku z této výchozí položky.

.. note:: Po provedení potřebných změn v nastavení blokační stránky zkontrolujte, zda je třeba nové nastavení nahrát na resolvery.

.. _pokrocila-konfigurace:

Pokročilá konfigurace
~~~~~~~~~~~~~~~~~~~~~

Pohled **Pokročilá konfigurace** zpřístupňuje technická nastavení na úrovni resolveru.

* **Volba konfigurace DNS překladu** — vyberte profil DNS překladu, který se má použít na tento resolver. Profily se definují v sekci :doc:`dns_resolution`. Výchozím profilem je **Default DNS resolution**.

V sekci **Expertní nastavení** (ve výchozím stavu sbalená) lze přepsat následující výchozí hodnoty:

* **Vypnout logování DNS** — když je zapnuto, resolver nezaznamenává lokální záznamy dotazů. Používejte pouze pokud to vyžaduje objem logů nebo požadavky na soukromí; mnoho funkcí (Hrozby, Obsah) na těchto záznamech závisí.
* **Upravit velikost rotace logů** — přepíše výchozí velikost pro rotaci log souborů resolveru.
* **Cíle syslogu** — přidá jeden či více vzdálených syslog cílů, na které bude resolver přeposílat logy. Dostupné log soubory a formáty popisuje sekce :doc:`syslog_integration`.
* **Počet procesů resolveru** — přepíše počet pracovních procesů pro překlad na hostiteli.
* **Naslouchat na všech IP adresách** — je-li zapnuto (výchozí), resolver naslouchá na všech IP adresách všech rozhraní hostitele. Vypněte pro omezení naslouchání pouze na vybranou podmnožinu (konfiguruje se přes Whalebone podporu).

Kliknutím na **Uložit** uložíte změny. Stejně jako u jiných změn konfigurace je vyžadováno nasazení na resolver.

.. _aktualizace:

Aktualizace
~~~~~~~~~~~

Pohled **Aktualizace** zobrazuje aktuální verzi resolveru a datum vydání a je rozdělen do tří podzáložek.

**Dostupná aktualizace**
    Ukazuje, zda je dostupná novější verze v aktuálním kanálu. Pokud je resolver aktuální, zobrazí se zpráva **Používáte nejnovější verzi a momentálně nejsou k dispozici žádné nové aktualizace.** Když je dostupná aktualizace, lze ji z této záložky spustit.

**Kanál aktualizací**
    Umožňuje přepínat mezi podporovanými vydavatelskými kanály resolveru. Existují tři kanály:

    .. list-table::
       :header-rows: 1
       :widths: 15 25 60

       * - Kanál
         - Stav
         - Klíčové vlastnosti
       * - **Verze 3**
         - Aktuální kanál — hlavní podporovaná větev, průběžně přibývají nové funkce.
         - **Vynucení bezpečného vyhledávání** (Google, YouTube, Bing, DuckDuckGo, Ecosia; kategorie: pro dospělé, zbraně, zneužívání dětí, drogy, terorismus, násilí). **Rate Limiting** (ochrana proti DDoS na UDP/53 — není dostupné pro DoH/DoT). **CPU-Aware Deferring** (zpomalí náročné klienty, když vytížení CPU vzroste). **Statické DNS záznamy** včetně SRV (A, AAAA, CNAME, TXT byly podporovány již dříve). Obsahuje všechny funkce verze 2.
       * - **Verze 2**
         - Pouze opravy — bezpečnostní a chybové opravy, žádné nové funkce.
         - **Komplexní zpravodajství o hrozbách** (odstraňuje omezení velikosti databáze ve verzích 1.0.96 a starších). Volitelný modul **integrace s Active Directory** — obohacuje logy o názvy zařízení pomocí reverzního DNS vyhledávání.
       * - **Verze 1**
         - Konec životního cyklu — nevychází další opravy.
         - Pro další bezpečnostní opravy přejděte na verzi 2.

    Pro přechod mezi kanály klikněte na **Přepnout na tuto verzi** na kartě požadovaného kanálu.

    .. note:: Některé funkce verze 3 (**Rate Limiting**, **CPU-Aware Deferring**, **Statické DNS záznamy**) se konfigurují přes YAML soubor pracovníky technické podpory Whalebone a nejsou v Admin Portálu dostupné přes UI.

**Vrácení změn**
    Pokud nedávná aktualizace nepřinesla očekávaný výsledek, lze v této záložce znovu aplikovat předchozí verzi. Pokud pro resolver není zaznamenána žádná předchozí verze, zobrazí se zpráva **Žádná předchozí verze není k dispozici**.

.. image:: ./img/rollback.png
   :align: center

.. _protokol-akci:

Protokol akcí
~~~~~~~~~~~~~

Chronologický záznam všech akcí provedených na tomto resolveru — vytvoření, nasazení konfigurace, aktualizace, návraty atd. Každý záznam obsahuje časové razítko, typ akce a výsledek (například *Akce byla úspěšně dokončena*). Tento pohled využijete při ladění neúspěšných nasazení nebo pro potvrzení, kdy se změna skutečně dostala k resolveru.

.. _integrace:

Integrace
~~~~~~~~~

Pohled **Integrace** sdružuje volitelné funkce, které obohacují chování resolveru o data z vašeho prostředí. V současnosti je k dispozici jedna integrace.

Vyhledávání názvů zařízení
""""""""""""""""""""""""""

Obohacuje DNS logy o názvy zařízení získané z PTR záznamů na vašich autoritativních DNS serverech. Konceptuální přehled najdete v sekci :doc:`active_directory`.

.. note:: Tato funkce vyžaduje nejnovější verzi resolveru. Pokud je nainstalovaná verze starší, zobrazí portál upozornění s odkazem **Aktualizovat verzi resolveru**.

.. important:: Veškeré změny nastavení integrací vyžadují nahrání politik na resolver ze stránky **Resolvery**.

K dispozici jsou následující pole:

* **Logovat názvy zařízení v síťovém provozu** — hlavní přepínač zapnutí/vypnutí integrace.
* **Segmentace sítě** — zvolte, zda má resolver používat jediný seznam autoritativních DNS serverů (**Ne**), nebo používat autoritativní DNS servery podle jednotlivých síťových segmentů konfigurovaných v sekci :doc:`dns_resolution` (**Ano**).
* **Autoritativní DNS servery** — seznam IP adres (a volitelné **Pokročilé nastavení**) používaných pro reverzní (PTR) vyhledávání při volbě segmentace sítě **Ne**.
* **Časový limit reverzního DNS dotazu** — časový limit jednoho dotazu v milisekundách (výchozí ``500``).
* **Počáteční kapacita úspěšné keše** — počet záznamů předem vyhrazených v keši úspěšných odpovědí (výchozí ``1000``).
* **Maximální kapacita úspěšné keše** — maximální počet záznamů v keši úspěšných odpovědí (výchozí ``10000``).
* **TTL úspěšné keše** — minimální alternativní TTL keše pro úspěšné PTR odpovědi v minutách (výchozí ``10``).
* **Počáteční kapacita keše neúspěchů** — počet záznamů předem vyhrazených v keši neúspěšných odpovědí (výchozí ``1000``).
* **Maximální kapacita keše neúspěchů** — maximální počet záznamů v keši neúspěšných odpovědí; při zaplnění se náhodná položka vyřadí (výchozí ``10000``).
* **TTL keše neúspěchů** — počet minut, po které jsou neúspěšné PTR dotazy uchovávány před opětovným pokusem (výchozí ``10``).

Kliknutím na **Uložit** uložíte změny.

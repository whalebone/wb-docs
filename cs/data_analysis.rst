Analýza dat
===========

Whalebone Portal (grafické uživatelské rozhraní) poskytuje uživateli řadu možností, jak analyzovat, co se děje na DNS resolverech a v síti.

Obsah
-------

Karta **Obsah** zobrazuje přehled zaznamenaného provozu podléhajícího nastavení filtrování obsahu. Pokud nemáte filtr obsahu povolen nebo jej nepoužíváte, nebude na této kartě nic zaznamenáno.

Jak zobrazit všechny dotazy určitého typu:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Nejjednodušší způsob, jak vybrat dotazy určitého typu, je kliknout na ikonu **filtr** a vybrat požadovaný typ dotazu. Na výběr je několik možností, včetně ``Sexuální obsah``, ``Hazardní hry``, ``Audio/video``, ``Reklama`` a dalších 13 kategorií z celkových 17. Případně můžete kliknout na některou z kategorií zobrazených v koláčovém grafu v části **Kategorie** nebo přímo v grafu zobrazujícím všechna data.


ow pro vyhledávání domény:
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Chcete-li vyhledat domény, můžete použít textové pole **Filtr výsledků** a zadat název hledané domény. Dalšími způsoby vyhledávání domény je kliknutí na doménu v sekci **Doména** nebo přímo v seznamu záznamů ve stejném sloupci.


Jak změnit rozsah dat dostupných údajů:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Rozsah dat, která lze zobrazit v náhledu portálu, lze změnit několika způsoby. Základní způsob výběru zahrnuje výběr předdefinovaných časových oken (1,7, 14 nebo 30 dní) z rozevíracího seznamu umístěného vedle **filtru výsledků**. V případě potřeby lze určit konkrétní časový rozsah pomocí oken **Datum a čas zahájení** a **Datum a čas ukončení**.


Kliknutím na koláčové grafy můžete také vyfiltrovat **IP klienta** a **Resolvery**.

Návrh na změnu kategorie
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Může se stát, že bude některá z domén špatně kategorizována. Ověřit do jakých kategorií doména spadá můžete pomocí nástroje **Analýza domény** nacházejícím se v uživatelském menu. Po zadání domény se objeví sekce **Kategorizace obsahu**, kde se zobrazí jednotlivé kategorie, do kterých doména spadá a zároveň se nabízí tlačítko **Navrhnout změnu kategorie** přes které je možné navrhnout změnu kategorizace. Zároveň pomocí tlačítka **Nahlásit jako škodlivou** je možné nahlásit doménu, jako false positive.

DNS Provoz:
-----------

Záložka **DNS Provoz** obsahuje přehled o provozu, který byl
byl zaznamenán na resolveru. Obsahuje všechny dotazy spolu s některými
dalšími informacemi, jako je typ, odpověď a TTL (time to live) odpovědi.

.. tip:: Data podléhají de-duplikaci. To znamená, že resolver
   zaznamenává pouze jedinečné kombinace dotazu, typu dotazu a odpovědi za 24 hodin.
   hodin. Z tohoto důvodu se může stát, že dotaz nebude viditelný na
   portálu, i když byl vyřešen.

Videoprůvodce krok za krokem si můžete prohlédnout :ref:`zde<Provoz DNS video>`.


Níže budou popsány některé užitečné možnosti filtrace dostupných dat.


Zobrazení dotazů určitého typu:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Nejjednodušším způsobem, jak vybrat dotazy určitého typu je pomocí zakliknutí ikony **filtr** a zvolení požadovaného typu dotazu. Na výběr je několik možností, mezi které se řadí: ``A``, ``AAAA``, ``CNAME``, ``MX``, ``NS``, ``PTR``, ``RRSIG``,
``SPF``, ``SRV`` a ``TXT``.



Zobrazení odpovědí podle typu:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

V okně **Odpovědi** je možné zvolit požadovanou odpověď, nebo v seznamu logů ve sloupci **odpověď** nebo požadovanou odpověď zakliknout.

Vyhledání domény:
~~~~~~~~~~~~~~~~~

K vyhledání domén lze využít textové pole **Filtr výsledků** do kterého lze zadat název hledané domény. Mezi další možnosti, jak vyhledat doménu je zakliknutí domény v části **Domény 2. řádu** popř. přímo v seznamu logů ve stejnojmenném sloupci.


Jak změnit časový rozsah událostí:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Rozsah data údajů, které lze zobrazit v náhledu na portálu, lze měnit několika způsoby. Mezi základní způsob výběru se řadí volba předdefinovaných časových oken (1,7 nebo 14) v rozbalovacím seznamu umístěném vedle **filtru výsledků**. V případě potřeby je možné specifikovat konkrétní časové rozmezí pomocí oken **Datum a čas začátku** a **Datum a čas konce**.


How to view DGA (Domain Generation Algorithm) indications:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Indikace DGA lze vyfiltrovat podobným způsobem, jako v případě zobrazení dotazů určitého typu, v tomto případě stačí zvolit poslední záznam v seznamu - **DGA**

Nahlášení "False negative"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

V některých případech je možné, že nedojde ke správné klasifikaci nebezpečnosti domény. V případě, že budete mít pocit, že by měla být doména blokována a není, je možné ji pomocí tlačítka **Nahlásit jako škodlivou** nahlásit, jako škodlivou doménu a tím dojde k vyvoření požadavku na přezkoumání domény. Tato volba se nacházív tabulce logů pod ikonou šipky u jednotlivých dotazů.


Hrozby
------

Hrozby jsou zvláštní události, při kterých dochází k požadavku DNS na doménu která se nachází v Whalebone dazabázi. Existují dva typy akce při zjištění hrozby. První je **audit** události a zároveň
druhým je její **Block**. Možnost **Audit** pouze zaznamená doménu, ale přístup je uživateli umožňěn. 

Akce, která má být provedena, závisí na nastavení bezpečnostních politik, které jsou
přiřazeny konkrétnímu resolveru. Více informací naleznete v sekci :ref:`Bezpečnostní politiky<Bezpecnostni politiky>`.

Existují některé předkonfigurované filtry, které lze aplikovat na data. Ukázky některých dotazů jsou zobrazeny níže. Tyto dotazy zobrazují
většinu případů použití, ale není zde žádné pevné omezení, protože
dostupný vyhledávač je **full-textový** a lze sestavit **jakýkoli** dotaz.

Videoprůvodce krok za krokem si můžete prohlédnout `zde<Typy hrozeb video>`.


Vyhledání událostí typu audit/block:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Existují dvě možnosti filtrování různých typů událostí. První možností je využítí vizuálního filtru. V rámci grafu můžete kliknutím na jednu z akcí (audit, blokování, povolení) filtrovat a zobrazit pouze případy, ve kterých k dané události došlo. Druhou možností je kliknout vedle pole **Filtr výsledku** na tlačítko **Filtr** a vybrat požadovanou možnost filtrování.

Vyhledání domény:
~~~~~~~~~~~~~~~~~~~~

Nejjednodušším způsobem vyhledání domény lze pomocí kliknutí na konkrétní doménu v hostorii logů. Druhou možností je pomocí zadání názvu domény do pole **Filtr výsledků**.

Vyhledání konkrétní IP adresy:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Vyfiltrování logů od konkrétní IP adresy je možné po vybrání konkrétní zdrojové IP adresy v historii logů. Druhou možností je pomocí zadání názvu domény do pole **Filtr výsledků**.


Vyhledání události na základě konkrétní kategorie hrozeb:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Existuje velké množství kategorií hrozeb.

Z nichž jmenujeme např.: *malware*, *c&c*, *blacklist*,
*phishing*, *coinminer*, *spam*, and *compromised*.

Jednoduchým způsobem vyhledání útoků je možné vybráním konkrétní kategorie z koláčových grafů nebo v sezamu logů v sloupci **Kategorie hrozeb**. Další možností je kliknout vedle pole **Filtr výsledku** na tlačítko **Filtr** a vybrat požadovanou možnost filtrování.


Jak změnit časový rozsah událostí:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Rozsah data údajů, které lze zobrazit v náhledu na portálu, lze měnit několika způsoby.
Mezi základní způsob výběru se řadí volba předdefinovaných časových oken (1,7, 14 nebo 30 dní) v rozbalovacím seznamu umístěném vedle **filtru výsledků**. V případě potřeby je možné specifikovat konkrétní časové rozmezí pomocí oken **Datum a čas začátku** a **Datum a čas konce**.


Analýza domény:
~~~~~~~~~~~~~~~

V případě, že se chcete dozvědět další informace o doméně, zejména jaké skóre 
Whalebone přiřazuje konkrétní doméně, kdy byla poprvé spatřena a zařazena do kategorie 
jako škodlivá, zda spadá do regulační kategorie nebo z jakých externích zdrojů. 
o ní víte, podívejte se na video :ref:`zde<Analyza domeny video>`.

Nahlášení "False positive"
~~~~~~~~~~~~~~~~~~~~~~~~~~

V některých případech je možné, že nedojde ke správné klasifikaci nebezpečnosti domény. V případě, že budete mít pocit, že by neměla být doména blokována a není, je možné ji pomocí tlačítka **Nahlásit falešnou detekci** nahlásit, jako špatně klasifikovanou doménu a tím dojde k vyvoření požadavku na přezkoumání domény. Tato volba se nacházív tabulce logů pod ikonou šipky u jednotlivých dotazů.


Fulltextové vyhledávání 
~~~~~~~~~~~~~~~~~~~~~~~

Pro pokročilejší použití lze použít fulltextový filtr a sestavit složený dotaz.
Tato pole lze spojovat pomocí logických operátorů. Podporovány jsou ``AND, OR, NOT, <, >`` a zástupný znak ``*``. Řetězce nemusí být obaleny uvozovkami. Příklad syntaxe je následující:
``action: block AND accu:>70 AND (client_ip: 10.20.30.41 OR 10.20.30.40 OR 192.168.*)``
``a NOT geoip.country_name: Germany AND matched_iocs.classification.type: malware AND NOT phishing`` 
Při spuštění fulltextového dotazu se aktualizuje obsah celého řídicího panelu.

+--------------------------------------+-------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| Hrozby                               | Popis                                                                                     |  Příklad hodnoty                                                         |
+======================================+===========================================================================================+==========================================================================+
| ``timestamp``                        | Přesný čas, kdy resolver zaregistroval požadavek / incident DNS                           | ``2022-10-14T12:28:01.000Z``                                             |
+--------------------------------------+-------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| ``client_ip``                        | Zdrojová IP adresa, ze které byl odeslán požadavek / incident DNS                         | ``192.168.2.3``                                                          |
+--------------------------------------+-------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| ``domain``                           | Doména v dotazu DNS                                                                       | ``whalebone.io`` OR ``whale*one.io``                                     |
+--------------------------------------+-------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| ``resolver_id``                      | The id of ther resolver which handled the event                                           | ``2404``                                                                 |
+--------------------------------------+-------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| ``device_id``                        | ID resolveru, který událost zpracoval                                                     | ``MB2A1b4OTDin3Xz6DgftAip72v57e``                                        |
+--------------------------------------+-------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| ``geoip.continent_code``             | Kód kontinentu z php knihovny geoIP                                                       | ``AF | AN | AS | EU | NA | OC | SA``                                     |
+--------------------------------------+-------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| ``geoip.country_code3``              | Kód země z php knihovny geoIP                                                             | ``RU | CZ | US | CN | DE | ...``                                         |
+--------------------------------------+-------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| ``geoip.country_name``               | Jméno země z php knihovny geoIP                                                           | ``Russia``                                                               |
+--------------------------------------+-------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| ``ip``                               | IP adresa v odpovědi DNS nebo IP adresa odpovědi, kdyby ji resolver nezablokoval          | ``174.85.249.36`` OR ``SERVFAIL`` OR ``NXDOMAIN``                        |
+--------------------------------------+-------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| ``action``                           | Akce, kterou resolver provedl s daným dotazem                                             | ``block | allow | audit``                                                |
+--------------------------------------+-------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| ``accu``                             | Skóre domény v době události                                                              |  ``0..100`` < and > operators can be used too                            |
+--------------------------------------+-------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| ``matched_iocs.classification.type`` | Typ zranitelnosti                                                                         | ``malware | c&c | phishing | coinminer | spam | compromised | blacklist``|
+--------------------------------------+-------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+


.. tip:: Filtrační operátory jsou umístěny staticky v URL. Proto si můžete vytvořit sadu
	filtrů předem (například zobrazení na jednotlivé IP adresy) a v případě potřeby je použít. Můžete je uložit do CRM a v případě řešení problémů k nim přistupovat okamžitě. To
	pomůže ušetřit váš čas, když zákazník požádá o podporu, protože můžete situaci okamžitě ověřit.
***********************
Přehled verzí resolveru
***********************

Tato stránka obsahuje poznámky k jednotlivým verzím Whalebone Resolveru určené
zákazníkům. Před aktualizací si přečtěte požadavky a poznámky k cílové verzi.

Resolver 3.5.1
==============

Požadavky před aktualizací
--------------------------

.. important::

   **Je vyžadován Docker Engine 24.0 nebo novější.**

   Tato verze není kompatibilní s Docker Engine 23.0 a staršími verzemi. Před
   aktualizací resolveru ověřte, že server používá Docker Engine 24.0 nebo
   novější. V opačném případě může aktualizace selhat a resolver může skončit ve
   stavu **Nedostupný**, jehož oprava vyžaduje ruční zásah na serveru.

   Virtualizované prostředí musí virtuálnímu stroji zpřístupnit požadované
   instrukce CPU x86-64-v2 nebo x86-64-v3, včetně AES. V opačném případě může
   resolver selhat kvůli závislosti použité knihovny. Další informace najdete v
   `průvodci řešením problémů <https://helpdesk.whalebone.io/en/support/solutions/articles/9000270277-no-threats-or-content-showing-after-upgrade>`_.

Hlavní změny v aktualizaci
--------------------------

.. only:: Immunity or Peacemaker

   * **Drobná úprava logování:** Běžné dotazy do databáze jsou nyní
     zaznamenávány s odpovídající úrovní logování.

.. only:: Aura

   * **Vyšší spolehlivost RADIUS:** Zabraňuje falešným upozorněním monitoringu
     a zbytečným restartům služeb v prostředích využívajících identity získané
     přes RADIUS.
   * **Drobná úprava logování:** Běžné dotazy do databáze jsou nyní
     zaznamenávány s odpovídající úrovní logování.

Resolver 3.5.0
==============

Požadavky před aktualizací
--------------------------

.. important::

   **Je vyžadován Docker Engine 24.0 nebo novější.**

   Tato verze není kompatibilní s Docker Engine 23.0 a staršími verzemi. Před
   aktualizací resolveru ověřte, že server používá Docker Engine 24.0 nebo
   novější. V opačném případě může aktualizace selhat a resolver může skončit ve
   stavu **Nedostupný**, jehož oprava vyžaduje ruční zásah na serveru.

   Virtualizované prostředí musí virtuálnímu stroji zpřístupnit požadované
   instrukce CPU x86-64-v2 nebo x86-64-v3, včetně AES. V opačném případě může
   resolver selhat kvůli závislosti použité knihovny.

   Souborový systém obsahující adresář ``/var`` musí mít celkovou kapacitu
   alespoň 70 GB. Úplné systémové požadavky najdete v části
   :doc:`local_resolver`.

Hlavní změny v aktualizaci
--------------------------

.. only:: Immunity or Peacemaker

   * **Výrazně vyšší výkon resolveru:** Ve stejném kontrolovaném testovacím
     prostředí dosáhl Resolver 3.5.0 2,3násobné propustnosti na jedno jádro CPU
     oproti Resolveru 3.4.1. Skutečný výkon závisí na konfiguraci nasazení a
     profilu provozu. To poskytuje větší kapacitu na stávajícím hardwaru a
     umožňuje předvídatelnější plánování kapacity a bezpečnější aktualizace.
   * **Deduplikace záznamů o hrozbách — ve výchozím nastavení vypnuta:**
     Opakované události spojené se stejnou hrozbou lze nyní seskupit v rámci
     nastavitelného časového okna. Jediná hrozba tak během DDoS útoku nebo
     jiného nárůstu provozu nebude nepřiměřeně dominovat statistikám hrozeb,
     přičemž zůstane zachována informace o jejím výskytu.
   * **Vyšší provozní stabilita:** Pomalé operace Dockeru a dočasná odpojení od
     cloudu již neblokují lokální kontroly stavu ani zpracování požadavků.

.. only:: Aura

   * **Výrazně vyšší výkon resolveru:** Ve stejném kontrolovaném testovacím
     prostředí dosáhl Resolver 3.5.0 2,3násobné propustnosti na jedno jádro CPU
     oproti Resolveru 3.4.1. Skutečný výkon závisí na konfiguraci nasazení a
     profilu provozu. To poskytuje větší kapacitu na stávajícím hardwaru,
     umožňuje plánování kapacity na základě naměřených dat a odstraňuje
     významnou překážku aktualizace na Resolver 3.x.
   * **Deduplikace záznamů o hrozbách — ve výchozím nastavení vypnuta:**
     Opakované události spojené se stejnou hrozbou lze nyní seskupit v rámci
     nastavitelného časového okna. Jediná hrozba tak během DDoS útoku nebo
     jiného nárůstu provozu nebude nepřiměřeně dominovat statistikám hrozeb,
     přičemž zůstane zachována informace o jejím výskytu.
   * **Spolehlivější aktualizace rozsahů IP adres a RADIUS:** Změny databází
     rozsahů IP adres a RADIUS v reálném čase se nyní aplikují atomicky v
     dávkách. To zvyšuje výkon aktualizací a zabraňuje částečnému uplatnění
     změn.
   * **Vyšší provozní stabilita:** Pomalé operace Dockeru a dočasná odpojení od
     cloudu již neblokují lokální kontroly stavu ani zpracování požadavků.

Resolver 3.4.1
==============

Požadavky před aktualizací
--------------------------

.. important::

   **Je vyžadován Docker Engine 24.0 nebo novější.**

   Tato verze není kompatibilní s Docker Engine 23.0 a staršími verzemi. Před
   aktualizací resolveru ověřte, že server používá Docker Engine 24.0 nebo
   novější. V opačném případě může aktualizace selhat a resolver může skončit ve
   stavu **Nedostupný**, jehož oprava vyžaduje ruční zásah na serveru.

   Virtualizované prostředí musí virtuálnímu stroji zpřístupnit požadované
   instrukce CPU x86-64-v2 nebo x86-64-v3, včetně AES. V opačném případě může
   resolver selhat kvůli závislosti použité knihovny.

Hlavní změny
------------

* **Bezpečnostní opravy a vyšší spolehlivost DNSSEC:** Verze obsahuje důležité
  bezpečnostní opravy DNS enginu, včetně oprav problémů v DNS-over-QUIC, které
  by v dotčených konfiguracích mohly umožnit vzdálené spuštění kódu. Zlepšuje
  také fungování DNSSEC v okrajových případech agresivního využití mezipaměti a
  aktualizuje certifikát IANA používaný k ustavení důvěry s kořenovou zónou.
* **Opravy chování DNS protokolu a resolveru:** Zlepšuje chování mezipaměti pro
  DoH, zpracování DNS64/CNAME, odpovědi EDNS BADVERS a vybrané okrajové případy
  local-data a RPZ.

Resolver 3.4.0
==============

Požadavky před aktualizací
--------------------------

.. important::

   **Je vyžadován Docker Engine 24.0 nebo novější.**

   Tato verze není kompatibilní s Docker Engine 23.0 a staršími verzemi. Před
   aktualizací resolveru ověřte, že server používá Docker Engine 24.0 nebo
   novější. Virtualizované prostředí musí zpřístupnit instrukce x86-64-v2 nebo
   x86-64-v3, včetně AES.

Hlavní změny
------------

Tato verze zlepšuje efektivitu aktualizací databází a provozní spolehlivost.

* **Flexibilnější kontrola místa na disku při aktualizaci:** Aktualizaci lze po
  ruční konfiguraci povolit i v nasazeních, která nesplňují minimální požadavek
  na místo na disku. Pro stabilní provoz důrazně doporučujeme splnit
  dokumentované hardwarové požadavky.
* **Efektivnější stahování databází:** Databáze se stahují a spravují samostatně
  pro jednotlivá databázová prostředí. Stahují se pouze změněné části.
* **Lepší souběžný provoz služeb:** HTTP a HTTPS služby blokační stránky lze
  navázat na konkrétní IP adresy, což usnadňuje provoz dalších služeb, například
  DoH, na stejném serveru.
* **Opravy provozní spolehlivosti:** Zlepšuje nastavení velikosti mezipaměti,
  kontroly časových razítek LMDB, restartování kontejnerů resolveru, sběr
  statistik Dockeru a ladicí logování blokační stránky.

.. only:: Aura

   * **Filtrování provozu RADIUS a Diameter:** Účetní provoz lze před předáním
     filtrovat pomocí konfigurovatelných pravidel atributů a AVP.
   * **Podpora pasivního listeneru Diameter:** Resolver může zpracovávat
     zrcadlený provoz Diameter CCR bez odesílání odpovědí.

Poznámky
--------

* Při aktualizaci se existující struktura databázové mezipaměti automaticky
  převede na novou strukturu rozdělenou podle databázového prostředí.
* Pokud je kontrola místa na disku obejita, může resolver běžet pod doporučenými
  požadavky. Tuto možnost používejte pouze v prověřených prostředích.
* Po aktualizaci se může zvýšit využití paměti. Jde o očekávané chování, protože
  konfigurace mezipaměti se nyní aplikuje správně a mezipaměť je uložena v RAM.

Resolver 3.3.0
==============

.. only:: Immunity or Peacemaker

   Požadavky před aktualizací
   --------------------------

   .. important::

      Je vyžadován Docker Engine 24.0 nebo novější. Virtualizované prostředí
      musí zpřístupnit instrukce x86-64-v2, včetně AES.

   Tato verze zlepšuje rozsah blokování, logování DNS provozu, aktualizace v
   reálném čase a provozní bezpečnost.

   * **Širší rozsah blokování:** Resolver blokuje domény pro více typů DNS
     dotazů, včetně TXT a CNAME.
   * **Rozšířené řízení logování DNS:** Volitelná anonymizace, deduplikace a
     vzorkování usnadňují práci s logy.
   * **Více aktualizací informací o hrozbách v reálném čase:** Resolver přijímá
     více indikátorů hrozeb průběžně.
   * **Rychlejší aktualizace politik:** Podporované změny politik a konfigurace
     se přenášejí přímo do resolverů.
   * **Bezpečnější aktualizace a provoz:** Přidává kontroly disku a rotace logů,
     kontrolu funkčnosti blokování, lepší obnovu a plynulejší metriky po restartu.

   .. note::

      Po aktualizaci mohou být některé místní logy jednorázově zpracovány znovu,
      což může dočasně vytvořit duplicitní exportované záznamy. DNS a blokování
      nejsou ovlivněny.

.. only:: Aura

   Tato verze zlepšuje rozsah blokování, práci s identitou, logování DNS
   provozu, aktualizace politik v reálném čase a provozní bezpečnost.

   * **Širší rozsah blokování:** Resolver může blokovat domény bez ohledu na typ
     DNS dotazu, včetně moderních typů, například HTTPS.
   * **Podpora identity Cisco EDNS0:** Resolver může získat identitu zařízení z
     nakonfigurovaných dat EDNS0 a použít ji při přiřazení politiky.
   * **Rozšířené řízení logování DNS:** Přidává volitelnou anonymizaci,
     deduplikaci a vzorkování.
   * **Rychlejší aktualizace politik:** Podporované změny politik a konfigurace
     se přenášejí přímo do resolverů.
   * **Bezpečnější aktualizace a provoz:** Přidává kontroly disku a rotace logů,
     kontrolu funkčnosti blokování, lepší obnovu a plynulejší metriky po restartu.

   .. note::

      Po aktualizaci mohou být některé místní logy jednorázově zpracovány znovu,
      což může dočasně vytvořit duplicitní exportované záznamy. DNS a blokování
      nejsou ovlivněny.

Resolver 3.2.0
==============

Pokročilá ochrana před hrozbami
-------------------------------

* **Kontrola CNAME řetězce:** Resolver při zpracování DNS dotazů kontroluje celý
  řetězec CNAME až do hloubky deseti úrovní.
* **Blokování hrozeb v TXT záznamech:** TXT dotazy na domény označené jako
  hrozby jsou aktivně blokovány.

Lepší viditelnost a logování
----------------------------

* **Podrobnější logy hrozeb a obsahu:** Exportované logy obsahují protokol,
  ``qclass`` a ``ede_code``.

Protokoly a uživatelská zkušenost
---------------------------------

* **Podpora DNS-over-QUIC (Beta):** DNS engine byl aktualizován na Knot Resolver
  6.2.0 a přidává předběžnou podporu DNS-over-QUIC. Beta verzi testujte pouze v
  nekritických prostředích.
* **Úprava YouTube Safe Search:** YouTube a související domény byly odebrány ze
  seznamu vynuceného Safe Search, aby byl obnoven přístup k živým přenosům.

Resolver 3.1.4
==============

* Zlepšena stabilita při vysoké DNS zátěži.
* Opraven vzácný problém se zamknutím databáze mezipaměti.

Resolver 3.1.3
==============

Tato verze opravuje chování mezipaměti Knot Resolveru, které mohlo příliš dlouho
uchovávat prázdné DNS odpovědi (NOERROR/NODATA) a způsobovat přetrvávající
výpadky po dočasných problémech upstream serveru.

* **Oprava:** Prázdné odpovědi se již neukládají s nepřiměřeně dlouhým TTL.
* **Výsledek:** Omezuje případy, kdy se doména obnoví až po vyčištění mezipaměti
  nebo změně resolveru.
* **Dopad:** Zlepšuje stabilitu DNS při dočasných problémech upstream nebo
  autoritativních serverů.
* **Doporučení:** Změna konfigurace není nutná. Po nasazení lze volitelně
  vyčistit mezipaměť.

Resolver 3.1.1
==============

* **Bezpečnější aktualizace a návrat k předchozí verzi:** Resolver se vrátí do
  funkčního stavu i po nasazení neplatné konfigurace.
* **Spolehlivější monitoring:** Opravuje chybějící metriky po neúspěšné
  aktualizaci a návratu k předchozí verzi.
* **Čistší provoz:** Omezuje zbytečné chyby tam, kde se nepoužívá volitelné
  logování dnstag/dnstap.
* **Blokační stránka ve veřejném cloudu:** Opravuje vzácné zobrazení nesprávného
  zákaznického brandingu.
* **Vyšší odolnost:** Zlepšuje automatickou obnovu po vzácných problémech s
  databází nebo načtením dat.

Resolver 3.0.1
==============

Požadavky před aktualizací
--------------------------

.. important::

   Je vyžadován Docker Engine 24.0 nebo novější. Virtualizované prostředí musí
   zpřístupnit instrukce x86-64-v2, včetně AES.

Opravy
------

* **Odolnost resolveru:** Opravuje dvě vzácné situace, které mohly při
  zpracování neobvyklých DNS zpráv způsobit ukončení resolveru. Změna
  konfigurace není nutná.

Resolver 3.0.0
==============

Požadavky před aktualizací
--------------------------

.. warning::

   Tato verze není kompatibilní s předáváním DNS dotazů pro doménu ``.local``.

.. important::

   Je vyžadován Docker Engine 24.0 nebo novější. Virtualizované prostředí musí
   zpřístupnit instrukce x86-64-v2, včetně AES.

Nové funkce
-----------

* Vynucení Safe Search.
* Odkládání zátěže podle využití CPU.
* Omezení rychlosti DNS dotazů.
* Statické DNS záznamy podporují všechny typy záznamů.

Změny
-----

* Přidána podpora Knot Resolveru 6.x a aktualizace na verzi 6.0.14.
* Přidána detekce pádů pro Knot Resolver 5 a 6.
* Do zpráv dnstap přidán příznak ``ratelimited``.
* Přidána podpora Safe Search pro klienty s filtrováním obsahu.
* Agent používá Ubuntu 24.04 a Python 3.12.
* Statistiky resolveru se sbírají přes řídicí socket.
* Zlepšena spolehlivost UNIX socketů a mazání mezipaměti jedné domény.

Resolver 2.1.7
==============

Tato verze se zaměřuje na bezpečnostní opravy a správné fungování DNSSEC.

* Opravuje okrajové případy agresivního využití mezipaměti při zpracování RRSIG
  a následujícího názvu NSEC.
* Aktualizuje certifikát IANA používaný k ustavení důvěry s kořenovou zónou.
* Zlepšuje DNSSEC odpovědi s prázdnými sekcemi ANSWER a AUTHORITY.
* Vylepšuje chování mezipaměti pro DoH.

Resolver 2.1.6
==============

* Zlepšuje chování sinkhole pro požadavky na záznamy HTTPS. Uživatelské a
  výchozí hodnoty sinkhole IPv4 a IPv6 se aplikují konzistentněji.

Resolver 2.1.5
==============

* Zlepšena stabilita při vysoké DNS zátěži.
* Opraven vzácný problém se zamknutím databáze mezipaměti.

Resolver 2.1.4
==============

Tato verze opravuje chování mezipaměti Knot Resolveru, které mohlo příliš dlouho
uchovávat prázdné DNS odpovědi (NOERROR/NODATA).

* Prázdné odpovědi se již neukládají s nepřiměřeně dlouhým TTL.
* Zlepšuje stabilitu při dočasných problémech upstream nebo autoritativních
  serverů.
* Změna konfigurace není nutná. Po nasazení lze volitelně vyčistit mezipaměť.

Resolver 2.1.1
==============

Požadavky před aktualizací
--------------------------

.. important::

   Je vyžadován Docker Engine 24.0 nebo novější. Virtualizované prostředí musí
   zpřístupnit instrukce x86-64-v2, včetně AES.

* Opravuje dvě vzácné situace, které mohly při zpracování neobvyklých DNS zpráv
  způsobit ukončení resolveru.
* Změna konfigurace není nutná.

Resolver 2.1.0
==============

Požadavky před aktualizací
--------------------------

.. important::

   Je vyžadován Docker Engine 24.0 nebo novější. Virtualizované prostředí musí
   zpřístupnit instrukce x86-64-v2, včetně AES.

Nové funkce
-----------

* Opravuje zranitelnost DNSSEC.
* Přidává EDE kódy, protokol, ``qclass`` a dobu odpovědi do logů a dnstap.
* Přidává mechanismus pro sdílení rozšířených logů.
* Vylučuje z logů provoz ``connectivity-check.whalebone.io``.
* Přidává anonymizaci IP adres klientů.
* Přidává volby pro zpřísnění TLS interní komunikace.
* Přidává identifikaci zákazníka podle prefixu IPv6.

Změny
-----

* Aktualizuje Knot Resolver na 5.7.5 a LMDB na 0.9.33.
* Rozšiřuje pasivní DNS logy o omezení rychlosti a diagnostická pole.
* Mění názvy výstupních souborů logcat na formát ``-<date>.ndjson``.
* Odstraňuje zastaralé proměnné prostředí související s NATS.

Resolver 2.0.1
==============

* Vrací Python agenta na verzi 3.8 kvůli kompatibilitě s Docker Engine 23.0 a
  staršími verzemi.

.. warning::

   Následující verze vyžaduje Docker Engine 24.0 nebo novější. Před aktualizací
   z Resolveru 2.0.1 aktualizujte Docker.

Resolver 2.0.0
==============

.. warning::

   Před aktualizací resolveru aktualizujte Docker Engine na verzi 24.0 nebo
   novější.

Hlavní změny
------------

* Zlepšuje záložní chování při poškození stažených databází.
* Přidává čas vytvoření databází do informací o stavu resolveru.
* Přidává podporu DNS dotazů za CGNAT.
* Přidává značky politik do dnstap a logů hrozeb a obsahu.
* Uchovává ETag databází i po restartu služeb.
* Přidává volitelné reverzní vyhledávání IP a konfigurovatelné filtrování logů.
* Předává zdrojový port HTTP požadavku funkci bypass blokační stránky.
* Zlepšuje kontroly stavu kontejnerů, místní API, práci s databázemi a souběžný
  přístup k LMDB.
* Odstraňuje tlačítko bypass ze stránek deny listu a zákonem nařízeného
  blokování.

Starší verze Resolveru 1.x
==========================

Resolver 1.x již není podporován. Následující historické verze jsou uvedeny pro
referenci.

Resolver 1.0.92-security-fix
----------------------------

Hlavní změny v aktualizaci
~~~~~~~~~~~~~~~~~~~~~~~~~~

Jedná se o cílenou bezpečnostní aktualizaci pro zákazníky, kteří stále
používají starší větev Resolveru 1.x.

Aktualizace přináší vybrané kritické bezpečnostní opravy, které snižují
bezprostřední bezpečnostní riziko pro dotčená nasazení Resolveru 1.x. Obsahuje
opravy scénářů pádu Resolveru při útocích vedoucích k odepření služby a vybraná
zlepšení správnosti DNS odpovědí.

Bezpečnostní opravy
~~~~~~~~~~~~~~~~~~~

Tato aktualizace obsahuje vybrané bezpečnostní opravy, které řeší scénáře pádu,
jež by mohly být v dotčených konfiguracích úmyslně vyvolány speciálně
vytvořeným DNS provozem.

Zlepšení správnosti DNSSEC a DNS odpovědí
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Aktualizace dále obsahuje vybrané opravy správnosti související se zpracováním
DNSSEC odpovědí a chováním mezipaměti Resolveru, včetně lepšího zpracování
prázdných odpovědí ANSWER/AUTHORITY a chování TTL v mezipaměti.

Zlepšení řízení ukládání do mezipaměti pro DoH
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Chování řízení ukládání do mezipaměti pro DNS-over-HTTPS bylo vylepšeno tak,
aby odpovědi lépe respektovaly limity TTL nastavené v mezipaměti Resolveru.

Omezený rozsah podpory starší větve
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tato aktualizace neobnovuje obecnou funkční ani provozní podporu Resolveru 1.x.
Je poskytována pouze jako cílená bezpečnostní oprava pro zákazníky, kteří
nemohou okamžitě přejít na Resolver 3.x.

Zákazníkům i nadále důrazně doporučujeme naplánovat aktualizaci na Resolver
3.x, který zůstává preferovanou a aktivně podporovanou verzí.

Resolver 1.0.93
---------------

* Při zjištění poškozených nebo chybějících databází při startu se jejich
  načtení přeskočí a v adresáři mezipaměti se vytvoří prázdné databáze.

Resolver 1.0.92
---------------

* Aktualizuje Knot Resolver na 5.7.4, přidává kořenový klíč DNSSEC KSK-2024 a
  omezuje buffering, který mohl přispívat k DoS přes TCP.
* Zlepšuje inicializaci, čištění a souběžné aktualizace databází.
* Přidává statistiky návštěv blokační stránky a vyžaduje TLS 1.2 nebo novější.
* Přepisuje komponenty kresman a consumer do jazyka Go pro lepší výkon a správu
  paměti.

Resolver 1.0.91
---------------

* Zlepšuje výkon consumeru a opravuje únik paměti.
* Zlepšuje správu databází a přidává konfigurovatelný počet gRPC streamů.
* Zajišťuje bezpečný souběžný přístup k mezipaměti certifikátů.

Resolver 1.0.89
---------------

* Aktualizuje Knot Resolver na 5.7.4 kvůli bezpečnostní opravě, omezení TCP
  bufferu a přidání kořenového klíče DNSSEC KSK-2024.

Resolver 1.0.87
---------------

* Opravuje přiřazení logů cloudových resolverů a zpracování škodlivých
  neexistujících domén.
* Otevírá logy dnstag v režimu přidávání kvůli rotaci logů a snížení využití CPU.

Resolver 1.0.84
---------------

* Přidává statistiky návštěv blokační stránky.
* Aktualizuje Knot Resolver na 5.7.3 a zlepšuje práci s databázemi při startu.
* Zabraňuje zaplnění disku dočasnými soubory při stahování databází.
* Zpřísňuje TLS blokační stránky na TLS 1.2 nebo novější.

Resolver 1.0.82
---------------

* Zavádí samostatné verzování komponent se závislostmi na softwaru třetích stran.
* Přidává podepsané obrazy kontejnerů, lepší zamykání a správu databází,
  konfigurovatelnou dobu bypassu a metriky blokační stránky.
* Přidává názvy hostitelů do logů hrozeb a zlepšuje stabilitu spojení.

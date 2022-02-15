****************
Lokální resolver
****************

Lokální Whalebone resolver přináší oproti cloudovým resolverům zásadní výhodu ve viditelnosti konkrétních lokálních IP adres, které na něj posílají dotazy. Whalebone resolver je založen na implementaci `Knot Resolveru <https://www.knot-resolver.cz/>`_ vyvíjeného v laboratořích CZ.NIC. 


Systémové požadavky
===================

Lokální resolver předpokládá, že bude provozovován na dedikovaném stroji na čerstvě nainstalovaném a podporovaném operačním systému.

* **Podporované operační systémy** (64-bitové, serverové edice následujících distribucí):

  * Red Hat Enterprise Linux 7, 8
  * CentOS 7, 8
  * Debian 9, 10
  * Ubuntu 16.04, 18.04, 20.04

* **Podporované souborové systémy** 

  * ext4
  * xfs pouze s podporou d_type (ftype=1)

* **Minimální hardwarové požadavky** (podporujeme fyzické i virtuální stroje):

  * 2 CPU jádra
  * 4 GB RAM
  * 40 GB HDD (nejméně 30 GB v oddílu /var)

* **Požadavky na síťovou komunikaci** (resolver pro svůj běh vyžaduje následující otevřené porty):
  
  * ``TCP+UDP/53`` do celého internetu pro potřeby DNS překladu
  * ``TCP/443`` to ``resolverapi.whalebone.io``, ``logger.whalebone.io``, ``agentapi.whalebone.io``, ``transfer.whalebone.io``, ``portal.whalebone.io``, ``index.docker.io``, ``registry-1.docker.io``, ``data.iana.org``
  * Dostupnost softwarových repozitářů pro daný operační systém

.. warning:: Bez dostupného portu 443 na výše zmíněné destinace instalace resolveru vůbec neproběhne (instalační skript bude přerušen).

.. note:: Kvůli odhadu sizingu pro větší podnikové a ISP sítě kontaktujte svého dodavatele. Nárůst systémových požadavků oproti standardním DNS resolverům (BIND, Unbound, apod.) se dá očekávat přibližně dvojnásobný na úrovni spotřeby RAM i zatížení CPU.


Instalace nového resolveru
==========================

V menu **Resolvery** klikněte na tlačítko **Vytvořit nový**. Zde zvolte název pro nový lokální resolver. Jedná se o čistě informativní údaj, který nemá vliv na fungování resolveru.
Po vyplnění názvu klikněte na tlačítko **Vytvořit resolver** 
Po stisknutí tlačítka se zobrazí informativní okno se seznamem podporovaných platforem a s příkazem pro instalaci, který zkopírujte na cílový stroj a spusťte.
Příkaz se postará o stažení instalačního skriptu, kterému předá jednorázový kód určený pro aktivaci lokálního resolveru (stejný příkaz nelze použít opakovaně).

.. image:: ./img/lrv2-create.gif
   :align: center

Po spuštění příkazu je prováděna kontrola operačního systému a případná instalace závislostí nutných pro běh lokálního resolveru. Skript o svém průběhu interaktivně informuje a zároveň vytváří i detailní log v souboru ``wb_install.log`` v aktuálním adresáři pro případ řešení neočekávaných chyb.
Úspěšný běh instalačního skriptu je zakončen oznámením ``Final tuning of the OS`` s hodnotou ``[ OK ]``. Po instalaci resolveru je na pozadí ještě prováděna jeho inicializace, která může trvat až jednotky minut, než začne resolver poskytovat své služby. 

.. image:: ./img/lrv2-install.gif
   :align: center

.. warning:: Lokální resolver je nakonfigurován jako tzv. open resolver. Bude se tedy snažit vyhovět komukoliv, kdo na něj zašle svůj dotaz. To je pohodlné z pohledu zajištění dostupnosti DNS překladu všem klientům na síti, ale je nutné zajistit, aby resolver, resp. port 53 (UDP a TCP), nebyl volně dostupný z Internetu, kvůli možnému zneužití pro DoS útoky.


Bezpečnostní politiky
=====================

V menu **Konfigurace** a záložce **Bezpečnostní politiky** je možnost definovat chování filtrace DNS provozu na resolverech. Ve výchozím stavu je k dispozici **Výchozí politika**, která je automaticky přiřazována novým resolverům.
V politice je možné definovat několik oblastí:

* **Filtrace nebezpečných domén**

  * Umožňuje provádět akce Audit (logování) nebo Blokaci (přesměrování na blokační stránku) přístupu na nebezpečné domény
  * Jednotlivé akce je možné úplně vypnout - např. vypnout blokaci pro testovací účely
  * Hodnota na posuvníku určuje míru jistoty, že se jedná o nebezpečnou doménu na škále 0 až 100 (0 není riziková doména, 100 je jistě nebezpečná)

.. tip:: Výchozí prahová hodnota blokace ``80`` je bezpečná i pro velké sítě s benevolentní politikou. Pro přísnější politiku ve velkých sítích doporučujeme volit blokaci v rozmezí ``70-75``, velmi přísné sítě (typicky v podnikovém prostředí) si mohou dovolit blokaci až na úroveň hodnoty ``60``. Audit je čistě informativní, ale příliš nízká hodnota může výrazně zvýšit počet logovaných incidentů.

* **Seznam blokovaných domén**

  * Seznamy domén, které mají být blokovány za všech okolností
  * Nemusí se jednat o rizikové domény, ale třeba o domény, které musí být blokovány na základě legislativního nařízení
  * O aktualizaci seznamů se stará společnost Whalebone

* **Výjimky**
  
  * Domény, které nebudou za žádných okolností blokovány
  * Výjimka se uplatňuje na danou doménu a všechny její subdomény, např.: výjimka na doménu ``whalebone.io`` se uplatní i na doménu ``docs.whalebone.io``, ale ne naopak

* **Blokace**
  
  * Domény, které budou za všech okolností blokovány (vyšší prioritu mají pouze **Výjimky**)
  * Blokace se uplatňuje na danou doménu a všechny její subdomény, např.: blokace domény ``malware.ninja`` se uplatní i na doménu ``super.malware.ninja``, ale ne naopak 

.. image:: ./img/lrv2-policies.gif
   :align: center

.. note:: Změny se na resolverech projeví cca do třiceti minut od uložení politik. Uložená změna konfigurace je použita pro přípravu nového balíku s informacemi o hrozbách, který si resolver z cloudu pravidelně stahuje.


Nastavení DNS překladu
======================

V menu **Konfigurace** na záložce **DNS překlad** najdete možnosti konfigurace lokálního resolveru. Stránka umožňuje základní nastavení bez nutnosti znalosti konfigurační syntax použitého resolveru. Dále je k dispozici textové pole, které umožňuje zadat jakoukoliv konfiguraci, kterou podporuje `Knot Resolver <https://www.knot-resolver.cz/>`_.

Dostupné možnosti konfigurace:

* **Povolit IPv6**

  * Pokud má stroj IPv6 správně nakonfigurovanou a funkční, je možné aktivovat pro resolver IPv6. V opačném případě může mít aktivace této volby negativní dopad na výkon a latenci.

* **Přesměrovat dotazy na nadřazené resolvery**
  
  * Tato volba umožňuje přesměrovat všechny nebo vybrané dotazy na vybrané nadřazené resolvery nebo autoritativní DNS servery (vhodné např. při přesměrování na doménové řadiče Active Directory)
  
  * **Zakázat DNSSEC validaci**

    * Při aktivaci této volby nebudou odpovědi z přesměrovaných dotazů validovány. Doporučujeme volbu aktivovat, pokud nadřazené servery nemají správně nakonfigurovaný DNSSEC

  * **Všechny dotazy na**

    * Možnost přesměrovat veškeré dotazy na jeden nebo více definovaných resolverů

  * **Následující domény**

    * Umožňuje zvolit konkrétní domény, které budou přesměrovány na definované resolvery
    * Je možné definovat různé resolvery pro různé domény

* **Statické záznamy**

  * Předdefinované odpovědi, které mají být vráceny na vybrané domény
  * Mohou sloužit pro speciální případy jako je monitoring, nebo velmi jednoduchá substituce vytvoření reálných záznamů na autoritativním serveru

* **Pokročilé nastavení DNS**

  * Textové pole pro `plnohodnotnou konfiguraci Knot Resolveru <https://knot-resolver.readthedocs.io/en/stable/daemon.html#configuration>`_
  * Podporuje Lua skriptování
  * Chybná konfigurace může ohrozit stabilitu, výkon a bezpečnostní funkce resolveru

.. image:: ./img/lrv2-resolution.gif
   :align: center

.. note:: Jakmile uživatel stiskne tlačítko **Uložit**, jsou změny v DNS překladu uloženy a nachystány na aplikaci na cílové resolvery. Samotné nasazení změn je ale nutné provést přímo ze stránky **Resolvery**. Je tedy možné dělat postupně více změn a aplikovat je najednou, aby se minimalizoval počet akcí zasílaných na resolver.


Správa resolverů
================

Na stránce **Resolvery** lze sledovat stav používaných resolverů, upravovat jejich konfiguraci, nasazovat aktualizace a instalovat nové resolvery.

Přehled resolverů
-----------------

V hlavním přehledu resolverů jsou k dispozici dlaždice s informacemi o jednotlivých resolverech. Přehled zahrnuje informace o operačním systému a využití zdrojů jako CPU, operační paměť a diskový prostor. V přehledu je také zahrnut stav služeb běžících na resolveru (očekává se, že je "Vše v pořádku") a stav odvozený od toho, zda resolver správně komunikuje s cloudem (pokud vše správně funguje, bude status "Aktivní").


Nasazení konfigurace
--------------------

Pokud jste změnili jakoukoliv konfiguraci související s logikou DNS překladu, je nutné změny na resolver manuálně nasadit. Pokud jsou k dispozici nějaké změny, které ještě nebyly na resolver nasazeny, bude v kartě viditelná červená ikonka s šipkou doprava dolů. Po kliknutí na ikonku si stránka vyžádá potvrzení, konfiguraci nasadí a zobrazí zprávu s potvrzením.

.. note:: Pokud se při pokusu o nasazení konfigurace zobrazí chyba místo potvrzení, může jít o krátkodobý výpadek spojení mezi resolverem a cloudem, zkuste tedy akci zopakovat.

.. image:: ./img/lrv2-deployconfig.gif
   :align: center


Resolver agent
===================

Interakce pomocí příkazové řádky
------------------
Akce, které provádí agent, je možné volat pomocí proxy bash skriput, který se nachází v adresíři **/var/whalebone/cli**. Tento skript volá python skript, který provádí příkazy jemu předané. Tyto příkazy jsou následující:

* **sysinfo** - vrací systémová data v následujícím JSON formátu
	* Parametry: žádné
	* Výstup: 
.. sourcecode:: js

	{
	   "hostname":"hostname",
	   "system":"Linux",
	   "platform":"CentOS Linux 7 (Core)",
	   "cpu":{
	      "count":4,
	      "usage":28.6
	   },
	   "memory":{
	      "total":7.6,
	      "available":3.9,
	      "usage":49.2
	   },
	   "hdd":{
	      "total":50.0,
	      "free":14.4,
	      "usage":71.1
	   },
	   "swap":{
	      "total":0.0,
	      "free":0.0,
	      "usage":0
	   },
	   "resolver":{
	      "answer.nxdomain":3284,
	      "answer.tc":35,
	      "answer.ad":849,
	      "answer.100ms":3983,
	      "answer.cd":6,
	      "answer.1500ms":74,
	      "answer.slow":215,
	      "answer.rd":224337,
	      "answer.1ms":104683,
	      "answer.servfail":215,
	      "predict.epoch":24,
	      "query.dnssec":6,
	      "answer.250ms":14941,
	      "query.edns":35498,
	      "answer.cached":86713,
	      "answer.nodata":3622,
	      "answer.aa":2362,
	      "answer.do":6,
	      "answer.edns0":35498,
	      "answer.ra":224337,
	      "predict.queue":0,
	      "answer.total":224337,
	      "answer.10ms":35351,
	      "answer.noerror":217216,
	      "answer.50ms":59766,
	      "answer.500ms":4642,
	      "answer.1000ms":653,
	      "predict.learned":80
	   },
	   "docker":{
	      "Platform":{
	         "Name":""
	      },
	      "Components":[
	         {
	            "Name":"Engine",
	            "Version":"17.12.1-ce",
	            "Details":{
	               "ApiVersion":"1.35",
	               "Arch":"amd64",
	               "BuildTime":"2022-02-27T22:17:54.000000000+00:00",
	               "Experimental":"false",
	               "GitCommit":"88888fc6",
	               "GoVersion":"go1.999.999",
	               "KernelVersion":"3.22.66-693.21.1.el7.x86_64",
	               "MinAPIVersion":"1.99",
	               "Os":"linux"
	            }
	         }
	      ],
	      "Version":"19.32.1-ce",
	      "ApiVersion":"1.98",
	      "MinAPIVersion":"1.12",
	      "GitCommit":"7390fc6",
	      "GoVersion":"go1.9.4",
	      "Os":"linux",
	      "Arch":"amd64",
	      "KernelVersion":"3.10.0-693.21.1.el7.x86_64",
	      "BuildTime":"2018-02-27T22:17:54.000000000+00:00"
	   },
	   "check":{
	      "resolve":"ok",
	      "port":"ok"
	   },
	   "containers":{
	      "lr-agent":"running",
	      "passivedns":"running",
	      "resolver":"running",
	      "kresman":"running",
	      "pcpy":"running",
	      "logrotate":"running",
	      "logstream":"running"
	   },
	   "images":{
	      "lr-agent":"whalebone/agent:1.1.1",
	      "passivedns":"whalebone/passivedns:1.1.1",
	      "resolver":"whalebone/kres:1.1.1",
	      "kresman":"whalebone/kresman:1.1.1",
	      "logrotate":"whalebone/logrotate:1.1.1",
	      "logstream":"whalebone/logstream:1.1.1"
	   },
	   "error_messages":{
	   },
	   "interfaces":[
	      {
	         "name":"lo",
	         "addresses":[
	            "127.0.0.1",
	            "::1",
	            "00:00:00:00:00:00"
	         ]
	      },
	      {
	         "name":"eth0",
	         "addresses":[
	            "1.1.1.1",
	            "::c8",
	            "fe80::",
	            "00:00:00:00:00:00"
	         ]
	      },
	      {
	         "name":"docker0",
	         "addresses":[
	            "198.1.1.1",
	            "00:00:00:00:00:00"
	         ]
	      }
	   ]
	}

* **stop** - zastaví až tři kontejnery
	* Parametry: kontejnery, které se mají zastavit (až 3), Příklad: ./cli.sh stop resolver lr-agent kresman
	* Výstup:  
.. sourcecode:: js

	{
		'resolver': {'status': 'success'}, 
		'lr-agent': {'status': 'success'}, 
		'kresman': {'status': 'success'}
	}

* **remove** - odtraní až 3 kontejnery
	* Parametry: kontejnery, které se mají odstranit (až 3), Příklad: ./cli.sh remove resolver lr-agent kresman
	* Výstup: 
.. sourcecode:: js 

	{
		'resolver': {'status': 'success'}, 
		'lr-agent': {'status': 'success'}, 
		'kresman': {'status': 'success'}
	}

* **upgrade** - upgraduje až tři kontejnery, konfigrurace kontejnerů je dána docker-composem v kontejneru agenta (možné najít v **/etc/whalebone/agent**)
	* Parametry: kontejnery, které se mají upgradovat (až 3), Příklad: ./cli.sh upgrade resolver lr-agent kresman
	* Výstup: ```json 
	{'resolver': {'status': 'success'}, 'lr-agent': {'status': 'success'}, 'kresman': {'status': 'success'}}
	```
* **create** - vytvoří kontejnery, konfigrurace kontejnerů je dána docker-composem v kontejneru agenta (možné najít v **/etc/whalebone/agent**)
	* Parametry: žádné, Příklad: ./cli.sh create
	* Výstup: 
.. sourcecode:: js

	{'resolver': {'status': 'success'}

* **list** - zobrazí čekající příkazy a změny, který by tyto příkazy provedly na kontejnerech zmíněných v těchto příkazech, tato akce je určená pro přímou interakci
	* Parametry: žádné, Příklad: ./cli.sh list
	* Výstup: 
.. code-block:: lua

	-------------------------------
	Changes for resolver
	New value for label: resolver-1.1.1
	  	Old value for label: resolver-1.0.0
	-------------------------------
	
* **run** - provede čekající příkazy
	* Parametry: žádné, Příklad: ./cli.sh run
	* Výstup:
.. sourcecode:: js

	{'resolver': {'status': 'success'}

* **delete_request** - odstraní čekající příkaz
	* Parametry: žádné, Příklad: ./cli.sh delete_request
	* Výstup:
.. code-block:: lua

	Pending configuration request deleted.

* **updatecache** - vynutí update IoC cache (používané k blokaci). Tato akce je určena pro manuální katualizaci blokovaných domén mimo peroidický interval
	* Parametry: žádné
	* Výstup:
.. sourcecode:: js

	{'status': 'success', 'message': 'Cache update successful'}
	
* **containers** - lists the containers and their information which include: labels, image, name and status. 
	* Parametry: žádné
	* Výstup: 
.. sourcecode:: js

	[
	   {
	      "id":"b8f4489379",
	      "image":{
	         "id":"c893b4df5ca3",
	         "tags":[
	            "whalebone/agent:1.1.1"
	         ]
	      },
	      "labels":{
	         "lr-agent":"1.1.1"
	      },
	      "name":"lr-agent",
	      "status":"running"
	   },
	   {
	      "id":"e433d58f13",
	      "image":{
	         "id":"2c4b84a7daee",
	         "tags":[
	            "whalebone/passivedns:1.1.1"
	         ]
	      },
	      "labels":{
	         "passivedns":"1.1.1"
	      },
	      "name":"passivedns",
	      "status":"running"
	   },
	   {
	      "id":"2aeec00121",
	      "image":{
	         "id":"fc442e625539",
	         "tags":[
	            "whalebone/kres:1.1.1"
	         ]
	      },
	      "labels":{
	         "resolver":"1.1.1"
	      },
	      "name":"resolver",
	      "status":"running"
	   },
	   {
	      "id":"662dac2e6c",
	      "image":{
	         "id":"b37d0d1bd10b",
	         "tags":[
	            "whalebone/kresman:1.1.1"
	         ]
	      },
	      "labels":{
	         "kresman":"1.1.1"
	      },
	      "name":"kresman",
	      "status":"running"
	   },
	   {
	      "id":"05188ac1df",
	      "image":{
	         "id":"5b50cdc924fc",
	         "tags":[
	            "whalebone/logrotate:1.1.1"
	         ]
	      },
	      "labels":{
	         "logrotate":"1.1.1"
	      },
	      "name":"logrotate",
	      "status":"running"
	   },
	   {
	      "id":"01e64dd697",
	      "image":{
	         "id":"fffb52c2dadd",
	         "tags":[
	            "whalebone/logstream:1.1.1"
	         ]
	      },
	      "labels":{
	         "logstream":"1.1.1"
	      },
	      "name":"logstream",
	      "status":"running"
	   }
	]


Každý z představených příkazů provádí stejně pojmenovanou akci. Status a výstup této akce je zobrazován v terminálu. Akce **list** a **run** jsou určeny k řešení situací, kdy je potřeba potvrzení akcí před provedením. Akce pro zobrazení zobrazí změny, které se mají provést a kontejnery, které budou ovlivněny. Toto slouží jako náhled situace, která by se měla provést. Akce pro provedení těchto příkazu je potom provede.

Akce pro upgrade a vytvoření kontejnerů používají docker-compose, který je možné najít v kontejneru agenta, jako konfiguraci pro provádění těchto akcí. Tento soucor je připnutý v adresáři **/etc/whalebone/agent** pokud se uživatel rozhodne ho upravovat. Všechny změny musí být zaneseny i do vzoru na adrese **portal.whalebone.io**. Bez nich budou tyto lokální změny přepsány při další akci manipulující s tímto souborem. 

Bash skript by měl výt volán takto: **./cli.sh action param1 param2 param3**. Action je jméno akce a jednotlivé parametry jsou parametry této akce. Pouze akce pro zastavení, odstranění a upgradování kontejnerů tyto parametry používají. 

Ve výchozím nastavení agent provádí všechny změny okamžitě. Je ale možné nastavit ukládání příkazů a jejich následné ruční provádění. Díky této možnosti je možné získat větší kontrolu nad tím, které akce agent provádí. Pro zapnutí této funkcionality je nutné nastavti proměnnou prostředí **CONFIRMATION_REQUIRED** na hodnotu **true**. Pro zobrazení změn je možné použít cli akci **list**. Pro provedení uložené akce je nutné využít cli možnosti **run**. Uložený příkaz může být právě jeden, pokud přijde další, nový přepíše ten starý. Pro manuální smazání čekajícího příkazu je možné využít akci **delete_request**. Akce, které mohou být uloženy touto možností, jsou: **upgrade**, **create** a **suicide**.

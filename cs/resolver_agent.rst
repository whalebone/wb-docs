Resolver agent
==============

Command line interface
-----------------------
Akce agenta lze vyvolat pomocí proxy bash skriptu, který se nachází v **/etc/whalebone/cli/cli.sh**. Tento skript volá python sccip, který se stará o provádění následujících akcí agenta: 

* **sysinfo** - vrací údaje o stavu systému ve formátu JSON.
	* Parametry: Žádné
	* Výstup: testované kategorie na testovaném klíči mohou mít dvě hodnoty **OK** a **FAIL**.
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
	* Parametry: kontejnery k zastavení (až 3), Příklad: ./cli.sh stop resolver lr-agent kresman

.. sourcecode:: js

	{
		'resolver': {'status': 'success'}, 
		'lr-agent': {'status': 'success'}, 
		'kresman': {'status': 'success'}
	}
	
* **remove** - odstraní až tři kontejnery
	* Parametry: kontejnery k odstranění (až 3), Příklad: ./cli.sh remove resolver lr-agent kresman
	

.. sourcecode:: js

	{
		'resolver': {'status': 'success'}, 
		'lr-agent': {'status': 'success'}, 
		'kresman': {'status': 'success'}
	}
	
* **upgrade** - aktualizuje až tři kontejnery, konfigurace kontejneru je určena pomocí docker-compose v kontejneru agenta (lze také nalézt ve adresáři **/etc/whalebone/agent**).
	* Parametry: kontejnery k upgradu (až 3), Příklad: ./cli.sh upgrade resolver lr-agent kresman
	

.. sourcecode:: js 

	{
		'resolver': {'status': 'success'}, 
		'lr-agent': {'status': 'success'}, 
		'kresman': {'status': 'success'}
	}
	
* **create** - vytvoří kontejnery, kontejnery jsou zadány pomocí docker-compose v kontejneru agenta (lze také nalézt v adresáři **/etc/whalebone/agent**).
	* Parametry: Žádné, Příklad: ./cli.sh create
	

.. sourcecode:: js

	{'resolver': {'status': 'success'}
	


	
* **updatecache** - vynutí aktualizaci mezipaměti IoC resolveru (která se používá pro blokování), tato akce by měla být provedena, aby se ručně vynutila aktualizace a obnovení domén přítomných v mezipaměti škodlivých domén.
	* Parametry: Žádné
	
	
.. sourcecode:: js

	{'status': 'success', 'message': 'Cache update successful'}
	
* **containers** - seznam kontejnerů a jejich informací, které zahrnují: štítky, obrázek, název a stav. 
	* Parametry: Žádné
	
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


Každá z těchto akcí provede podobně pojmenovanou akci a vypíše stav, nebo výstup této akce. Akce **list** a **run** jsou určeny pro stav, kdy je vyžadováno potvrzení určité akce. Seznam akcí zobrazuje akci, která má být provedena, a změny, které by tato akce provedla u kontejnerů uvedených v této akci. Slouží jako příklad toho, co by se stalo, kdyby byla čekající akce provedena. Spuštěná akce pak provede akci čekající na spuštění.

Akce **upgrade** a **create** využívají šablonu docker-compose přítomnou v kontejneru agenta k vytvoření/upgradu požadovaného kontejneru. Tato šablona se nachází v **/etc/whalebone/agent**, pokud se ji uživatel rozhodne změnit. Tuto změnu je však třeba provést i v šabloně přítomné na **portal.whalebone.io**, pokud se tak nestane, budou lokální změny při příští aktualizaci přepsány z cloudu. 

Bash skript by měl být vyvolán takto: ``./cli.sh action param1 param2 param3```. **Action** je název akce a **parameters** jsou parametry akce. Používají je pouze akce pro zastavení, odebrání a upgrade kontejneru a určují, kterých kontejnerů se má příslušná akce týkat.

Přísný režim
------------------
Výchozí volbou agenta je okamžité provedení akcí ze správy cloudu. Je však možné povolit ruční potvrzování požadavků. To dává správci kontrolu nad tím, kdy a co bude provedeno. Chcete-li povolit Přísný režim resolveru, vytvořte prosím ticket na podporu Whalebone.

Pro vypsání změn, které požadavek zavádí, je třeba použít volbu cli **list**. Pro spuštění požadavku použijte volbu cli **run**. Ve frontě může být pouze jeden čekající požadavek. Nový požadavek z cloudu přepíše předchozí, ale nový požadavek stejně obsahuje celý požadovaný stav. Pro odstranění čekajícího požadavku použijte volbu cli **delete_request**. Akce, které mohou přetrvávat, jsou následující: **upgrade**, **create** a **suicide**. Viz příklady použití příkazů CLI.

* **list** - vypíše čekající příkaz a změny, které by byly provedeny v kontejnerech zadaných v čekající akci, tato akce je určena pro lidskou kontrolu, proto je její formát 
	* Parametry: Žádné
	* Příklad: ./cli.sh list


.. code-block:: lua

	-------------------------------
	Changes for resolver
	New value for label: resolver-1.1.1
	
	  	Old value for label: resolver-1.0.0
	-------------------------------
	
* **run** - provede čekající příkaz
	* Parametry: žádné
	* Příklad: ./cli.sh run
	
.. sourcecode:: js

	{'resolver': {'status': 'success'}

* **delete_request** - odstraní čekající požadavek.
	* Parametry: žádné
	* Příklad: ./cli.sh delete_request
	
.. code-block:: lua

	Pending configuration request deleted.


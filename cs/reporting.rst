.. _header-n233:

Reporty
=======

Reporty lze nakonfigurovat v rozbalovací nabídce pod účtem uživatele. Přizpůsobit lze frekvenci doručování reportů, preferovaný den v týdnu, jazyk a příjemce.

.. note:: Výchozím příjemcem je vlastník účtu a reporty jsou doručovány na jeho registrovanou e-mailovou adresu.

.. image:: ./img/report-configuration.gif
   :align: center

Upozornění
==========

Upozornění poskytují přehled o klíčových informacích, včetně stavu resolveru, stavu DNS překladu, využití hardwaru a bezpečnostních incidentech. Všechny tyto informace lze předávat přes více kanálů, např. e-mail, Slack, syslog nebo webhook. Nové upozornění můžete vytvořit z předdefinovaných šablon a následně jej upravit editací jeho parametrů. Podrobný videonávod najdete :ref:`zde<Alerty video>`.

.. note:: Pro zapnutí upozornění je nejprve nutné přiřadit příjemce kliknutím na název upozornění.

.. note:: Syslog používá nešifrovaný TCP jako transportní protokol.

.. tip:: Whalebone používá regionální cloudové služby pro optimalizaci komunikace mezi klienty a cloudovými komponentami. Region, ke kterému je zákaznický resolver připojen, najdete v URL Admin Portálu daného zákazníka. Například pokud je URL https://portal.eu-01.whalebone.io/en/client-123456, tenant je registrován v regionu EU-01. To je užitečné při nastavování pravidel firewallu v síti zákazníka. Někteří zákazníci mohou používat prostředí Legacy, kde URL tenanta bude https://portal.whalebone.io/en/client-123456.

Upozornění zaslaná přes syslog nebo webhook jsou odesílána z IP adres uvedených v tabulce níže. Pokud zvolíte některý z těchto kanálů, ujistěte se, že na firewallu povolíte příchozí TCP provoz, abyste mohli zprávy přijímat.

+----------------+---------------------------------+
| Region         | IP adresa                       |
+================+=================================+
| AM-01          | 34.174.88.243                   |
+----------------+---------------------------------+
| APAC-01        | 34.126.172.166                  |
+----------------+---------------------------------+
| EU-01          | 34.140.218.91                   |
+----------------+---------------------------------+
| Legacy         | 159.100.247.142, 159.100.247.58 |
+----------------+---------------------------------+

DNS provoz - počet unikátních dotazů z IP
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Toto upozornění se spustí, když jedna zdrojová IP adresa dosáhne limitu unikátních požadavků s definovanými atributy.

Parametry:

* **MINUTES**: časové okno v minutách (Default=15)
* **TRESHOLD**: počet událostí v časovém okně pro spuštění upozornění (Default=100)
* **QUERY_TYPE**: filtr podle typu DNS dotazu (Default=*)
* **RESPONSE_TYPE**: filtr podle DNS odpovědi (Default=*)
* **IP_WILDCARD**: zahrnout do upozornění pouze tyto IP adresy oddělené čárkou (Default=*)
* **IP_WILDCARD_IGNORE**: ignorovat v upozornění tyto IP adresy oddělené čárkou (Default=none)
* **DOMAIN_WILDCARD**: zahrnout do upozornění pouze tyto domény oddělené čárkou (Default=*)
* **DOMAIN_WILDCARD_IGNORE**: ignorovat v upozornění tyto domény oddělené čárkou (Default=none)
* **DGA**: filtr pro algoritmicky generované domény (DGA) - pouze DGA, bez DGA, nebo obojí (Default=*)

Formát webhook a syslog zprávy:

.. code-block:: json

   {
      "client_name": "string",
      "alert": "string",
      "IP address": "string",
      "Number of requests": "number",
      "timestamp": "date"
   }

DNS provoz - procentuální nárůst dotazů
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Toto upozornění bude odesláno, když je počet DNS dotazů procentuálně vyšší v nastaveném časovém období.

Parametry:

* **MINUTES**: časové okno (Default=15)
* **PERCENT**: procentuální navýšení (např. 200 %) - rozdíl mezi dvěma intervaly (Default=50)
* **QUERY_TYPE**: filtr podle typu DNS dotazu (Default=*)
* **RESPONSE_TYPE**: filtr podle DNS odpovědi (Default=*)

Formát syslog zprávy:

.. code-block::

   Whalebone detected spike in %QUERY_TYPE% requests of more than %PERCENT% at %TIMESTAMP%.

Formát webhook zprávy:

.. code-block:: json

   {
      "client_name": "string",
      "client_id": "number",
      "resolver_id": "number",
      "timestamp": "date"
   }

DNS provoz - Phishing na základě podobné domény
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Toto upozornění je odesláno, když je detekován možný homografní útok pro zadanou doménu.

Parametry:

* **DOMAIN**: doména, která se má monitorovat kvůli možným homografním útokům. DŮLEŽITÉ: Jedno upozornění může monitorovat pouze jednu doménu.
* **DISTANCE**: počet znaků, které se mohou lišit ve phishingové doméně (Default=1)
* **DOMAIN_WILDCARD_IGNORE**: ignorovat tento seznam domén oddělených čárkou. Pokud je DISTANCE větší než 1, detekce se provede pro domény, které podporují globální i regionální top-level formáty. Doporučuje se přidat legitimní domény na whitelist, aby se předešlo falešným poplachům. (Default=none)

Formát webhook a syslog zprávy:

.. code-block:: json

   {
      "client_name": "string",
      "client_id": "number",
      "alert": "string",
      "Level2 domain": "string",
      "Query": "string",
      "Query type": "string",
      "Timestamp (UTC)": "date",
      "Client IP": "string"
   }

DNS provoz - počet unikátních dotazů
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Toto upozornění je odesláno při překročení počtu unikátních DNS dotazů na základě daného filtru.

Parametry:

* **MINUTES**: časové okno (Default=15)
* **TRESHOLD**: práh - počet událostí v časovém okně pro spuštění upozornění (Default=100)
* **QUERY_TYPE**: filtr podle typu DNS dotazu (Default=*)
* **RESPONSE_TYPE**: filtr podle DNS odpovědi (Default=*)

Formát webhook a syslog zprávy:

.. code-block:: json

   {
      "client_name": "string",
      "client_id": "number",
      "resolver_id": "number",
      "timestamp": "date"
   }

DNS traffic - detekce chyby DNSSEC
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Toto upozornění je odesláno, když počet DNSSEC chyb překročí předdefinovaný práh v pozorovaném období.

Parametry:

* **MINUTES**: časové okno, ve kterém se DNSSEC chyby počítají (Default=15)
* **TRESHOLD**: počet událostí v časovém okně pro spuštění upozornění (Default=100)
* **QUERY_TYPE**: filtr podle typu DNS dotazu (Default=*)
* **EDE_CODE**: filtr podle EDE kódu v DNS odpovědi (Default=Všechny DNSSEC kódy)

Formát webhook a syslog zprávy:

.. code-block:: json

   {
      "client_name": "string",
      "client_id": "number",
      "alert": "string",
      "Level2 domain": "string",
      "Query": "string",
      "Query type": "string",
      "Timestamp (UTC)": "date",
      "Client IP": "string",
      "EDE Code": "number"
   }

DNS provoz - detekce DNS tunnelingu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Upozornění se spustí, když je detekováno vytváření tunelu pomocí DNS protokolu na neznámou doménu.

Parametry:

* **MINUTES**: časové okno, ve kterém se počítají události s detekovaným DNS tunelováním (Default=5)
* **TRESHOLD**: počet událostí v časovém okně pro spuštění upozornění (Default=1)
* **QUERY_TYPE**: filtr podle typu DNS dotazu (Default=*)
* **RESPONSE_TYPE**: filtr podle DNS odpovědi (Default=*)
* **IP_WILDCARD**: zahrnout do upozornění pouze tyto IP adresy oddělené čárkou (Default=*)
* **IP_WILDCARD_IGNORE**: ignorovat v upozornění tyto IP adresy oddělené čárkou (Default=none)
* **DOMAIN_WILDCARD**: zahrnout do upozornění pouze tyto domény oddělené čárkou (Default=*)
* **DOMAIN_WILDCARD_IGNORE**: ignorovat v upozornění tyto domény oddělené čárkou (Default=none)

Formát webhook a syslog zprávy:

.. code-block:: json

   {
      "client_name": "string",
      "client_id": "number",
      "alert": "string",
      "Level2 domain": "string",
      "Query": "string",
      "Query type": "string",
      "Timestamp (UTC)": "date",
      "Client IP": "string"
   }

Resolver - výpadek komunikace s cloudem
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Toto upozornění je odesláno, když backend neobdrží žádnou zprávu od lokálního resolveru déle než 20 minut.

Formát webhook a syslog zprávy:

.. code-block:: json

   {
      "client_name": "string",
      "client_id": "number",
      "resolver_id": "number",
      "timestamp": "date"
   }

Resolver - nedostatek systémových prostředků
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Toto upozornění je odesláno, když lokální resolver detekuje, že využití systémových prostředků překračuje definovaný práh. Parametry jsou vyjádřeny jako procenta využitých oproti celkovým prostředkům. Například pokud chcete být upozorněni při využití 80 % celkového místa na disku hostitele, nastavte THRESHOLD_HDD na 80.

* **THRESHOLD_CPU**: využití CPU (Default=80)
* **THRESHOLD_MEMORY**: využití RAM (Default=90)
* **THRESHOLD_HDD**: využití HDD (Default=80)

Formát webhook a syslog zprávy:

.. code-block:: json

   {
      "client_name": "string",
      "client_id": "number",
      "resolver_id": "number",
      "hostname": "string",
      "timestamp": "date",
      "CPU-usage": "number",
      "Memory-usage": "number",
      "Disk-usage": "number",
      "Alert-name": "string"
   }

Resolver - výpadek překladu
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Resolver periodicky provádí kontroly pro testování překladu známých domén. Každou minutu se kontrolují Google.com, facebook.com, microsoft.com a apple.com. Výchozí nastavení parametrů je velmi přísné, takže upozornění se odešle i tehdy, když během 10minutového intervalu selže překlad jedné ze čtyř domén.

Parametry:

* **TRESHOLD**: počet událostí v časovém okně pro spuštění upozornění (Default=1)
* **MINUTES**: časové okno v minutách (Default=10)

Formát webhook a syslog zprávy:

.. code-block:: json

   {
      "subject": "DNS resolution failure",
      "client_name": "string",
      "client_id": "number",
      "resolver_id": "number",
      "hostname": "string",
      "timestamp": "date"
   }

Hrozby - počet za časový interval
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Toto upozornění je odesláno, když počet detekovaných hrozeb překročí nastavenou mez v daném časovém období.

Parametry:

* **MINUTES**: časové okno v minutách (default=15)
* **TRESHOLD**: počet událostí v časovém okně pro spuštění upozornění (default=100)
* **LOG_TYPE**: (default=*): filtr podle typu události (audit/block)

Formát webhook a syslog zprávy:

.. code-block:: json

   {
      "client_name": "string",
      "client_id": "number",
      "resolver_id": "number",
      "timestamp": "date"
   }

Threats - událost detekce
~~~~~~~~~~~~~~~~~~~~~~~~~

Toto upozornění je odesláno, když je detekována událost dle zvoleného filtru.

Parametry:

* **LOG_TYPE**: (Default=*): filtr podle typu akce (audit/block)
* **THREAT_TYPE**: (Default=*): filtr podle typu detekované hrozby

Formát webhook a syslog zprávy:

.. code-block:: json

   {
      "client_name": "string",
      "domain": "string",
      "client": "string",
      "country_code2": "string",
      "client_id": "number",
      "timestamp": "date",
      "action": "string",
      "threat_type_filter": "string"
   }

Threats - nově blokovaná doména
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Toto upozornění je odesláno, pokud resolver detekuje nově blokovanou hrozbu v zadaném časovém rámci.

Parametry:

* **DAYS**: počet dní, ve kterých se budou vyhledávat nově blokované domény (default=30)
* **DOMAIN_WILDCARD**: zahrnout do upozornění pouze následující domény oddělené čárkou (Default=*)

Formát webhook a syslog zprávy:

.. code-block:: json

   {
      "client_name": "string",
      "client_id": "number",
      "resolver_id": "number",
      "timestamp": "date",
      "domain": "string",
      "client": "string"
   }

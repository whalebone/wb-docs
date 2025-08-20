==================
Syslog Integration
==================

Integrace syslogu ve Whalebone poskytuje spolehlivý export bezpečnostních a provozních dat v reálném čase přímo z každého lokálního resolveru Whalebone do průmyslově standardních SIEM nástrojů, jako jsou Splunk, Elastic nebo jakékoliv kompatibilní externí řešení pro správu logů. Tato schopnost umožňuje organizacím centralizovat sběr logů, korelovat události DNS zabezpečení s dalšími zdroji dat a vytvářet automatizované detekční a reakční workflow. Streamováním událostí ve standardním formátu syslog je zajištěna bezproblémová integrace do stávající monitorovací infrastruktury a současně je podporována compliance, auditní požadavky a pokročilá analýza hrozeb.

Integraci syslogu lze povolit v Admin Portálu v sekci Resolvers > Edit resolver > Advanced Configuration > Expert settings.

.. image:: ./img/syslog-1.png
    :align: center

Požadavky
---------

* Resolver s povolenou integrací syslogu může otevřít spojení k cílovému externímu řešení pro správu logů na portu uvedeném v nastavení resolveru. Protokol je ve výchozím nastavení UDP.

Logovací soubory
----------------

Administrátoři mají možnost určit, jaký typ dat chtějí exportovat. Popis jednotlivých logovacích souborů je uveden níže:

* **content.log**: Domény blokované obsahovým filtrem.

* **debug.log**: Dodatečná ladicí data. Tento soubor obsahuje data pouze v případě, že je ladicí režim povolen technikem Whalebone.

* **metrics.log**: Metriky týkající se operačního systému, využití disku, využití CPU, využití paměti, statistik běhu Dockeru a jednotlivých služeb Whalebone.

* **passivedns.log**: Veškerý DNS provoz.

* **whalebone.log**: Všechny detekované hrozby.

* **agent/agent-docker-connector.log**: Seznam odstraněných Docker kontejnerů. Docker kontejnery jsou odstraňovány nebo nahrazovány během aktualizací nebo změn konfigurace.

* **agent/agent-lr-agent.log**: Přehled komunikace a detailní konfigurace získané z Whalebone cloudu.

* **agent/agent-main.log**: Zprávy o kontrolách stavu souvisejících se službou lr-agent.

* **agent/agent-status.log**: Stav služby, která přijímá aktualizace konfigurace z Whalebone cloudu.

.. note:: Nejvýznamnější logovací soubory jsou content.log, passivedns.log a whalebone.log. Ostatní slouží především k řešení potíží techniky Whalebone.

Příklady
--------

Zde jsou některé příklady nejčastěji používaných logovacích souborů content.log, passivedns.log a whalebone.log:

content.log
^^^^^^^^^^^

.. code-block:: python

    {
        "timestamp": "2025/06/12 06:44:27.049917",
        "action": "block",
        "server_ip": "192.168.0.10",
        "client_ip": "192.168.10.41",
        "domain": "whalebone.com",
        "ioc": "whalebone.com",
        "identity": "wb-default-policy",
        "mobile_client_id": "",
        "device_id": "",
        "content_types": [
            "social-networks"
         ],
        "legal_types": [],
        "app_blocked_intersect": [],
        "scheduled_filter": [],
        "scheduled_internet": "false",
        "policy_name": "",
        "policy_group_id": "",
        "policy_tags": "",
        "pin": "0",
        "region": "eu-01",
        "segment_id": "",
        "brand_id": "",
        "subscription_id": "",
        "answer": "SINKHOLE_IP",
        "sinkhole_type": "1",
        "port": "56121",
        "type": "A",
        "rcode": "0",
        "matrix": {
            "content": "true",
            "advertisement": "false",
            "legal": "false",
            "whitelist": "false",
            "blacklist": "false",
            "bypass": "false",
            "apps_blocked": "false",
            "apps_allowed": "false"
        }
    }

Důležité údaje v souboru content.log:

- **timestamp**: Datum a čas, kdy došlo k události.

- **action**: Akce provedená resolverem (např. "block" nebo "allow").

- **client_ip**: IP adresa klienta, který provedl DNS dotaz.

- **server_ip**:IP adresa resolveru, který DNS dotaz zpracoval.

- **domain**: Název domény, která byla požadována.

- **type**: Typ DNS záznamu (např. "A", "AAAA", "CNAME").

passivedns.log
^^^^^^^^^^^^^^

.. code-block:: python

    {
        "response_time": "2025-07-24T06:16:50.140828Z",
        "client": "192.168.10.41",
        "server": "192.168.0.10",
        "class": "IN",
        "type": "A",
        "query_port": 39170,
        "response_port": 53,
        "query": "whalebone.com.",
        "answer": "3.33.251.168",
        "identity": "wb-default-policy",
        "ttl": 1,
        "res_action": "allow",
        "ede_code": -1,
        "protocol": "UDP",
        "region": "eu-01",
        "rtt": 0
    }

Důležité položky v souboru passivedns.log:

- **response_time**: Datum a čas, kdy byla odeslána odpověď.

- **client**: IP adresa klienta, který provedl DNS dotaz.

- **server**: IP adresa resolveru, který DNS dotaz zpracoval.

- **query**: Název domény, která byla požadována.

- **answer**:IP adresa vrácená v DNS odpovědi.

- **res_action**: Akce provedená resolverem (např. "allow" nebo "block").

- **ede_code**: Kód Extended DNS Error, který poskytuje dodatečné informace o DNS odpovědi.

- **type**: Typ DNS záznamu (např. "A", "AAAA", "CNAME").

whalebone.log
^^^^^^^^^^^^^

.. code-block:: python

    {
        "timestamp": "2025/08/18 13:07:20.460737",
        "action": "block",
        "server_ip": "192.168.0.10",
        "client_ip": "192.168.10.41",
        "domain": "spam.test.attacker.online",
        "ioc": "spam.test.attacker.online",
        "identity": "wb-default-policy",
        "mobile_client_id": "",
        "device_id": "",
        "accuracy": "100",
        "threat_types": [
            "spam"
        ],
        "app_blocked_intersect": [],
        "scheduled_internet": "false",
        "policy_name": "",
        "policy_group_id": "",
        "policy_tags": "",
        "pin": "0",
        "region": "eu-01",
        "segment_id": "",
        "brand_id": "",
        "subscription_id": "",
        "answer": "SINKHOLE_IP",
        "sinkhole_type": "8",
        "port": "63559",
        "type": "HTTPS",
        "qclass": "IN",
        "rcode": "0",
        "ede_code": -1,
        "protocol": "UDP",
        "matrix": {
            "accuracy_audit": "true",
            "accuracy_block": "true",
            "content": "false",
            "advertisement": "false",
            "legal": "false",
            "whitelist": "false",
            "blacklist": "false",
            "bypass": "false",
            "apps_blocked": "false",
            "apps_allowed": "false"
        }
    }

Důležité položky v souboru whalebone.log:

- **timestamp**: Datum a čas, kdy byla odeslána odpověď.

- **action**: Akce provedená resolverem (např. "allow", "audit" nebo "block").

    - "block": DNS dotaz byl zablokován a klientovi byla vrácena odpověď s IP adresou blokační stránky.

    - "audit": DNS dotaz byl zaznamenán pro účely auditu. Tento typ akce se používá pro monitorování a analýzu provozu bez zásahu do běžného chování klientů.

    - "allow": DNS dotaz byl povolen a na základě uživately žádosti o přístup ke stránce.

- **client_ip**: IP adresa klienta, který provedl DNS dotaz.

- **server_ip**: IP adresa resolveru, který DNS dotaz zpracoval.

- **domain**: Název domény, která byla požadována.

- **accuracy**: Přesnost vyjadřuje úroveň jistoty, že je doména skutečně nebezpečná, na základě několika faktorů, jako je shoda mezi dodavateli databází hrozeb, objem provozu přes resolvery Whalebone, podezřelé vzorce komunikace a výsledky interního výzkumu. Hodnota se pohybuje v rozmezí od 0 do 100, kde 100 znamená nejvyšší míru jistoty, že se jedná o doménu s nebezpečným obsahem.

- **threat_types**: Typ detekované hrozby (např. "spam", "phishing", "malware").

Limitatace
----------

* Integrace syslogu používá protokol UDP. Pokud chcete použít protokol TCP nebo TLS, obraťte se prosím na Whalebone HelpDesk.

===============
SNMP Monitorování
===============

High Level Síťové schéma
---------------------------

  .. figure:: ./img/highlevelnetworkdiagram.PNG


Agent SNMP Whalebone je v resolverech povolen k aktivnímu sledování místních zdrojů, požadavků a statistik.

SNMP OID
--------
SNMP OID je zkratka pro identifikátory objektů pro vytvoření šablony SNMP pro nástroj monitorování sítě. V následující tabulce jsou uvedeny identifikátory OID SNMP Whalebone.


+-------------------+-----+----------------------------------------------------------------------+
| Property          | ID  | SNMP OID                                                             |
+===================+=====+======================================================================+
| Hostname          | 1   | .1.3.6.1.4.1.8072.1.3.2.4.1.2.9.119.104.97.108.101.98.111.110.101.1  |
+-------------------+-----+----------------------------------------------------------------------+
| Check Port        | 2   | .1.3.6.1.4.1.8072.1.3.2.4.1.2.9.119.104.97.108.101.98.111.110.101.2  |
+-------------------+-----+----------------------------------------------------------------------+
| Check Resolve     | 4   | .1.3.6.1.4.1.8072.1.3.2.4.1.2.9.119.104.97.108.101.98.111.110.101.3  |
+-------------------+-----+----------------------------------------------------------------------+
| CPU Count         | 6   | .1.3.6.1.4.1.8072.1.3.2.4.1.2.9.119.104.97.108.101.98.111.110.101.4  |
+-------------------+-----+----------------------------------------------------------------------+
| Memory Available  | 7   | .1.3.6.1.4.1.8072.1.3.2.4.1.2.9.119.104.97.108.101.98.111.110.101.6  |
+-------------------+-----+----------------------------------------------------------------------+
| Memory Total      | 8   | .1.3.6.1.4.1.8072.1.3.2.4.1.2.9.119.104.97.108.101.98.111.110.101.7  |
+-------------------+-----+----------------------------------------------------------------------+
| Memory Usage      | 9   | .1.3.6.1.4.1.8072.1.3.2.4.1.2.9.119.104.97.108.101.98.111.110.101.8  |
+-------------------+-----+----------------------------------------------------------------------+
| HDD Free          | 10  | .1.3.6.1.4.1.8072.1.3.2.4.1.2.9.119.104.97.108.101.98.111.110.101.9  |
+-------------------+-----+----------------------------------------------------------------------+
| HDD Total         | 11  | .1.3.6.1.4.1.8072.1.3.2.4.1.2.9.119.104.97.108.101.98.111.110.101.10 |
+-------------------+-----+----------------------------------------------------------------------+
| HDD Usage         | 12  | .1.3.6.1.4.1.8072.1.3.2.4.1.2.9.119.104.97.108.101.98.111.110.101.11 |
+-------------------+-----+----------------------------------------------------------------------+
| Swap Free         | 13  | .1.3.6.1.4.1.8072.1.3.2.4.1.2.9.119.104.97.108.101.98.111.110.101.12 |
+-------------------+-----+----------------------------------------------------------------------+
| Swap Total        | 14  | .1.3.6.1.4.1.8072.1.3.2.4.1.2.9.119.104.97.108.101.98.111.110.101.13 |
+-------------------+-----+----------------------------------------------------------------------+
| Swap Usage        | 15  | .1.3.6.1.4.1.8072.1.3.2.4.1.2.9.119.104.97.108.101.98.111.110.101.14 |
+-------------------+-----+----------------------------------------------------------------------+
| Timestamp         | 16  | .1.3.6.1.4.1.8072.1.3.2.4.1.2.9.119.104.97.108.101.98.111.110.101.15 |
+-------------------+-----+----------------------------------------------------------------------+
| Requests Total    | 17  | .1.3.6.1.4.1.8072.1.3.2.4.1.2.9.119.104.97.108.101.98.111.110.101.16 |
+-------------------+-----+----------------------------------------------------------------------+
| equests Internal  | 18  | .1.3.6.1.4.1.8072.1.3.2.4.1.2.9.119.104.97.108.101.98.111.110.101.17 |
+-------------------+-----+----------------------------------------------------------------------+
| Requests UDP      | 19  | .1.3.6.1.4.1.8072.1.3.2.4.1.2.9.119.104.97.108.101.98.111.110.101.18 |
+-------------------+-----+----------------------------------------------------------------------+
| Requests TCP      | 20  | .1.3.6.1.4.1.8072.1.3.2.4.1.2.9.119.104.97.108.101.98.111.110.101.19 |
+-------------------+-----+----------------------------------------------------------------------+
| Requests DoT      | 21  | .1.3.6.1.4.1.8072.1.3.2.4.1.2.9.119.104.97.108.101.98.111.110.101.20 |
+-------------------+-----+----------------------------------------------------------------------+
| Requests DoH      | 22  | .1.3.6.1.4.1.8072.1.3.2.4.1.2.9.119.104.97.108.101.98.111.110.101.21 |
+-------------------+-----+----------------------------------------------------------------------+
| Requests XDP      | 23  | .1.3.6.1.4.1.8072.1.3.2.4.1.2.9.119.104.97.108.101.98.111.110.101.22 |
+-------------------+-----+----------------------------------------------------------------------+
| Answers Total     | 24  | .1.3.6.1.4.1.8072.1.3.2.4.1.2.9.119.104.97.108.101.98.111.110.101.23 |
+-------------------+-----+----------------------------------------------------------------------+
| Answers cached    | 25  | .1.3.6.1.4.1.8072.1.3.2.4.1.2.9.119.104.97.108.101.98.111.110.101.24 |
+-------------------+-----+----------------------------------------------------------------------+
| Answers No error  | 26  | .1.3.6.1.4.1.8072.1.3.2.4.1.2.9.119.104.97.108.101.98.111.110.101.25 |
+-------------------+-----+----------------------------------------------------------------------+
| Answers No data   | 27  | .1.3.6.1.4.1.8072.1.3.2.4.1.2.9.119.104.97.108.101.98.111.110.101.26 |
+-------------------+-----+----------------------------------------------------------------------+
| Answers NX-Domain | 28  | .1.3.6.1.4.1.8072.1.3.2.4.1.2.9.119.104.97.108.101.98.111.110.101.27 |
+-------------------+-----+----------------------------------------------------------------------+
| Answers SERVFAIL  | 29  | .1.3.6.1.4.1.8072.1.3.2.4.1.2.9.119.104.97.108.101.98.111.110.101.28 |
+-------------------+-----+----------------------------------------------------------------------+
| Answers 1ms       | 30  | .1.3.6.1.4.1.8072.1.3.2.4.1.2.9.119.104.97.108.101.98.111.110.101.29 |
+-------------------+-----+----------------------------------------------------------------------+
| Answers 10ms      | 31  | .1.3.6.1.4.1.8072.1.3.2.4.1.2.9.119.104.97.108.101.98.111.110.101.30 |
+-------------------+-----+----------------------------------------------------------------------+
| Answers 50ms      | 32  | .1.3.6.1.4.1.8072.1.3.2.4.1.2.9.119.104.97.108.101.98.111.110.101.31 |
+-------------------+-----+----------------------------------------------------------------------+
| Answers 100ms     | 33  | .1.3.6.1.4.1.8072.1.3.2.4.1.2.9.119.104.97.108.101.98.111.110.101.32 |
+-------------------+-----+----------------------------------------------------------------------+
| Answers 250ms     | 34  | .1.3.6.1.4.1.8072.1.3.2.4.1.2.9.119.104.97.108.101.98.111.110.101.33 |
+-------------------+-----+----------------------------------------------------------------------+
| Answers 500ms     | 35  | .1.3.6.1.4.1.8072.1.3.2.4.1.2.9.119.104.97.108.101.98.111.110.101.34 |
+-------------------+-----+----------------------------------------------------------------------+
| Answers 1000ms    | 36  | .1.3.6.1.4.1.8072.1.3.2.4.1.2.9.119.104.97.108.101.98.111.110.101.35 |
+-------------------+-----+----------------------------------------------------------------------+
| Answers 1500ms    | 37  | .1.3.6.1.4.1.8072.1.3.2.4.1.2.9.119.104.97.108.101.98.111.110.101.36 |
+-------------------+-----+----------------------------------------------------------------------+
| Answers slow      | 38  | .1.3.6.1.4.1.8072.1.3.2.4.1.2.9.119.104.97.108.101.98.111.110.101.37 |
+-------------------+-----+----------------------------------------------------------------------+
| Answers AA        | 39  | .1.3.6.1.4.1.8072.1.3.2.4.1.2.9.119.104.97.108.101.98.111.110.101.38 |
+-------------------+-----+----------------------------------------------------------------------+
| Answers TC        | 39  | .1.3.6.1.4.1.8072.1.3.2.4.1.2.9.119.104.97.108.101.98.111.110.101.39 |
+-------------------+-----+----------------------------------------------------------------------+
| Answers RA        | 40  | .1.3.6.1.4.1.8072.1.3.2.4.1.2.9.119.104.97.108.101.98.111.110.101.40 |
+-------------------+-----+----------------------------------------------------------------------+
| Answers RD        | 41  | .1.3.6.1.4.1.8072.1.3.2.4.1.2.9.119.104.97.108.101.98.111.110.101.41 |
+-------------------+-----+----------------------------------------------------------------------+
| Answers AD        | 42  | .1.3.6.1.4.1.8072.1.3.2.4.1.2.9.119.104.97.108.101.98.111.110.101.42 |
+-------------------+-----+----------------------------------------------------------------------+
| Answers CD        | 43  | .1.3.6.1.4.1.8072.1.3.2.4.1.2.9.119.104.97.108.101.98.111.110.101.43 |
+-------------------+-----+----------------------------------------------------------------------+
| Answers DO        | 44  | .1.3.6.1.4.1.8072.1.3.2.4.1.2.9.119.104.97.108.101.98.111.110.101.44 |
+-------------------+-----+----------------------------------------------------------------------+
| Answers ENDS0     | 45  | .1.3.6.1.4.1.8072.1.3.2.4.1.2.9.119.104.97.108.101.98.111.110.101.45 |
+-------------------+-----+----------------------------------------------------------------------+
| Queries EDNS      | 46  | .1.3.6.1.4.1.8072.1.3.2.4.1.2.9.119.104.97.108.101.98.111.110.101.46 |
+-------------------+-----+----------------------------------------------------------------------+
| Queries DNSSEC    | 47  | .1.3.6.1.4.1.8072.1.3.2.4.1.2.9.119.104.97.108.101.98.111.110.101.47 |
+-------------------+-----+----------------------------------------------------------------------+
| Predict Epoch     | 48  | .1.3.6.1.4.1.8072.1.3.2.4.1.2.9.119.104.97.108.101.98.111.110.101.48 |
+-------------------+-----+----------------------------------------------------------------------+
| Predict learned   | 49  | .1.3.6.1.4.1.8072.1.3.2.4.1.2.9.119.104.97.108.101.98.111.110.101.49 |
+-------------------+-----+----------------------------------------------------------------------+
| Predict Queue     | 50  | .1.3.6.1.4.1.8072.1.3.2.4.1.2.9.119.104.97.108.101.98.111.110.101.50 |
+-------------------+-----+----------------------------------------------------------------------+



Integrace Zabbix
===========================


Agent shromažďuje provozní informace lokálně a posílá data na server Zabbix ke zpracování. Kromě toho Zabbix 
nabízí funkce pro reportování a vizualizace dat na základě uložených dat z resolveru. 

Zabbix je monitorovací nástroj, který poskytuje výkonnostní metriky, jako je využití sítě, využití procesoru a paměti. Monitoruje také síť 
odpojování a nedostupnost serveru. 

Jak importovat šablonu Whalebone 
------------------------------------

- Chcete-li importovat šablonu Whalebone, přejděte na stránku **Configuration**. V části Konfigurace přejděte na položku **Šablony**.

	.. figure:: ./img/importemplate.PNG
		:width: 350pt

	

- V záložce **Šablony** zvolte **Import** a zvolte soubor šablony.

	.. figure:: ./img/importtemplate2.PNG
		:width: 350pt


Jak přidat resolver v nástroji Zabbix
-------------------------------------

- Chcete-li přidat hosta, přejděte do části Konfigurace a klikněte na položku **hosts**. Klikněte na tlačítko **create host** a zadejte název hostitele, skupiny. Poté přidejte ip adresu resolveru.

  	.. figure:: ./img/addhost.PNG 
	 	:width: 350pt


- Pod rozhraním vyberte **SNMP** → Zadejte SNMP **IP adresu** → Port **161** → SNMP verzi SNMPv2 a poté přidejte **SNMP community**.

	.. figure:: ./img/addhost1.PNG

- Po přidání hosta přejděte na kartu **Templates** → Vyberte šablonu Whalebone. Klikněte na tlačítko **Select** a **Add**.

	.. figure:: ./img/addhost3.PNG
		:width: 350pt


- Po výběru šablony Whalebone se vraťte do **Host** a klikněte na tlačítko **add**. Na kartě vidíme, že resolver byl přidán do monitoringu Zabbix.

	.. figure:: ./img/addhost4.PNG


.. note:: SNMP data from the resolver to Zabbix will take time to initialized. Wait the Zabbix to gather data from the server. Always observe the availability on the right corner to see if it's green. Green means its already connected to the whalebone resolver.


Jak přidat widget Whalebone na dashboard Zabbix
---------------------------------------------------

- Chcete-li přidat dahboard, přejděte do části **Monitoring** a poté do části **Dashboard**. V globálním zobrazení dashboardu vidíme možnost **Edit dahboard**. Klepnutím na tlačítko přidáte nové grafy.

	.. figure:: ./img/dashboard.PNG


.. note:: Před přidáním grafů na dashboard se ujistěte, že host již grafy detekoval. Grafy najdete v části **Configuration** → **Hosts** → **Graphs**.


- Klikněte na **Edit dashboard** a přidejte widget v **Add widget** → **Type** →  **Graph** a zadejte název widgetu.

	.. figure:: ./img/dashboard2.PNG
		:width: 350pt


- Vyberte **Data set**, kterým je název hosta, a vyberte **Item pattern**, kde můžeme najít šablonu Whalebone.

	.. figure:: ./img/dashboard4.PNG 


- Vyberte položky, které chcete přidat na widget pro grafickou vizualizaci. Po přidání **Items** vyberte základní barvu pro grafy, poté můžete upravit šířku, velikost bodu, průhlednost a výplň.

	.. figure:: ./img/dashboard5.PNG
		:width: 350pt


- Widget byl úspěšně přidán na dahboard. Chcete-li widget upravit nebo změnit, klikněte na ikonu ozubeného kola.

	.. figure:: ./img/dashboard6.PNG
		:width: 350pt


- Nezapomeňte kliknout na tlačítko uložit vpravo nahoře, abyste widget uložili na dashboard.

	.. figure:: ./img/dashboard7.PNG


Jak přidat spouštěče (triggers) v systému Zabbix
------------------------------------------------

Spouštěče jsou logické výrazy, které "vyhodnocují" data shromážděná položkami a představují aktuální stav systému. Nastavení spouštěče umožňuje definovat hranici toho, jaký stav je přijatelný.
Pokud tedy příchozí data překročí přijatelný stav, je spouštěč "spuštěn" - neboli změní stav na **PROBLEM**. Příklad: Pokud by Whalebone resolver narazil na 1000 NXDOMAIN odpovědí, spouštěč bude mít hodnotu
inicializován, aby upozornil, že data překročila nastavené prahové hodnoty. 

- Chcete-li konfigurovat spouštěč, přejděte do části **Configuration** → **Hosts**. Klikněte na kartu **Triggers**.

	.. figure:: ./img/trigger.PNG
		:width: 350pt


- Vytvořit spouštěč → Zadejte název a přidejte výraz. Řekněme, že chceme spouštět, pokud hodnota NXDOMAIN resolveru překročí hodnotu 60. Pro tento spouštěč vyberte závažnost - **Severity**.

	.. figure:: ./img/trigger2.PNG
		:width: 350pt


- Klikněte na tlačítko **Add** → Na kartě **Condition** → **Item** → **Select**. Zde vybereme položku **NXDOMAIN**.

	.. figure:: ./img/trigger3.PNG


- Na kartě **Condition** nastavte **Count** → **Time shift - now-h** → **Result**. Pro pole **Result** vyberte operand a poté nastavte hodnotu na **60**. Tato podmínka se spustí, pokud NXDOMAIN překročí hodnotu 60.
	.. figure:: ./img/trigger4.PNG


- Klikněte na tlačítko **Inser** a uložte spouštěče. Ujistěte se, že je spouštěč v šabloně povolen.

	.. figure:: ./img/trigger5.PNG


- Na kartě **Problems** zkontrolujte položku **NXDOMAIN**, která překračuje prahovou hodnotu.

	.. figure:: ./img/trigger6.PNG


- Na dashboardu lze identifikovat NXDOMAIN, který překračuje prahovou hodnotu.

	.. figure:: ./img/trigger8.PNG


Jak nakonfigurovat akce spouštěče
------------------------------------

Akční spouštěče jsou logické výrazy, které "vyhodnocují" data shromážděná položkami a představují aktuální stav systému. Výraz spouštěče umožňuje definovat hranici, kdy jsou data "přijatelná". Proto,
pokud příchozí data překročí přijatelný stav, je spouštěč "spuštěn" nebo změní stav na PROBLÉM. Pro tento příklad řekněme, že NXDOMAIN překročí hodnotu 60. Spouštěč pošle e-mail správci nebo vytoří oznámení.

- Prvním krokem je nastavení spouštěcí akce pomocí e-mailu. Přejděte do **Administration** a zde do **Media types**. Vytvořte nový a zadejte název. Dále zadejte název SMTP serveru a e-mail na který budou oznámení zasílána. Autentikaci volte metodou jména a hesla.

	.. figure:: ./img/triggeraction.PNG
		:width: 350pt
		

- Po nastavení e-mailu → Přejděte do **Configuration** → **Actions** → Spouštěče akcí. Na spouštěči Akce → Vytvořit akci → Zadejte název → Přidejte podmínku **New condition**.

	.. figure:: ./img/triggeraction2.PNG
		:width: 350pt
		

- V okně **New condition** vyberte Typ: **Trigger**, Operátor : **equals**: a jako spouštěč Zvolte **NXDOMAIN**.

	.. figure:: ./img/triggeraction3.PNG
		:width: 350pt
 

- Vyberte položku NXDOMAIN pro spouštěče akcí. Klikněte na tlačítko **Add**.

	.. figure:: ./img/triggeraction4.PNG
		:width: 350pt
		 

- V okně **Actions** → Klikněte na **Operations** → Zvolte výchozí na 1 min a klikněte na tlačítko **Add**

	.. figure:: ./img/triggeraction5.PNG
		:width: 350pt
		

- Zvolte dobu trvání kroku (steps) na 1 minutu. Na operaci klikněte na **add** → **Send to users** → **Admin (Jméno administrátora)** → Send only to: **E-mail**.

	.. figure:: ./img/triggeraction6.PNG
		:width: 350pt
		

Jak zobrazit předdefinovaný dashboard Whalebone
-----------------------------------------------

Pro příkalad, šablona Whalebone má ukázkový dashboard, který obsahuje přehled dat z resolveru.

- Chcete-li tento panel zobrazit, přejděte do části **Monitoring** → **hosts**. Poté v **hosts** klikněte na dasboard.

	.. figure:: ./img/templatedashboard.PNG
		:width: 250pt
	

Toto je přehled předdefinovaného Whalebone dashboardu.

	.. figure:: ./img/templatedashboard2.PNG


Nasazení
==========

Nasazení lokálního resolveru
------------------------------
Na rozdíl od jiných podobných služeb lze Whalebone nasadit jako plnohodnotný lokální resolver DNS. Tento typ nasazení doporučujeme.
Instalace je poměrně jednoduchá. Potřebujete pouze přístup k portálu Whalebone Portal a virtuální nebo fyzický server, který je z hlediska hardwaru poměrně nenáročný.
Z hlediska systémových požadavků Whalebone podporuje nejnovější verze nejpoužívanějších linuxových distribucí Debian, Ubuntu, CentOS a Red hat Enterprise Linux.
Minimální velikost hardwaru jsou 2 jádra CPU, 4 GB RAM a 40 GB pevný disk. Takový stroj zvládne až 20 000 uživatelů. 

Před nastavením serveru se ujistěte, jestli splňujete síťové požadavky a nebráníte přístupu na server zvenčí. Jakmile je server připraven, přejděte na portál Whalebone a vytvořte nový resolver.
Vymyslete vhodný název, který můžete později změnit. Jakmile iniciujete přidání nového resolveru, zobrazí se jednořádkový příkaz instalačního skriptu. Zkopírujte jej do schránky.
V tomto okamžiku přistupte k terminálu serveru vytvořeného pro tento resolver. Zbývá jen spustit instalační skript dříve zkopírovaný do schránky.
Instalace by neměla trvat déle než několik minut. Skript vás bude informovat o jejím průběhu. Pokud instalace neproběhla úspěšně, zašlete nám protokol o instalaci a my se na to podíváme.
Zanedlouho se stav resolveru změní. Jakmile se resolver stane aktivním, můžete na něj směrovat provoz a začít chránit svou síť.


.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/W_sWor-Wg-U" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
|
|
|

Cloudové resolvery
---------------------------
Whalebone nabízí také cloudové resolvery s ochranou proti malwaru a blokováním obsahu. Jejich adresy najdete v portálu Whalebone na kartě Cloudový resolver.
Můžete je používat přímo jako primární nebo sekundární resolvery nebo jako zálohu ke stávajícímu lokálnímu resolveru.

Pro konfiguraci zadejte své veřejné rozsahy IP, které chcete nasměrovat na cloudové resolvery. Poté stačí nastavit adresu cloudového resolveru Whalebone jako adresu serveru DNS ve vaší síti.
Stejně jako u místních resolverů můžete vytvořit různé zásady a přiřadit je jednotlivým IP adresám nebo rozsahům. To vám umožní nabízet službu Whalebone institucím, například školám,
které nutně nezískávají konektivitu od vás, ale vy spravujete jejich síť. Po uložení a nasměrování provozu stačí počkat, až se změny rozšíří mezi vaše klienty.

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/kdpjCenhTVg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
|
|
|

Konfigurace
=============

Základní konfigurace
-------------------
Každá síť má své specifické potřeby. Whalebone se dokáže přizpůsobit každé z nich a přizpůsobí se jí. Jednou z klíčových součástí, které je třeba při implementaci systému Whalebone nakonfigurovat, je nastavení "bezpečnostních politik".
Tato část konfigurace umožňuje upravit výchozí nastavení. Můžete například snížit práh blokování nebo blokování zcela deaktivovat, čímž vám zůstane režim auditu.
V tomto režimu Whalebone sleduje incidenty, aniž by jim bránil. Základem konfigurace auditu a blokování je takzvané "skóre", které jednotlivým doménám přiřazuje náš algoritmus. 
Čím vyšší je skóre, tím je doména nebezpečnější. Je na vás, zda si vyberete z přednastavených úrovní citlivosti, nebo se rozhodnete nastavit práh ručně. Sítím poskytovatelů internetových služeb doporučujeme "Blokovat opatrně". 
Čím nižší je prahová hodnota, tím citlivější je blokování. Mějte však na paměti, že nastavení nízkého prahu zvyšuje riziko falešných pozitivních výsledků.

Můžete si také vybrat různé typy hrozeb, které mají být blokovány. V případě potřeby si můžete snadno vytvořit vlastní blokační seznamy nebo definovat domény, které mají být vždy přístupné. Našim zákazníkům se líbí, že Whalebone dokáže splnit zákonné požadavky na blokování
jejich vlády za ně. Pokud nenajdete svou zemi na našem seznamu, dejte nám vědět a my se postaráme, aby se tam dostala.
Pokud jste si aktivovali doplněk pro filtrování obsahu, můžete jej nakonfigurovat také zde. Vytvořte si libovolný počet jedinečných zásad zabezpečení.
Poté můžete přejít do konfigurace daného resolveru a přiřadit tyto zásady různým IP adresám nebo rozsahům. Stačí, když v podrobnostech o resolveru přejdete do části "Přiřazení zásad".
a přiřadit zásady konkrétní IP adrese nebo rozsahu. Nezapomeňte nastavení uložit.

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/sUqVXKaPuIc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

|
|
|

Bezpečnostní politiky
---------------------
Jednou z klíčových součástí, které je třeba při implementaci systému Whalebone nakonfigurovat, je nastavení bezpečnostních politik. Tato část konfigurace umožňuje upravit výchozí nastavení. Můžete například snížit práh blokování nebo blokování zcela deaktivovat.
což vám ponechá režim jen auditu. V tomto režimu Whalebone sleduje incidenty, aniž by jim bránil. Jádrem konfigurace auditu a blokování je tzv. skóre.
které je jednotlivým doménám přiřazeno naším algoritmem. Čím vyšší je skóre, tím je doména nebezpečnější. Je na vás, zda si vyberete z přednastavených úrovní citlivosti, nebo se rozhodnete nastavit práh ručně.


Síti ISP doporučujeme **blokovat opatrně** Čím nižší je prahová hodnota, tím citlivější je blokování. Mějte však na paměti, že nastavení nízké prahové hodnoty zvyšuje riziko falešných pozitivních výsledků. 
Můžete také zvolit různé typy hrozeb, které mají být blokovány.

V případě potřeby si můžete snadno vytvořit vlastní seznam blokování nebo definovat domény, které mají být vždy přístupné.  Našim zákazníkům se líbí, že Whalebone za ně dokáže splnit zákonné požadavky na blokování ze strany jejich vlády.
Pokud v našem seznamu nenajdete svou zemi, dejte nám vědět a my se postaráme o nápravu.

Pokud jste si aktivovali doplněk pro filtrování obsahu, můžete jej nakonfigurovat také zde. Vytvořte si libovolný počet jedinečných zásad zabezpečení.
Poté můžete přejít do konfigurace daného řešení a přiřadit tyto zásady různým IP adresám nebo rozsahům. Stačí, když v detailu resolveru přejdete do části **Přiřazení zásad**.
a přiřadit zásady konkrétní IP adrese nebo rozsahu. Nezapomeňte nastavení uložit.

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/vjzOeHAYi4A" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
|
|
|

Konfigurace bokační stránky
---------------------------
Pomocí Whalebone portálu můžete plně přizpůsobit blokáční stránky, které se zobrazí v případě, že se někdo pokusí ve svém prohlížeči přistoupit na nebezpečnou webovou stránku. Tento nástroj potřebuje místní resolver, u kterého můžete blokovací stránku přepnout z cloudu na lokální. 
Chcete-li nakonfigurovat blokační stránky, přejděte do části **Konfigurace** a poté do části **Blokační stránky**. Můžete upravit ty stávající nebo vytvořit zcela nové. Při vytváření nové blokující stránky můžete definovat její název, doménu a jazyk stránky.
Poté vyplňte všechny potřebné údaje včetně názvu společnosti, jejího loga a kontaktních informací. Tyto informace můžete samozřejmě později změnit. Pokud tak chcete učinit, použijte kouzelnou hůlku nebo upravujte přímo v kódu HTML. Design i obsah blokační stránky můžete upravit podle svého uvážení. Stačí, když zachováte potřebné proměnné zobrazené nad blokovacím polem.

Jakmile uložíte upravenou blokační stránku, přejděte do části **Resolvery** a vyberte resolver, na kterého chcete blokační stránku použít. Přejděte na **Přiřazení politik** a přiřaďte blokační stránku na daný resolver.
Případně ji můžete přiřadit konkrétní IP adrese nebo rozsahu. Když už jste u toho, můžete také aktivovat **bypass**, který uživateli přesto umožní přístup k blokované doméně.
.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/K0p2l-qxHtk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

|
|
|

Alerty
------
Nastavte si alerty a získávejte živě aktualizace o tom, co se děje s Vašimi resolvery, jak je vaše síť zabezpečená a jak dobře funguje překlad DNS. 
Základní nastavení je jednoduché: stačí si vybrat, jaký typ informací chcete dostávat a jak často chcete být upozorňováni. Upozornění můžete dostávat prostřednictvím e-mailu, nebo služby Slack.
Upozornění Whalebone můžete také integrovat do svých systémů prostřednictvím Webhooku nebo syslogu. Velmi doporučujeme alespoň základní nastavení alertů pro monitorování překladu a funkčnost serveru na kterém resolver běží.

Určitě začněte nastavením výstrah pro selhání překladu. Poté nastavte výstrahy pro selhání hardwarových prostředků, například nedostatek místa místa na disku, RAM nebo CPU.
Můžete také sledovat selhání komunikace mezi resolverem a Whalebone cloudem, kdy rozlišení funguje v pořádku, ale resolver není synchronizován s datovými centry Whalebone.

Můžete dokonce vytvářet pokročilá upozornění na provoz DNS a bezpečnostní incidenty. S nastavením pokročilých výstrah vám rádi pomůžeme, ať už během úvodní technické konzultace,
na konci zkušební verze nebo kdykoli se rozhodnete kontaktovat podporu společnosti Whalebone.

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/GXUkPICav-o" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
|
|
|

Analýza
========

Analýza domény
----------------
Existují dva způsoby, jak ručně provést analýzu domény v databázi Whalebone. Jedním ze způsobů je pomocí nástroje **Analýza domény** z uživatelské nabídky.
Druhou možností je zkontrolovat konkrétní doménu přímo z kontextové nabídky v přehledech **Hrozby** nebo **DNS provoz**. Poté se zobrazí všechny informace 
které společnost Whalebone o dané doméně shromáždila. Jako příklad jsme použili stránku **kidos-bank.ru**. Vidíme, že s doménou jsou spojeny různé typy hrozeb.
Její skóre je 80-100 a v březnu 2021 byla označena jako nebezpečná. V následujících grafech můžete vidět vývoj detekcí, respektive DNS 
požadavků na překlad domény v síti. Výsledek analýzy také ukazuje, že doméně není přiřazena kategorie obsahu a její blokování nebylo provedeno 
nařízena ze zákona. Takto se můžete dotázat na jakoukoli doménu. Stačí ji zadat do textového pole **Doména ke kontrole**. Vidíme, že doména **facebook.com** není považována za bezpečnostní hrozbu, 
probíhá na ní poměrně velký provoz a Whalebone ji kategorizuje jako **sociální síť**. Pokud zadáme **porn.com**, vidíme, že se kategorie změnila na **Sexuální obsah**.

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/WJzsGvBiF80" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

|
|
|

Provoz DNS
------------
V protokolu "DNS traffic" si můžete prohlédnout časovou osu požadavků a odpovědí DNS za posledních 1, 7 nebo 14 dní. V dashboardu je zobrazen první překlad domény danou IP adresou za posledních 24 hodin,
typ dotazu, výsledek řešení, zdrojovou a cílovou IP adresu. Vyhledávání je možné pomocí zakliknutí konrkrétních hodnot a také pomocí fulltextu.

Souhrnné grafy pod hlavní časovou osou zobrazují přehled nejčastějších odpovědí, domén druhé úrovně a IP adres s největším provozem. Všechna data jsou přístupná také ve formátu tabulky a můžete je dokonce exportovat do souboru CSV
s maximálním počtem 1 000 000 řádků. Protokoly o provozu DNS jsou dočasně uloženy na serveru resolveru. Odtud k nim můžete přistupovat pro vlastní zpracování. Jednou z největších výhod sledování dat o provozu DNS je možnost filtrování chyb v odpovědích, jako jsou NXDOMAIN a SERVFAIL.
To umožňuje zobrazit škodlivý provoz na zařízeních připojených k síti. Toto video ukazuje zahashovanou IP adresu s téměř 240 000 překlady různých domén, které vedou k chybám NXDOMAIN a SERVFAIL. Můžete zde vidět veřejné i soukromé IP adresy.

Toto zobrazení je obzvláště užitečné, pokud do filtru přidáte další dotazy, například **MX**. Takové nastavení filtru vám ukáže IP adresy ve vaší síti, které rozesílají spam, a hrozí tedy, že se dostanou na černou listinu a následně ohrozí i ostatní zákazníky, pokud jsou za NAT.
Podobně můžete zvolit například dotazy **A**. Specializujeme se na detekci škodlivé komunikace DGA. Klienti, kteří jsou takto infikováni, se připojují ke kvazi náhodně generovaným doménám, které se snaží komunikovat s řídicím centrem malwaru.

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/Qgj-fUHS5qg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

|
|
|

Hrozby
---------
Whalebone se zaměřuje na ochranu vaší sítě. Proto máte přístup ke kompletnímu přehledu incidentů, které se staly za posledních 90 dní.
Přehled nabízí nejen informace, ale také možnost filtrace a analýzy dat. Výsledky jsou rozděleny do tří kategorií: události, které byly zablokovány, auditovány a povoleny. 
Auditované domény představují domény, které jsou poněkud podezřelé. Jejich skóre je dostatečně vysoké na to, aby byly uvedeny v protokolu, ale nižší, než je práh blokování. Pokud jde o blokované domény, resolver vrací plně přizpůsobenou stránku blokování s volitelným tlačítkem pro obejití.

Data můžete také filtrovat podle typu incidentu. Podívejme se na příklad komunikace s řídicím centrem malwaru. Vidíme konkrétní blokované domény a také místní nebo veřejné IP adresy, které se k nim pokoušely přistupovat.
Toto je příklad aktivního intenzivního provozu z konkrétní IP adresy a komunikace s malwarem Necurs. Takto infikovaný klient by ovlivnil i kvalitu připojení ostatních klientů. 
Pro každý jednotlivý záznam můžete v kontextové nabídce zvolit různé typy kontroly domény. Velmi praktické je zahájit analýzu vygooglováním domény. Nejčastěji vám však výsledky pouze sdělí, že doména je nebezpečná. 

Dalším způsobem kontroly domény je použití různých bezpečnostních zdrojů. Příkladem takové služby je velmi užitečná webová stránka **Virustotal**. Pokud ani po analýze nejste přesvědčeni, že k zablokování byl dobrý důvod,
neváhejte nám takovou doménu **nahlásit**. Případ prověříme a ozveme se vám. V případě, že se skutečně ukáže, že se jedná o falešně pozitivní blokaci, globálně povolíme přístup k doméně všem zákazníkům Whalebone zákazníkům.

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/GVZoMOEUWzM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
|
|
|

Analýza dat
---------------
Portál Whalebone umožňuje podrobnou fulltextovou filtraci a související analýzu dat. Důkladný manuál naleznete v technické dokumentaci dostupné na adrese docs.whalebone.io. v části Analýza dat.
Najdete zde seznam různých operátorů, příklady jejich použití a odkazy na možné rozdíly mezi přehledem provozu DNS a hrozeb. Můžete používat zástupné nebo logické operátory. Při použití fulltextové filtrace,
je třeba všechny parametry zadat přímo do adresy URL. Tímto způsobem můžete snadno vytvářet filtry pro budoucí použití.

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/TVhyQP_AG-Y" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

|
|
|

API
----
Pomocí rozhraní Whalebone API můžete integrovat Whalebone do svých vlastních systémů. Nejprve je třeba vytvořit nový klíč.
Přejděte do konfigurace klíčů API z kontextové nabídky kliknutím na ikonu panáčka. Po vytvoření nového klíče API se zobrazí všechny potřebné údaje. Secret API klče nebude nikdy 
znovu zobrazen, proto se ujistěte, že jste si jej skutečně a správně zkopírovali. Klíč API můžete kdykoli zneplatnit. Stačí kliknout na příslušnou ikonu. K dispozici máme podrobnou interaktivní dokumentaci 
pro rozhraní Whalebone API dostupnou na apidocs.whalebone.io/public, nebo pomocí kliknutí na ikonu otazníku. Dokumentace vás provede různými kategoriemi 
informací a nastavení s konkrétními příklady. Část "Event" obsahuje veškeré informace o hrozbách, například typy hrozeb a domény. Můžete dokonce modelovat 
API volání přímo v dokumentaci a ihned je používat. Kromě toho rozhraní API obsahuje určité informace, které zatím nejsou k dispozici na portálu Whalebone, 
například podrobnosti o ověřování DNSSEC. Samozřejmě můžete přistupovat k informacím o resolverech, jako je latence, stav resolverů nebo využití systémových prostředků. 
Než začnete modelovat volání API v dokumentaci, doporučujeme ji autorizovat pomocí klíčů API. To vám umožní přímo pracovat s vaším účtem v dokumentaci.

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/9SsxMVR6ino" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


|
|
|

.. _domain-resolution-troubleshooting:

Řešení problémů s překladem domény
----------------------------------
Když uživatelé internetu nemají přístup k doméně, často si myslí, že je to chyba poskytovatele internetu. Nejčastěji se však nejedná o problém poskytovatele, ale samotné domény.
Bez ohledu na to musíte zákazníkovi stejně odpovědět a vysvětlit mu situaci. Pojďme se podívat, jak Whalebone tento proces zjednoduší.

Nejprve prozkoumejte potenciální zablokování domény vyhledáním domény v části **Hrozby**. Doporučujeme používat vyhledávací operátory a dotazovat se na subdomény.
Ukázalo se, že doména **sufr.cz** nebyla zablokována jako hrozba. Druhým krokem je přejít do **DNS provozu** a zkontrolovat, zda k doméně vůbec někdo přistupoval. Pokud ano, podívejte se, jak se Whalebone vypořádává s překladem.
Ukazuje se, že k pokusům o přístup k doméně došlo. V takovém případě musíme zkontrolovat výsledky. Vidíme, že odpověď pro tuto doménu byla **SERVFAIL**. Pro další postup řešení problémů můžeme analyzovat doménu prostřednictvím kontextové nabídky. 

Doporučujeme použít nástroj **DNS Viz**. Nástroj DNS Viz je určen k úplné kontrole chování překladu DNS. Přímé prokliknutí vede k výsledkům ověření DNSSEC. Ukazuje se, že problém této konkrétní domény spočívá v tom, že má problémy s **prošlými kryptografickými podpisy**.
Pokud máte pocit, že stále nevíte, co se s doménou děje, neváhejte nás kontaktovat e-mailem na adrese support@whalebone.io. Rádi se na Váš problém podíváme.

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/sV2Ql8erWwY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

|
|
|


.. _domain-tracing:

Sledování domén
-----------------
Pro funkční připojení k internetu je nezbytné dobře fungující DNS překlad. Proto se můžete v portálu pro správu ujistit, že jednotlivé resolvery fungují v pořádku.
Stačí vybrat příslušný místní resolver, otevřít kontextovou nabídku a kliknout na tlačítko **Trace domény**. V tomto okamžiku zadejte doménu, kterou chcete zkoumat. Řekněme, že je to whalebone.io.

Vyberte jeden z typů dotazů, například **A**, a doménu vytrasujte. Výsledek řešení si můžete prohlédnout zde. V horní části je zobrazen výsledek dotazu. Zelená barva vám říká, že s překladem DNS není nic v nepořádku. 
Pokud se vyskytne nějaký problém, budou informace o konkrétním problému uvedeny oranžovou nebo červenou barvou. Například pokud doména neexistuje, bude výsledkem **NXDOMAIN** V případě, že je s rozlišením problém, zobrazí se odpověď **SERVFAIL**.
Pokud narazíte na nějaké problémy, pošlete protokol na adresu **support@whalebone.io** a my Vám pomůžeme s investigací.

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/WD6RawjWGqo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>




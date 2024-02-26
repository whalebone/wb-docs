
************************
Instalace krok za krokem
************************


Chcete-li nainstalovat HOS do zařízení, musíte jej nejprve nakonfigurovat. Přejděte do **Whalebone Portalu**, přejděte do  (1) **Uživatelského menu** a zde na (2) **Home Office Security**.


.. image:: ./img/hos-sbs-1.png
    :align: center


Skupina **Default** by již měla existovat. Pokud ne, vytvořte ji kliknutím na tlačítko (3) a **+ Vytvořit skupinu**.

.. image:: ./img/hos-sbs-2.png
    :align: center


* **Název**: Tento údaj by měl jasně identifikovat skupinu zařízení, aby se odlišila od ostatních. Pokud používáte pouze jednu, můžete jeho název ponechat jako Default Group (Výchozí skupina). 
* **Bezpečnostní politika**: Odpovídá zásadám, které vytvoříte v nabídce Konfigurace. Jedná se o soubor pravidel. Na základě zásad se zařízení nebo místní/cloudový resolver rozhoduje, co má při překladu DNS dělat. Tato sada pravidel zůstává v zařízení a je zpočátku aktualizována a později synchronizována. Z tohoto důvodu portál zajišťuje monitorování těchto zařízení.
* **Blokační stránka**: odpovídá stránkám blokování, které vytvoříte v nabídce Konfigurace. 
* **Výjimky na domény**: Služba HOS nebude přesměrovávat žádné dotazy DNS, které obsahují dotaz na doménu na seznamu výjimek. Např. při zadání ``example.com`` bude dotaz DNS vyřešen jako obvykle na resolveru nakonfigurovaném operačním systémem. Stejné pravidlo platí pro dotaz ``subdomena.example.com``.
* **Automatická aktualizace**: Pokud je tato konfigurační možnost zaškrtnuta, aplikace HOS v systému Windows se aktualizuje na nejnovější produkční verzi, jakmile je k dispozici ke stažení novější verze. Tato volba se projeví pouze v systému Windows, v mobilních zařízeních provádí aktualizace ekosystém výrobce.
* **Vypnout HOS uvnitř podnikové sítě**: Po zaškrtnutí této možnosti se zobrazí další 3 textová pole. Konfigurace umožňuje, aby došlo k vypnutí HOS v podnikové sítě na základě procesu dotaz-odpověď. 
    * **Interní doména**: Specifikuje na jakou interní doménu se bude HOS periodicky dotazovat.
    * **Interní odpověď**: HOS po odelsání dotazu na interní doménu očekává odpověď specifikovanou v tomto poli.
    * **Typ dotazu**: Dle zvoleného typu dotazu (A, AAAA a MX) musí být korektně nakonfigurován záznam na interním domain controlleru.  


.. warning:: Dvě výše uvedená nastavení (Automatická aktualizace a Výjimka pro doménu) jsou k dispozici pouze ve verzi 2.10.0 pro Windows a vyšší. Pokud používáte starší verzi, je nutné provést update manuálně.

Po dokončení klikněte na tlačítko **Přidat** a vytvořte tuto skupinu.



.. image:: ./img/hos-sbs-3.png
    :align: center


Kliknutím na tlačítko (5) **Install to group** zobrazíte pokyny k instalaci a/nebo získáte odkaz ke stažení instalačního programu HOS.

.. image:: ./img/hos-sbs-4.png
    :align: center


Pokud jste si ještě nestáhli instalační program (6). Během stahování instalačního programu zkopírujte instalační příkaz do schránky (7). 

Instalace nebo aktualizace:

.. code-block:: shell

    msiexec /i "Whalebone.Home.Office.Security.Installer.msi" TOKEN="60d5806e-07fe-432a-a4ad-7797d82782b3"

Odinstalace:

.. code-block:: shell

    msiexec /x "Whalebone.Home.Office.Security.Installer.msi

.. image:: ./img/hos-sbs-5.png
    :align: center


Najděte složku, ve které je instalátor umístěn. Měl by to být soubor s názvem **Whalebone.Home.Office.Security.Installer.msi**.

Otevřete příkazový řádek, změňte adresář na složku, kde je instalátor, a vložte (8) příkaz myší (klikněte pravým tlačítkem myši). Spusťte příkaz. To vyžaduje oprávnění správce.


Instalační program má minimální uživatelské rozhraní. Pokud se neobjevila žádná chybová zpráva, považujte instalaci za úspěšnou.

.. image:: ./img/hos-sbs-6.png
    :align: center

.. Tip:: The installer has very minimal UI. If there was no error message, consider the installation successful.

.. image:: ./img/hos-sbs-7.png
    :align: center

Zařízení je nyní viditelné na webové stránce Whalebone Portal.


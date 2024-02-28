Integrace API
-------------
Whalebone API je jednoduchý a praktický způsob, jak přistupovat ke všem datům, která jsou shromažďována Whalebone resolvery a integrovat je do externích systémů. Dokumentace API má dvě oddělené schémata. Jedno pro získávání událostí od Whalebone a druhé pro získávání a konfiguraci nastavení.


* Pokud chcete získávat incidenty, data DNS provozu a metriky resolveru, použijte `toto schéma. <https://apidocs.whalebone.io/public/>`__

* Pokud chcete konfigurovat resolver, aktualizovat politiky, přidávat domény na seznamy povolených/zakázaných nebo získat nastavení, použijte `toto schéma. <https://portal.whalebone.io/api/public/v1/doc>`__


Pro autentizaci k API potřebuje každý uživatel sadu klíčů **Access Key** a **Secret Key**. Tyto lze spravovat v nabídce **API keys** v rozbalovacím menu pod účtem uživatele.

Video návod krok za krokem můžete shlédnout `zde. <https://docs.whalebone.io/cs/latest/video_guides.html#api>`__

   
* **Generování API klíče**

Generování API klíče lze provést kliknutím na tlačítko **Generate new key**.

.. comment :: .. image:: ./img/key-generation.gif
.. comment ::    :align: center

.. note:: Nezapomeňte si zkopírovat `Key secret`, protože jej nelze získat opětovně.


* **Deaktivace API klíče**

V případě, že se API klíč ztratí nebo bude kompromitován, jeho zrušení lze provést ve stejném menu kliknutím na ikonu červeného koše.
Každý klíč je úzce spojen s ID uživatele a neexistuje centrální správa klíčů. Aby bylo možné zneplatnit klíč, ke kterému nemáte přístup, musí příslušný uživatel klíč sám smazat, nebo musí být smazán celý uživatelský účet.

.. comment :: image:: ./img/key-revocation.gif
.. comment ::   :align: center
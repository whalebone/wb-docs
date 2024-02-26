Konfigurace rozlišení DNS
=========================

Možnosti konfigurace resolveru najdete v zíložce **Konfigurace**  na kartě **DNS Překlad**. Tato záložka umožňuje provést základní konfiguraci bez znalosti konfigurační syntaxe. 
Dále je zde textová oblast umožňující definovat libovolnou konfiguraci k základnímu `Knot Resolveru <https://www.knot-resolver.cz/>`_.

Dostupné možnosti konfigurace:

* **Používat IPv6 pro dotazy na autoritativní servery**
  * Pokud je systém správně nakonfigurován, je možné povolit IPv6.
  * V opačném případě by aktivace protokolu IPv6 mohla mít negativní vliv na výkon a latenci resolveru.

* **Přesměrovat dotazy na nadřazené resolvery**

  * Tato možnost umožňuje přesměrovat všechny nebo vybrané dotazy na předřazené resolvery nebo autoritativní servery DNS (vhodné např. pro přesměrování na řadiče domény služby Active Directory).
    * **Zakázat DNSSEC validac**
    * Pokud je tato možnost zaškrtnuta, odpovědi z přesměrovaných dotazů nebudou ověřovány pomocí DNSSEC.  
    * Tuto možnost doporučujeme zaškrtnout v případě, že předávací server nemá správně nakonfigurován DNSSEC.

  * **Všechny dotazy na**

    * Možnost předání všech dotazů jednomu nebo více resolverům.
    * Toto nastavení ukládá všechny odpovědi do mezipaměti!

  * **Následující domény**
    * Možnost vybrat konkrétní domény, které mají být předávány na jeden ,nebo více resolverů.
    * Pro různé domény lze definovat různé resolvery.
    * Ukládání do mezipaměti pro vybrané domény bude vypnuto!

* **Statické záznamy**

  * Předdefinované odpovědi, které mají být vráceny pro konkrétní domény.
  * Mohly by sloužit pro speciální účely, jako je monitorování nebo velmi jednoduché nahrazování záznamů na autoritativním serveru.


* **Nastavení DNS překladu**
  * Textová oblast pro pokročilou konfiguraci.
  * Slouží k přímé konfiguraci Knot Resolveru.
  * `Kompletní konfigurace Knot Resolveru <https://knot-resolver.readthedocs.io/en/stable/config-overview.html>`_
  * Podporuje skriptování v jazyce Lua.


 
.. image:: ./img/lrv2-resolution.gif
   :align: center

.. note:: Po stisknutí tlačítka **Uložit** jsou změny v rozlišení DNS uloženy a připraveny k nasazení na cílové resolvery. Samotné nasazení je třeba provést ze stránky **Resolvery**. Je možné provést více změn a použít je všechny najednou, aby se minimalizoval počet nasazení na resolver.

.. warning:: Chybná konfigurace může ovlivnit stabilitu, výkon nebo bezpečnostní funkce resolveru. V případě chybné syntaxe se po spuštění **Nahrát konfiguraci** zobrazí chybový kód.
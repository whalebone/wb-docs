Hrozby
======

Hrozby jsou speciální události, při kterých se DNS požadavek na doménu nachází v reputační databázi. Při detekci hrozby existují dva typy akcí. První je **audit**, kdy se doména pouze zaznamená, ale přístup je stále možný. Druhou akcí je **block**, který zabrání požadavku na škodlivý web a přesměruje uživatele na blokační stránku.

Podrobný videonávod najdete :ref:`zde<Threats video>`.

Hrozby jsou kategorizované podle následujících typů:

* Blacklist
* C&C
* Coinminer
* Compromised
* Malware
* Phishing
* Spam

Jak hledat události blokované pomocí blokovaného seznamu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tip:: Kategorie Blokovaný seznam je vlastní seznam spravovaný administrátory zákazníka pro blokování domén na vyžádání. Blacklist je součástí dat Whalebone threat intelligence pro známé domény hostující více hrozeb nebo pro případy, kdy nelze přesnou kategorii určit.

Kategorii Blokovaný seznam můžete vybrat v koláčových grafech nebo v seznamu logů ve sloupci **Kategorie**. Další možností je kliknout na tlačítko **Filtrovat** a nastavit filtr **Blokovaný seznam** na hodnotu **Ano**.

Jak analyzovat doménu
~~~~~~~~~~~~~~~~~~~~~

Pokud se chcete dozvědět více o analýze domén, hodnocení škodlivých domén, kategoriích domén nebo o tom, co o nich vědí externí zdroje, podívejte se na podrobný videonávod :ref:`zde<Domain analysis video>`.

Jak nahlásit „False Positive“
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

V některých případech může být hodnocení domény nesprávné. Pokud se domníváte, že doména nemá být blokována, ale je, můžete ji nahlásit jako chybně klasifikovanou pomocí tlačítka **Nahlásit falešnou detekci**, čímž vytvoříte požadavek na revizi domény.

.. figure:: ./img/data-analysis-4.png
   :alt: Nahlásit falešnou detekci
   :align: center

   Nahlášení falešné detekce

Možnosti filtrování
~~~~~~~~~~~~~~~~~~~

* **IP klienta**: Zdrojová IP adresa, která vytvořila DNS požadavek nebo incident.
* **ID zařízení zákazníka**: Jedinečný identifikátor zařízení, které vytvořilo DNS požadavek nebo bylo zapojeno do incidentu.
* **Doména**: Doména v DNS dotazu.
* **Akce**: Akce, kterou resolver provedl nad daným dotazem, např. ``block``, ``allow`` a ``audit``.
* **Kategorie hrozeb**: Kategorie hrozby, např. ``malware``, ``phishing`` nebo ``c&c`` (command and control).
* **Název hrozby**: Konkrétní název hrozby, který může poskytnout detailnější informace o jejím charakteru.
* **Blokovaný seznam**: Zapnutí nebo vypnutí filtru pro domény, které jsou přítomné v blokovaném seznamu.
* **Kód země**: Kód země spojený s IP adresou klienta, který může pomoci určit geografickou lokaci zdroje DNS požadavku nebo incidentu.
* **ID resolveru**: Jedinečný identifikátor resolveru, který zpracoval DNS požadavek nebo byl zapojen do incidentu; pomáhá identifikovat vzory nebo konkrétní resolvery spojené s určitými typy hrozeb.

.. only:: Immunity or DNS4GOV

  .. tip:: ID zařízení zákazníka bylo přiřazeno klientem Home Office Security nainstalovaným na zařízení. Seznam zařízení najdete v sekci **Home Office Security** v portálu, která je dostupná v uživatelském menu.

.. only:: Aura or Peacemaker

  .. tip:: ID zařízení zákazníka přiřazuje zákazník pomocí Retail API. Seznam zařízení najdete v sekci **Retail** v portálu.

Export CSV
~~~~~~~~~~

CSV export obsahuje následující údaje:

* datum
* akce
* IP adresa klienta
* název zařízení
* země
* doména
* skóre
* kategorie hrozby
* název hrozby
* název resolveru

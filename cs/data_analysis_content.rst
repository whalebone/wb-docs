Obsah
=====

Záložka **Obsah** zobrazuje přehled blokovaných domén podle nastavení filtrování obsahu. Pokud nemáte filtr obsahu zapnutý nebo jej nepoužíváte, v této záložce se nebudou zaznamenávat žádná data. K dispozici je 18 kategorií, například ``Sexuální obsah``, ``Gambling``, ``Audio/video`` nebo ``Hry``.

Možnosti filtrování
~~~~~~~~~~~~~~~~~~~

Tlačítko Filtrovat obsahuje různé možnosti podle typu analyzovaných dat. Pro jednotlivé typy dat jsou dostupné tyto možnosti:

* **IP klienta**: Filtruje data podle konkrétních IP adres klientů.
* **ID zařízení zákazníka**: Filtruje data podle konkrétních ID zařízení.
* **Doména**: Filtruje data podle konkrétních názvů domén.
* **Kategorie obsahu**: Filtruje data podle konkrétních kategorií obsahu (např. Sexuální obsah, Gambling, Audio/video, Hry).
* **Legal**: Filtruje domény blokované z důvodu regulatorních omezení.
* **ID resolveru**: Filtruje data přijatá konkrétními resolvery.

.. only:: Immunity or DNS4GOV

  .. tip:: ID zařízení bylo přiřazeno klientem Home Office Security nainstalovaným na zařízení. Seznam zařízení najdete v sekci **Home Office Security** v portálu, která je dostupná v uživatelském menu.

.. only:: Aura or Peacemaker

  .. tip:: ID zařízení přiřazuje zákazník pomocí Retail API. Seznam zařízení najdete v sekci **Retail** v portálu.

Změna kategorizace domény
~~~~~~~~~~~~~~~~~~~~~~~~~

Pokud je doména kategorizována nesprávně, můžete zkontrolovat, do kterých kategorií spadá pomocí nástroje **Analýza domény** v uživatelském menu. Po zadání domény se zobrazí sekce **Kategorizace obsahu**, která ukáže kategorie, do nichž doména spadá, a nabídne také tlačítko **Navrhnout změnu kategorie** pro návrh změny kategorizace. Doménu je také možné nahlásit jako nebezpečnou pomocí tlačítka **Nahlásit jako škodlivou**.

Export CSV
~~~~~~~~~~

Data v CSV souboru obsahují následující údaje:

* datum
* IP adresa klienta
* název zařízení
* doména
* typ kategorie obsahu

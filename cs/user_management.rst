.. _header-n18:

Správa uživatelů
================

Správa uživatelů se nachází v **Uživatelském menu** > **Uživatelé**.

V této nabídce může správce spravovat uživatelské účty. Může přidávat, odebírat nebo zakazovat jejich používání. Kromě toho jsou mu k dispozici informace o posledním přihlášení a poslední změně hesla pro každý účet.

.. tip:: Když je uživatel pozván do organizace portálu a ještě nemá účet Whalebone, je pro něj vytvořen nový účet a na jeho registrovanou e-mailovou adresu je zaslán aktivační odkaz.

Podporovány jsou dva typy uživatelů:

**Uživatelé**: Uživatelé, kteří mají svůj primární účet zaregistrovaný pod identifikátorem konkrétní organizace.

**Externí uživatelé:** Uživatelé patřící pod jinou organizaci, ale mohou mít přiřazenou roli pod jinou organizací Whalebone, např. prodejci.

.. tip:: Každému uživateli lze přiřadit jednu nebo více rolí, které lze kombinovat a vytvořit tak jeho konečnou roli.

Níže jsou popsány jednotlivé role a činnosti, které mohou vykonávat.

Definice rolí
=============

Existují čtyři hlavní typy rolí:

- **Vlastník**: Vlastník má plný přístup ke všem nastavením a datům v rámci organizace. Tato role je obvykle přiřazena osobě, která vytvořila účet organizace. Navíc má tato role výhradní schopnost spravovat strukturu podřízených organizací.
- **Administrárot**: Role správce má rozsáhlá oprávnění k řízení organizace, včetně správy uživatelů, konfiguračních nastavení a přístupu ke všem datům. U této role je možné povolit nebo zakázat přístup k podřízeným organizacím. Pokud je povolen přístup k podřízeným organizacím, může v nich správce spravovat uživatele a nastavení, avšak nemůže spravovat strukturu více podřízených organizací.
- **Pouze čtení**: Role pouze čtení má přístup pouze pro čtení k datům a nastavením organizace. Tato role je vhodná pro uživatele, kteří potřebují sledovat nebo kontrolovat informace, aniž by mohli cokoli měnit. Tato role má možnost povolit nebo zakázat přístup k podřízeným organizacím.
- **Administrátor s dalšími oprávněními**: Role speciální je určena pro uživatele, kteří potřebují podrobnější oprávnění přizpůsobená konkrétním úkolům. Tato role umožňuje přiřazení přesných akcí a úrovní přístupu na základě odpovědností uživatele v rámci organizace.

Oprávnění role Administrátor s dalšími oprávněními
==================================================

Oprávnění této role jsou rozdělena do dvou hlavních kategorií: **Práva na správu** a **Práva na zobrazení**. Práva na správu umožňují uživatelům provádět konkrétní akce, zatímco práva na zobrazení poskytují přístup pouze pro čtení k určitým datům nebo nastavením.

Práva na správu
---------------

V této sekci jsou uvedena oprávnění, která mohou být přiřazena uživatelům, a seznam činností, které mohou vykonávat.

API tokeny
~~~~~~~~~~

- Vytvářet a odvolávat API tokeny pro programový přístup k portálu Whalebone

DNS admin
~~~~~~~~~

- Přiřadit rozsahy IP adres k politikám na cloudových resolverech
- Zobrazit, vytvořit, upravit a smazat lokální resolvery
- Zobrazit, vytvořit, upravit a smazat nastavení DNS překladu pro lokální resolvery
- Přiřadit nastavení DNS překladu k lokálním resolverům
- Upravovat expertní nastavení na lokálních resolverech
- Aktualizovat a vrátit se zpět k předchozí verzi software na lokálních resolverech
- Zobrazit stav a logy lokálních resolverů
- Nastavit vyhledávání názvů zařízení z Active Directory pro lokální resolvery

.. only:: Aura or Peacemaker

    Produkt manager
    ~~~~~~~~~~~~~~~

    .. only:: Peacemaker

        .. warning:: Toto oprávnění je dostupné pouze v Peacemaker Profit.

    -  Zobrazit Produktový dashboard s přehledem předplatných, objemů provozu, statistik blokování, trendů adopce a předpovědí růstu

.. only:: Aura or Peacemaker

    Retail admin
    ~~~~~~~~~~~~

    .. only:: Peacemaker

        .. warning:: Toto oprávnění je dostupné pouze v Peacemaker Profit.

    -  Zobrazit Retail dashboard s přehledem retailových předplatných, zařízení a uživatelů
    -  Spravovat předplatné, zařízení a uživatele v rámci retailové organizace

.. only:: Aura or Peacemaker

    Retail operátor
    ~~~~~~~~~~~~~~~

    .. only:: Peacemaker

        .. warning:: Toto oprávnění je dostupné pouze v Peacemaker Profit.

    - Zobrazit Retail dashboard s přehledem retailových předplatných, zařízení a uživatelů
    - Spravovat předplatné, zařízení a uživatele v rámci retailové organizace
    - Zobrazit zablované hrzby v DNS provozu

Správce alertů
~~~~~~~~~~~~~~

- Zobrazit, vytvořit, upravit a smazat upozornění
- Spravovat nastavení upozornění
- Zobrazit, vytvořit a smazat místa, kam se upozornění odesílají

Správce bezpečnostních politik
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Zobrazit, vytvořit, upravit a smazat bezpečnostní politiky
- Spravovat nastavení blokačních stránek, párování politik a přiřazení politik k lokálním resolverům
- Zobrazit přiřazení politik ke cloudovým resolverům
- Zobrazit, vytvořit, upravit a smazat seznamy povolených a blokovaných domén
- Zobrazit logy lokálních resolverů

Správce blokačních stránek
~~~~~~~~~~~~~~~~~~~~~~~~~~

- Zobrazit, vytvořit, upravit a smazat blokační stránky

Správce cloudových resolverů
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Přiřadit rozsahy IP adres k politikám na cloudových resolverech

.. only:: Immunity or DNS4GOV

    Správce Home Office Security
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    - Zobrazit, vytvořit, upravit a smazat skupiny zařízení Home Office Security, včetně přiřazení politik a dalších nastavení ke skupinám
    - Smazat zařízení Home Office Security
    - Změnit skupiny zařízení Home Office Security registrovaných klientů

.. only:: Immunity or DNS4GOV

    Správce Identity protection
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    - Zobrazit incidenty identity protection a změnit jejich stav

Správce reportů
~~~~~~~~~~~~~~~

- Nastavit naplánované reporty
- Zobrazit uložené reporty

Správce uživatelů
~~~~~~~~~~~~~~~~~

.. warning:: Toto oprávnění by mělo být přiřazeno pouze vysoce důvěryhodným uživatelům, protože umožňuje správu uživatelských účtů v organizaci. V případě zneužití může vést k neoprávněnému přístupu nebo změnám v nastavení organizace.

- Zobrazit, deaktivovat a smazat uživatelské účty v rámci organizace
- Pozvat nové uživatele do organizace
- Měnit role a oprávnění uživatelů

Úprava seznamů
~~~~~~~~~~~~~~

- Zobrazit, vytvořit, upravit a smazat vlastní seznamy povolených a blokovaných domén používané pro filtrování a blokování

Práva na zobrazení
------------------

Číst veškerý provoz (obsah, DNS, hrozby)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: Peacemaker

    .. warning:: Toto oprávnění je dostupné pouze v Peacemaker Content Filtering a Peacemaker Profit.

- Zobrazit veškerá data o DNS provozu, obsahu a hrozbách v organizaci

.. only:: Peacemaker or Immunity or DNS4GOV

    Cloudové resolvery pouze pro čtení
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    - Zobrazit přiřazení politik a rozsahů IP adres ke cloudovým resolverům

Čtenář audit logů
~~~~~~~~~~~~~~~~~

- Zobrazit audit logy organizace pro sledování změn a akcí v rámci organizace

Data hrozeb
~~~~~~~~~~~

- Zobrazit data o detekovaných hrozbách

DNS provoz
~~~~~~~~~~

- Zobrazit data o DNS provozu

Pouze čtení - vše
~~~~~~~~~~~~~~~~~

- Toto oprávnění je ekvivalentní roli Pouze čtení. Viz výše uvedený popis role **Pouze čtení**.

Prohlížeč seznamu
~~~~~~~~~~~~~~~~~

- Zobrazit vlastní seznamy povolených a blokovaných domén a jejich obsah používaný pro filtrování a blokování

Provozní obsah
~~~~~~~~~~~~~~

.. only:: Peacemaker

    .. warning:: Filtrování obsahu je dostupné pouze v Peacemaker Content Filtering a Peacemaker Profit.

- Zobrazit zablokované DNS dotazy na domény s blokovaným obsahem

Resolver operátor
~~~~~~~~~~~~~~~~~

- Zobrazit bezpečnostní politiky a jejich konfigurace
- Zobrazit nastavení DNS překladu pro lokální resolvery
- Zobrazit seznamy povolených a blokovaných domén používané pro filtrování a blokování
- Zobrazit nastavení blokačních stránek
- Zobrazit seznam lokálních resolverů a jejich stavy bez přístupu k jejich konfiguracím a logům

.. only:: Aura or Peacemaker

    Retail operátor bez zařízení
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. only:: Peacemaker

        .. warning:: Toto oprávnění je dostupné pouze v Peacemaker Profit.

    - Zobrazit Retail dashboard s přehledem retailových předplatných, zařízení a uživatelů
    - Zobrazit zablokované hrozby v DNS provozu

Zobrazení uživatelů
~~~~~~~~~~~~~~~~~~~

- Zobrazit uživatelské účty v rámci organizace

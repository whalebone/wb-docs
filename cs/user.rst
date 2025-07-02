.. _header-n18:

Správa uživatelů/organizací
============================

Správa uživatelů
----------------

Uživatele lze spravovat na příslušné kartě v nabídce **Uživatelé** nacházejícím se pod ikonou panáčka.

V této nabídce může správce spravovat uživatelské účty. Může přidávat, odebírat nebo zakazovat jejich používání. Kromě toho jsou mu k dispozici informace o posledním přihlášení a poslední změně hesla pro každý účet.

.. tip:: Když je uživatel pozván do organizace portálu a ještě nemá účet Whalebone, je pro něj vytvořen nový účet a na jeho registrovanou e-mailovou adresu je zaslán aktivační odkaz.

Podporovány jsou dva typy uživatelů:

**Uživatelé**: 
   * uživatelé, kteří mají svůj primární účet zaregistrovaný pod identifikátorem konkrétní organizace.

**Externí uživatelé:** **(pokud jsou k dispozici)** 
   * uživatelé, kteří patří pod jinou organizaci.
   * mohou mít přiřazenou roli pod jinou organizací Whalebone.
   * např. prodejci

.. tip:: Každému uživateli lze přiřadit jednu nebo více rolí, které lze kombinovat a vytvořit tak jeho konečnou roli. Oprávnění jsou aditivní (stohovatelná).¨


Níže jsou popsány jednotlivé role a činnosti, které mohou vykonávat.


.. csv-table:: 
   :align: left
   :header: "Akce", "Data o provozu", "Data hrozeb", "Úprava seznamů", "Správce bezpečnostních politik", "API tokeny", "Pouze čtení", "Resolver operátor", "DNS Admin", "Správce HomeOffice Security", "Správce uživatelů", "Administrátor"

   "**View Threat Data**", "☑", "☑", " ", " ", " ", "☑", " ", " ", " ", " ", "☑"
   "**View DNS Traffic**", "☑", " ", " ", " ", " ", "☑", " ", " ", " ", " ", "☑"
   "**View Whitelists/Blacklists**", " ", " ", "☑", "☑", " ", "☑", " ", " ", " ", " ", "☑"
   "**Edit Whitelists/Blacklists**", " ", " ", "☑", "☑", " ", " ", " ", " ", " ", " ", "☑"
   "**View Security Policies**", " ", " ", " ", "☑",  " ", "☑", " ", " ", " ", " ", "☑"
   "**Edit Security Policies**", " ", " ", " ", "☑", " ", " ", " ", " ", " ", " ", "☑"
   "**View Resolver Configuration**", " ", " ", " ", "☑", " ", "☑", "☑", "☑", " ", " ", "☑"
   "**Edit Resolver Configuration**", " ", " ", " ", "☑", " ", " ", " ", "☑", " ", " ", "☑"
   "**View API Tokens**", " ", " ", " ", " ", "☑", "☑", " ", " ", " ", " ", "☑"
   "**Generate API Tokens**", " ", " ", " ", " ", "☑", " ", " ", " ", " ", " ", "☑"
   "**View Network Configuration**", " ", " ", " ", "☑", " ", "☑", "☑", "☑", " ", " ", "☑"
   "**Edit Network Configuration**", " ", " ", " ", "☑", " ", " ", " ", "☑", " ", " ", "☑"
   "**View Alerts**", " ", " ", " ", " ", " ", "☑", " ", " ", " ", " ", "☑"
   "**Edit Alerts**", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "☑"
   "**View Reports**", " ", " ", " ", " ", " ", "☑", " ", " ", " ", " ", "☑"
   "**Edit Reports**", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "☑"
   "**HOS device management and policy settings**", " ", " ", " ", " ", " ", " ", " ", " ", "☑", " ", "☑"
   "**Manage user accounts**", " ", " ", " ", " ", " ", " ", " ", " ", " ", "☑", "☑"

.. _header-n748:

Nastavení organizace
---------------------

Nastavení organizace najdete v nabídce **Nastavení organizace**.


Politika přístupu
~~~~~~~~~~~~~~~~~~~~

Zásady přístupu k portálu definují bezpečnostní mechanismus pro uživatele přistupující k portálu.
Whalebone Portal. Lze nakonfigurovat následující nastavení:

**Povolené rozsahy IP**: 
Rozsahy IPv4 nebo IPv6 v notaci CIDR, např. 10.0.0.0/24, které mají povolen přístup k portálu Whalebone.

**Zamykání účtu**: 
Pokud je povoleno, může omezit počet neúspěšných pokusů o přihlášení.

   K dispozici jsou tyto možnosti:

   - **Limit nesprávných pokusů**: 
   
     - Počet neúspěšných pokusů o přihlášení před zablokováním účtu. Výchozí hodnota je 5.

   - **Doba trvání uzamčení (minuty)**: 
   
     - Doba v minutách, po kterou je zákázán další pokus o přihlášení.

   - **Reset počítadla (minuty)**:
   
     - Doba trvání v minutách před resetováním počítadla neúspěšných pokusů.

   - **Limit CAPTCHA**:
   
     - Počet neúspěšných pokusů o přihlášení před zapnutím ověření CAPTCHA.

**Vyžadovat vícefaktorovou autentizaci**:
Vyžadujte, aby uživatelé používali aplikaci dvoufaktorového ověřování (2FA) a při přihlášení k portálu zadávali další tokeny.


Politika hesel
~~~~~~~~~~~~~~~

Lze nakonfigurovat následující nastavení hesla:

**Expirace hesla (ve dnech)**:
Doba platnosti hesla: Počet dní, než je třeba heslo změnit.

**Historie hesla**:
Počet starých hesel, která nelze znovu použít při nastavování nových hesel.

**Atributy hesla**:
Heslo, které se má změnit: Atributy, které by mělo nové heslo mít.

Atributy, které může mít nové heslo, jsou následující:

   - Minimální délka

   - Počet číslic

   - Počet malých písmen

   - Počet velkých písmen

   - Počet speciálních znaků
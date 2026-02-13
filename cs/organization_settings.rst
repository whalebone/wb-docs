Nastavení organizace
--------------------

Nastavení organizace najdete v nabídce **Uživatelské menu** > **Nastavení organizace**.

Politika přístupu
~~~~~~~~~~~~~~~~~

Zásady přístupu k portálu definují bezpečnostní mechanismus pro uživatele přistupující k portálu Whalebone Portal, kde lze nakonfigurovat následující nastavení:

**Povolené rozsahy IP**: Rozsahy IPv4 nebo IPv6 v notaci CIDR, např. 10.0.0.0/24, které mají povolen přístup k portálu Whalebone.

**Zamykání účtu**: Pokud je povoleno, může omezit počet neúspěšných pokusů o přihlášení.

**Vyžadovat vícefaktorovou autentizaci**: Vyžadujte, aby uživatelé používali aplikaci dvoufaktorového ověřování (2FA) a při přihlášení k portálu zadávali další tokeny.

Možnosti zámku účtu jsou:

K dispozici jsou tyto možnosti:

- **Limit nesprávných pokusů**: Počet neúspěšných pokusů o přihlášení před zablokováním účtu. Výchozí hodnota je 5.
- **Doba trvání uzamčení**: Doba v minutách, po kterou je zákázán další pokus o přihlášení.
- **Reset počítadla**: Doba trvání v minutách před resetováním počítadla neúspěšných pokusů.
- **Limit CAPTCHA**: Počet neúspěšných pokusů o přihlášení před zapnutím ověření CAPTCHA.

Politika hesel
~~~~~~~~~~~~~~

Pro hesla lze nastavit následující požadavky:

- **Expirace hesla (ve dnech)**: Počet dní, než je třeba heslo změnit.
- **Historie hesla**: Počet starých hesel, která nelze znovu použít při nastavování nových hesel.
- **Minimální délka**: Minimální délka hesla
- **Počet číslic**: Počet číslic v hesle
- **Počet speciálních znaků**: Počet speciálních znaků v hesle
- **Počet malých písmen**: Počet malých písmen v hesle
- **Počet velkých písmen**: Počet velkých písmen v hesle

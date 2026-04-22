Nastavení SSO
=============

.. note:: Při zadávání konfigurace SSO je jedinečný identifikátor v poli **Jméno** prázdný, který je automaticky generován při prvním uložení konfigurace. Tento identifikátor se používá v URL adresách SSO, takže je zásadní pro správné nastavení na straně poskytovatele identity.

.. warning:: Admin Portal vytvoří SSO endpointy do 3 hodin po uložení konfigurace. Během této doby nebudou URL adresy pro SSO dostupné a při pokusu o jejich použití můžete narazit na chyby. Před testováním konfigurace SSO proto vyčkejte, než budou endpointy vytvořeny. Všechny další změny konfigurace SSO se projeví okamžitě a není potřeba čekat na znovuvytvoření endpointů.

Stránka konfigurace Single Sign-On je dostupná z uživatelského menu v pravém horním rohu Admin Portalu. Otevřete ji kliknutím na ikonu uživatele a následně v rozbalovacím menu vyberte možnost „Nastavení jednotného přihlášení“.

Na stránce konfigurace SSO budete vyzváni k zadání následujících informací:

* **Jméno**: Jedinečný identifikátor konfigurace SSO.
* **Formát Name ID**: Formát Name ID, který bude použit v průběhu SSO přihlášení. Admin Portal podporuje následující formáty:

  * `urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified`
  * `urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress`
  * `urn:oasis:names:tc:SAML:2.0:nameid-format:persistent`
  * `urn:oasis:names:tc:SAML:2.0:nameid-format:transient`

* **Atribut organizace**: (Volitelné) Název claimu, který se použije k identifikaci organizace v procesu SSO. Tento claim musí obsahovat jedinečný identifikátor organizace.
* **Klíč rolí**: Název claimu, který se použije k určení role uživatele pro přiřazení odpovídajících oprávnění k uživatelskému účtu.
* **Obsah metadat**: Obsah SSO metadat poskytnutý vaším poskytovatelem identity. Obvykle zahrnuje informace o IdP, jako je entity ID, SSO URL a certifikát. Tuto možnost použijte, pokud váš poskytovatel identity nepodporuje hostování metadat na URL adrese, není dostupný z internetu nebo pokud metadata chcete zadat ručně.
* **Adresa URL metadat**: URL adresa, ze které lze načíst SSO metadata. Pokud je toto pole vyplněné, Admin Portal načte metadata z této adresy namísto ručně zadaného obsahu metadat.
* **Domény**: Seznam domén oddělených čárkou, kterým je povoleno používat SSO pro autentizaci. Slouží k omezení přístupu přes SSO jen na uživatele z konkrétních domén.
* **Role**: Mapování rolí definovaných ve vašem poskytovateli identity na role používané v Admin Portalu. Díky tomu můžete uživatelům přiřadit odpovídající oprávnění na základě jejich rolí v IdP.
* **Nastavení členů organizací**: Mapování identifikátorů organizací z vašeho poskytovatele identity na názvy organizací používané v Admin Portalu. Slouží k přiřazení uživatelů ke správné organizaci podle informací z IdP.

.. figure:: /img/sso-1.png
   :alt: Stránka SSO Settings - Obecná nastavení

   Příklad části Obecná nastavení na stránce konfigurace SSO v Admin Portalu.

.. figure:: /img/sso-2.png
   :alt: Stránka SSO Settings - Domény

   Příklad konfigurace domén na stránce konfigurace SSO v Admin Portalu.

.. figure:: /img/sso-3.png
   :alt: Stránka SSO Settings - Mapování rolí

   Příklad konfigurace mapování rolí na stránce konfigurace SSO v Admin Portalu.

.. figure:: /img/sso-4.png
   :alt: Stránka SSO Settings - Nastavení organizací

   Příklad konfigurace nastavení organizací na stránce konfigurace SSO v Admin Portalu.

SSO URL adresy Admin Portalu
----------------------------

Při konfiguraci poskytovatele identity budete muset zadat odpovídající URL adresy pro přihlašování přes SSO. Admin Portal používá následující URL:

* **Autentizační URL**: `https://login.whalebone.io/sso/<ssoid>/auth` - URL adresa, kterou uživatelé otevřou pro zahájení autentizace přes SSO.
* **URL s metadaty**: `https://login.whalebone.io/sso/<ssoid>/saml/metadata` - URL adresa, ze které může IdP načíst metadata SSO.
* **Testovací URL**: `https://login.whalebone.io/sso/<ssoid>/test` - URL adresa pro testování konfigurace SSO. Zobrazuje SAML odpověď přijatou od IdP, což je užitečné při řešení problémů a ověření, že konfigurace SSO funguje správně.

.. note:: `<ssoid>` je jedinečný identifikátor vaší konfigurace SSO, který najdete v Admin Portalu v poli **Jméno** po vytvoření konfigurace SSO.

Integrace s populárními poskytovateli identity
----------------------------------------------

Microsoft Active Directory Federation Services (ADFS)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Microsoft ADFS je populární poskytovatel identity podporující Single Sign-On založené na protokolu SAML. Pro integraci ADFS s Admin Portalem je potřeba v ADFS vytvořit nový Relying Party Trust a nakonfigurovat jej s odpovídajícími nastaveními, například SSO URL adresami a claims. Pro zjednodušení konfigurace v ADFS můžete použít URL s metadaty z Admin Portalu.

Níže je přehled hlavních kroků pro integraci ADFS s Admin Portalem. Začněme přidáním nového Relying Party Trust v ADFS:

1. Otevřete konzoli ADFS Management a přejděte do sekce „Relying Party Trusts“.
2. Klikněte na „Add Relying Party Trust“ a spusťte průvodce.
3. Vyberte „Claims aware“ a klikněte na „Start“.
4. Stáhněte SSO metadata z Admin Portalu pomocí poskytnuté URL s metadaty a uložte je do souboru na ADFS serveru.
5. Zvolte „Import data about the relying party from a file“, zadejte cestu k uloženému souboru metadat a klikněte na „Next“.

  .. warning:: Možnost „Import data about the relying party published online or on a local network“ není dostupná, protože SSO v Admin Portalu vyžaduje minimálně TLS 1.2, se kterým má ADFS potíže.

6. Dokončete konfiguraci podle pokynů průvodce a ujistěte se, že nastavíte správné claims tak, aby odpovídaly nastavením Formát Name ID, Klíč rolí a Atribut organizace v Admin Portalu.

Přidání claims v ADFS je zásadní pro správné fungování SSO. Je potřeba přidat claims, které odpovídají Name ID:

1. V konzoli ADFS Management klikněte pravým tlačítkem na nově vytvořený Relying Party Trust a vyberte „Edit Claim Issuance Policy...“.
2. Klikněte na „Add Rule...“ a vytvořte nové claim pravidlo.
3. Vyberte „Send LDAP Attributes as Claims“ a klikněte na „Next“.
4. Zvolte odpovídající attribute store (např. Active Directory) a nastavte claim pravidla tak, aby se uživatelský UPN (user principal name) posílal jako Name ID.
5. Vytvořte další claim pravidla, která budou posílat členství uživatele ve skupinách nebo jiné atributy jako claims odpovídající nastavením Klíč rolí a Atribut organizace v Admin Portalu.

.. figure:: /img/sso-adfs-1.png
   :alt: Konfigurace claim pravidel v ADFS

   Příklad konfigurace claim pravidel v ADFS pro Name ID.

Níže je postup pro přidání claims v ADFS tak, aby odpovídaly Klíč rolí v Admin Portalu:

1. V konzoli ADFS Management klikněte pravým tlačítkem na Relying Party Trust vytvořený pro Admin Portal a vyberte „Edit Claim Issuance Policy...“.
2. Klikněte na „Add Rule...“ a vytvořte nové claim pravidlo.
3. Vyberte „Send LDAP Attributes as Claims“ a klikněte na „Next“.
4. Zvolte odpovídající attribute store (např. Active Directory).
5. Nastavte claim pravidla tak, aby jako claim odpovídající Klíč rolí v Admin Portalu odesílala hodnotu „Token-Groups Unqualified Name“ uživatele (nebo jiný atribut obsahující členství uživatele ve skupinách).

.. figure:: /img/sso-adfs-2.png
   :alt: Konfigurace claim pravidel v ADFS

   Příklad konfigurace claim pravidel v ADFS pro Klíč rolí.

Volitelně můžete přidat i claims pro Klíč organizace, pokud chcete v Admin Portalu přiřazovat uživatele ke konkrétním organizacím na základě jejich atributů v ADFS. Postup je podobný jako u Klíč rolí, jen nastavíte claim pravidla tak, aby odesílala atribut obsahující identifikátor organizace.

Posledním krokem je dokončení konfigurace v Admin Portalu zadáním odpovídajících hodnot do polí Formát Name ID, Klíč rolí a Klíč organizace tak, aby odpovídaly claimům nakonfigurovaným v ADFS. Postup je následující:

1. V Admin Portalu přejděte na stránku Nastavení jednotného přihlášení.
2. Nastavte formát NameID na `urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified` (nebo jiný formát odpovídající Name ID claimu nakonfigurovanému v ADFS).
3. Nastavte Klíč rolí na název claimu odpovídající členství uživatele ve skupinách (např. `http://schemas.microsoft.com/ws/2008/06/identity/claims/role`).
4. Pokud jste nastavili Klíč organizace, zadejte název claimu odpovídající identifikátoru organizace (např. `http://schemas.microsoft.com/ws/2008/06/identity/claims/tenant`).
5. Pokud ADFS server není dostupný z internetu, můžete stáhnout metadata z Metadata URL (např. `https://<ADFS_SERVER>/FederationMetadata/2007-06/FederationMetadata.xml`) a vložit je ručně do pole Metadata contents. Pokud je ADFS server dostupný z internetu, můžete Metadata URL zadat přímo do pole Metadata URL.
6. Zadejte domény, kterým je povoleno používat SSO pro autentizaci (např. `example.com`).
7. V sekci mapování rolí přiřaďte odpovídající role tak, aby uživatelé získali správná oprávnění v Admin Portalu podle svého členství ve skupinách v ADFS.
8. Volitelně nakonfigurujte Nastavení organizací, pokud chcete v Admin Portalu přiřazovat uživatele ke konkrétním organizacím na základě jejich atributů v ADFS.
9. Uložte konfiguraci SSO a před testováním autentizačního procesu SSO vyčkejte, než budou vytvořeny SSO endpointy.

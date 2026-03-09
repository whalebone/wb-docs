Řešení problémů
===============

Pokud narazíte na problémy se Single Sign-On, níže najdete několik běžných kroků pro jejich řešení.

404 stránka nenalezena
----------------------

Pokud při přístupu na SSO URL obdržíte chybu 404, může to znamenat, že SSO endpointy ještě nebyly vytvořeny. Po uložení konfigurace SSO vyčkejte 3 hodiny, než budou endpointy připraveny. Pokud problém přetrvává i po této době, kontaktujte podporu Whalebone.

404 stránka nenalezena i po 3 hodinách
--------------------------------------

Pokud chybu 404 dostáváte i po době potřebné k vytvoření SSO endpointů, může jít o problém v konfiguraci SSO. Zkontrolujte, že URL s metadaty je správná a dostupná z internetu a že obsah metadat je validní. Pokud potíže přetrvávají, obraťte se na podporu Whalebone.

Chybějící atribut identity
--------------------------

Pokud se zobrazí chyba oznamující, že chybí povinný atribut identity, může to znamenat, že Name ID claim poskytovaný vaším poskytovatelem identity chybí nebo neodpovídá očekávanému formátu. Navštivte testovací URL, zkontrolujte odpověď IdP a ověřte, že Name ID je přítomen a má očekávaný formát. Pokud Name ID chybí nebo neodpovídá formátu, zkontrolujte konfiguraci IdP, aby byla správně nastavena pro poskytování potřebných claims.

Chybějící atribut klíč rolí
---------------------------

Pokud se zobrazí chyba oznamující, že chybí povinný atribut rolí, může to znamenat, že claim Klíč rolí poskytovaný vaším poskytovatelem identity chybí nebo neodpovídá očekávanému formátu. Navštivte testovací URL, zkontrolujte odpověď IdP a ověřte, že Klíč rolí je přítomen a má očekávaný formát. Pokud Klíč rolí chybí nebo neodpovídá formátu, zkontrolujte konfiguraci IdP, aby byla správně nastavena pro poskytování potřebných claims.

Níže je příklad výstupu z testovací URL:

.. code-block:: json

  {
    "aud": "https://login.whalebone.io/sso/12345678-90ab-cdef-1234-567890abcdef/",
    "exp": 1771579797,
    "iat": 1771576197,
    "iss": "https://login.whalebone.io/sso/12345678-90ab-cdef-1234-567890abcdef/",
    "nbf": 1771576197,
    "sub": "user@test.intra",
    "attr": {
      "SessionIndex": [
        "_c3148bb6-4b6a-40e3-b0b3-88ba4b99da32"
      ],
      "http://schemas.microsoft.com/ws/2008/06/identity/claims/role": [
        "Domain Admins",
        "Domain Users"
      ]
    },
    "saml-session": true
  }

V tomto příkladu je claim Klíč rolí `http://schemas.microsoft.com/ws/2008/06/identity/claims/role` a obsahuje hodnoty „Domain Admins“ a „Domain Users“. V poli Klíč rolí v konfiguraci SSO je potřeba použít celý název claimu, aby byly role v Admin Portalu správně rozpoznány a přiřazeny.

Detailní řešení problémů
------------------------

Někdy je pro nalezení hlavní příčiny problémů se SSO potřeba podrobněji analyzovat SAML dotazy a odpovědi. K inspekci síťového provozu během autentizačního procesu SSO můžete použít vývojářské nástroje v prohlížeči. Postup řešení problémů obvykle zahrnuje tyto kroky:

1. Otevřete vývojářské nástroje v prohlížeči (obvykle stisknutím `F12` nebo přes pravé tlačítko myši a volbu „Inspect“).
2. Přejděte na záložku „Network“ pro sledování dotazů a odpovědí.
3. Spusťte autentizační proces SSO otevřením autentizační URL.
4. SAML odpověď se hledá snáz, protože se odesílá na URL `https://login.whalebone.io/sso/<ssoid>/saml/acs`. SAML odpověď najdete v Payload u POST dotazu na tuto URL.
5. SAML dotaz bývá obvykle v požadavku, kterému SAML odpověď předchází, a je odeslán na SSO URL IdP. Najdete jej podle parametru `SAMLRequest` v URL nebo v těle dotazu.
6. SAML dotaz i odpověď bývají typicky kódované v Base64, takže je budete muset dekódovat pro analýzu obsahu. Pro dekódování Base64 zpráv SAML můžete použít online nástroje nebo příkazovou řádku.

.. warning:: Při sdílení SAML dotazů a odpovědí nebo při jejich vkládání do online nástrojů buďte opatrní, protože mohou obsahovat citlivé informace. Pokud chcete pro dekódování použít online nástroje, doporučuje se použít testovací prostředí. Před sdílením s týmy podpory nebo na veřejných fórech vždy zajistěte, aby byla data správně anonymizována a neobsahovala osobní údaje ani citlivé atributy.
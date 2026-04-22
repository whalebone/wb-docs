Přehled
=======

.. warning:: Tato funkce je momentálně ve verzi beta a může se měnit. Přestože je plně funkční, uživatelské rozhraní nemusí být zcela doladěné a některé okrajové případy zatím nemusí být pokryté. Pokud chcete tuto funkci používat, kontaktujte prosím tým podpory Whalebone, aby ji pro váš účet aktivoval.

Single Sign-On (SSO) je proces autentizace uživatele, který umožňuje přístup do více aplikací pomocí jedné sady přihlašovacích údajů. To znamená, že jakmile se uživatel přihlásí do jedné aplikace, může přistupovat do dalších propojených aplikací bez nutnosti opětovného přihlášení. V kontextu Whalebone Admin Portalu umožňuje SSO uživatelům ověřit svou identitu pomocí existujících přihlašovacích údajů od poskytovatele identity třetí strany (IdP). Tím lze zvýšit bezpečnost a zlepšit uživatelskou zkušenost díky omezení potřeby více hesel a opakovaných přihlášení.

Pro nastavení Single Sign-On je potřeba nakonfigurovat vašeho poskytovatele identity tak, aby fungoval s Admin Portalem. Obvykle to zahrnuje vytvoření nové aplikace v IdP a nastavení potřebných parametrů, jako jsou redirect URI a claims. Jakmile tyto údaje máte, můžete je zadat do nastavení konfigurace SSO v Admin Portalu.

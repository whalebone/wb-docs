Blokační stránky
================

V případě blokování přístupu k doméně odpovídají resolvery klientům IP adresou blokační stránky, kde jsou uživatelé informováni o tom, že na danou stránku nemohou přistoupit a důvod, proč byl přístup zablokován. Pro blokační stránky Whalebone poskytuje vzorovou šablonu, kterou lze libovolně upravovat. Kód šablony je napsán tak, aby byl kompatibilní s co nejširším rozsahem prohlížečů.

Různé verze **blokačních stránek** mohou být přiřazeny různým segmentům sítí v **Resolvery** → **Přiřazení politiky**.

.. figure:: ./img/blocking-pages-overview.png
   :alt: Přehled blokačních stránek
   :align: center

   Přehled blokačních stránek

Whalebone nabízí čtyři varianty blokačních stránek:

* **Bezpečnost**: zobrazeno, když je přístup blokován z bezpečnostních důvodů
* **Blacklist**: zobrazeno, když je přístup blokován administrátory
* **Právní**: zobrazeno, když je přístup regulován na základě zákona nebo soudního příkazu
* **Obsah**: zobrazeno, když je přístup blokován kvůli obsahu domény

Navíc každá verze může existovat v různých jazykových mutacích. Jazyk blokační stránky se odvíjí od jazyka prohlížeče, ze kterého je na ni přistupováno.

.. figure:: ./img/blocking-pages.png
   :alt: Blokační stránky
   :align: center

   Blokační stránky

Nastavení blokačních stránek poskytuje následující možnosti:

1. Použití šablony: Při použití šablony jsou zadané informace vloženy přímo do kódu šablony. To je nejrychlejší a nejjednodušší způsob, jak přizpůsobit blokační stránku. Nastavení blokační stránky lze provést kliknutím na tlačítko **Kouzelná hůlka**. Při použití šablony dojde k přemázání předešlé konfigurace.

   .. figure:: ./img/template.png
      :alt: Použití šablony
      :align: center

2. Výchozí lokalizace blokační stránky: Tato možnost umožňuje přizpůsobit výchozí jazyk blokační stránky. V případě, že některý prohlížeč neuvádí svůj preferovaný jazyk, funguje "výchozí" jazyk jako záložní mechanismus. Výchozí lokalita je označena pomocí symbolu hvězdičky (*) vedle typu jazyka.

3. Odstranění lokalizace blokační stránky: Lokalitu lze smazat kliknutím na ikonu **Koše**.

Každou z verzí blokační stránky (Bezpečnost, Blacklist, Právní, Obsah) lze detailněji přizpůsobit úpravou HTML kódu. Po kliknutí na každou verzi se zobrazí editor, který umožňuje provést jakékoli požadované změny.

Editor také exponuje rozhraní "Ověření", které analyzuje konečný HTML kód a kontroluje povolené funkce. Kontrola je založena na `id` konkrétních prvků. Více informací a požadavků pro každou funkci lze najít kliknutím na příslušné štítky.

.. note:: Každá verze blokační stránky má unikátní charakteristiky, které lze vybrat. Například, blokační stránka pro **Bezpečnost** může zahrnovat tlačítko **Obejití blokace**, které není dostupné ve verzi stránky v případě **Regulace** a **Blacklist**.

Po editaci a uložení změn na blokačních stránkách je důležité, aby byly aplikovány na jednotlivé resolvery.

.. tip:: Blokační stránky jsou zobrazovány přímo z webového serveru na resolveru. Stránky se očekávají jako jediný soubor, takže veškeré další zdroje (CSS, obrázky, skripty) musí být buď přímo vloženy do HTML kódu, nebo dostupné z veřejně přístupného webového serveru. Resolver neposkytuje žádnou možnost vkládat jiný obsah.

:ref:`Zde<Konfigurace bokacni stranky video>` si můžete prohlédnout videonávod.

Podpis blokačních stránek pomocí certifikační autority
------------------------------------------------------

Pro nasazení, kde máte kontrolu nad pracovními stanicemi, což je typicky firemní prostředí s Group Policy, můžete do jejich úložišť s důvěryhodnými certifikačními autoritami vložit vlastní certifikační autoritu, kterou používají resolvery. To vede k tomu, že prohlížeče přímo přecházejí na blokační stránku bez zobrazení varování o neplatném certifikátu. Resolver v podstatě provádí útok man-in-the-middle pokaždé, když provádí přesměrování na blokační stránku a poskytuje vlastní certifikát pro blokovanou doménu.

Vlastní certifikační autoritu vytvoříte a nastavíte v následujících krocích:

1. Vytvořte soubor adresář /certs:

   .. code-block:: shell

      mkdir /certs

2. Vytvořte soubor "v3_cfg" v adresáři /certs s následujícím obsahem:

   .. code-block:: INI

      [req]
      x509_extensions = v3_ca_extensions
      distinguished_name = req_dn
      [v3_ca_extensions]
      basicConstraints = critical,CA:TRUE
      subjectKeyIdentifier = hash
      authorityKeyIdentifier = keyid:always,issuer:always
      keyUsage = critical, digitalSignature, cRLSign, keyCertSign
      subjectAltName = @alt_names
      [alt_names]
      DNS.1 = localhost
      [req_dn]
      countryName = Country Name (2 letter code)
      countryName_default = US
      stateOrProvinceName = State or Province Name (full name)
      stateOrProvinceName_default = New York
      localityName = Locality Name (eg, city)
      localityName_default = New York City
      organizationName = Organization Name (eg, company)
      organizationName_default = My Organization
      commonName = Common Name (eg, your name or your server's hostname)
      commonName_max = 64

3. Vygenerujte klíč certifikační autority:

   .. code-block:: shell

      openssl ecparam -name prime256v1 -genkey -noout -out /certs/ca.key

4. Vytvořte a podepište certifikát certifikační autority:

   .. code-block:: shell

      openssl req -x509 -new -nodes -key /certs/ca.key -sha256 -days 3650 -out /certs/ca.crt -config /certs/v3_cfg

5. Exportujte privátní klíč a certifikát do PFX souboru:

   .. code-block:: shell

      openssl pkcs12 -export -out /certs/ca.pfx -inkey /certs/ca.key -in /certs/ca.crt -certpbe PBE-SHA1-3DES -keypbe PBE-SHA1-3DES -export -macalg sha1

5. Zazálohujte adresář /certs na bezpečné místo mimo resolver pro případ nutnosti jeho obnovy.

6. Pošlete název a cestu k souboru s privátním klíčem a certifikátem na podporu Whalebone. Naši technici zajistí nastavení služeb, aby začaly používat nově vytvořenou certifikační autoritu.

7. Přidejte veřejný klíč certifikační autority (/certs/ca.crt) do seznamu důvěryhodných certifikačních autorit na všech pracovních stanicích ve Vaší správě.


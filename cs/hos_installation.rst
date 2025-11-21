Instalace
=========

Než začnete
-----------

* Zajistěte si přístup do portálu Whalebone.
* Ověřte síťový přístup na TCP 443.
* Pokud zavádíte pro více uživatelů, připravte si prostředí **MDM** nebo **Active Directory**.

Konfigurace v portálu
---------------------

1. Přihlaste se do portálu Whalebone.

2. Přejděte do **Home Office Security**, které se nachází v menu pod ikonou uživatele v pravém horním rohu obrazovky.

    .. image:: ./img/hos-sbs-1.png
        :align: center

3. Ověřte přítomnost nebo vytvořte **skupinu zařízení** pomocí tlačítka **+ Vytvořit skupinu**.

    .. image:: ./img/hos-sbs-2.png
        :align: center

4. Možnosti konfigurace skupiny zařízení:
    
      * **Název:** Identifikační štítek, např. Výchozí skupina (Default Group).
    
      * **Bezpečsnotní politika:** Vyberte preferovanou bezpečnostní politiku.
    
      * **Blokovační stránka:** Definujte, jaká šablona blokační stránky se má zobrazit.
    
      * **Výjimky na domény:** Zadejte domény, které by měly být vyjmuty z ochranu.
    
      * **Vypnout home office zabezpečení uvnitř podnikové sítě:** Volitelné; definujte:
        
          * *Interní doména*: Dotazovaná doména, která je dostupná pouze z interní sítě.
          * *Interní odpověď*: Hodnota vrácená při připojení uvnitř sítě.
          * *Typ dotazu*: Záznam A / AAAA / TXT, odpovídající vaší DNS konfiguraci.

5. Kliknutím na **Přidat** skupinu uložíte.

    .. image:: ./img/hos-sbs-3.png
        :align: center

Bezobslužná instalace (Windows 64-bit)
--------------------------------------

1. Vyberte cílovou skupinu, do které chcete přidat nově nainstalovaného klienta, kliknutím na tlačítko **Instalace do skupiny**, čímž se zobrazí odkazy ke stažení a instalační příkazy.

2. Stáhněte soubor **Whalebone.Home.Office.Security.Installer.msi** z `https://github.com/whalebone/home-office-security/releases <https://github.com/whalebone/home-office-security/releases>`_.

3. Zkopírujte instalační příkaz z portálu, například:
    
    .. code-block:: bash

        msiexec /i "Whalebone.Home.Office.Security.Installer.msi" TOKEN="12345678-1234-1234-1234-123456789012" REGION="eu-01"

4. Použijte preferované MDM k distribuci aplikace uživatelům vytvořením nového nasazení s příkazem zkopírovaným z portálu.

Odinstalace
-----------

.. code-block:: bash

    msiexec /x "Whalebone.Home.Office.Security.Installer.msi"


Instalace přes GUI (Windows 64-bit)
-----------------------------------

1. Vyberte cílovou skupinu, do které chcete přidat nově nainstalovaného klienta, kliknutím na tlačítko **Instalace do skupiny**, čímž se zobrazí odkazy ke stažení a instalační příkazy.

2. Stáhněte soubor **Whalebone.Home.Office.Security.Installer.msi** z `https://github.com/whalebone/home-office-security/releases <https://github.com/whalebone/home-office-security/releases>`_.

3. Dvojklikněte na stažený soubor MSI pro spuštění.

4. Zadejte párovací token, který naleznete na portálu, do okna instalačního programu. Například:
    
    .. code-block:: text

      aG9zLmFwcDovL2F1dGg/dG9rZW49MTIzNDU2NzgtMTIzNC0xMjM0LTEyMzQtMTIzNDU2Nzg5MDEyJnJlZ2lvbj1ldS0wMQ==

Ruční instalace (Android / iOS)
-------------------------------

* Vyberte cílovou skupinu, do které chcete přidat nově nainstalovaného klienta, kliknutím na tlačítko **Instalace do skupiny**, které zobrazí odkazy ke stažení a aktivační QR kód.
* Odešlete odkaz a QR kód uživatelům.
* Uživatelé si aplikaci nainstalují a budou vyzváni k naskenování QR kódu k dokončení procesu instalace.

Ověření po instalaci
--------------------

Zařízení se po úspěšné registraci objeví v seznamu zařízení v nastavení Home Office Security.
Odinstalování lokálního resolveru
=================================

Pro odinstalování resolveru a odstranění všech konfiguračních souborů Whalebone je třeba provést následující kroky:


.. warning:: Před zahájením procesu je třeba upozornit, že všechny jednotlivé komponenty, které podporují funkčnost resolveru, jsou spuštěny jako docker kontejnery. Kroky 1 a 2 platí pouze v případě, že je hostitelský server **dedikovaný** a **žádné další služby** nejsou spuštěny jako kontejnery. V případě jiné situace nás prosím kontaktujte a my vám poskytneme aktuální seznam kontejnerů, které by měly být odstraněny.

**1. Krok** – Zastavte a odstraňte všechny spuštěné kontejnery docker:

   .. code::

   		docker rm -f lr-agent && docker rm -f $(docker ps -q)

**2. Krok** – Odinstalujte docker:

   Postupujte podle pokynů pro příslušný operační systém:

   -  `CentOS <https://docs.docker.com/install/linux/docker-ce/centos/#uninstall-docker-engine---community>`__

   -  `Red Hat <https://docs.docker.com/install/linux/docker-ce/fedora/#uninstall-docker-engine---community>`__

   -  `Debian <https://docs.docker.com/install/linux/docker-ce/debian/#uninstall-docker-engine---community>`__

   -  `Ubuntu <https://docs.docker.com/install/linux/docker-ce/ubuntu/#uninstall-docker-engine---community>`__

**3. Krok** – Odstranění všech konfiguračních souborů resolveru a souvisejících dat:

   .. code:: 

      rm -rf /etc/whalebone 
      rm -rf /var/whalebone
      rm -rf /var/lib/kres


**4.Krok** – Odstranění protokolů o provozu DNS a incidentech:

   Pokud chcete resolver zcela odinstalovat včetně záznamů z přenosů a incidentů DNS, odstraňte také složku s záznamy.
   Pokud je vaším záměrem pouze přeinstalovat resolver, ale protokoly ponechat, můžete tento krok přeskočit.

    .. code::

        rm -rf /var/log/whalebone
    
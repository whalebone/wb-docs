Cloudové nasazení
================

Whalebone lze nasadit v několika scénářích, které lze dokonce kombinovat tak, aby splňovaly požadavky konkrétních sítí. Kombinace cloudového a lokálního DNS resolveru s jediným portátálem pro správu je vhodná i v případě složitých, distribuovaných sítí.

.. tip:: Všechny níže uvedené možnosti lze kombinovat dohromady. Různé síťové segmenty a zóny mohou mít různé požadavky a možnosti.

.. tip:: Pokud ani jeden z níže uvedených scénářů konfigurace nevyhovuje Vašemu preferovanému případu použití, obraťte se na podporu společnosti Whalebone a my vám pomůžeme s návrhem architektury, která bude vyhovovat vašim potřebám a požadavkům.


Použití stávající DNS pro přesměrování na Whalebone Cloud DNS
-------------------------------------------------------------

Jedná se o nejjednodušší způsob o nasazení. Chcete-li používat Whalebone resolver, stačí změnit konfiguraci vašich DNS resolverů a nasměrovat je na cloudové resolvery Whalebone.
Nevýhodou tohoto nasazení je, že všechny incidenty budou viditelné se zdrojovou IP adresou DNS forwarderu namísto původní zdrojové IP adresy. Přesto se toto nasazení může hodit, pokud je prioritou zabránit hrozbám s co nejmenším úsilím a změnami infrastruktury.


.. image:: ./img/deployment_cloud.png
   :align: center

Cloudové DNS (příme spojení)
-----------------------------

Toto nasazení je podobné předávání požadavků na cloudové resolvery Whalebone, ale požadavky jsou odesílány přímo do cloudu bez místní mezipaměti DNS. To lze obvykle nastavit pro všechny koncové body prostřednictvím DHCP. Nepoužití místní mezipaměti DNS však znamená zvýšenou latenci způsobenou síťovou komunikací mezi klientem a cloudovým resolverem.
Pokud nejsou jednotlivé počítače skryty za NAT, budou jejich IP adresy přímo viditelné v hlášení Whalebone a klienty lze snadno rozlišit.

.. image:: ./img/deployment_cloud_direct.png
   :align: center

Whalebone Peacemaker
===================

Místní překladač DNS pro poskytovatele internetových služeb (ISP)
-----------------------------------------------------------------

Tento scénář nasazení využívá místní resolver Whalebone, který komunikuje s cloudem Whalebone prostřednictvím rozhraní API. Řešení DNS probíhá přímo na resolveru a je zcela nezávislé na dostupnosti cloudu. V případě, že resolver nebude schopen dosáhnout cloudové služby, nebude schopen aktualizovat informace o hrozbách a hlásit případné incidenty.
Hlavní výhodou tohoto nasazení je viditelnost místní sítě a jednotlivých IP adres a nízká latence.


.. image:: ./img/deployment_isp.png
   :align: center

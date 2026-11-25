======================
Integrace s Logmanager
======================

Logmanager je platforma pro log management a SIEM, která umožňuje centralizovaný sběr, ukládání a analýzu logů z různých zdrojů v IT prostředí.

Whalebone podporuje integraci s platformou Logmanager prostřednictvím exportování Syslogu. Díky tomu mohou zákazníci centralizovat bezpečnostní události z Whalebone, analyzovat je společně s ostatními logy a využívat pokročilé možnosti monitoringu a detekce v prostředí Logmanager. Logmanager poskytuje připravenou podporu pro zpracování logů z Whalebone a popisuje celý postup konfigurace na své dokumentační stránce. Ta obsahuje informace o konfiguraci parseru, podporovaných typech logů i doporučeném nastavení.

* Podrobný návod pro konfiguraci v Logmanageru naleznete zde: `Logmanager dokumentace <https://doc.logmanager.com/3.12.0/cz/log-source-devices/whalebone/>`_

* Pro nastavení exportu Syslogu ve Whalebone postupujte podle naší dokumentace: :doc:`syslog_integration`

Po konfiguraci Syslog exportu ve Whalebone a nastavení příjmu logů v Logmanageru budou události z Whalebone automaticky zpracovávány parserem Logmanageru a připraveny k dalšímu vyhodnocování.
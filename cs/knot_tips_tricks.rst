Knot Resolver - Tipy a Triky
============================

Pokročilá konfigurace Whalebone resolveru umožňuje použít využít přímou konfiguraci Knot Resolveru. V této části popíšeme nejčastější případy použití a příklady takových konfigurací.
Zásady a akce se vyhodnocují v pořadí, v jakém jsou definovány (s výjimkou speciálních řetězových akcí, které jsou popsány v oficiální dokumentaci Knot Resolveru). První shoda provede akci, zbytek pravidel zásad se nevyhodnocuje. Pokud budete kombinovat různé fragmenty konfigurace, můžete stejný modul načíst jen jednou na začátku konfigurace.


Povolení konkrétních rozsahů IP adres
-------------------------------------

Definujte seznam rozsahů IP, které budou mít povoleno používat tento DNS resolver. Dotazy ze všech ostatních rozsahů budou odmítnuty.

.. code-block:: lua

  --načtení modulů
  modules = {'policy', 'view'}

  --definuje seznam povolených rozsahů
  --127.0.0.1 by měl být vždy povolen
  allowed = {
    '127.0.0.1/32',
    '10.10.20.5/32',
    '10.30.10.0/24'
  }

  --cyklus procházející seznam pololených rozsahů
  for i,subnet in ipairs(allowed) do
    view:addr(subnet, policy.all(policy.PASS))
  end

  --ostatní rozsahy jsou zablokovány
  view:addr('0.0.0.0/0', policy.all(policy.DENY))


Odmítnutí určitých rozsahů IP
-----------------------------

Definujte seznam rozsahů IP, které budou blokovány pro použití tohoto DNS resolveru. Dotazy ze všech ostatních rozsahů budou povoleny.

.. code-block:: lua

  --načtení modulů
  modules = {'policy', 'view'}

  --definuje seznam blokovaných rozsahů
  blocked = {
    '10.10.20.5/32',
    '10.30.10.0/24'
  }

  --cyklus procházející seznam blokovaných rozsahů
  for i,subnet in ipairs(blocked) do
    view:addr(subnet, policy.all(policy.REFUSE))
  end

Povolit seznam domén
---------------------

.. code-block:: lua

  --načtení modulů
  modules = {'policy'}

  --definuje seznam povolených domén
  domains = {
    'example.com',
    'anotherexample.org'
  }

  --cyklus procházející seznam povolených domén
  for i,domain in ipairs(domains) do
    policy.add(policy.suffix(policy.PASS, {todname(domain)}))
  end

Deny list of domains
---------------------

.. code-block:: lua

  -- load modules
  modules = {'policy'}

  --definuje seznam blokovaných domén
  domains = {
    'example.com',
    'anotherexample.org'
  }

  --cyklus procházející seznam blokovaných domén vracející NXDOMAIN
  for i,domain in ipairs(domains) do
    policy.add(policy.suffix(policy.DENY, {todname(domain)}))
  end
  

Globální vypnutí DNSSEC validace
--------------------------------

.. code-block:: lua

  trust_anchors.negative = { '.' }

Vypnutí DNSSEC validace pro konkrétní doménu
--------------------------------------------

.. code-block:: lua

  trust_anchors.set_insecure({ 'domain.com' })


Zákaz náhodného výběru dotazů
-----------------------------

.. code-block:: lua

  policy.add(policy.suffix(policy.FLAGS('NO_0X20'), {todname('domain.com')}))


Zakáz minimalizace QNAME
------------------------

.. code-block:: lua

  policy.add(policy.suffix(policy.FLAGS('NO_MINIMIZE'), {todname('domain.com')}))

Zakáz ukládání domény do mezipaměti
-----------------------------------

.. code-block:: lua

  policy.add(policy.suffix(policy.FLAGS('NO_CACHE'), {todname('domain.com')}))

Povolení metrik Prométheus
--------------------------

Resolver může vystavit své metriky v textovém formátu Prometheus. 
Následující skript povolí modul HTTP a zpřístupní příslušný endpoint ``/metrics``.

Další informace a možnosti konfigurace naleznete na stránce `Dokumentace k Knot Resolveru <https://knot-resolver.readthedocs.io/en/stable/modules-stats.html#prometheus-metrics-endpoint>`_.


.. code-block:: lua

	modules.load('http')
	function startHttp ()
	net.listen('127.0.0.1', 8453, { kind = 'webmgmt' })
	end
	pcall(startHttp)

Knot Resolver - Tips & Tricks
=============================

Advanced configuration of Whalebone resolver allows to apply any Knot Resolver configuration. In this section we are going to describe the most frequent use cases and examples of such configuration snippets.
Views, policies and their actions are evaluated in the sequence as they are defined (except special chain actions that are described in the official Knot Resolver documentation). First match will execute the action, the rest of the policy rules is not evaluated. If you are going to combine different configuration snippets, you can load the same module just once at the beginning of the configuration.

Allow particular IP ranges
--------------------------

Define a list of IP ranges that will be allowed to use this DNS resolver. Queries from all other ranges will be refused.

.. code-block:: lua

  -- load modules
  modules = {'policy', 'view'}

  --define list of ranges to allow
  --127.0.0.1 should always be allowed
  allowed = {
    '127.0.0.1/32',
    '10.10.20.5/32',
    '10.30.10.0/24'
  }

  -- allow list of ranges
  for i,subnet in ipairs(allowed) do
    view:addr(subnet, policy.all(policy.PASS))
  end

  -- block all other ranges
  view:addr('0.0.0.0/0', policy.all(policy.DENY))


Refuse particular IP ranges
---------------------------

Define a list of IP ranges that will be blocked to use this DNS resolver. Queries from all other ranges will be allowed.

.. code-block:: lua

  -- load modules
  modules = {'policy', 'view'}

  --define list of ranges to block
  blocked = {
    '10.10.20.5/32',
    '10.30.10.0/24'
  }

  -- block list of ranges
  for i,subnet in ipairs(blocked) do
    view:addr(subnet, policy.all(policy.REFUSE))
  end

Allow list of domains
---------------------

.. code-block:: lua

  -- load modules
  modules = {'policy'}

  --define list of allowed domains
  domains = {
    'example.com',
    'anotherexample.org'
  }

-- allow list of domains
for i,domain in ipairs(domains) do
  policy.add(policy.suffix(policy.PASS, {todname(domain)}))
end

Deny list of domains
---------------------

.. code-block:: lua

  -- load modules
  modules = {'policy'}

  --define list of denied domains
  domains = {
    'example.com',
    'anotherexample.org'
  }

  -- deny list of domains, while returning NXDOMAIN
  for i,domain in ipairs(domains) do
    policy.add(policy.suffix(policy.DENY, {todname(domain)}))
  end
  

Disable DNSSEC globally
-----------------------

.. code-block:: lua

  trust_anchors.negative = { '.' }

Disable DNSSEC validation for a domain
--------------------------------------

.. code-block:: lua

  trust_anchors.set_insecure({ 'domain.com' })


Disable Query Case Randomization
--------------------------------

.. code-block:: lua

  policy.add(policy.suffix(policy.FLAGS('NO_0X20'), {todname('domain.com')}))


Disable QNAME Minimization
--------------------------

.. code-block:: lua

  policy.add(policy.suffix(policy.FLAGS('NO_MINIMIZE'), {todname('domain.com')}))

Disable Domain caching
----------------------

.. code-block:: lua

  policy.add(policy.suffix(policy.FLAGS('NO_CACHE'), {todname('domain.com')}))

Enable Prometheus Metrics
-------------------------

The resolver can expose its metrics in Prometheus text format. 
The following script enables the HTTP module and the respective ``/metrics`` endpoint is made available.

More information and configuration options can be found on `Knot Resolver Documentation <https://knot-resolver.readthedocs.io/en/stable/modules-stats.html#prometheus-metrics-endpoint>`_

.. code-block:: lua

	modules.load('http')
	function startHttp ()
	net.listen('127.0.0.1', 8453, { kind = 'webmgmt' })
	end
	pcall(startHttp)

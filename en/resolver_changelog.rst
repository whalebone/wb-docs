******************
Resolver changelog
******************

This page contains customer-facing release notes for Whalebone Resolver.
Before upgrading, review the requirements and notes for the target version.

Resolver 3.4.1
==============

Required before upgrade
-----------------------

.. important::

   **Docker Engine 24.0 or newer is required.**

   This release is not compatible with Docker Engine 23.0 and earlier. Before
   upgrading the resolver, make sure the server is running Docker Engine 24.0
   or newer. Otherwise, the upgrade may fail and the resolver may end up in an
   **Unavailable** state, requiring manual intervention on the server.

   Virtualized environments must expose the required x86-64-v2 or x86-64-v3
   CPU instructions, including AES, to the virtual machine. Otherwise, the
   resolver may fail because of a library dependency.

Release highlights
------------------

* **Security and DNSSEC reliability fixes:** Includes important upstream
  security fixes in the resolver engine, including DNS-over-QUIC issues that
  could allow remote code execution in affected configurations. It also
  improves DNSSEC correctness in aggressive-caching edge cases and updates the
  IANA certificate used during root trust-anchor bootstrapping.
* **Resolver protocol and DNS behavior fixes:** Improves DoH cache-control
  behavior, DNS64/CNAME handling, EDNS BADVERS responses, and selected
  local-data and RPZ edge cases. These changes improve resolver correctness and
  standards compliance in specific DNS scenarios.

Resolver 3.4.0
==============

Required before upgrade
-----------------------

.. important::

   **Docker Engine 24.0 or newer is required.**

   This release is not compatible with Docker Engine 23.0 and earlier. Before
   upgrading the resolver, make sure the server is running Docker Engine 24.0
   or newer. Otherwise, the upgrade may fail and the resolver may end up in an
   **Unavailable** state, requiring manual intervention on the server.

   Virtualized environments must expose the required x86-64-v2 or x86-64-v3
   CPU instructions, including AES, to the virtual machine.

Release highlights
------------------

This release improves database update efficiency and operational reliability.

* **Flexible upgrade handling for disk-space requirements:** Resolver upgrades
  can be allowed after manual configuration when a deployment does not meet the
  minimum disk-space requirement. Meeting the documented minimum hardware
  requirements is still strongly recommended for stable operation.
* **More efficient database downloads:** Resolver databases are downloaded and
  managed per database environment. Only changed database parts are
  downloaded, reducing unnecessary full database transfers.
* **Improved service coexistence on resolver hosts:** Blocking-page HTTP and
  HTTPS listeners can bind to specific IP addresses, making it easier to run
  the blocking page alongside services such as DoH on the same host.
* **Operational reliability fixes:** Improves cache sizing, LMDB timestamp
  checks, resolver-container restart behavior, Docker statistics collection,
  and blocking-page debug logging.

.. only:: Aura

   * **RADIUS and Diameter traffic filtering:** Accounting traffic can be
     filtered before forwarding using configurable attribute and AVP rules.
   * **Passive Diameter listener support:** Resolver deployments can process
     mirrored Diameter CCR traffic without sending responses.

Notes
-----

* During upgrade, the existing resolver database cache layout is migrated
  automatically to the new per-environment structure. No manual migration is
  expected during the standard upgrade path.
* If disk-space validation is bypassed, the resolver may still be running below
  the recommended storage requirements. Use this only in controlled and
  reviewed environments.
* Resolver memory usage may increase after upgrade. This is expected because
  the cache configuration is now applied correctly and the cache is stored in
  memory. A larger cache can improve the cache hit ratio and performance.

Resolver 3.3.0
==============

.. only:: Immunity or Peacemaker

   Required before upgrade
   -----------------------

   .. important::

      Docker Engine 24.0 or newer is required. Virtualized environments must
      expose the required x86-64-v2 CPU instructions, including AES.

   This release improves blocking coverage, DNS traffic logging, real-time
   updates, and operational safety.

   * **Stronger blocking coverage:** Domains are blocked across more DNS query
     types, including TXT and CNAME.
   * **Enhanced DNS traffic logging controls:** Optional anonymization,
     deduplication, and sampling make logs easier to use for reporting,
     troubleshooting, and high-volume operations.
   * **More real-time threat-intelligence updates:** Resolvers receive more
     threat indicators in real time.
   * **Faster policy updates:** Supported policy and configuration changes are
     streamed directly to resolvers.
   * **Safer upgrades and operations:** Adds pre-upgrade disk and log-rotation
     validation, blocking health checks, improved recovery behavior, and
     smoother metrics after resolver restarts.

   .. note::

      After upgrade, some existing local log files may be processed once more,
      temporarily duplicating exported logs. DNS resolution and blocking are
      not affected.

.. only:: Aura

   This release improves blocking coverage, identity handling, DNS traffic
   logging, real-time policy updates, and operational safety.

   * **Stronger blocking coverage:** Domains can be blocked regardless of DNS
     query type, including modern query types such as HTTPS.
   * **Cisco EDNS0 identity support:** The resolver can extract device identity
     from configured EDNS0 packet data and use it for policy matching.
   * **Enhanced DNS traffic logging controls:** Adds optional anonymization,
     deduplication, and sampling.
   * **Faster policy updates:** Supported policy and configuration changes are
     streamed directly to resolvers.
   * **Safer upgrades and operations:** Adds pre-upgrade disk and log-rotation
     validation, blocking health checks, improved recovery behavior, and
     smoother metrics after resolver restarts.

   .. note::

      After upgrade, some existing local log files may be processed once more,
      temporarily duplicating exported logs. DNS resolution and blocking are
      not affected.

Resolver 3.2.0
==============

Advanced threat protection
--------------------------

* **Deep CNAME inspection:** The resolver inspects the complete CNAME chain, up
  to ten levels deep, when processing DNS requests.
* **TXT-record threat blocking:** TXT queries to domains identified as threats
  are actively blocked, helping prevent command-and-control communication and
  data exfiltration.

Enhanced visibility and logging
-------------------------------

* **Richer threat and content logs:** Exported logs include the protocol,
  ``qclass``, and ``ede_code`` fields.

Protocol upgrades and user experience
-------------------------------------

* **DNS-over-QUIC support (Beta):** The DNS engine was upgraded to Knot Resolver
  6.2.0, adding early support for DNS-over-QUIC. Test this beta feature in
  non-critical environments.
* **YouTube Safe Search update:** YouTube and related domains were removed from
  the enforced Safe Search list to restore access to YouTube live streams.

Resolver 3.1.4
==============

* Improved stability under heavy DNS traffic.
* Fixed rare cache database locking issues.

Resolver 3.1.3
==============

This release fixes Knot Resolver caching behavior that could keep empty DNS
answers (NOERROR/NODATA) cached for too long, causing persistent resolution
failures after transient upstream issues.

* **Fix:** Empty responses no longer persist with an unexpectedly long TTL.
* **Result:** Reduces cases where affected domains recover only after a cache
  flush or switching resolvers.
* **Impact:** Improves DNS resolution stability during transient upstream or
  authoritative-server anomalies and reduces the need for manual cache clearing.
* **Recommendation:** No configuration changes are required. Temporary TTL caps
  used only as a workaround can be reviewed after upgrade. Optionally flush the
  cache after deployment to clear already-stuck entries sooner.

Resolver 3.1.1
==============

* **Safer upgrades and rollbacks:** Hardens rollback flows so the resolver
  returns to a working state even if an invalid configuration is deployed.
* **More reliable monitoring:** Fixes an edge case where resolver metrics could
  disappear after a failed upgrade and rollback.
* **Cleaner operations:** Reduces noisy errors where optional dnstag/dnstap
  logging is not used.
* **Public-cloud blocking page:** Fixes a rare case where incorrect customer
  branding could be shown.
* **Improved resilience:** Improves automatic recovery after rare database or
  load failures.

Resolver 3.0.1
==============

Required before upgrade
-----------------------

.. important::

   Docker Engine 24.0 or newer is required. Virtualized environments must
   expose x86-64-v2 CPU instructions, including AES.

Fixed
-----

* **Resolver robustness:** Fixes two rare conditions that could cause the
  resolver to exit while processing unusual DNS messages. No configuration
  changes are required.

Resolver 3.0.0
==============

Required before upgrade
-----------------------

.. warning::

   This release is not compatible with DNS forwarding for the ``.local``
   domain.

.. important::

   Docker Engine 24.0 or newer is required. Virtualized environments must
   expose x86-64-v2 CPU instructions, including AES.

New features
------------

* Safe Search enforcement.
* CPU-aware deferring.
* DNS rate limiting.
* Static DNS records support all record types.

Changes
-------

* Added support for Knot Resolver 6.x and upgraded to Knot Resolver 6.0.14.
* Added crash detection for Knot Resolver 5 and 6.
* Added the ``ratelimited`` flag to dnstap messages.
* Added Safe Search support for content-filtered clients.
* Updated the agent base image to Ubuntu 24.04 and Python 3.12.
* Resolver statistics are collected through the management socket.
* Improved UNIX-socket reliability and single-domain cache clearing.

Resolver 2.1.7
==============

This release focuses on upstream security and DNSSEC correctness fixes.

* Fixes aggressive-caching edge cases in RRSIG label and NSEC next-name
  handling.
* Updates the IANA certificate used during root trust-anchor bootstrapping.
* Improves DNSSEC responses with empty ANSWER and AUTHORITY sections.
* Improves DoH cache-control behavior.

Resolver 2.1.6
==============

* Improved HTTPS sinkhole behavior for HTTPS-record requests. User-defined and
  default IPv4 and IPv6 sinkhole values are applied more consistently.

Resolver 2.1.5
==============

* Improved stability under heavy DNS traffic.
* Fixed rare cache database locking issues.

Resolver 2.1.4
==============

This release fixes Knot Resolver caching behavior that could keep empty DNS
answers (NOERROR/NODATA) cached for too long.

* Corrects handling of cached empty responses so they do not persist with an
  unexpectedly long TTL.
* Improves stability during transient upstream or authoritative-server issues.
* No configuration changes are required. Optionally flush the cache after
  deployment to clear already-stuck entries sooner.

Resolver 2.1.1
==============

Required before upgrade
-----------------------

.. important::

   Docker Engine 24.0 or newer is required. Virtualized environments must
   expose x86-64-v2 CPU instructions, including AES.

* Fixes two rare conditions that could cause the resolver to exit while
  processing unusual DNS messages.
* No configuration changes are required.

Resolver 2.1.0
==============

Required before upgrade
-----------------------

.. important::

   Docker Engine 24.0 or newer is required. Virtualized environments must
   expose x86-64-v2 CPU instructions, including AES.

New features
------------

* Fixes a DNSSEC vulnerability.
* Adds EDE codes, protocol, ``qclass``, and response time to logs and dnstap.
* Adds a mechanism for sharing extended log data.
* Excludes ``connectivity-check.whalebone.io`` traffic from logs.
* Adds client-IP anonymization support.
* Adds TLS-hardening options for internal communication.
* Adds IPv6-prefix-based customer identity support.

Changes
-------

* Upgrades Knot Resolver to 5.7.5 and LMDB to 0.9.33.
* Extends passive DNS logs with rate-limiting and diagnostic fields.
* Changes logcat output filenames to use a ``-<date>.ndjson`` suffix.
* Removes deprecated NATS-related environment variables.

Resolver 2.0.1
==============

* Rolls the agent's Python version back to 3.8 for compatibility with Docker
  Engine 23.0 and earlier.

.. warning::

   The next release requires Docker Engine 24.0 or newer. Upgrade Docker before
   upgrading beyond Resolver 2.0.1.

Resolver 2.0.0
==============

.. warning::

   Upgrade Docker Engine to version 24.0 or newer before upgrading the
   resolver.

Highlights
----------

* Improves fallback behavior when downloaded databases are corrupted.
* Adds database creation timestamps to resolver status information.
* Adds support for DNS requests originating behind CGNAT.
* Adds policy tags to dnstap, threat, and content logs.
* Persists database ETags across service restarts.
* Adds optional reverse-IP lookup and configurable log filtering.
* Passes the HTTP originator port to blocking-page bypass requests.
* Improves container health checks, local API reliability, database handling,
  and concurrent LMDB access.
* Removes the bypass button from deny-list and legally mandated blocking pages.

Legacy Resolver 1.x
===================

Resolver 1.x is end of life. The following historical releases are included for
reference.

Resolver 1.0.93
---------------

* If corrupted or missing databases are detected at startup, they are skipped
  and empty databases are initialized in the cache directory.

Resolver 1.0.92
---------------

* Upgrades Knot Resolver to 5.7.4, adds the KSK-2024 DNSSEC root key, and
  reduces buffering that could contribute to TCP denial-of-service conditions.
* Improves database initialization, cleanup, and concurrent update handling.
* Adds blocking-page visit statistics and strengthens blocking-page TLS
  configuration to require TLS 1.2 or newer.
* Rewrites kresman and consumer components in Go for improved performance and
  memory management.

Resolver 1.0.91
---------------

* Improves consumer performance and fixes a memory leak.
* Improves database lifecycle handling and configurable gRPC streams.
* Makes generated-certificate cache access thread-safe.

Resolver 1.0.89
---------------

* Upgrades Knot Resolver to 5.7.4 to address a security vulnerability, reduce
  TCP buffering, and add the KSK-2024 DNSSEC root key.

Resolver 1.0.87
---------------

* Fixes cloud-resolver log attribution and handling of malicious,
  non-existent domains.
* Opens dnstag logs in append mode to support log rotation and reduce CPU use.

Resolver 1.0.84
---------------

* Adds blocking-page visit statistics.
* Upgrades Knot Resolver to 5.7.3 and improves startup database handling.
* Prevents temporary database-download artifacts from filling disk space.
* Strengthens blocking-page TLS configuration to require TLS 1.2 or newer.

Resolver 1.0.82
---------------

* Introduces component-specific versioning for components with third-party
  dependencies.
* Adds signed container images, improved database locking and lifecycle
  handling, configurable bypass duration, and blocking-page metrics.
* Adds hostname enrichment to threat logs and improves connection stability.

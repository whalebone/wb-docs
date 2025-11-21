Operation and Monitoring
========================

Device states
-------------

======== ===================================================================================================
State        Description
======== ===================================================================================================
Active   The device was running and communicating with the Whalebone backend for the last 24 hours.
Inactive The device was not running or was unable to connect to the Whalebone backend for the last 24 hours.
======== ===================================================================================================

Automatic resolver selection
----------------------------

The HOS client automatically connects to the **nearest Whalebone DNS cloud resolver** for the fastest possible response time. When an internal domain is detected, HOS seamlessly switches to the internal resolver, ensuring access to corporate resources without manual configuration.

Protection behavior
-------------------

* Uses **DNS-over-HTTPS** to encrypt and validate queries.
* Local domains are resolved by the operating system's DNS resolver when the "Disable home office security inside corporate network" feature is enabled and properly configured.
* The agent monitors network changes and automatically adjusts the state.

Monitoring
----------

* In the Portal, view each device's group, policy, last seen timestamp, and connection state.
* Internet reachability checks use native Windows API, minimizing false "No Internet" states.
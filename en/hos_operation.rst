Operation and Monitoring
========================

Device states
-------------

============ ===================================================================================== ==========================================
State        Description                                                                           Trigger
============ ===================================================================================== ==========================================
**Active**   The devices contacted the Whalebone backend at least once in the past 24 hours.                        
**Inactive** The devices did not contact the Whalebone backend at least once in the past 24 hours. Device connected to the corporate network.
============ ===================================================================================== ==========================================

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
Operation and Monitoring
========================

Device activity in the Admin Portal
-----------------------------------

The Admin Portal reports whether a device has communicated with the Whalebone backend in the last 24 hours. This activity status is separate from the protection state shown in the Home Office Security client: an active device is not necessarily filtering DNS traffic at that moment.

======== ===================================================================================================
State        Description
======== ===================================================================================================
Active   The device contacted the Whalebone backend at least once in the last 24 hours.
Inactive The device has not contacted the Whalebone backend in the last 24 hours.
======== ===================================================================================================

.. _hos-client-states:

Client protection states
------------------------

The Home Office Security client shows specific protection states and failure reasons on the home screen. Each state has a title and a subtitle.

.. list-table:: Home screen states
   :header-rows: 1
   :widths: 25 35 40

   * - State
     - Title
     - Subtitle
   * - Starting
     - Just a second …
     - Connecting to the protection service
   * - Active
     - Protection is active
     - Malicious websites are being filtered
   * - Paused by user
     - Protection paused
     - Turn protection back on using the toggle
   * - Trusted network
     - You are on a trusted network
     - Your protection is enabled at the network level
   * - VPN detected
     - VPN detected
     - Protection is on standby
   * - Incompatible software
     - VPN detected
     - Protection is on standby
   * - No internet
     - You are not connected to the internet
     - Protection will start when the connection is restored

The trusted-network state applies when the **Disable HOS inside corporate network** option is enabled and the configured internal DNS record matches the expected response. HOS pauses local filtering while protection is provided at the network level. VPN detection and incompatible software also put protection on standby; both states display the same home screen message.

.. _hos-error-states:

Protection error states
-----------------------

The following states explain why protection could not be enabled.

.. list-table:: Error messages on the home screen
   :header-rows: 1
   :widths: 25 35 40

   * - State
     - Title
     - Subtitle
   * - DoH unreachable
     - Protective DNS resolvers cannot be reached
     - Protective DNS servers cannot be reached. Contact your IT administrator.
   * - DoH failed
     - Protective DNS resolvers cannot be reached
     - Protective resolvers failed. Contact your IT administrator.
   * - Proxy blocked
     - Network proxy is blocking protection
     - Network proxy is blocking protection. Contact your IT administrator.
   * - Protection service stopped
     - Protection service is not running
     - Contact your IT administrator
   * - Whalebone servers unavailable
     - Protection could not be enabled
     - Whalebone servers cannot be reached. Contact your IT administrator.
   * - Windows service unavailable
     - Protection could not be enabled
     - Windows service cannot be started. Restart your computer or contact your IT administrator.

**DoH unreachable** means that the client cannot connect to any suitable DNS-over-HTTPS resolver. **DoH failed** means that the selected resolver timed out on 10 consecutive requests. Although both states share a title, their subtitles distinguish the failure.

For recommended actions and log collection, see :doc:`hos_troubleshooting`.

Windows tray notifications
--------------------------

The Home Office Security client also reports the failure reason in Windows tray notifications.

.. list-table:: Windows tray messages
   :header-rows: 1
   :widths: 30 70

   * - Condition
     - Notification
   * - DoH unreachable or DoH failed
     - Protection could not be enabled since protective resolvers cannot be reached. Please contact your IT administrator.
   * - Proxy blocked
     - Protection could not be enabled due to incorrect network proxy settings. Please contact your IT administrator.
   * - Protection service stopped
     - Protection could not be enabled since the protection service is not running. Restart your computer or contact your IT administrator.
   * - Whalebone servers unavailable
     - Protection could not be enabled since cloud services cannot be reached. Please contact your IT or security administrator.
   * - Windows service unavailable
     - Protection could not be enabled since the protection service is not responding. Restart your computer or contact your IT administrator.
   * - Resolved
     - All issues have been resolved.

Automatic resolver selection
----------------------------

The HOS client automatically connects to the **nearest Whalebone DNS cloud resolver** for the fastest possible response time. When an internal domain is detected, HOS seamlessly switches to the internal resolver, ensuring access to corporate resources without manual configuration.

Monitoring
----------

* In the Portal, view each device's group, policy, last seen timestamp, and connection state.
* Internet reachability checks use native Windows API, minimizing false "No Internet" states.

Resolver management
===================

On the **Resolvers** page, there is an overview of the created resolvers. Administrators can adjust the configuration, deploy updates, and install new resolvers.

Resolvers overview
------------------

In the main resolver overview, there are tiles with resolver details. The overview includes information about the operating system and resources, such as CPU, memory and HDD usage. There is also the status of the communication channel between the resolver and the cloud, indicated by the color-coded dot.

The resolver can be in one of these states:

* **Active**: This is the expected status in production environments and signals that everything is running correctly.
* **Resolution problem**: The resolver is unable to translate DNS requests.
* **Unavailable**: The resolver has lost connection with Whalebone Cloud. This state does not affect the DNS translation; however, the resolver cannot get threat database updates and might not respond to policy or configuration changes initiated from the portal.
* **Upgrading**: An upgrade command has been issued to the resolver. This state should not persist for more than a few minutes.
* **Not installed**: The resolver was not yet installed.

Deploy configuration
--------------------

If there have been any configuration changes that affect the DNS resolution, you have to **deploy** the configuration afterwards. Otherwise, the changes will not take effect. In case there are any configuration changes available to be deployed, there will be a **red icon** with a downward arrow visible on the resolver card. Once clicked, the webpage will ask for confirmation, and the successful deployment will be notified in the top right corner.

.. note:: If the deployment resulted in an error, try to repeat the action. The reason for the error could be a short-term communication outage between the cloud and the resolver.

The following animation demonstrates a configuration deployment to a resolver.

.. image:: ./img/lrv2-deployconfig.gif
   :align: center

Configure Policy per Network Segment
------------------------------------

Security and content polices can be assigned in a granular manner to different segments of the network.

The setting applies per resolver and can be configured under **Resolvers** → ``Name of the resolver`` → **Policy Assignment**.

.. note:: The configuration is **per resolver**. In case you want to apply the configuration to more than one resolver, please modify all the necessary resolvers.

The policies can be applied by adding IP ranges in the available input form:

Policy assignment.

.. image:: ./img/add-policy.PNG
   :align: center

In order to provide a better understanding, let's consider an example with the network range ``10.10.0.0/16``.

We have created 3 different policies:

* **Default**: the policy that we want to apply to the whole network; this is the most generic policy
* **Exception**: a policy that must be applied to a specific segment in the network, which will have all security and content filtering disabled.
* **Schools**: a policy that we want to apply to 2 different subnets that have been assigned to school environments. In this case, we have chosen to be more strict in the blocking.

Example policy settings.

.. figure:: ./img/policies-example-1.png
   :alt: Default policy
   :align: center

   Default policy

.. figure:: ./img/policies-example-2.png
   :alt: Exception policy
   :align: center

   Exception policy

.. figure:: ./img/policies-example-3.png
   :alt: Schools policy
   :align: center

   Schools policy

.. note:: The Default policy is applied to all undefined ranges. In case different policies affect the same range, the more granular policy is applied.

Let's summarize the requirements in the following matrix:

========== ===============================
**Policy** **Network**
========== ===============================
Default    10.10.0.0/16
Exception  10.10.10.0/24
Schools    10.10.20.0/24 and 10.10.40.0/24
========== ===============================

The following image shows the process of assigning the policies:

.. image:: ./img/policy_task.png
   :align: center

.. note::  After adding the networks, you must click on **Save to Resolver** in order to take effect. The changes will then be validated, and a pop-up message will provide additional information.

In order to assign additional entries to an existing assignment, a new network range can be appended using a `newline` as a separator.

Building on the previous example, in case we wanted to add the subnet ``10.10.30.0/24`` to the Exception Policy, we can simply add the subnet to the existing policy assignment:

.. image:: ./img/add-range.gif
   :align: center

Configure Blocking Pages
------------------------

In a similar manner to the Security Policies, the Blocking Pages can also be assigned to particular network ranges.

The first step is to select the **On-premise local resolver** for the **Blocking Page Location** option. Two new fields are enabled where the IPv4 and IPv6 addresses of the Blocking Pages must be filled in.

.. tip:: The Blocking Pages are being hosted **directly** on the Resolvers so the IP addresses that are advertised to the clients must be used. The clients will then be redirected to the IP address of the resolver upon blocking. Please ensure that ports 80 and 443 are accessible on the firewall.

For each IP range that is added, there is a drop-down menu for the Blocking Page that should be assigned.

.. figure:: ./img/blocking-page-assign.png
   :alt: Assign a Blocking Page to an IP range
   :align: center

   Assign Blocking Page to IP range

.. important:: The first entry in the **Policy Assignment** is considered the Default/Fallback. In case a client accesses the resolver from an undefined IP range, the respective options will apply.

.. note:: After making the necessary changes to the Blocking Page settings, please check whether the resolvers need to be redeployed.

Upgrade or Rollback a Resolver
------------------------------

When a new version of the Resolver is released, a **blue box** with the text **There is an available upgrade for resolvers. You can find it under the "Upgrade available" link** that appears on the resolvers' overview page.

.. image:: ./img/upgrade.png
   :align: center

Upon clicking the **Upgrade available** link, you are redirected to a page that provides an overview of the new upgrade, its release notes, and a button that initializes the upgrade procedure.

.. image:: ./img/upgrade-2.png
   :align: center

From this menu, the upgrade of the resolver can be initiated by clicking the **Upgrade resolver now** button.

In case the installation of the new version does not yield the expected outcome, a rollback to the previous version is possible anytime in the **Rollback** tab, which can be found in **Resolvers** → ``Name of the resolver`` → Upgrade:

.. image:: ./img/rollback.png
   :align: center

.. _header-n18:

User Management
===============

User management is located in the **User menu** > **Users**.

Under this menu, an Administrator can manage user accounts by adding, removing, editing, or disabling them. Additionally, they are presented with an overview of the last login and password change details for each account.

.. tip:: When a user is invited to join an organization and does not already have a Whalebone account, a new account is created for them, and an activation link is sent to their registered email address.

The two types of users that are supported are:

**Users**: Users whose primary account is registered with the specific organization.

**External users:** Users who belong to another organization but can be assigned a role under a different Whalebone Portal tenant, e.g., resellers.

.. tip:: Each user can be assigned one or more roles, which can be combined to shape their final role. The permissions are additive.

Below are described the different roles and the actions that they can perform.

Role Definitions
----------------

There are four main types of roles:

- **Owner**: The Owner has full access to all settings and data within the organization. This role is typically assigned to the individual who created the organization account. Moreover, this role has the exclusive ability to manage the multi-tenant structure.
- **Admin**: The Admin role has extensive permissions to manage the organization, including user management, configuration settings, and access to all data. This role has an option to enable or disable access to subtenants. If multi-tenant access is enabled, the Admin can manage users and settings across all subtenants within the organization, but cannot manage the multi-tenant structure itself.
- **Viewer**: The Viewer role has read-only access to the organization's data and settings. This role is suitable for users who need to monitor or review information without making any changes. This role has an option to enable or disable access to subtenants.
- **Special**: The Special role is designed for users who require granular permissions tailored to specific tasks. This role allows for the assignment of precise actions and access levels based on the user's responsibilities within the organization.

Special Role Permissions
------------------------

Role permissions are divided into two main categories: **Management permissions** and **View permissions**. Management permissions allow users to perform specific actions, while View permissions grant read-only access to certain data or settings.

Management permissions
----------------------

This section lists the permissions that can be assigned to users along with the actions they can perform.

Alerts admin
~~~~~~~~~~~~

- View, create, edit, and delete alerts
- Manage alert settings and configurations
- View, create, edit, and delete alert destinations

API credentials
~~~~~~~~~~~~~~~

- Create and revoke API credentials for accessing the Whalebone Portal programmatically

Blocking page editor
~~~~~~~~~~~~~~~~~~~~

- View, create, edit, and delete custom blocking pages

.. only:: Peacemaker or Immunity or DNS4GOV

    Cloud Resolvers Admin
    ~~~~~~~~~~~~~~~~~~~~~

    - Assign IP ranges to policies on cloud resolvers

DNS admin
~~~~~~~~~

- Assign IP ranges to policies on cloud resolvers
- View, create, edit, and delete on-premises DNS resolvers
- View, create, edit, and delete DNS resolution configurations for on-premises DNS resolvers
- Assign DNS resolution configurations to on-premises DNS resolvers
- Edit expert settings for on-premises DNS resolvers
- Update and rollback on-premises DNS resolver software
- View DNS resolver status and logs
- Set up device name lookup from Active Directory for on-premises DNS resolvers

.. only:: Immunity or DNS4GOV

    Home Office Security admin
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    - View, create, edit, and delete Home Office Security device groups, including assigning policies and other settings to groups
    - Delete Home Office Security devices
    - Change Home Office Security device groups for registeredclients

.. only:: Immunity or DNS4GOV

    Identity protection admin
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    - View identity protection incidents and change their status

List editor
~~~~~~~~~~~

- View, create, edit, and delete custom allow and deny lists used for filtering and blocking

.. only:: Aura or Peacemaker

    Product manager
    ~~~~~~~~~~~~~~~

    .. only:: Peacemaker

        .. warning:: This permission is available only in Peacemaker Profit.

    - View the Product dashboard with an overview of subscriptions, traffic volumes, blocking statistics, adoption trends, and forecasted growth

Reports admin
~~~~~~~~~~~~~

- Set up scheduled reports
- View saved reports

.. only:: Aura or Peacemaker

    Retail admin
    ~~~~~~~~~~~~

    .. only:: Peacemaker

        .. warning:: This permission is available only in Peacemaker Profit.

    - View retail dashboard with an overview of retail subscriptions, devices, and users
    - Manage subscriptions, devices, and users

.. only:: Aura or Peacemaker

    Retail operator
    ~~~~~~~~~~~~~~~

    .. only:: Peacemaker

        .. warning:: This permission is available only in Peacemaker Profit.

    - View retail dashboard with an overview of retail subscriptions, devices, and users
    - Manage subscriptions, devices, and users
    - View blocked threats in DNS traffic

Security policy admin
~~~~~~~~~~~~~~~~~~~~~

- View, create, edit, and delete security policies
- Manage blocking page settings, policy matching strategy, and policy assignments on on-premises DNS resolvers
- View policy assignments on cloud resolvers
- View, create, edit, and delete custom allow and deny lists used for filtering and blocking
- View DNS resolver logs

Users admin
~~~~~~~~~~~

.. warning:: This permission should be granted with caution, as it allows significant control over user accounts within the organization. If misused, users with the Users admin permission could potentially create admin accounts for themselves or others, leading to unauthorized access to sensitive data and settings.

- View, disable, and delete user accounts within the organization
- Invite new users to join the organization
- Change user roles and permissions

View permissions
----------------

Audit logs reader
~~~~~~~~~~~~~~~~~

- View audit logs for tracking changes and activities within the organization

.. only:: Peacemaker or Immunity or DNS4GOV

    Cloud Resolvers Read Only
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    - View the assignment of policies and IP ranges on cloud resolvers

List viewer
~~~~~~~~~~~

- View custom allow and deny lists and their contents used for filtering and blocking

Read all traffic (content, DNS, threats)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. only:: Peacemaker

    .. warning:: Content filtering is available only in Peacemaker Content Filtering and Peacemaker Profit.

- View all traffic data, including domains with blocked content, and detected threats

Read only - all
~~~~~~~~~~~~~~~

This permission is equivalent to the Viewer role. See the **Viewer** role description above.

Read only operations
~~~~~~~~~~~~~~~~~~~~

- View security policies and their configurations
- View DNS resolution settings for on-premises DNS resolvers
- View the allow and deny lists used for filtering and blocking
- View the configuration of blocking pages
- View the list of on-premises DNS resolvers and their statuses without access to their configurations and logs

.. only:: Aura or Peacemaker

    Retail operator without devices
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. only:: Peacemaker

        .. warning:: This permission is available only in Peacemaker Profit.

    - View retail dashboard with an overview of retail subscriptions, devices, and users
    - View blocked threats in DNS traffic

Traffic Content
~~~~~~~~~~~~~~~

.. only:: Peacemaker

    .. warning:: Content filtering is available only in Peacemaker Content Filtering and Peacemaker Profit.

- View blocked DNS requests to domains with restricted content

Traffic DNS
~~~~~~~~~~~

- View all DNS requests and responses

Traffic Threats
~~~~~~~~~~~~~~~

- View detected threats in the traffic

Users view
~~~~~~~~~~

- View user accounts within the organization
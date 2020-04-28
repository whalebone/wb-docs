.. _header-n18:

User/Organization Management
============================

User Management
---------------

The users can be managed under the respective tab on the User Menu.

Under this menu, an Administrator is able manage user accounts by
adding, removing or disabling them. Additionally they are presented with
an overview of last login and last password change details per account.

.. tip:: When a user is invited to join an organization and does not already have a Whalebone account, a new account is created for them and an activation link is being sent to their registered email address.


The two types of users that are supported are:

-  **Users**: users that have their primary account registered under the
   specific organization.

-  **External Users:** **(If available)** users that belong to another
   organization but can be assigned a role under a different Whalebone
   Portal tenant. e.g. resellers

Each user can be assigned one or more roles which can be combined
to shape their final role. Below are described the different roles and the actions that they are able to perform.

=============================== ================ =============== =================== ============= =========
**Action**                      **Read Traffic** **List Editor** **API Credentials** **Read only** **Admin**
=============================== ================ =============== =================== ============= =========
**View Threat Data**            ☑                                                    ☑             ☑
**View DNS Traffic**            ☑                                                    ☑             ☑
**View Whitelists/Blacklists**                   ☑                                   ☑             ☑
**Edit Whitelists/Blacklists**                   ☑                                                 ☑
**View Security Policies**                       ☑                                   ☑             ☑
**Edit Security Policies**                                                                         ☑
**View Resolver Configuration**                                                      ☑             ☑
**Edit Resolver Configuration**                                                                    ☑
**View API Tokens**                                              ☑                   ☑             ☑
**Generate API Tokens**                                          ☑                                 ☑
**View Network Configuration**                                                       ☑             ☑
**Edit Network Configuration**                                                                     ☑
**View Alerts**                                                                      ☑             ☑
**Edit Alerts**                                                                                    ☑
**View Reports**                                                                     ☑             ☑
**Edit Reports**                                                                                   ☑
=============================== ================ =============== =================== ============= =========

.. _header-n748:

Organization Settings
---------------------

The Organization Setting can be found under the User Menu.

.. _header-n750:

Portal Access Policy
~~~~~~~~~~~~~~~~~~~~

Portal Access Policy defines security mechanism for users accessing
Whalebone's Portal. The following settings can be configured:

-  **Allowed IP Ranges**: IPv4 or IPv6 ranges in CIDR notation, e.g.
   10.0.0.0/24 that are allowed to access Whalebone Portal.

-  **Account Lockout**: If enabled, it can limit the number of failed
   login attempts. The available options are:

   -  **Failed Login Limit**: Number of unsuccessful login attempts
      before locking the account. Default is 5.

   -  **Lockout Duration**: Time duration in minutes for disallowing
      login requests.

   -  **Lockout Reset Time**: Time duration in minutes before resetting
      the number of failed attempts.

   -  **CAPTCHA Threshold**: Number of unsuccessful login attempts
      before enabling the CAPTCHA verification.

.. _header-n766:

Password Policy
~~~~~~~~~~~~~~~

The following password setting can be configured:

-  **Expiration Time**: Number of days before a password needs to be
   changed.

-  **Password history**: Number of old passwords that cannot be reused
   when setting up a new passwords.

-  **Password Attributes**: The attributes that a new password should
   have. The attributes that a new password can have are the following:

   -  Minimum Length

   -  Number of Digits

   -  Number of lowercase characters

   -  Number of uppercase characters

   -  Number of special characters

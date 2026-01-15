Organization Settings
=====================

The Organization settings can be found under **User menu** > **Organization settings**.

Portal Access Policy
~~~~~~~~~~~~~~~~~~~~

Portal Access Policy defines the security mechanisms for users accessing Whalebone's Portal, where the following settings can be configured:

**Allowed IP ranges**: IPv4 or IPv6 ranges in CIDR notation, e.g., 10.0.0.0/24, that are allowed to access the Whalebone Portal.

**Account lockout**: If enabled, it can limit the number of failed login attempts.

**Multi-factor authentication**: Require users to use a two-factor authentication (2FA) application and enter an additional token upon logging to the portal.

The account lockout options are:

- **Failed login limit**: Number of unsuccessful login attempts before locking the account. Default is 5.
- **Lockout duration**: Time duration in minutes for disallowing login requests.
- **Lockout reset time**: Time duration in minutes before resetting the number of failed attempts.
- **CAPTCHA threshold**: Number of unsuccessful login attempts before enabling the CAPTCHA verification.

Password Policy
~~~~~~~~~~~~~~~

The following password settings can be configured:

- **Expiration time (in days)**: Number of days before a password needs to be changed.
- **Password history**: Number of old passwords that cannot be reused when setting up a new password.
- **Minimal length**: Minimum length of the password
- **Digits**: Number of digits in the password
- **Special characters**: Number of special characters in the password
- **Lowercase**: Number of lowercase characters in the password
- **Uppercase**: Number of uppercase characters in the password

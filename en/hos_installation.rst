Installation
============

Before you begin
----------------

* Ensure access to the **Whalebone Portal**.
* Confirm network access on TCP 443.
* If rolling out to multiple users, prepare your **MDM** or **Active Directory** environment.

Portal configuration
--------------------

1. Log in to the **Whalebone Portal**.

2. Navigate to **Home Office Security**, located in the menu under the user icon in the upper-right corner of the screen.

    .. image:: ./img/hos-sbs-1.png
        :align: center

3. Verify or create a **Device Group** using the **+ Add device group** button.

    .. image:: ./img/hos-sbs-2.png
        :align: center

4. Device group configuration options:
    
      * **Name:** identifiable label, e.g., Default Group.
    
      * **Policy:** select your preferred security policy.
    
      * **Blocking page:** define which blocking template to display.
    
      * **Domain exceptions:** enter domains that should bypass protection.
    
      * **Disable HOS inside corporate network:** optional; define:
        
          * *Internal Domain*: the queried domain that is reachable only from the internal network.
          * *Expected Response*: value returned when inside the network.
          * *Query Type*: A / AAAA / TXT record, matching your DNS configuration.

5. Click **Add** to save the group.

    .. image:: ./img/hos-sbs-3.png
        :align: center

Unattended Installation (Windows 64-bit)
----------------------------------------

1. Select the target group to which you want to add the newly installed client by clicking the **Install to group** button to download the application and display the installation commands.

2. Download the required installation file.

3. Copy the installation command from the Portal, for example:
    
    .. code-block:: bash

        msiexec /i "Whalebone.Home.Office.Security.Installer.msi" TOKEN="12345678-1234-1234-1234-123456789012" REGION="eu-01"

4. Use your preferred MDM to distribute the application to users by creating a new deployment with the command copied from the Portal.

Uninstallation
--------------

.. code-block:: bash

    msiexec /x "Whalebone.Home.Office.Security.Installer.msi"


GUI Installation (Windows 64-bit)
---------------------------------

1. Select the target group to which you want to add the newly installed client by clicking the **Install to group** button to download the application and display the installation commands.

2. Download the required installation file.

3. Double-click the downloaded MSI file to execute it.

4. Enter the pairing token that you can find on the Portal into the installer's window. For example:
    
    .. code-block:: text

      aG9zLmFwcDovL2F1dGg/dG9rZW49MTIzNDU2NzgtMTIzNC0xMjM0LTEyMzQtMTIzNDU2Nzg5MDEyJnJlZ2lvbj1ldS0wMQ==

Manual Installation (Android / iOS)
-----------------------------------

* Select the target group to which you want to add the newly installed client by clicking the **Install to group** button, which displays download links and the activation QR code.
* Send the link and the QR code to users.
* Users will install the app and be prompted to scan the QR code to complete the installation process.

Post-installation verification
------------------------------

The device appears in the **Portal → Home Office Security → Devices** list after successful registration.
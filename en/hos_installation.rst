
*************************
Step by step installation
*************************


To install HOS on device you need to configure it first. Open `Whalebone Portal` web page and use (1) `User menu` to navigate to (2) `Home Office Security`.

.. image:: ./img/hos-sbs-1.png
    :align: center


A Default Device group should already exist. If not, create one by clicking the (3) a `+ Add device group` button.

.. image:: ./img/hos-sbs-2.png
    :align: center


* **Name**: This should clearly identify the device group to differentiate it from others. If you only use one, you may leave its name as Default Group. 
* **Policy**: corresponds to the policies you create in the Configuration menu. It is a set of rules that instructs how to operate. Based on policy the device or the local/cloud resolver decides what to during DNS resolution. This set of rules persist on the device and is updated initially and later synchronized. Because of this Portal provides monitoring of these devices.
* **Blocking page**: corresponds to the blocking pages you create in the Configuration menu. 
* **Domain exceptions**: HOS service will not divert any DNS queries that contain question for domain on the exception list. E.g. when ``example.com`` is specified, the DNS request will be resolved as usual on the resolver configured by operating system. A same rule applies for question ``subdomain.example.com``.
* **Automatic upgrade**: When this configuration option is checked, HOS application on Windows will update to latest production version when a newer version is available to download. This option takes effect on Windows only, on mobile upgrades are performed by the vendor ecosystem.

.. warning:: Please note that two settings mentioned above (Automatic upgrade and Domain exception) are featured in version 2.10.0 for Windows only. If you are running earlier version, please update to 2.10.0 manually.

When you're done, click (4) `Add` button to create this group.

HOS may become inactive when it detects that device is connected to secure network. 

.. image:: ./img/hos-sbs-3.png
    :align: center


Click (5)  `Install to group` button to see installation instructions and/or get download link to the HOS installer.

.. image:: ./img/hos-sbs-4.png
    :align: center


If you haven't already download the installer (6). While the installer is being downloaded please copy the installation command to clipboard (7). 
To install or Update:

.. code-block:: shell

    msiexec /i "Whalebone.Home.Office.Security.Installer.msi" TOKEN="60d5806e-07fe-432a-a4ad-7797d82782b3"

Uninstall:

.. code-block:: shell

    msiexec /x "Whalebone.Home.Office.Security.Installer.msi

.. image:: ./img/hos-sbs-5.png
    :align: center


Find the folder where the installer is located. It should be file named `Whalebone.Home.Office.Security.Installer.msi`.

Open up a command prompt, change directory to the folder where is the installer and paste (8) the command with your mouse (right click). Execute the command. This requires admin priviledges.

Installer will end prematurely with error when executed without token argument.

.. image:: ./img/hos-sbs-6.png
    :align: center

.. Tip:: The installer has very minimal UI. If there was no error message, consider the installation successful.

.. image:: ./img/hos-sbs-7.png
    :align: center

Device is now visible in the Whalebone Portal web page. 



******************************
Home Office Security Overview
******************************

Whalebone Home Office Security (HOS) provides an off-network DNS filtering functionality for desktop and mobile devices. It intercepts DNS traffic and inspects it before sending network packets to the wild. 
It protects the device from network threat by scanning every DNS packet. At the moment, Windows, Android and iOS devices are supported. For detailed OS version support, see below.

.. image:: ./img/hos-overview.png
    :align: center

HOS comes with Windows Installer for the deployment. No user interaction is required to perform the installation, however the installer requires a ``token``. The default target directory is:
``C:\Program Files (x86)\Whalebone\Home Office Security\``

For Android the default install location is:
``/storage/emulated/0/Android/io.whalebone.securedns.corp/``

Supported OS
====================

================ =================================== ========================== ================== =============== ===============
Windows Desktop  Windows Server                      Android                    iOS and iPadOS     MacOS           Linux
================ =================================== ========================== ================== =============== ===============
☐ Windows XP     ☐ Windows 2000                      ☑ Android 5 and higher    ☑ all versions    Not supported   Not supported
☐ Windows Vista  ☐ Windows 2003, Windows 2003 R2     ☐ Android 4.4 and lower    
☑ Windows 7      ☐ Windows 2008, Windows 2008 R2  
☑ Windows 8      ☑ Windows 2012, Windows 2012 R2  
☑ Windows 8.1    ☑ Windows 2016                   
☑ Windows 10     ☑ Windows 2019                   
☑ Windows 11                                                                                           
================ =================================== ========================== ================== =============== ===============

Windows 7 systems must be up-to-date or at least have KB3033929 installed.

Windows Server 2016 systems must have secure boot disabled.



Uninstalling a local resolver
=============================

In order to uninstall a resolver and remove all Whalebone configuration files the following steps should be followed:

.. warning:: Before starting the process it should be noted that all the individual components that support the resolver functionality are being executed as docker containers. Steps 1 and 2 apply only in case the host server is **dedicated** and **no other services** are running as containers. Should the situation be different, please contact us and we will provide an up to date list of the containers that should be removed.

1. **Stop and remove all the running docker containers**:

   .. code::

   		docker rm -f lr-agent && docker rm -f $(docker ps -q)

2. **Uninstall Docker**:

   Please follow the instructions for the applicable operating system:

   -  `CentOS <https://docs.docker.com/install/linux/docker-ce/centos/#uninstall-docker-engine---community>`__

   -  `Red Hat <https://docs.docker.com/install/linux/docker-ce/centos/#uninstall-docker-engine---community>`__

   -  `Debian <https://docs.docker.com/install/linux/docker-ce/debian/#uninstall-docker-engine---community>`__

   -  `Ubuntu <https://docs.docker.com/install/linux/docker-ce/ubuntu/#uninstall-docker-engine---community>`__

3. **Remove all resolver configuration files and related data**:

   .. code:: 

      rm -rf /etc/whalebone 
      rm -rf /var/whalebone
      rm -rf /var/lib/kres


4. **Remove DNS traffic and incidents logs**:
    If you want to fully uninstall the resolver including the logs from DNS traffic and incidents, delete also the log folder.
    If your intention is just to re-install the resolver but keep the logs, you can skip this step.
    
    .. code::     
      rm -rf /var/log/whalebone

    
API Integration
------------
Whalebone API is a practical way to access all the data that are gathered by Whalebone's resolvers and integrate them to external systems. 
The API documentation has two separate schemas. One for getting the events from Whalebone and one for getting and configuring the settings. 

#. If you want to retrieve incidents, DNS traffic data and resolver metrics use this schema: https://apidocs.whalebone.io/public/

#. If you want to configure the resolver, update policies, add domains to allow/deny lists or get the settings, use this schema: https://portal.whalebone.io/api/public/v1/doc  

In order to authenticate to the API, every user needs a set of `Access Key` and `Secret Key`. These can be managed from the option `API keys` on the dropdown menu, under the user's account.

You can watch step-by-step video guide `here <https://docs.whalebone.io/en/latest/video_guides.html#api>`__

   
* **API Key Generation**

The generation of the API key can be achieved by clicking the `Generate new key` button.

.. comment :: .. image:: ./img/key-generation.gif
.. comment ::    :align: center

.. note:: Make sure to copy the `Key secret` as it cannot be retrieved again.

* **API Key Revocation**

In case an API key gets lost or compromised, its revocation can be achieved  by the same menu by clicking the red trash bin icon.
Every key is tightly-coupled with the user ID and there is no central key management. In order to invalidate a key that you do not have access to, the respective user needs to delete the key himself or the entire user must be deleted.

.. comment :: image:: ./img/key-revocation.gif
.. comment ::   :align: center
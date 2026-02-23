Content
=======

The **Content** tab shows an overview of blocked domains subject to content filtering settings. If you do not have the content filter enabled or are not using it, nothing will be logged in this tab. There are 18 categories to choose from, including ``Sexual Content``, ``Gambling``, ``Audio/video``, or ``Games``.

Filtering Options
~~~~~~~~~~~~~~~~~

The Filter button contains different options based on the type of data being analyzed. Here are the available options for each data type:

* **Client IP**: Filter the data based on specific client IP addresses.
* **Device ID**: Filter the data based on specific device IDs.
* **Domain**: Filter the data based on specific domain names.
* **Content category**: Filter the data based on specific content categories (e.g., Sexual Content, Gambling, Audio/video, Games).
* **Legal**: Filter the domains blocked by regulatory restrictions.
* **Resolver ID**: Filter the data received by specific resolvers.

.. only:: Immunity or DNS4GOV

  .. tip:: The device ID has been assigned by the Home Office Security client installed on the device. The list of devices is in the **Home Office Security** section of the portal, which is located in the user menu.

.. only:: Aura or Peacemaker

  .. tip:: The device ID has been assigned by the customer using the Retail API. The list of devices is in the **Retail** section of the portal.

Domain Categorization Change
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In case of a domain categorized incorectly you can check which categories a domain falls into by using the **Domain Analysis** tool located in the user menu. After entering a domain, the **Content Categorization** section will appear, showing the categories the domain falls into and also offering a **Suggest Category Change** button to suggest a change in categorization. It is also possible to report a domain as a false negative using the **Report as malicious** button.

CSV Export
~~~~~~~~~~

The CSV data contains the following details:

* date
* client's IP address
* device name
* domain
* content category type

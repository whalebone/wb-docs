******************
End user dashboard
******************

Whalebone also provides web UI for the end users. This is usually done in an environment, where ISP or Telco allows customers to configure the security service. UI is fully customizable and can be whitelabeled by the service provider. The integration is done by Whalebone specialists directly with cooperation of the service provider team.


Integration requirements
========================

There are three four main points of integration of the Whalebone security service with the existing infrastructure and services.

* **DNS resolvers user awareness**

  * Usually done through gathering of authentication audit (e.g. RADIUS)
  * Static IP x User assignemnts are supported and are delivere through API integration (see below)
  * Other authentication services and methods are supported on request

* **End user dashboard**

  * Simple UI to provide the user with configuration and reporting options
  * Authentication through Single sign-on from the service provider existing interface
  * Fully customizable to follow the look and feel of the service provider

* **Blocking page**
  
  * Simple UI to inform the user about the security incident
  * Fully customizable to follow the look and feel of the service provider
  * Optional Bypass button to allow the user to continue to the destination website

* **API integration**
  
  * Whalebone offers API to receive calls about subscribed and unsubscribed users
  * Whalebone is able to send API calls containing user alerts and reports

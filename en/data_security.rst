Data Security
=============

Data security is a critical aspect of any software application, and it is especially important for applications that handle sensitive data. In this section, we will discuss which data Whalebone collects, how it is stored, and how it is protected.

Any data processed by Whalebone is used solely to provide the service to the customer and to improve service quality. Whalebone uses the data as input to machine learning and detection engines to improve detection across the entire customer base, but no specific data is shared with other customers. Completely anonymized datasets (all identifiable attributes are removed and IP addresses are scrambled with a one-way encryption function) could be shared with chosen research institutes cooperating on research with Whalebone under strict NDA. The datasets are not sold or disclosed to third parties and privacy is a major cornerstone of Whalebone's business.

DNS Requests
------------

Whalebone collects DNS requests made by devices on the network. This data is used to identify potential threats and to provide insights into network activity. The DNS requests are stored in a secure database that is protected by encryption and access controls.

The following details are stored for each DNS request:

- Timestamp: The date and time when the DNS request was made.
- Source IP: The IP address of the device that made the DNS request. In case of complex network topologies, this may be the IP address of a network gateway or proxy server.
- Query: The domain name that was requested.
- Level 2 domain: The second-level domain extracted from the query, which can be used for categorization and analysis.
- Response: The response received for the DNS request, which may include the resolved IP address or an error message.
- Device ID: A unique identifier for the device that made the DNS request, if available.
- DNS query class: The class of the DNS query (e.g., IN for Internet).
- DNS query type: The type of the DNS query (e.g., A, AAAA, CNAME).
- Time-to-live (TTL): The TTL value associated with the DNS response, which indicates how long the response is valid.
- Protocol: The protocol used for the DNS request (e.g., UDP, TCP, DNS over HTTPS).
- EDE code: The Extended DNS Error code, if applicable, which provides additional information about the DNS response.
- Organization name: The name of the organization associated with the DNS request.
- Geolocation: The geographical location associated with the source IP address, if available.
- Server IP: The IP address of the DNS server that processed the request.
- Resolver ID: A unique identifier for the DNS resolver that processed the request.

Data At Rest
------------

All data is stored in a secure database that is protected by encryption and access controls. The database is regularly backed up to ensure that data can be recovered in the event of a disaster. Access to the database is restricted to authorized personnel only, and all access is logged and monitored.

Data In Transit
---------------

All data transmitted between clients and Whalebone infrastructure is encrypted using industry-standard protocols such as TLS. This ensures that data is protected from interception and tampering while in transit. Additionally, Whalebone uses secure APIs for communication between different components of the system, and all API endpoints are protected with authentication and authorization mechanisms to prevent unauthorized access.

Endpoint protection:

- Admin Portal: HTTPS with at least TLSv1.2 encryption, role-based access control, and optional multi-factor authentication.
- API Endpoints: HTTPS with at least TLSv1.2 encryption, API key authentication, and rate limiting to prevent abuse.
- Communication between on-premises components and cloud infrastructure: HTTPS with TLSv1.3 encryption, mutual TLS authentication, and strict access controls to ensure secure communication between on-premises components and cloud infrastructure.
- DNS over UDP: DNS requests sent over UDP are protected using DNSSEC to ensure the integrity and authenticity of the data. This protocol does not support data encryption.
- DNS over TCP: DNS requests sent over TCP are protected using DNSSEC to ensure the integrity and authenticity of the data. This protocol does not support data encryption.
- DNS over HTTPS (DoH): DNS requests sent over HTTPS are encrypted using TLSv1.3, providing confidentiality and integrity for the data in transit.
- DNS over TLS (DoT): DNS requests sent over TLS are encrypted using TLSv1.3, providing confidentiality and integrity for the data in transit.
- [EXPERIMENTAL FEATURE] DNS over QUIC (DoQ): DNS requests sent over QUIC are encrypted using TLSv1.3, providing confidentiality and integrity for the data in transit.

Data Retention
--------------

Whalebone retains live data for 3 months and backups for 6 months. The data is automatically deleted after the retention period expires, and all backups are securely deleted as well. Users can also request the deletion of their data at any time, and Whalebone will comply with such requests in accordance with applicable laws and regulations.
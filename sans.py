sample_encryption_policy = """
1. Overview
See Purpose.
2. Purpose
The purpose of this policy is to provide guidance that limits the use of encryption to those
algorithms that have received substantial public review and have been proven to work
effectively. Additionally, this policy provides direction to ensure that Federal regulations are
followed, and legal authority is granted for the dissemination and use of encryption technologies
outside of the United States.
3. Scope
This policy applies to all <Company Name> employees and affiliates.
4. Policy
4.1 Algorithm Requirements
4.1.1 Ciphers in use must meet or exceed the set defined as "AES-compatible" or
"partially AES-compatible" according to the IETF/IRTF Cipher Catalog, or the
set defined for use in the United States National Institute of Standards and
Technology (NIST) publication FIPS 140-2, or any superseding documents
according to the date of implementation. The use of the Advanced Encryption
Standard (AES) is strongly recommended for symmetric encryption.
4.1.2 Algorithms in use must meet the standards defined for use in NIST publication
FIPS 140-2 or any superseding document, according to date of implementation.
The use of the RSA and Elliptic Curve Cryptography (ECC) algorithms is
strongly recommended for asymmetric encryption.
4.1.3 Signature Algorithms
Algorithm Key Length
(min)
Additional Comment
ECDSA P-256 Consider RFC6090 to avoid patent
infringement.
RSA 2048 Must use a secure padding scheme. PKCS#7 
SANS Institute 2014 – All Rights Reserved Page 2
Consensus Policy Resource Community
padding scheme is recommended. Message
hashing required.
LDWM SHA256 Refer to LDWM Hash-based Signatures Draft
4.2Hash Function Requirements
In general, <Company Name> adheres to the NIST Policy on Hash Functions.
4.3 Key Agreement and Authentication
4.3.1 Key exchanges must use one of the following cryptographic protocols: DiffieHellman, IKE, or Elliptic curve Diffie-Hellman (ECDH).
4.3.2 End points must be authenticated prior to the exchange or derivation of session
keys.
4.3.3 Public keys used to establish trust must be authenticated prior to use. Examples
of authentication include transmission via cryptographically signed message or
manual verification of the public key hash.
4.3.4 All servers used for authentication (for example, RADIUS or TACACS) must
have installed a valid certificate signed by a known trusted provider.
4.3.5 All servers and applications using SSL or TLS must have the certificates signed
by a known, trusted provider.
4.4 Key Generation
4.4.1 Cryptographic keys must be generated and stored in a secure manner that prevents
loss, theft, or compromise.
4.4.2 Key generation must be seeded from an industry standard random number
generator (RNG). For examples, see NIST Annex C: Approved Random Number
Generators for FIPS PUB 140-2.
5. Policy Compliance
5.1 Compliance Measurement
The Infosec team will verify compliance to this policy through various methods, including but
not limited to, business tool reports, internal and external audits, and feedback to the policy
owner. 
SANS Institute 2014 – All Rights Reserved Page 3
Consensus Policy Resource Community
5.2 Exceptions
Any exception to the policy must be approved by the Infosec team in advance.
5.3 Non-Compliance
An employee found to have violated this policy may be subject to disciplinary action, up to and
including termination of employment.
6 Related Standards, Policies and Processes
National Institute of Standards and Technology (NIST) publication FIPS 140-2,
NIST Policy on Hash Functions
"""

sample_encryption_policy_2 = """
1. 0 Purpose
To provide our members a template that can be modified for your company’s use in developing an
Enterprise Encryption Policy. This policy template and the procedures it encompasses are to ensure
the confidentiality and integrity of your company’s information through the implementation of
cryptographic controls.
2.0 Scope
Define the scope covered in the policy. Our recommendations for this section are delineated below.
This policy covers all of our company’s information, systems, networks, and other information assets
to ensure adequate controls are in place to ensure the confidentiality, integrity and availability of our
data. These critical assets must be managed and controlled to protect our company from loss due to
misuse, disclosure, fraud, or destruction.
This policy applies to all company employees, temporary employees, contractors, consultants,
vendors, service providers, partners, affiliates, third parties or any other person or entity
authorized to utilize our information resources. This includes all information systems, hardware,
software, data, media, and paper files at our company and any approved third-party facilities.
This policy also pertains to all systems, networks, and users connected to our company resources
through any means, including but not limited to: local access, leased lines, wireless access
points, or any other telecommunications device, through either private or public networks. It also
applies to all third-party local and remote connections as well as non-company assets involved in
the storage, processing, or transmission of company’s information or data.
3.0 Policy
A. Cryptographic Controls - this section covers the use of cryptography to encrypt sensitive data. The
recommended text includes:
Cryptographic controls must be utilized for sensitive information classified by our company as
{PROTECTED} or {RESTRICTED} including, but not limited to: Personally Identifiable Information (PII),
Protected Health Information (PHI), credit card numbers, passwords, intellectual property (define),
budget or contract proposals, legal correspondence and research and development information.
(Define your list of critical data). All encryption mechanisms utilized by our company must be
authorized by the appropriate authority.
Users must not attempt to utilize any form of cryptography, including, but not limited to, encryption,
digital signatures, and digital certificates, which has not been approved and installed/implemented by
Version 1.0 Date: 10/5/2019
Encryption Policy Template
Version 1.0 Date: 10/5/19
our designated representative (maybe an outside consultant, define who this is). The use of all encryption
mechanisms must meet relevant regulatory and legal requirements, including any import/export
requirements and use of cryptography in other countries. Define the recommended encryption methods -
such as AES-128, RSA, Bitlocker, or ECC.
B. Key Management (if applicable) - Define the scope of your key management system. Suggested text
includes:
All encryption keys must be managed using a commercially available key management system. The key
management system must ensure that all encryption keys are secured and there is limited access to
company personnel. Master keys and privileged access to the key management system must be granted to
at least two administrators. Keys generated by the key management system must not be easily discernible
and easy to guess. When keys are transmitted to third party users, the encryption key must be transmitted
over a different communication channel than the data that has been encrypted. All key recovery operations
must be authorized and all activities must be logged by the key management system. All logged activities
must be periodically reviewed (state how often and by whom) of the company.
C. Network Encryption - Define how transmission of sensitive data is handled. Suggested text follows.
All sensitive information classified by our company as PROTECTED or RESTRICTED including, but not limited
to, PII, PHI, credit card numbers, passwords, and research and development information, must be encrypted
when transmitted outside of our company. This includes transmission of information via email or other
communication channels. Remote management activities for our company, such as contractors accessing
our network remotely, must consistently employ session encryption. Define remote access procedures such
as using VPN to access corporate systems while teleworking.
D. Hard Disk Encryption - Define how sensitive data is encrypted at rest. Suggested text follows.
All sensitive information classified by our company as PROTECTED or RESTRICTED including, but not limited
to PII, PHI, credit card numbers, and passwords, must be encrypted. When feasible, hardware
encryption must be utilized over software encryption. It is our company’s policy to use laptops and desktops
that have encrypted hard drives - or use Apple’s FileVault - a built-in disk encryption feature.
4.0 Roles and Responsibilities
A. Responsible Parties. Define roles and responsibilities in this section, sample text below.
Our company’s leadership and management team are responsible for maintaining and enforcing the
policies, standards and guidelines established within this document. Employees, contractors, vendors,
service providers, partners, affiliates, and third parties are responsible for ensuring all actions are in
accordance with our management policies and objectives.
Encryption Policy Template
All users are required to sign our company’s Acceptable Use Policy and acknowledge they understand and
will abide by the standards and individual responsibilities it defines. All changes to the Acceptable Use Policy
are communicated to all staff, contractors and other third parties in a timely fashion.
B. Ownership
All IT policies, standards, and guidelines are owned, established and managed by the CIO (or equivalent
authority) within our company.
C. Communication
All policies, standards and guidelines are available for reference to all company users. The availability of this
program will also be communicated to all users annually.
D. Policy Review and Maintenance
This document will be updated upon any material change to the company and its employees in timely
fashion.
5.0 Compliance
All users must comply with our company’s corporate policies. Any user found to be abusing the privilege of
using our corporate assets and access to business systems, or not in compliance with any of these policies,
may be subject to disciplinary action, up to and including termination of employment.
6.0 Applicability
A. This policy is applicable to all company employees working both on site and remotely"""

cloud_security_alliance_encryption = "https://raw.githubusercontent.com/cloudsecurityalliance/CSA-Guidance/master/Domain%2011-%20Data%20Security%20and%20Encryption.md"
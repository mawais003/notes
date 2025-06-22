# ISC2

There are 5 domains in it.

1. 
2. 
3. 
4. 
5. 

## 1. Security Principles

- CIA Triad (Confidentiality, Integrity and Availability)

    - Confidentiality relates to authorized access to certain information for authorized users while safeguarding the data breaches.
    - Integrity means keeping the data in usefullness state for the purpose this is meant to use.
    - Availibality refers to the presence of information for users at the time of their need.

- Security and Privacy

    - Security refers to securing the user's data and informations.
    - Privacy specifically refers to not keeping in view the users privacy, their data shouldn't be misued or their identity not disclosed.
        - EU enacted it as GDPR (General Data Protection Regulation) in 2016 in EU.

- Compenents of Threat
    - threat actor : refers to the target of threat
    - threat vector : is the approach using which threat reaches the threat actor
    - more vulnerable : easy targets of threats

> Risk Management Terminologies

1. An asset
is something in need of protection.
2. A vulnerability
is a gap or weakness in those
protection efforts.
3. A threat
is something or someone that
aims to exploit a vulnerability to
thwart protection efforts.

HIPA - 1996 - US

> 3 types of Security Controls

1. Physical Control

Physical controls address security needs using physical hardware devices, such as badge readers, architectural features of buildings and facilities, and specific security actions taken by staff.

They typically provide ways of controlling, directing, or preventing the movement of people and equipment throughout a specific physical location, such as an office suite, factory, or other facility.

Physical controls also provide protection and control over entry onto the landsurrounding the buildings, parking lots, or other areas within the organization’s control. In most situations, physical controls are supported by technical controls as a means of incorporating them into an overall security system.

Visitors and guests accessing a workplace, for example, must often enter the facility through a designated entrance and exit, where they can be identified, their visit’s purpose assessed, and then allowed or denied entry. Employees would enter, perhaps through other entrances, using company-issued badges or other tokens to assert their identity and gain access.

2. Technical Controls

Technical controls (also called logical controls) are security controls that computer systems and networks
directly implement.

These controls can provide automated protection from unauthorized access or misuse, facilitate detection of
security violations, and support security requirements for applications and data.

Technical controls can be configuration settings or parameters stored as data, managed through a software graphical user interface (GUI), or they can be hardware settings done with switches, jumper plugs or other means.
 
However, the implementation of technical controls always requires significant operational considerations and should be consistent with the management of security within the organization.
 
3. Administrative Controls

Administrative controls (also known as managerial controls) are directives, guidelines, or advisories aimed at the people within the organization. They provide frameworks, constraints, and standards for human behavior and should cover the entire scope of the organization’s activities and its interactions
with external parties and stakeholders.
 
Administrative controls can and should be powerful, effective tools for achieving information security. Even the simplest security awareness policy can be an  effective control if it is implemented through systematic training and practice.

Many organizations are improving their overall security posture by integrating their administrative controls into the task-level activities and operational decision processes that their workforce uses throughout the day. This can be done by providing them as in-context ready references and advisory resources or by linking them directly into training activities.

These and other techniques bring the policies to a more neutral level and away from the decision-making of only the senior executives. It also makes them immediate, useful, and operational on a
daily and per-task basis.

These require technical controls to integrate the badge or token readers, door release mechanisms, and identity management and access control systems into a more seamless security system.


> Professional Code of Conduct

>> ISC2 Code of Ethics Preamble

The Preamble states the purpose and intent of the ISC2 Code of Ethics.

- The safety and welfare of society and the common good, duty to our principles, and duty to each other require that we adhere and be seen to adhere to the highest
ethical standards of behavior.
- Therefore, strict adherence to this Code is a condition of certification.

>> ISC2 Code of Ethics Canons

The Canons represent the important beliefs held in common by the members of ISC2. 
Cybersecurity professionals who are members of ISC2 have a duty to the following four entities in the Canons.

1. Protect society, the common good, necessary public trust and confidence, and the infrastructure.
2. Act honorably, honestly, justly, responsibly, and legally.
3. Provide diligent and competent service to principles.
4. Advance and protect the profession.

> Governance Elements

Regulations, Standards, Policies, and Procedures: These are interconnected concepts that guide an organization's actions. Regulations are laws created by governments, which lead to the development of standards, policies, and procedures.

- **Governance** refers to the system of rules, practices, and processes by which an organization is directed and controlled. It involves decision-making, setting policies, and ensuring compliance.

1.  Regulations and Laws: Regulations and laws are created by governments to enact public policy. Examples include HIPAA, GDPR, and ISO standards.

2.  Standards: Standards provide a framework for introducing policies and procedures in support of regulations. Organizations may adopt multiple standards as part of their information systems security programs.

3. Policies: Policies are broad statements that provide guidance and direction. They are informed by applicable laws and regulations and specify which standards and guidelines the organization will follow.

4. Procedures: Procedures are detailed, step-by-step instructions that support policies. They define the explicit, repeatable activities necessary to accomplish a specific task or set of tasks.

Examples of Standards and Regulations: Examples include HIPAA, GDPR, ISO standards, NIST standards, and IETF standards.

## 2. Incident Response, Business Continuity and Disaster Recovery Concepts

### Incident Terminology

> Breach

The loss of control, compromise, unauthorized disclosure, unauthorized acquisition, or any similar occurrence where:a person other than an authorized user accesses or potentially accesses personally identifiable information; or an authorized user accesses personally identifiable information for other than an authorized purpose. *NIST SP 800-53 Rev. 5*

> Event

Any observable occurrence in a network or system. *NIST SP 800-61 Rev 2*

> Exploit

A particular attack. It is named this way because these attacks exploit system vulnerabilities.

> Incident

An event that actually or potentially jeopardizes the confidentiality, integrity or availability of an information system or the information the system processes, stores, or transmits.

> Introsuion

A security event, or combination of events, that constitutes a deliberate security incident in which an intruder gains, or attempts to gain, access to a system or system resource without authorization. *IETF RFC 4949 Ver 2*

> Threat

Any circumstance or event with the potential to adversely impact organizational operations (including mission, functions, image, or reputation), organizational assets, individuals, other organizations, or the nation through an information system via unauthorized access, destruction, disclosure, modification of information, and/or denial of service. *NIST SP 800-30 Rev 1*

> Vulnerability

Weakness in an information system, system security procedures, internal controls, or implementation that could be exploited by a threat source. *NIST SP 800-30 Rev 1*

> Zero Day

A previously unknown system vulnerability  with the potential of exploitation without risk of detection or prevention because it does not, in general, fit recognized patterns, signatures, or methods.

### The Goal of Incident Response

The priority of any incident response is to protect life, health, and safety.  When any decision related to priorities is to be made, always choose safety first.

An event is any measurable occurrence, and most events are harmless. However, if the event has the potential to disrupt the business’s mission, then it is called an incident. Every organization must have an incident response plan that will help preserve business viability and survival.

The incident response process is aimed at reducing the impact of an incident so the organization can resume the interrupted operations as soon as possible.

Incident response planning is a subset of the greater discipline of business continuity management (BCM).


> Concept of "Red Book"

The business continuity plan needs to be maintained somewhere where it can be accessed often in modern organizations, everything is digital and not provided as a hard copy. This can be dangerous just like storing everything within the main company building. Some organizations have what is called the **red book**, which is given to the appropriate individual outside the facility. All the procedures are outlined in that document in case for example, a hurricane hits the power is out and all the facilities are compromised and there is no access to electronic backups. It is important to update this hard copy red book any time the electronic copy is updated. So both versions remain consistent.

### Components of a Business Continuity Plan

Business continuity planning (BCP) is the proactive development of procedures to restore business operations after a disaster or other significant disruption to the organization.

The term business is used often, as this is mostly a business function as opposed to a technical one. However, in order to safeguard the confidentiality, integrity, and availability of information, the technology must align with the business needs.

- List of the BCP team members, including multiple contact methods and backup members
- Guidance for management, including designation of authority for specific managers
- Contact numbers for critical members of the supply chain (vendors, customers, possible external emergency providers, third-party partners)
- How/when to enact the plan 
- Immediate response procedures and checklists (security and safety procedures, fire suppression procedures, notification of appropriate emergency- response agencies, etc.)
- Notification systems and call trees for alerting personnel that the BCP is being enacted.

EXHIBIT D
INFORMATION SECURITY REQUIREMENTS

to the Software License and Hosted Services Agreement (Agreement Reference AHT-ORR-0224) between Ambry Health Technologies, Inc. and Orrinfield Health System, Inc.

Capitalized terms not defined here have the meanings given in the Agreement.

D.1 Security Program

D.1.1 Ambry will maintain a written information security program with administrative, technical and physical safeguards appropriate to the sensitivity of Patient Data, reviewed at least annually by Ambry's Chief Information Security Officer.

D.1.2 Ambry will maintain a SOC 2 Type II report covering the Services and will provide the most recent report to Customer each year within 30 days after it is issued.

D.1.3 Customer Data will be encrypted in transit using TLS 1.2 or higher and at rest using AES-256.

D.2 Access Control

D.2.1 Ambry personnel will access Customer Data only as needed to provide support, maintain the Services or comply with law, using named accounts protected by multi-factor authentication.

D.2.2 Ambry will review privileged access quarterly and will remove access within 24 hours after an employee's role changes or employment ends.

D.2.3 The Portal will support Customer's single sign-on for Authorized Users and will enforce multi-factor authentication for Patient Users who enable proxy access.

D.3 Vulnerability Management

D.3.1 Ambry will engage an independent firm to perform a penetration test of the Portal and App at least annually and will share an executive summary with Customer.

D.3.2 Critical vulnerabilities will be remediated within 7 days, high within 30 days, and medium within 90 days after identification.

D.4 Security Incidents

D.4.1 "Security Incident" means any actual or reasonably suspected unauthorized access to, acquisition of, or use, disclosure, modification or destruction of Customer Data, or any compromise of the systems that store it.

D.4.2 Ambry will notify Customer of a Security Incident as soon as practicable and in all cases within 72 hours after Ambry becomes aware of it. Notice will be given by telephone to Customer's security operations center and in writing to privacy@orrinfield.example and security@orrinfield.example. Ambry will not delay notice in order to complete its investigation.

D.4.3 The initial notice will include, to the extent then known, a description of the incident, the categories and approximate number of patients affected, containment actions taken, and a point of contact. Ambry will provide written updates at least every 3 days until the incident is resolved and a final report within 20 days after resolution.

D.4.4 Ambry will preserve relevant logs and evidence, cooperate with Customer's investigation and any law enforcement inquiry, and will not notify patients or regulators about an incident involving Customer Data without Customer's prior written approval, unless required by law.

D.5 Subprocessors

D.5.1 Ambry may use subprocessors to host the Services, send SMS and email notifications, and provide customer support tooling. Ambry remains responsible for each subprocessor's performance.

D.5.2 Ambry maintains the current list of subprocessors, with each one's function and processing location, in the Ambry Customer Trust Center at https://trust.ambryhealth.example/subprocessors. The list is available to Customer's administrators at all times without a request.

D.5.3 Ambry will give Customer written notice at least 30 days before authorizing a new subprocessor, or replacing an existing one, to process Patient Data. If Customer reasonably objects on data protection grounds within that 30 day period, Ambry will either not use that subprocessor for Customer Data or permit Customer to terminate the affected Services and receive a refund of prepaid fees for the remaining Term.

D.5.4 Each subprocessor will be bound by written obligations at least as protective as this Exhibit D and the Business Associate Agreement.

D.6 Business Continuity

D.6.1 Ambry will maintain a disaster recovery plan with a recovery time objective of 4 hours and a recovery point objective of 15 minutes for the Portal and test it at least annually.

D.6.2 Backups will be performed at least daily and retained for 14 days on a rolling basis during the Term.

D.7 Audit

Once per contract year, and after any Security Incident, Customer or its independent auditor may assess Ambry's compliance with this Exhibit D on 30 days notice, during business hours and subject to reasonable confidentiality terms.

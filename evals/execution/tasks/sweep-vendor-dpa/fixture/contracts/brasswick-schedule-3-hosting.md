# SCHEDULE 3: HOSTING FACILITIES

This is Schedule 3 to the Laboratory Information System Services Agreement dated 4 September 2023 between Brasswick Lab Informatics Ltd. (the "Supplier") and Orrinfield Medical Group, a division of Orrinfield Health System, Inc. (the "Customer"). Defined terms have the meanings given in Clause 1 of the Agreement.

## Part 1: Approved Facilities

The Supplier shall host the System and Customer Data at the following facilities only:

| Role | Facility and location | Customer Data held |
|---|---|---|
| Primary (production) | Halverson Colocation, Building C, Columbus, Ohio, United States | Production database, application servers, interface engine and document store |
| Secondary (disaster recovery) | Kestowe Data Centres, Montreal, Quebec, Canada | Nightly replicated copy of production database, including patient results |
| Test environment | Halverson Colocation, Building C, Columbus, Ohio, United States | De-identified test data refreshed on request under Clause 3.5 |

## Part 2: Operation of the Secondary Facility

2.1 The secondary facility shall receive an encrypted replication of the production database each night between 02:00 and 03:30 Eastern Time. Replication traffic shall travel over a dedicated encrypted link between the primary and secondary facilities.

2.2 The secondary facility shall be kept in a warm standby state capable of assuming production operations within the recovery time objective set out in Clause 7.3.

2.3 The Supplier shall retain the seven (7) most recent nightly copies at the secondary facility. Older copies shall be overwritten on a rolling basis.

2.4 The Supplier shall carry out a failover test to the secondary facility once in each contract year at a time agreed with the Customer's Director of Laboratory Services, and shall fail back to the primary facility within forty-eight (48) hours of the test commencing.

## Part 3: Facility Standards

3.1 Each facility listed in Part 1 shall:

(a) hold a current SOC 2 Type II report or ISO/IEC 27001 certification;

(b) provide redundant power supplies with generator backup capable of at least seventy-two (72) hours of operation without refuelling;

(c) restrict physical access to authorised personnel using badge and biometric controls, with visitor logs retained for at least ninety (90) days; and

(d) be monitored by on-site security staff twenty-four (24) hours a day.

3.2 The Supplier shall provide the Customer with copies of the reports or certificates referred to in paragraph 3.1(a) on an annual basis.

## Part 4: Change of Facility

4.1 Any change to the facilities listed in Part 1 requires a written variation to this Schedule signed by both parties in accordance with Clause 7.2.

Agreed on behalf of the Supplier: /s/ Alastair Merriden, Managing Director

Agreed on behalf of the Customer: /s/ Yolanda Freitag-Osei, Chief Medical Officer

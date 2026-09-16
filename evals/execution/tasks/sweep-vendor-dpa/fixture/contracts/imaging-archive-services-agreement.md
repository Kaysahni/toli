# IMAGING ARCHIVE SERVICES AGREEMENT

**Agreement Reference:** OHS-IT-2020-031

This IMAGING ARCHIVE SERVICES AGREEMENT (this "**Agreement**") is entered into effective as of September 1, 2020 (the "**Effective Date**") between **Orrinfield Health System, Inc.**, a Wessex Plains nonprofit corporation having its principal office at 2200 Larchmont Parkway, Carrow Falls, Wessex Plains ("**Customer**"), and **Brightwater Radiology Systems, Inc.**, a Delaware corporation having its principal office at 1400 Eastgate Commons, Building B, Marlow Heights, Minnesota ("**Vendor**"). Customer and Vendor are each a "**Party**" and together the "**Parties**."

## ARTICLE 1. DEFINITIONS

Capitalized terms have the meanings set out below or where first defined in the body of this Agreement.

**1.1 "ARCHIVE"** means the vendor-neutral archive platform operated by Vendor under this Agreement, including its image ingestion gateways, storage tiers, index database, zero-footprint viewer and all disaster recovery infrastructure.

**1.2 "CUSTOMER IMAGES"** means all diagnostic images, DICOM objects, non-DICOM clinical media, structured reports, key image notes and presentation states that Customer or its affiliated clinics transmit to, or that are generated within, the Archive, together with all associated metadata, including patient identifiers, accession numbers, study descriptions and audit logs.

**1.3 "DOCUMENTATION"** means Vendor's then-current user guides, conformance statements and interface specifications for the Archive.

**1.4 "INCIDENT"** means any actual or reasonably suspected unauthorized access to, or acquisition, use, disclosure, alteration, loss or destruction of, Customer Images.

**1.5 "SUBPROCESSOR"** means any third party, including an affiliate of Vendor, that Vendor engages to host, store, access or otherwise process Customer Images.

**1.6 "TRANSITION PERIOD"** has the meaning given in Section 12.4.

**1.7 "STUDY"** means a set of images and related objects sharing a single Study Instance UID.

## ARTICLE 2. SERVICES

**2.1 Archive Services.** Vendor shall provide Customer with long-term storage, indexing, lifecycle management and retrieval of Customer Images through the Archive, as described in the Documentation and in Exhibit A (Service Description) (the "**Services**").

**2.2 Integration.** Vendor shall maintain HL7 and DICOM interfaces between the Archive and (a) Customer's radiology information system, (b) the modality fleet listed in Exhibit A, and (c) Customer's enterprise electronic health record, so that prior studies are available to reading radiologists within the times set out in Article 4.

**2.3 Migration.** During the first one hundred eighty (180) days after the Effective Date, Vendor shall migrate Customer's legacy image archive (approximately 41 terabytes as of the Effective Date) into the Archive without additional charge. Vendor shall reconcile study counts before and after migration and deliver a written reconciliation report to Customer's Director of Imaging Informatics.

**2.4 Support.** Vendor shall provide 24x7x365 telephone support for Severity 1 issues and business-hours support for all other issues, in accordance with the support tiers set out in Exhibit A.

**2.5 Exhibits.** The following exhibits form part of this Agreement: Exhibit A (Service Description), Exhibit B (Fees) and Exhibit C (Transition and Data Return). In the event of a conflict, the body of this Agreement controls over Exhibits A and B, and Exhibit C controls with respect to the return and disposition of Customer Images following expiration or termination.

## ARTICLE 3. FEES

**3.1 Fees.** Customer shall pay the fees set out in Exhibit B, consisting of an annual platform fee and a per-Study storage fee billed quarterly based on the number of new Studies ingested.

**3.2 Payment.** Invoices are payable within sixty (60) days after receipt. Amounts disputed in good faith may be withheld pending resolution, provided Customer notifies Vendor of the dispute before the due date.

**3.3 Price Protection.** Fees are fixed for the first three (3) Contract Years. Thereafter, Vendor may increase fees once per Contract Year by an amount not exceeding the lesser of four percent (4%) or the annual change in the Consumer Price Index for All Urban Consumers.

**3.4 Taxes.** Customer is a tax-exempt organization and will provide Vendor with its exemption certificate.

## ARTICLE 4. SERVICE LEVELS

**4.1 Availability.** The Archive shall be available at least 99.95% of each calendar month, excluding scheduled maintenance performed between 01:00 and 05:00 Central Time with at least seven (7) days advance notice.

**4.2 Retrieval Performance.** Vendor shall return the first image of any Study stored on the online tier within three (3) seconds, and any Study stored on the long-term tier within ninety (90) seconds, for at least 98% of requests each month.

**4.3 Credits.** For each full tenth of a percentage point by which availability falls below the commitment in Section 4.1, Customer shall receive a credit equal to two percent (2%) of the monthly platform fee, capped at thirty percent (30%). Credits shall be applied against the next invoice.

## ARTICLE 5. CUSTOMER OBLIGATIONS

**5.1** Customer shall provide network connectivity from its facilities to Vendor's ingestion gateways meeting the minimum bandwidth set out in the Documentation.

**5.2** Customer is responsible for the accuracy of patient demographic information sent from its source systems and for reconciling any orders that fail to match.

**5.3** Customer shall designate a system administrator who will manage user accounts for Customer personnel and affiliated radiologists.

## ARTICLE 6. PROTECTION OF CUSTOMER IMAGES

**6.1 Ownership.** As between the Parties, Customer owns all Customer Images. Vendor acquires no right in Customer Images other than the limited right to process them in order to perform the Services.

**6.2 Permitted Use.** Vendor shall not access, use or disclose Customer Images except (a) as necessary to perform the Services, (b) as directed in writing by Customer, or (c) as required by law, after giving Customer advance notice where legally permitted. Vendor shall not de-identify, aggregate or sell Customer Images or use them to develop or train any algorithm, product or service.

**6.3 Business Associate Agreement.** The Parties have entered into Customer's Business Associate Agreement dated the Effective Date, which remains in effect for so long as Vendor or any Subprocessor holds Customer Images.

**6.4 Safeguards.** Vendor shall maintain administrative, physical and technical safeguards appropriate to the sensitivity of Customer Images, including encryption at rest using AES-256, TLS 1.2 or higher in transit, role-based access controls, multifactor authentication for all administrative access, and immutable audit logging retained for at least six (6) years.

**6.5 Storage Location.** Vendor shall store Customer Images, including every replica, backup, disaster recovery copy and long-term archive tier, exclusively in data centers physically located in the United States. The primary Archive is hosted in Vendor's colocation space in Chaska, Minnesota and the disaster recovery site is located in Omaha, Nebraska. Vendor shall give Customer at least ninety (90) days prior written notice before moving either site to a different location within the United States, and shall not move any Customer Images to a location outside the United States.

**6.6 Audits.** Once per Contract Year, and additionally after any Incident, Customer or its independent auditor may review Vendor's security controls on thirty (30) days notice. Vendor may satisfy this right in part by delivering its current SOC 2 Type II report.

## ARTICLE 7. INCIDENT RESPONSE

**7.1 Notification.** Vendor shall notify Customer of any Incident without unreasonable delay and in no event later than twenty-four (24) hours after Vendor first becomes aware of the Incident. Vendor is deemed aware of an Incident as of the time any Vendor employee or Subprocessor knew or reasonably should have known of it. Notice shall be given by telephone to Customer's security operations center at (555) 014-2290 and confirmed by email to security@orrinfield.example.

**7.2 Investigation.** Following notice, Vendor shall investigate the Incident, contain and remediate it, preserve relevant evidence, and provide Customer with written status updates at least every forty-eight (48) hours until the Incident is closed, followed by a root cause report within thirty (30) days after closure.

**7.3 Notification to Individuals.** Customer shall control the content and timing of any notification to affected individuals, regulators or the media. Vendor shall reimburse Customer's reasonable out-of-pocket costs of such notifications to the extent the Incident resulted from Vendor's breach of this Agreement.

## ARTICLE 8. SUBPROCESSORS

**8.1 Published List.** Vendor maintains, and shall keep current throughout the Term, a list of all Subprocessors, identifying each Subprocessor's legal name, the services it performs and the location of any processing, at trust.brightwater.example/subprocessors. The page is publicly accessible and does not require login.

**8.2 Advance Notice.** Vendor shall notify Customer in writing no fewer than forty-five (45) days before engaging any new Subprocessor or replacing an existing Subprocessor. Notice under this Section shall be sent by email to vendorrisk@orrinfield.example and is not satisfied by updating the web page alone.

**8.3 Objection.** Customer may object to a new or replacement Subprocessor on reasonable data protection grounds within the notice period. If the Parties cannot resolve the objection, Customer may terminate the affected Services without penalty and receive a pro rata refund of prepaid fees.

**8.4 Responsibility.** Vendor shall impose on each Subprocessor written obligations no less protective than those in Articles 6 through 8 and remains liable for the acts and omissions of its Subprocessors.

## ARTICLE 9. WARRANTIES

**9.1** Vendor warrants that (a) the Archive will perform materially in accordance with the Documentation, (b) the Archive is cleared by the U.S. Food and Drug Administration to the extent such clearance is required for its intended use, and (c) Vendor will not introduce malicious code into Customer's environment.

**9.2** Customer's exclusive remedy for breach of Section 9.1(a) is for Vendor to correct the nonconformity or, if Vendor fails to do so within sixty (60) days, to terminate this Agreement and receive a refund of prepaid fees for the remainder of the Term.

**9.3** EXCEPT AS EXPRESSLY STATED IN THIS AGREEMENT, NEITHER PARTY MAKES ANY WARRANTY, WHETHER EXPRESS, IMPLIED OR STATUTORY, AND EACH PARTY DISCLAIMS ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.

## ARTICLE 10. INDEMNITY

**10.1 By Vendor.** Vendor shall defend Customer against any third party claim alleging that the Archive infringes a United States patent, copyright or trademark, or arising from an Incident caused by Vendor or its Subprocessors, and shall pay any resulting damages, settlements and reasonable attorneys' fees.

**10.2 Procedure.** The indemnified Party shall give prompt notice of the claim, allow the indemnifying Party to control the defense, and provide reasonable cooperation at the indemnifying Party's expense.

## ARTICLE 11. LIMITATION OF LIABILITY

**11.1** EXCEPT FOR THE EXCLUDED CLAIMS, NEITHER PARTY SHALL BE LIABLE FOR ANY LOST PROFITS OR INDIRECT, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES, AND EACH PARTY'S AGGREGATE LIABILITY SHALL NOT EXCEED THE FEES PAID AND PAYABLE UNDER THIS AGREEMENT DURING THE TWENTY-FOUR (24) MONTHS PRECEDING THE EVENT GIVING RISE TO THE CLAIM.

**11.2** "Excluded Claims" means claims arising from a Party's indemnity obligations, a breach of Article 6, 7 or 8, or a Party's gross negligence or willful misconduct. Vendor's aggregate liability for Excluded Claims relating to Incidents shall not exceed ten million dollars ($10,000,000).

## ARTICLE 12. TERM AND TERMINATION

**12.1 Term.** This Agreement begins on the Effective Date and continues for an initial term of five (5) Contract Years. It then renews for successive two (2) year renewal terms unless either Party gives notice of non-renewal at least one hundred eighty (180) days before the end of the current term (the initial term and all renewal terms, the "**Term**").

**12.2 Termination for Cause.** Either Party may terminate this Agreement on written notice if the other Party materially breaches it and does not cure the breach within forty-five (45) days after receiving notice describing it.

**12.3 Termination for Insolvency.** Either Party may terminate this Agreement immediately if the other Party becomes insolvent, makes an assignment for the benefit of creditors, or becomes the subject of any bankruptcy proceeding that is not dismissed within sixty (60) days.

**12.4 Transition Period.** Upon expiration or any termination of this Agreement, Customer may elect, by notice given no later than the effective date of expiration or termination, to continue receiving read-only access to the Archive and migration assistance for a period of up to one hundred twenty (120) days (the "**Transition Period**"). Customer shall pay fees during the Transition Period at the rates then in effect, prorated monthly. The obligations of Articles 6, 7 and 8 continue to apply throughout the Transition Period.

**12.5 Return and Destruction.** The export, return and destruction of Customer Images following expiration or termination, and Vendor's related certification, shall be carried out as set out in Exhibit C (Transition and Data Return).

**12.6 Survival.** Articles 6, 7, 10 and 11, Sections 12.4 and 12.5, Exhibit C, and any other provisions that by their nature are intended to survive, shall survive expiration or termination.

## ARTICLE 13. INSURANCE

Vendor shall maintain throughout the Term, with insurers rated A- or better by A.M. Best: (a) commercial general liability insurance of not less than $2,000,000 per occurrence; (b) technology errors and omissions insurance of not less than $5,000,000 per claim; and (c) cyber and network security liability insurance of not less than $10,000,000 per claim, naming Customer as an additional insured where commercially available.

## ARTICLE 14. GENERAL PROVISIONS

**14.1 Governing Law and Venue.** This Agreement is governed by the laws of the State of Wessex Plains, without regard to conflict of laws principles. The state and federal courts sitting in Carrow Falls have exclusive jurisdiction.

**14.2 Notices.** Legal notices shall be in writing and delivered by recognized overnight courier to the addresses in the preamble, attention General Counsel, with an email copy to legal@orrinfield.example (for Customer) or contracts@brightwater.example (for Vendor).

**14.3 Assignment.** Neither Party may assign this Agreement without the other Party's written consent, except to a successor to all or substantially all of its business or assets that assumes this Agreement in writing, provided that Vendor gives Customer at least thirty (30) days notice of any such assignment.

**14.4 Force Majeure.** Neither Party is liable for delay caused by events beyond its reasonable control, except that force majeure does not excuse Vendor's obligations under Articles 6 and 7 or its disaster recovery obligations under Exhibit A.

**14.5 Non-Solicitation.** During the Term and for one (1) year afterward, neither Party shall solicit for employment any employee of the other Party who was directly involved in the Services, other than through general job postings.

**14.6 Entire Agreement.** This Agreement, including its Exhibits and the Business Associate Agreement, constitutes the entire agreement of the Parties regarding its subject matter and supersedes all prior proposals. It may be amended only by a written instrument signed by authorized representatives of both Parties.

IN WITNESS WHEREOF, the Parties have caused this Agreement to be executed by their duly authorized representatives.

| ORRINFIELD HEALTH SYSTEM, INC. | BRIGHTWATER RADIOLOGY SYSTEMS, INC. |
|---|---|
| By: _/s/ Lorraine E. Castellanos_ | By: _/s/ Pieter J. Vandermolen_ |
| Name: Lorraine E. Castellanos | Name: Pieter J. Vandermolen |
| Title: Chief Information Officer | Title: Chief Executive Officer |
| Date: August 27, 2020 | Date: August 24, 2020 |

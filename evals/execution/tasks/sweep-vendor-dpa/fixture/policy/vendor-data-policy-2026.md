# Orrinfield Health: Vendor Data Protection Standard (2026)

**Document owner:** Office of Compliance and Privacy
**Approved by:** Compliance Committee, meeting of May 12, 2026
**Effective:** July 1, 2026
**Replaces:** Vendor Security Addendum Guidelines (2023 edition)
**Review cycle:** Annual

## 1. Purpose

Orrinfield Health operates 41 primary care, urgent care and specialty clinics across the Carrow Valley and Tessary Bay regions. Almost every one of those clinics depends on outside vendors that see, store or move information about our patients: the record system, the lab interface, the people who answer the phone after hours, the company that picks up specimens at 4:30 in the afternoon.

This standard sets the minimum contract terms Orrinfield requires from any vendor that handles Patient Data. It exists because the 2023 guidelines were written as recommendations, and in practice our negotiated terms drifted widely from one agreement to the next. Starting with this edition, the four requirements in Section 4 are mandatory. They are not negotiating targets.

## 2. Scope

This standard applies to every vendor agreement under which the vendor, or anyone working on the vendor's behalf, may access, store, transmit or otherwise process Patient Data.

It does not govern:

- agreements with individual clinicians who hold Orrinfield privileges (see the Medical Staff Bylaws);
- payer contracts and health plan participation agreements;
- research collaborations governed by an IRB-approved data use agreement.

Where an agreement is in scope, the requirements apply to the agreement as a whole as currently in effect, including every exhibit, schedule, addendum, order form and amendment incorporated into it. A compliant clause in the main body does not help if a schedule attached to the same agreement says something different, and a non-compliant clause may be corrected by a signed amendment.

## 3. Definitions

**Patient Data** means any information, in any form, that identifies or could reasonably be used to identify a current, former or prospective Orrinfield patient, together with any health, billing, insurance, scheduling or demographic information linked to that patient. Patient Data includes images, audio recordings, specimen labels and requisition forms.

Information that has been de-identified in accordance with Orrinfield's De-identification Procedure (PRV-114) is not Patient Data for the purposes of this standard. Workforce records about Orrinfield employees and contractors, business contact details for vendor or Orrinfield personnel, and aggregate operational statistics that do not relate to an identifiable patient are also not Patient Data, although other Orrinfield policies may still protect them.

**Security Incident** means any actual or reasonably suspected unauthorized access to, or acquisition, use, disclosure, alteration, loss or destruction of, Patient Data.

**Subprocessor** means any third party (including an affiliate of the vendor) that the vendor engages to access, store or process Patient Data.

**Termination** means the expiration or termination of the agreement for any reason, or the end of any wind-down or transition period that the agreement grants after expiration or termination, whichever is later.

## 4. Mandatory Contract Requirements

Every in-scope agreement must contain terms that meet each of the following. Terms stricter than the requirement (for example, a shorter notification window) satisfy it.

### Requirement 1: Breach notification within 72 hours

The vendor must notify Orrinfield of any Security Incident no later than 72 hours after the vendor discovers it or reasonably should have discovered it.

The clock starts at discovery. Language that starts the notification period at a later point, such as when the vendor "confirms," "completes its investigation of," or "determines the scope of" an incident, does not meet this requirement unless the agreement also caps the total time from discovery to notice at 72 hours. A promise to notify "promptly" or "without undue delay" with no outer limit does not meet it either.

A longer notification period is acceptable only for incidents that do not involve Patient Data.

### Requirement 2: Published subprocessor list and 30 days notice of changes

The vendor must:

(a) maintain a current list of its Subprocessors that Orrinfield can view at any time without having to ask for it, such as on a public web page or inside a customer portal; and

(b) give Orrinfield written notice at least 30 days before any new Subprocessor begins processing Patient Data, or before an existing Subprocessor is replaced.

Notice given after a Subprocessor has already been engaged does not count. A list that is available only "on request" does not satisfy part (a).

### Requirement 3: Patient Data stored only in the United States

Patient Data, including backups, replicas, disaster recovery copies and archives, must be stored only in data centers or facilities physically located in the United States.

Remote access from outside the United States is addressed by the Offshore Access Procedure (PRV-131) and is not a violation of this requirement on its own, as long as the data itself remains stored in the United States.

### Requirement 4: Certified deletion within 30 days of Termination

Within 30 days after Termination, the vendor must delete (or return and then delete) all Patient Data in its possession or in the possession of its Subprocessors, including backup copies, and must provide Orrinfield with a written certification that deletion is complete.

If a vendor cannot delete backup media within 30 days, the agreement does not meet this requirement, even if production systems are cleared sooner.

## 5. Applying the Standard

### 5.1 New agreements

Procurement will not route a new in-scope agreement for signature until the Privacy Office has confirmed the four requirements are met. The model Data Protection Exhibit (template DPE-2026) meets all four and should be used as the starting point.

### 5.2 Existing agreements

Existing agreements are not automatically out of compliance on July 1, 2026, but each must be brought into line at or before its next renewal. Compliance will review the active vendor portfolio before the renewal cycle begins and will send each non-compliant agreement to the contract owner with the specific clause that needs to change.

Agreements that have already been terminated, and where Patient Data has been returned or deleted, do not need to be amended.

### 5.3 Exceptions

An exception to any requirement in Section 4 must be approved in writing by the Chief Compliance Officer and the Chief Information Security Officer, must name a compensating control, and expires after 12 months. As of the effective date, no exceptions have been granted.

## 6. Other Expectations (Not Mandatory)

The following remain good practice and will be scored in vendor risk assessments, but a gap here does not make an agreement non-compliant with this standard:

- SOC 2 Type II report or HITRUST certification, refreshed annually;
- encryption of Patient Data at rest using AES-256 or equivalent;
- cyber liability insurance of at least $5 million per claim for vendors holding more than 10,000 patient records;
- annual security awareness training for vendor personnel with access to Patient Data;
- participation in Orrinfield's annual tabletop exercise for Tier 1 vendors.

## 7. What Changed From the 2023 Guidelines

For reference only. The 2023 guidelines recommended, but did not require, breach notice within five business days, subprocessor disclosure on request, and deletion "within a commercially reasonable period." They did not address data location. Agreements negotiated under the 2023 guidelines frequently reflect those older positions and should be read carefully.

## 8. Related Documents

- PRV-114 De-identification Procedure
- PRV-131 Offshore Access Procedure
- DPE-2026 Model Data Protection Exhibit
- Business Associate Agreement template (BAA-2024)
- Vendor Risk Assessment Questionnaire (VRAQ v5)

## 9. Contacts

Questions about this standard go to the Privacy Office at privacy@orrinfield.example or to Dana Okwuosa, Director of Vendor Risk.

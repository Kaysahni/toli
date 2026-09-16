# Amendment No. 2 to Managed Backup and Vaulting Services Agreement

**Agreement:** Managed Backup and Vaulting Services Agreement No. SDV-MSA-22-0088, effective March 14, 2022, as amended by Amendment No. 1 effective May 1, 2023 (together, the "Agreement")
**Parties:** Orrinfield Health System, Inc. ("Customer") and Sablemoor Data Vaulting, Inc. ("Provider")
**Date of this amendment:** June 2, 2025

Capitalized words not defined in this Amendment No. 2 have the meanings given in the Agreement.

## Background

A. The initial term of the Agreement ended on March 14, 2025 and the Agreement renewed for a one (1) year renewal term under Section 9.1.

B. Following a regional power event that affected Provider's Ashburn campus in late 2024, Provider has expanded its replication architecture and Customer wishes to take advantage of it.

C. Customer also wishes to add Provider's immutable backup option, which became generally available in 2025, for its tier 1 systems.

The parties therefore agree as follows.

## 1. Data location

Section 6.1 of the Agreement is deleted in its entirety and replaced with the following:

"6.1 **Data Location.**
Provider will store Customer Data in its data centers in Ashburn, Virginia and Hillsboro, Oregon, and may maintain a third encrypted replica in its facility in Frankfurt, Germany for geographic resiliency.
The third replica is encrypted with the same keys as the primary copy and is not accessible to Provider personnel located at that facility without approval from Provider's security operations center."

## 2. Immutable backup add-on

2.1 Customer orders the Immutable Vault add-on (SKU SDV-IMV-100) for the tier 1 Protected Systems identified in Section 2.1 of the Agreement.

2.2 With the add-on, each Restore Point is written to storage that cannot be altered or deleted by anyone, including Customer and Provider administrators, until its lock period ends. Customer may choose a lock period of seven (7) or fourteen (14) days per Protected System in the console. The lock period never extends a Restore Point beyond the retention tier assigned to that Protected System and does not affect Provider's obligations under Section 9.5.

2.3 The add-on is priced at $9.00 per terabyte per month of locked storage, billed with the monthly fees under Section 4.1 of the Agreement, as amended by Amendment No. 1.

2.4 Provider will add a monthly immutability report to the console showing, for each tier 1 Protected System, the number of locked Restore Points and the earliest unlock date.

## 3. Renewal term

The current renewal term is extended to end on March 14, 2027. After that date, Section 9.1 of the Agreement applies to further renewals.

## 4. Onboarding

Provider will complete configuration of the Immutable Vault add-on within thirty (30) days after the date of this amendment and will not charge for the add-on until configuration is complete and Customer's infrastructure team has confirmed a successful test restore from a locked Restore Point.

## 5. No other changes

Except as set out in this Amendment No. 2, the Agreement continues unchanged. This amendment may be signed electronically and in counterparts.

**Signed**

For Orrinfield Health System, Inc.
/s/ Anil R. Deshpande
Vice President, Infrastructure and Operations
June 2, 2025

For Sablemoor Data Vaulting, Inc.
/s/ Theodore K. Wainscott
Chief Operating Officer
June 2, 2025

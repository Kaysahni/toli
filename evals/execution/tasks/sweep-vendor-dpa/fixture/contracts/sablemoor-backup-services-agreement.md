# Sablemoor Data Vaulting, Inc.
## Managed Backup and Vaulting Services Agreement

**Customer:** Orrinfield Health System, Inc., 2200 Larchmont Parkway, Carrow Falls
**Provider:** Sablemoor Data Vaulting, Inc., 610 Halvard Street, Tollerton, Wessex Plains
**Agreement number:** SDV-MSA-22-0088
**Effective date:** March 14, 2022

This agreement explains how Provider will back up, vault and restore the clinical systems that Customer relies on to run its clinics. We have tried to write it in plain language. Where a word is capitalized, it has the meaning given in Section 1.

---

## 1. Key terms

**Customer Data** means everything Customer or its systems send to Provider for backup, including database snapshots, virtual machine images, file shares and log archives, and every copy of that material Provider creates. Customer's clinical systems hold patient records, so Customer Data will include protected health information.

**Protected Systems** means the servers, virtual machines and databases listed in the Service Order, as updated from time to time through the Provider console.

**Restore Point** means a recoverable copy of a Protected System as of a given time.

**Security Event** means any actual or reasonably suspected unauthorized access to, use, disclosure, alteration, corruption, loss or destruction of Customer Data.

**Subservicer** means any company Provider uses to store, transmit, access or otherwise handle Customer Data, including colocation operators, network carriers with access to unencrypted data, and Provider affiliates.

**Service Order** means the order form signed by both parties on or after the effective date that lists the Protected Systems, the storage commitment and the fees.

## 2. What Provider does

2.1 **Backups.** Provider will take Restore Points of each Protected System on the schedule in the Service Order. The default schedule is hourly incremental snapshots for tier 1 systems (the electronic health record database, the laboratory interface engine and the picture archive index) and nightly snapshots for everything else.

2.2 **Vaulting.** Provider will copy every Restore Point to a second, geographically separate Provider data center within four (4) hours after it is taken, so that Customer Data survives the loss of a single site.

2.3 **Restores.** Customer can start file, database or full system restores from the Provider console at any time. For tier 1 systems, Provider commits to a recovery point objective of one (1) hour and a recovery time objective of four (4) hours.

2.4 **Annual recovery test.** Once each year, at a time Customer chooses, Provider will run a full recovery exercise of the tier 1 systems into an isolated environment and give Customer a written test report.

2.5 **Monitoring.** Provider watches every backup job. If a job fails twice in a row, Provider's operations center will open a ticket and call Customer's on-call infrastructure contact.

## 3. What Customer does

3.1 Customer will install and keep current the Provider backup agent on each Protected System.

3.2 Customer will keep the Service Order accurate. If Customer adds a system that holds patient information but does not add it to the Service Order, Provider is not responsible for failing to back it up.

3.3 Customer will keep its console credentials secure and use multifactor authentication for every console account.

## 4. Fees

4.1 Customer will pay the monthly fees in the Service Order. Fees are based on the committed storage amount. If Customer's actual protected storage is higher than the commitment for two consecutive months, Provider will bill the overage at the rate in the Service Order.

4.2 Provider invoices on the first business day of each month. Payment is due within thirty (30) days.

4.3 Late amounts accrue interest at one percent (1%) per month, but Provider will not charge interest on amounts Customer disputes in good faith and in writing.

4.4 Provider will not suspend backups or restores for non-payment unless an undisputed invoice is more than ninety (90) days overdue and Provider has given Customer's Chief Financial Officer at least fifteen (15) days written warning. Provider will never delete Customer Data as a consequence of non-payment during the term.

## 5. Service levels

5.1 **Console availability.** The Provider console will be available 99.9% of the time in each calendar month.

5.2 **Backup success.** At least 99.5% of scheduled backup jobs each month will complete successfully, not counting failures caused by Customer systems being offline.

5.3 **Restore commitment.** If Provider misses the tier 1 recovery time objective during an actual recovery (not a test), Customer will receive a credit equal to fifty percent (50%) of that month's fees.

5.4 **Credits.** Other service level misses earn a credit of ten percent (10%) of that month's fees per miss, up to fifty percent (50%) total. Customer must request credits within sixty (60) days after the end of the month.

## 6. Protecting Customer Data

6.1 **Data Location.** Provider will store Customer Data only in Provider's data centers in Ashburn, Virginia and Hillsboro, Oregon. This applies to primary backups, vaulted copies, replicas and any archive or long-term retention copies. Provider will not store Customer Data anywhere else.

6.2 **Encryption.** Customer Data is encrypted by the backup agent before it leaves Customer's network, using AES-256, and stays encrypted in transit and at rest. Customer may choose to hold its own encryption keys through the key management option in the Service Order.

6.3 **Access.** Only Provider personnel who need access to perform the services may access Customer Data, and every access is logged. Provider will give Customer a copy of those logs within five (5) business days after Customer asks.

6.4 **No other use.** Provider will use Customer Data only to deliver the services. Provider will not mine, analyze, sell or share Customer Data.

6.5 **Business associate terms.** The business associate agreement the parties signed with this agreement is part of this agreement. If it conflicts with this Section 6 or Sections 7 through 9, whichever term better protects Customer Data applies.

6.6 **Security program.** Provider will maintain a written information security program, obtain a SOC 2 Type II report each year covering the services, and share that report with Customer under confidentiality.

## 7. Security Events

7.1 **When Provider tells Customer.** Provider will tell Customer about any Security Event within seventy-two (72) hours after Provider discovers it. Provider discovers a Security Event when anyone at Provider or any Subservicer knows about it, or would have known about it by following Provider's own monitoring procedures. Provider will not wait until its investigation is finished before telling Customer.

7.2 **How.** Provider will call Customer's security operations center at the number listed in the Service Order and follow up in writing to security@orrinfield.example.

7.3 **What happens next.** Provider will keep Customer informed at least daily while the Security Event is open, give Customer a written incident report within fifteen (15) days after it closes, and cooperate with any notices Customer needs to send to patients or regulators.

7.4 **Costs.** If the Security Event was caused by Provider or a Subservicer, Provider will pay Customer's reasonable costs of notices, call center support and credit monitoring for affected individuals.

## 8. Subservicers

8.1 **Where to find the list.** Provider publishes the name, function and location of every Subservicer on the Customer Data Governance page of the Provider console at console.sablemoor.example/governance/subservicers. The page is always up to date and every Customer console user can view it.

8.2 **Changes.** Provider will give Customer written notice at least thirty (30) days before any new Subservicer starts handling Customer Data, and at least thirty (30) days before replacing any existing Subservicer. Notice goes to Customer's contract owner by email and is also posted in the console.

8.3 **Objections.** If Customer reasonably objects to a new Subservicer on security or privacy grounds, the parties will work together in good faith. If they cannot agree before the change takes effect, Customer may end this agreement without paying any early termination fee.

8.4 **Provider stays responsible.** Provider is responsible for the work of its Subservicers as if it were doing that work itself.

## 9. Ending the agreement

9.1 **Term.** The initial term is three (3) years from the effective date. After that, the agreement renews for one (1) year at a time unless either party tells the other in writing, at least ninety (90) days before renewal, that it does not want to renew.

9.2 **Ending for a reason.** Either party can end this agreement if the other party seriously breaks it and does not fix the problem within thirty (30) days after being told about it in writing.

9.3 **Ending early for convenience.** Customer can end this agreement at any time with one hundred twenty (120) days written notice, but must then pay an early termination fee equal to three (3) months of the committed monthly fee.

9.4 **Getting data back.** Before this agreement ends, Customer can restore or export any Customer Data it wants to keep using the console, at no extra charge.

9.5 **Deleting everything.** Within thirty (30) days after this agreement ends or expires for any reason, Provider will permanently delete all Customer Data, in every location and every form, including vaulted copies, replicas, archive copies and any copies held by Subservicers. Provider will then send Customer a written certificate, signed by Provider's Chief Security Officer, confirming that all Customer Data has been deleted. Provider will not keep any backup of Customer Data after that thirty (30) day period for any reason.

9.6 **What survives.** Sections 6, 7, 9.5, 10, 11 and 12 continue after the agreement ends.

## 10. Promises and disclaimers

10.1 Provider promises that the services will work substantially as described in this agreement and in the Provider service documentation.

10.2 Provider promises that it has not placed, and will not place, any code in the backup agent that disables it or deletes data on a timer or on a remote command other than a command given by Customer.

10.3 Beyond those promises, the services are provided without other warranties, including implied warranties of merchantability and fitness for a particular purpose.

## 11. Liability and indemnity

11.1 Provider will defend and hold Customer harmless from third party claims arising from a Security Event caused by Provider or a Subservicer, or from Provider's breach of Section 6 or 9.5.

11.2 Neither party is responsible to the other for lost profits or indirect damages.

11.3 Except for Section 11.1, a breach of Section 6, 7 or 8, or gross negligence or willful misconduct, each party's total liability is capped at the fees Customer paid in the eighteen (18) months before the claim. For those excluded matters, Provider's total liability is capped at seven million five hundred thousand dollars ($7,500,000).

11.4 Provider will carry cyber liability insurance of at least $7,500,000 per claim and technology errors and omissions insurance of at least $3,000,000 per claim throughout the term.

## 12. Everything else

12.1 **Law.** The laws of the State of Wessex Plains apply. Any lawsuit will be brought in the courts located in Carrow Falls.

12.2 **Notices.** Formal notices must be in writing. Notices to Customer go to the Vice President of Infrastructure, with a copy to legal@orrinfield.example. Notices to Provider go to the General Counsel at legal@sablemoor.example.

12.3 **Hiring.** Neither party will recruit the other party's employees who worked on the services for twelve (12) months after they last did so, except through public job postings.

12.4 **Changes to this agreement.** Any change must be in a written amendment signed by both parties. Provider cannot change these terms by updating a web page or the console.

12.5 **Whole agreement.** This agreement, the Service Order and the business associate agreement make up the whole agreement between the parties about the services.

---

**Signed**

For Orrinfield Health System, Inc.
Signature: /s/ Anil R. Deshpande
Name: Anil R. Deshpande
Title: Vice President, Infrastructure and Operations
Date: March 11, 2022

For Sablemoor Data Vaulting, Inc.
Signature: /s/ Corinna Blaylock
Name: Corinna Blaylock
Title: Chief Revenue Officer
Date: March 14, 2022

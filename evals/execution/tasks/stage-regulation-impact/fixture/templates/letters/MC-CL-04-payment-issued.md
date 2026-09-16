<!-- MC-CL-04 Claim Payment Issued | all states | rev 2024-09-09 -->

{{letter_date}}

Claim number: {{claim_number}}

Dear {{claimant_first_name}},

We have issued a payment on your claim.

  Payment amount:    {{payment_amount}}
  Payable to:        {{payees}}
  Payment method:    {{payment_method}}
  For:               {{coverage_description}}
  Deductible applied: {{deductible_applied}}

{{#if mortgagee_on_check}}
Because your mortgage company has an interest in your home, the check is made payable to both you and {{mortgagee_name}}. Your mortgage company may have its own process for releasing funds for repairs.
{{/if}}

{{#if holdback}}
We are holding back {{holdback_amount}} of recoverable depreciation. We will pay this amount once repairs are complete and you send us the final invoice.
{{/if}}

If you have questions about this payment, contact {{adjuster_name}}.

Marlowe Crest Insurance Company

"""Generate the stage-feedback-synthesis fixture and checklist.

Run: python3 build/generate.py
Distinct-customer counts per theme are computed here from the same data that
is written to the fixture, then written into checklist.json.
"""
import csv, json, random, re, shutil, datetime as dt
from pathlib import Path
from prose import SALES_CALLS, FORUM

random.seed(20260916)
ROOT = Path(__file__).resolve().parent.parent
FIX = ROOT / "fixture"
INTERNAL = "pinmoor.example"
THEMES = ["T1", "T2", "T3", "T4", "T5"]

# ---------------------------------------------------------------- companies
NAMED = ["Birchway Dental Group", "Copperlane Hotels", "Greyloch Manufacturing", "Quenby Foods",
         "Radleigh Senior Living", "Kittering Freight", "Westmere Retail Group", "Fenwright Engineering",
         "Sunderby Clinics", "Pellam Outdoor Supply", "Everleigh Staffing", "Lindqvist Architecture",
         "Marisol Home Care", "Brightwater Charter Network", "Canterfield Logistics", "Hollins Park Fitness",
         "Moss & Vane Legal", "Nettlefield Brewing", "Ostrander Plumbing", "Galloway Print Works",
         "Carrow Street Bakeries", "Wrenfield Pediatrics", "Bramblecote Nurseries", "Orwell Bay Seafoods",
         "Tamsin Labs", "Aldercrest Schools Foundation", "Stonewick Veterinary", "Ivel River Credit Services",
         "Harlow & Pike Builders", "Tollbridge Ceramics", "Harrowgate Tile Supply"]
STEMS = ["Ash", "Bell", "Cald", "Dun", "Elm", "Farr", "Gild", "Haw", "Ingle", "Kel", "Lark", "Merr", "North",
         "Oak", "Pem", "Quill", "Rush", "Salt", "Thistle", "Vant", "Wex", "Yarr", "Black", "Cold", "Fox", "Glen",
         "Iron", "Kest", "Low", "Maple", "Nether", "Pen", "Red", "Stan", "Brack", "Chil", "Dray", "Hol", "Lang",
         "Tarn", "Umber", "Wyn", "Ebb", "Fern", "Gorse", "Heron", "Juni", "Moor"]
ENDS = ["grove", "mont", "wick", "haven", "worth", "dale", "field", "ridge", "brook", "mere", "beck",
        "hollow", "ford", "stead", "cott", "gate", "bury", "combe", "shaw", "thorpe"]
INDUSTRY = ["Dental", "Logistics", "Credit Union", "Veterinary Group", "Builders", "Family Medicine", "Staffing",
            "Senior Care", "Architects", "Foods", "Hospitality", "Charter Schools", "Engineering", "Auto Group",
            "Insurance Brokers", "Garden Centers", "Printing", "Physical Therapy", "Brewing Co", "Home Health",
            "Outfitters", "Title and Escrow", "Clinics", "Manufacturing", "Pharmacy", "Marine Supply",
            "Landscaping", "Bakeries", "Law Group", "Pet Hospitals", "Property Management", "Cabinetry",
            "Dermatology", "Transit", "Hardware", "Orthodontics", "Precision Parts", "Community Bank"]
BLOCK = {"Ashford", "Oakbrook", "Oakdale", "Elmhurst", "Blackburn", "Stanford", "Redford", "Ashbury",
         "Glenbrook", "Foxford", "Salthaven", "Northgate", "Northfield", "Marshfield", "Oakfield", "Bellmont"}

def gen_companies(n):
    out, used = [], set()
    while len(out) < n:
        w = random.choice(STEMS) + random.choice(ENDS)
        if w in used or w in BLOCK:
            continue
        used.add(w)
        out.append(f"{w} {random.choice(INDUSTRY)}")
    return out

GENERATED = gen_companies(180)
CHURN_POOL = GENERATED[110:]        # churned accounts only appear in the churn survey
ACTIVE_GEN = GENERATED[:110]

def domain(company):
    words = re.sub(r"[^a-z ]", "", company.lower().replace("&", "and")).split()
    return "".join(words[:2]) + ".example"

FIRST = ["Adaeze", "Alma", "Bram", "Carys", "Dmitri", "Elif", "Farah", "Gideon", "Hana", "Idris", "Jolene",
         "Kasimir", "Leonie", "Mateus", "Nell", "Oskar", "Pilar", "Quentin", "Rhea", "Saoirse", "Tomasz",
         "Uma", "Vikram", "Wilhelmina", "Xavi", "Yusra", "Zeno", "Bettina", "Callum", "Delphine", "Emeka",
         "Frida", "Gus", "Hollis", "Ines", "Jasper", "Kalani", "Lorcan", "Maribel", "Nils", "Odette", "Pax",
         "Rosalind", "Stellan", "Tova", "Ulrich", "Vesna", "Wade", "Yolanda", "Zadie"]
LAST = ["Abernethy", "Baptiste", "Carmody", "Dalca", "Eklund", "Fairley", "Grunwald", "Hakimi", "Ilves",
        "Jankowski", "Kowalczyk", "Lindahl", "Mbatha", "Novak", "Okonjo", "Pradhan", "Quist", "Rasmussen",
        "Sarkisian", "Thorne", "Ueda", "Vasquez", "Whitlock", "Yilmaz", "Zamora", "Achterberg", "Boateng",
        "Cespedes", "Drummond", "Esposito", "Farouk", "Gallagher", "Holm", "Iwasaki", "Jovanovic", "Keane"]
CONTACTS = {}

def contact(company, fresh=False):
    lst = CONTACTS.setdefault(company, [])
    if not lst or (fresh and len(lst) < 3) or (len(lst) < 3 and random.random() < 0.2):
        lst.append(f"{random.choice(FIRST).lower()}.{random.choice(LAST).lower()}@{domain(company)}")
    return random.choice(lst)

def rand_dt(start, end):
    a = dt.datetime.fromisoformat(start); b = dt.datetime.fromisoformat(end)
    t = a + dt.timedelta(seconds=random.randint(0, int((b - a).total_seconds())))
    return t.replace(hour=random.randint(6, 19), minute=random.randint(0, 59))

# ------------------------------------------------------------ theme texts
# Ticket entries: (subject, description) or (subject, description, follow_up_of_index)
TICKETS = {
"T1": ("2026-07-02", [
    ("Ledgerline export columns shifted", "Since the update last week the export we send to Ledgerline has the employer retirement match in the wrong column. Our payroll person caught it before submitting but this is scary."),
    ("payroll bridge file rejected", "Tallybook rejected our payroll file this morning with mapping error 412. Nothing changed on our side. Can someone look today? Payroll runs Thursday."),
    ("Export date format", "The pay period dates in the Payroll Bridge CSV are coming out as DD/MM/YYYY now. Ledgerline expects MM/DD. Did a setting change?"),
    ("missing employees in export", "Two new hires from 7/14 are not in the payroll export even though they show as active in People. Had to key them manually."),
    ("URGENT payroll sync", "Our sync to Tallybook has failed three pay periods in a row. We have been exporting by hand and re-uploading. Please escalate."),
    ("Deductions doubled in GL file", "The general ledger file doubled the health savings deduction line for everyone on the Denver entity. Finance flagged it at month end close."),
    ("Export button greyed out", "Payroll Bridge export button is disabled for our second pay group. The first pay group exports fine."),
    ("Re: export columns", "Following up on my earlier ticket, the column order is still wrong after the hotfix. We re-mapped in Ledgerline as a workaround but that will break again when you fix it properly, right?", 0),
    ("Wrong cost center on payroll export", "Cost center codes are blank in the export file for anyone who transferred departments this quarter."),
    ("Ledgerline integration disconnects", "Every Monday the Ledgerline connection shows Disconnected and we have to re-enter the API token before running payroll."),
    ("file encoding", "The export now has a byte order mark at the start of the file and our payroll provider's importer chokes on the first header. Worked fine in June."),
    ("Payroll export totals don't match", "Gross pay total on the Payroll Bridge summary screen is 1,204.50 higher than the downloaded file. Which one is right?"),
    ("Overtime missing in Tallybook push", "Overtime hours approved in timesheets are not included when we push to Tallybook. Regular hours go through."),
    ("export error", "Getting Something went wrong (code PB-500) when generating the payroll file for the 8/15 run."),
    ("terminated employees still exported", "People we terminated in July are still showing up in the payroll export with zero hours, which makes Ledgerline create a paycheck stub for them."),
    ("Help with 3.14 changes to payroll file?", "Our accountant says the file layout changed with your July release and nobody told us. Is there a changelog for the export format?"),
    ("Payroll sync stuck in pending", "The Tallybook sync has said Pending for 6 hours. Payroll deadline is 3pm Eastern."),
    ("Bonus earnings code", "One-time bonus earnings are exported under the regular earnings code so they are getting taxed at the wrong supplemental rate on the provider side."),
    ("export again", "Same problem as my ticket from July, the employer contribution columns are misaligned in the Ledgerline file. Please fix for real.", 0),
    ("Can't map new fields", "After the update the field mapping screen for Payroll Bridge is missing the Local Tax field, so local tax for our Ohio employees never makes it to the export."),
    ("payroll file has duplicates", "Rows are duplicated for employees with two job codes in the payroll export. Our provider imported both and we nearly double paid three people."),
    ("Question about export timing", "Is there a known issue with the Payroll Bridge right now? The export is timing out for our Canada pay group only."),
]),
"T2": ("2026-07-03", [
    ("PTO balance wrong for part timers", "Our part-time staff at 24 hours a week are accruing as if they were full time. Balances are about 40% too high."),
    ("accrual not prorated", "Employees who started mid-year got a full year of vacation front loaded instead of a prorated amount."),
    ("Carryover cap ignored", "Our policy caps carryover at 40 hours but on anniversary dates the system carried over everything. Several people now show 120+ hours."),
    ("sick leave balances", "Sick time accrual stopped for anyone who changed from hourly to salaried in July. Their balance has not moved in 6 weeks."),
    ("Time off balance jumped", "Maria in our warehouse shows 312 hours of vacation. She had 36 last month. What happened?"),
    ("accrual recalculation", "We edited the Standard PTO policy to fix a typo in the name and it recalculated accruals for everyone back to hire date. Balances are all off now."),
    ("Negative balances", "Several employees are showing negative time off balances even though they have never taken leave. Looks like accruals were reversed."),
    ("Paid holiday counted as PTO", "The July 4 holiday was deducted from PTO balances for our part-time group."),
    ("Leave balances don't match payroll", "Our payroll provider's leave balances and Pinmoor's differ for about 30 people. Pinmoor seems to be the one that is wrong, it double accrued the 7/31 period."),
    ("prorate question", "Is Time Off supposed to prorate accruals by scheduled hours? It isn't doing it for anyone on a 0.6 FTE schedule."),
    ("Accrual tier not applied", "Employees who hit 5 years should move to the 6 hr per pay period tier. Nobody moved up on their anniversary."),
    ("vacation hours off", "Vacation hours for our Ontario employees are off by a few hours each pay period. Rounding?"),
    ("Re: part time accruals", "Still wrong after your fix went out Tuesday. Attaching a screenshot of three employees.", 0),
    ("Accrual policy assignment", "When we assign a new hire to the Part Time PTO policy, they still accrue on the Full Time schedule."),
    ("Balance audit", "Can you send us an audit log of accrual transactions? Our balances are wrong and we need to rebuild them before year end."),
    ("Floating holiday balance reset", "Floating holiday balances reset to zero mid-year for everyone on the Retail policy."),
    ("time off accruals incorrect after rehire", "Rehired employees are accruing from their original hire date instead of the rehire date, so they are getting the higher tier."),
    ("Accruals", "Accruals are wrong again this pay period. This is the third time this quarter we are fixing balances by hand.", 1),
]),
"T3": ("2026-07-10", [
    ("Mobile app keeps logging out", "Our field staff say Pinmoor Go logs them out every time they close the app. They are using SSO through our identity provider."),
    ("Have to sign in every time", "Employees have to sign in again every time they open the mobile app to clock in, and it is slowing down shift start."),
    ("face unlock not working", "Face unlock on iOS stopped being remembered after the latest app update. It asks for the full password each time."),
    ("Session timeout mobile", "Is there a setting for the mobile session length? People are getting kicked out after a couple of minutes."),
    ("Android app logout", "On Android the app returns to the login screen whenever the phone locks."),
    ("SSO loop on mobile", "Tapping Sign in with SSO in the app opens the browser, authenticates, then drops back to the login screen. Endless loop for about half our users."),
    ("app sign out issue", "Our staff cannot request time off from the app because they get signed out mid-request and lose what they typed."),
    ("Pinmoor Go login", "Getting lots of complaints that the app forgets the login. Desktop is fine."),
    ("Re: mobile logout", "Any update? Still happening on version 5.2.1 of the app.", 0),
    ("Mobile re-authentication", "Our identity team sees a new auth request from Pinmoor Go every few minutes per user, which is tripping our risky sign-in alerts."),
    ("kicked out of app", "Staff are kicked out of the app when switching to their camera to upload a receipt."),
    ("Remember me not remembered", "The Keep me signed in toggle on mobile does nothing."),
    ("Mobile clock in", "Clock in on the app fails because it logs out before the location check finishes."),
    ("login every time", "Why do I have to log in every single time I open the Pinmoor app? This did not happen before summer."),
    ("App logs out on wifi change", "App logs users out whenever they move between the store wifi and cellular."),
    ("Mobile SSO", "Since the 5.2 app release, SSO sessions on mobile last about 5 minutes. On 5.1 they lasted weeks."),
]),
"T4": ("2026-07-01", [
    ("Can't edit review questions", "We launched our mid-year review cycle and noticed a typo in question 3. The template is locked and the only option is to cancel the cycle."),
    ("Add a question after launch", "Leadership wants to add one question to the review cycle that went live Monday. Is there really no way without starting over?"),
    ("Canceling cycle deletes responses", "We cancelled a review cycle to fix the rating scale and lost 40 self reviews that were already submitted. Can those be restored?"),
    ("change reviewer", "A manager left the company and we cannot reassign his direct reports' reviews to the new manager inside the active cycle."),
    ("Review template locked", "Template shows as locked because it is used in an active cycle. We have other cycles that need a different version of it."),
    ("rating scale wrong", "We picked a 4 point scale by mistake when setting up the cycle. After launch it cannot be changed."),
    ("Review cycle setup confusing", "The cycle setup wizard does not say that the questions become read only once you hit Launch. Please add a warning at minimum."),
    ("Performance review edit", "Need to fix the competency descriptions in a launched review. HR shouldn't have to email 200 people to say ignore question 5."),
    ("Adding late hires to cycle", "People hired after the review cycle launched can't be added to it."),
    ("re: locked template", "Following up. We ended up running the review in a spreadsheet because we could not change the form. Please prioritize.", 0),
    ("Peer reviewers", "Can't add peer reviewers once the cycle has started, the button is gone."),
]),
"T5": ("2026-07-20", [
    ("Reports timing out", "Headcount by department over time report spins and then shows Request timed out. We have about 1,400 employees."),
    ("Report builder slow", "Custom reports in Insights take 3 to 4 minutes to load since July. Used to be seconds."),
    ("Scheduled report empty", "Our weekly turnover report arrived by email with no rows. Running it manually times out."),
    ("Insights won't load", "The Insights dashboard never finishes loading for our admin users. Small filters work, whole company does not."),
    ("export report error", "Trying to export the compensation report for all 900 employees gives a 504 error."),
    ("demographics report", "Cannot generate the demographics report for our annual compliance filing, it times out every time. We have a filing deadline."),
    ("slow reports", "Is Insights having performance problems? Our reports with more than a year of data do not finish."),
    ("Report timeouts large org", "Any report that includes all 11 locations times out. Filtering to one location works."),
    ("turnover dashboard", "Turnover dashboard is blank for company-wide view. It loads for individual departments."),
]),
}

NPS_THEME = {
"T1": [(6, "Would be a 9 but the payroll export to Ledgerline broke twice this summer and I had to fix it by hand."),
       (5, "Payroll Bridge has been unreliable since July. The rest of the product is solid."),
       (6, "The export file format changed without notice and our accountant was not happy."),
       (4, "Tallybook sync failures cost me two late nights this quarter."),
       (7, "Love the people directory. Hate that I have to double check every payroll file now."),
       (3, "Fix the payroll export please. That is the only reason for this score."),
       (5, "Integration with our payroll provider is flaky, columns move around."),
       (7, "Good support team but they could not tell us why the GL export doubled deductions."),
       (3, "Payroll file errors nearly caused us to underpay staff. Considering alternatives.")],
"T2": [(4, "Time off balances are wrong for our part-time employees and my team spends hours correcting them."),
       (5, "Accruals are a mess this quarter."),
       (6, "PTO tracking used to be the best part. Now employees don't trust the balances they see."),
       (4, "Prorated accruals do not work, which is a big deal for a company with lots of part-timers."),
       (8, "Carryover did not respect our cap. Otherwise happy."),
       (6, "Employees keep asking me why their vacation hours changed."),
       (7, "Fix leave accruals and you would get a 10 from me.")],
"T3": [(3, "The app logs our staff out constantly. They have mostly given up on it."),
       (6, "Mobile experience got worse after the update, having to sign in every time is painful."),
       (5, "Pinmoor Go needs to remember logins. Our warehouse team hates it."),
       (7, "Web app great, mobile app keeps kicking people out."),
       (4, "SSO on the phone is broken for us."),
       (5, "Our frontline workers only use mobile, and it forgets them every few minutes.")],
"T4": [(6, "Review cycles are too rigid. You cannot fix a mistake once the cycle is live."),
       (4, "Had to restart our annual reviews because we could not edit the questions."),
       (7, "Performance module setup is not intuitive and locks you in too early."),
       (7, "Let us change reviewers mid-cycle.")],
"T5": [(6, "Reporting is slow for a company our size."),
       (5, "Insights times out on anything company-wide."),
       (6, "Reports take forever to load with 2,000 employees."),
       (7, "Custom reports are great in theory but they rarely finish for us.")],
}

CHURN_THEME = {
"T1": ["The payroll export kept breaking and our payroll provider is not something we can change.",
       "We could not risk another bad payroll file.",
       "Ledgerline integration errors every other pay period.",
       "Payroll Bridge problems since July were the final straw."],
"T2": ["Time off balances were wrong for months and employees lost trust.",
       "Part-time accruals never calculated correctly.",
       "We were fixing PTO balances by hand every pay period."],
"T3": ["Our hourly staff could not stay signed in to the mobile app.",
       "Mobile app logouts made clock in unusable."],
"T4": ["Review cycle tool was too inflexible for how we run reviews.",
       "Lost submitted self reviews when we had to restart a cycle."],
"T5": ["Reporting did not scale to our headcount.",
       "Reports timing out, could not get data for our board."],
}

# ------------------------------------------------------------ decoy texts
D1_TICKETS = [
    ("Benefits document upload failing", "Employees get Upload failed, try again when attaching dependent verification documents in benefits enrollment."),
    ("Upload still failing", "Still broken. Three more employees today."),
    ("Enrollment upload error", "Another employee could not upload her marriage certificate for spouse coverage."),
    ("RE: Upload failed", "Following up again on the upload issue. Enrollment closes on the 30th."),
    ("Cannot attach birth certificate", "Employee in our glaze department cannot attach a birth certificate PDF for his daughter. Same error as the other tickets."),
    ("upload", "same upload error"),
    ("Upload failed on phone", "Tried from a phone camera photo this time. Still Upload failed, try again."),
    ("Dependent docs", "Dependent verification uploads are failing for everyone at our Millbrook plant."),
    ("Enrollment deadline and uploads", "If employees cannot upload documents before the enrollment deadline will their coverage be denied? We have had upload failures all week."),
    ("Please escalate upload bug", "Please escalate. This is the 10th ticket we have opened for the benefits upload failure."),
    ("Upload error screenshot", "Attaching a screenshot of the upload error from our shipping supervisor."),
    ("Upload failing again", "Upload failed again for two employees on second shift."),
    ("Docs won't attach", "Documents will not attach in benefits enrollment. Tried two different browsers."),
    ("File size?", "Is there a file size limit on benefits documents? The files failing are under 2 MB."),
    ("Still no fix", "No update on the upload issue. Our broker is asking why documents are missing."),
    ("benefits upload", "Another one. Employee ID 3318, upload failed for a dependent document."),
    ("Upload issue (duplicate of earlier)", "Opening a new ticket because the old one was closed without a fix. Uploads still fail."),
    ("Upload problem", "Employees get an error when uploading documents in benefits enrollment."),
    ("Fwd: upload not working", "Forwarding from one of our kiln operators: I tried to upload my son's birth certificate three times and it says upload failed."),
    ("Upload error for spouse documents", "Spouse verification document upload fails for employee ID 2291."),
    ("Benefits upload urgent", "Enrollment closes Friday and at least 15 employees still cannot upload documents."),
    ("Can HR upload on behalf?", "Can HR upload dependent documents on behalf of employees? The employee side upload keeps failing."),
    ("HR side upload also failing", "Tried uploading from the admin side as a workaround and that fails too."),
    ("upload", "Upload failed, try again. Again."),
    ("Documents missing from enrollment", "Our broker's report shows missing documents for 22 employees, all of them hit the upload error."),
    ("Any update?", "Any update on the benefits document upload issue?"),
    ("Re: Any update?", "Checking in again on the upload failures."),
    ("Upload fails for scanned documents", "Scanned documents from our office scanner also fail to upload."),
    ("Extension request", "Because of the upload bug we need to extend enrollment. Can the enrollment window be changed after it opens?"),
    ("Upload failing", "Upload failing for new hire enrollment too, not just open enrollment."),
]
D2_TICKETS = [
    ("Org chart PDF cuts off names", "Exporting the org chart to PDF cuts off the bottom row of names at the page edge."),
    ("org chart export", "Org chart PDF export truncates names when the chart is deeper than 4 levels."),
    ("Org chart PDF landscape", "Landscape org chart export still clips names on the right side."),
    ("Org chart printing for customer demo", "Could not print a clean org chart for a demo, the PDF is missing half the names in the last row."),
    ("PDF org chart", "Names overlap and get cut off in the org chart PDF. Reproduced on two tenants."),
    ("Org chart export still broken", "Still seeing clipped names in the org chart PDF on the latest build."),
    ("Org chart PDF blank pages", "Org chart PDF for a 300 person sample company has two blank pages and cut off names."),
    ("org chart", "Bottom level of the org chart is clipped in PDF export."),
    ("Org chart export fonts", "Long job titles overflow their boxes in the org chart PDF."),
    ("Org chart PDF (from sales)", "Prospect asked for an org chart PDF sample. The one I exported has cut off names, can we fix before Thursday?"),
    ("Org chart zoom", "Org chart export ignores the zoom level and crops the chart."),
    ("Org chart PDF names cut off again", "Org chart PDF export cuts off names on the bottom row again."),
]
D2_NPS = [(6, "Dogfooding note: org chart PDF export cuts off names, embarrassing in demos."),
          (7, "Org chart export needs work."),
          (8, "Everything is solid except the org chart PDF, which clips names."),
          (7, "Would be a 9 if org chart printing worked.")]
STAFF = ["dana.whitcombe@pinmoor.example", "leo.fairweather@pinmoor.example", "theo.marchetti@pinmoor.example",
         "priya.venkataraman@pinmoor.example", "marcus.bell@pinmoor.example"]
STAFF_TENANTS = ["Alderpoint Sample Co", "Quarry Lane Sample Co"]

# ------------------------------------------------------------ noise
NOISE_TICKETS = [
    ("pwreset", "Locked out", "One of our managers is locked out after too many password attempts. Can you unlock her account?"),
    ("add_admin", "Add a second admin", "Please give {name} full admin rights. I am going on leave next week."),
    ("invoice_count", "Invoice question", "Our August invoice shows {n} employees but we only have {m} active. Can you check how billable headcount is counted?"),
    ("withholding", "Tax withholding form", "Where do employees update their federal withholding in Pinmoor? I can't find it in the employee profile."),
    ("api_key", "API key rotation", "How do we rotate our API key without breaking the integration with our applicant tracking system?"),
    ("holiday_add", "Add a company holiday", "How do I add a new company holiday to next year's calendar? We are adding the day after Thanksgiving."),
    ("custom_field", "Custom field dropdown", "Can a custom field have more than 50 dropdown options? We need one for job sites."),
    ("offer_letter", "Offer letter template variables", "The salary variable in our offer letter template shows as blank in the preview. Is that expected until it is sent?"),
    ("sso_switch", "SAML setup help", "We are moving identity providers next month. Is there a guide to switching SSO without locking everyone out?"),
    ("future_term", "Termination with future date", "Can I enter a termination now with an effective date of {date}? I don't want them to lose access early."),
    ("import_date", "Bulk import errors", "Our employee import file fails on row {n} with Invalid date. The date looks fine to me, file attached."),
    ("esign_pending", "Document shows pending", "An employee says she signed her handbook acknowledgment but it still shows as pending."),
    ("bulk_manager", "Change manager for a team", "Is there a way to change the manager for {k} people at once?"),
    ("remove_admin", "Remove former admin access", "Please remove admin access for {name}, she left the company."),
    ("audit_export", "Full data export", "We need a full export of employee records for our auditors. What formats are available?"),
    ("card", "Update credit card", "How do I update the card on file? Ours expires this month."),
    ("timezone", "Wrong time zone on timesheets", "Timesheets for our Arizona location show times an hour off. Where is the location time zone set?"),
    ("announcement", "Company announcement not showing", "We posted an announcement but some employees don't see it on their home page. Is it filtered by location?"),
    ("admin_training", "Admin training", "We have a new HR coordinator starting. Do you have training sessions for new admins?"),
    ("deduction_code", "Deduction code question", "Which deduction code should we use for a commuter benefit?"),
    ("new_dept", "Add new department", "How do we add a new department and move people into it without changing their cost center history?"),
    ("emergency", "Emergency contacts required", "Can we make emergency contact a required field for all employees?"),
    ("work_auth", "Work authorization expiry reminders", "Does Pinmoor send reminders when work authorization documents are about to expire?"),
    ("anniv_report", "Report for anniversaries", "How do I build a report of work anniversaries for next month? I want to send cards."),
    ("shift_swap", "Shift swap approvals", "Can shift swaps skip manager approval if both employees are in the same role?"),
    ("welcome_bounce", "Welcome emails bouncing", "New hire welcome emails went to personal addresses that bounce. Can we resend to an updated address?"),
    ("name_change", "Legal name change", "An employee changed her legal name. Will updating it in People update her past documents too?"),
    ("add_seats", "Adding employees before renewal", "Who should I talk to about adding {k} more employees before our renewal?"),
    ("kiosk_pin", "Kiosk PIN reset", "How does a manager reset an employee's kiosk PIN?"),
    ("delegate", "Delegate approvals while on vacation", "Can I delegate my time off approvals to another manager while I'm out for two weeks?"),
    ("ack_report", "Handbook acknowledgment report", "Is there a report of who has not acknowledged the updated handbook?"),
    ("paystub_tile", "Hide pay stub tile", "Our pay stubs live in our payroll provider, not Pinmoor. Can we hide the pay stub tile so employees stop clicking it?"),
    ("spanish", "Spanish language support", "Does the employee side of Pinmoor support Spanish? About a third of our staff would prefer it."),
    ("sandbox", "Sandbox request", "Can we get a sandbox account to test a new onboarding flow before we roll it out?"),
    ("webhook_retry", "Webhook retries", "If our endpoint is down, how many times do webhooks retry?"),
    ("photos_off", "Profile photos", "Can we turn off profile photo uploads for employees?"),
    ("posters", "Digital workplace posters", "Does Pinmoor provide digital workplace posters for remote staff?"),
    ("merge_titles", "Merge duplicate job titles", "We have Sales Associate and Sales Assoc. as separate job titles. Can they be merged?"),
    ("digest", "Too many notification emails", "Managers are getting an email for every single time off request. Can that be a daily digest?"),
    ("admin_2fa", "Two-factor for admins", "Can we require two-factor authentication just for admin users?"),
    ("restore_doc", "Recover deleted document", "I deleted an employee's signed offer letter by mistake. Can it be restored?"),
    ("dup_profile", "Duplicate employee record", "A rehire created a second profile for the same person. How do we merge them?"),
    ("tax_exempt", "Sales tax on invoice", "We are tax exempt, can you remove sales tax from our invoice? Certificate attached."),
    ("onboard_task", "Onboarding task stuck", "An onboarding task assigned to IT is stuck as overdue after IT marked it done."),
    ("new_site", "New location setup", "We opened a new site in {city}. What do we need to set up besides the location record?"),
    ("survey_anon", "Pulse survey anonymity", "If fewer than 5 people answer a pulse survey, can managers see who answered?"),
    ("phone_list", "Export phone list", "Is there a way to export a phone list of all employees for our front desk?"),
    ("salary_bands", "Salary bands", "Can we store salary bands per job title and show them only to HR?"),
    ("custom_role", "Custom role for payroll clerk", "We need a role that can see compensation but not manager notes. Is that possible?"),
    ("typo", "Typo on welcome screen", "The employee welcome screen says Recieve instead of Receive."),
    ("drop_addon", "Downgrade at renewal", "We want to drop one add-on at renewal. What is the notice period?"),
    ("cal_feed", "Time off calendar feed", "The shared time off calendar feed stopped updating in our calendar app. We re-subscribed and it works again, just letting you know."),
    ("delete_data", "Delete former employee data", "A former employee asked us to delete her personal data. How do we do that in Pinmoor?"),
    ("badge_photos", "Download photos for badges", "Can we bulk download employee photos for badge printing?"),
    ("seasonal_billing", "Seasonal employees billing", "Do seasonal employees count toward our billable headcount if they are inactive in the off season?"),
    ("benefit_elig", "Benefits eligibility rule", "How do we set benefits eligibility to start the first of the month after 60 days?"),
]
CITIES = ["Fairhaven", "Dunmore Flats", "Lake Orris", "Port Callan", "Westbrook Hills", "Tillery", "Maren Springs"]

NPS_NOISE = [
    (9, "Easy to use and support is quick.", None), (10, "Onboarding new hires is so much smoother than our old system.", None),
    (9, "Great product.", None), (8, "Does what we need.", None), (10, "The employee directory is the best I have used.", None),
    (10, "Support answered in 10 minutes on a Saturday. Impressed.", None), (7, "Solid overall. Some screens feel dated.", None),
    (9, "Our managers actually use it, which is saying something.", None), (9, "Good value for the price.", None),
    (7, "Setup took longer than we were told, but it has been fine since.", None), (8, "I like it.", None),
    (10, "Document signing saved us a filing cabinet.", None), (9, "Would recommend to other small nonprofits.", None),
    (10, "The implementation team was excellent.", None), (8, "Works.", None),
    (9, "Clean interface, easy for employees who are not tech savvy.", None),
    (5, "Price went up more than I expected at renewal.", "price"), (6, "A bit expensive for a company our size.", "price"),
    (7, "Wish we could customize the employee home page more.", None),
    (8, "Search in the directory could be smarter about nicknames.", None),
    (9, "Time off requests and approvals are simple and our staff like them.", None),
    (7, "The help center articles are out of date in places.", None), (10, "Onboarding checklists are great.", None),
    (6, "Too many emails from the system.", "digest"), (9, "Customer success manager is responsive.", None),
    (7, "I would like more integrations with our applicant tracking system.", None),
    (10, "Employees love having everything in one place.", None),
    (10, "Better than the last three HR systems I have used.", None), (8, "Its fine.", None),
    (7, "The API docs could use more examples.", None),
    (9, "We use maybe half the features but the half we use is great.", None),
    (6, "Hard to find some admin settings.", None), (10, "Very happy.", None), (9, "Kiosk clock in is reliable.", None),
    (9, "Our auditors liked the audit log.", None), (7, "Survey tool is basic.", None),
    (8, "Wish there was a chat integration for approvals.", "N:slack"), (8, "Please add dark mode.", "N:darkmode"),
    (5, "Renewal pricing conversation was frustrating.", "price"),
    (7, "Would like more control over notification settings.", "digest"),
    (9, "The mobile app is handy for approving requests on the go.", None),
    (10, "New hire paperwork used to take a day, now it takes an hour.", None),
    (9, "Everything in one place, reasonable price.", None), (7, "Good, not great.", None),
    (8, "Reports are useful for our small team.", None), (9, "Training videos are helpful.", None),
    (8, "Would give a 10 if bulk edits were easier.", None), (7, "We are still learning the system.", None),
    (10, "Great customer support team, especially Ruth.", None), (9, "Reliable.", None),
    (6, "Admin permissions are too coarse.", "custom_role"), (8, "Custom fields are flexible enough for us.", None),
    (6, "The benefits enrollment flow was confusing for our older employees.", None),
    (10, "I recommend Pinmoor to every HR person I know.", None), (9, "It has improved a lot in the last year.", None),
    (9, "Easy to train new managers on.", None), (9, "The e-signature feature works well.", None),
    (6, "Needs better offline support for remote sites.", None),
    (7, "Spanish translations would help our workforce.", "spanish"),
    (10, "We moved from spreadsheets and this is a huge upgrade.", None), (10, "Implementation was painless.", None),
    (8, "Missing some features compared to bigger platforms, but much simpler.", None),
    (9, "Our CFO likes the cost.", None), (6, "Response times on tickets have gotten slower.", "support_speed"),
    (5, "Support takes a day or two to respond now.", "support_speed"), (8, "Nothing to add.", None),
    (9, "Good for mid-size companies like ours.", None), (8, "Shift scheduling would make this a 10.", "shift_sched"),
    (10, "Love the onboarding portal for new hires.", None),
]
D1_NPS = (2, "Benefits upload has been broken for weeks and support cannot fix it.")

CHURN_NOISE = [
    ("Business changes", "acquired", "We were acquired and the parent company uses its own HR system."),
    ("Business changes", "acquired", "Acquisition closed in July, moving everyone to the buyer's platform."),
    ("Business changes", "acquired", "New owners standardized on their HRIS."),
    ("Business changes", "acquired", ""),
    ("Business changes", "downsized", "We closed two locations and no longer need a full HR platform."),
    ("Business changes", "downsized", "Headcount dropped below 40 after restructuring."),
    ("Business changes", "downsized", "Layoffs. Nothing to do with the product."),
    ("Business changes", "downsized", ""),
    ("Switched provider", "peo", "Moved to a PEO that bundles HR software with benefits."),
    ("Switched provider", "peo", "Our broker recommended a PEO for better health plan rates."),
    ("Switched provider", "peo", "PEO pricing was cheaper once benefits were included."),
    ("Switched provider", "peo", ""),
    ("Price", "price", "Too expensive for our size."),
    ("Price", "price", "Renewal quote was higher than we budgeted."),
    ("Price", "price", "Found a cheaper option that covers the basics."),
    ("Not using it enough", "low_use", "We only used the directory and time off requests."),
    ("Not using it enough", "low_use", "Never finished implementation after our HR manager left."),
    ("Not using it enough", "low_use", "Managers did not adopt it."),
    ("Not using it enough", "low_use", ""),
    ("Other", "champion_left", "Our HR director who chose Pinmoor left and her replacement prefers another tool."),
    ("Other", "champion_left", "New VP of People brought her previous vendor with her."),
    ("Other", "champion_left", ""),
    ("Business changes", "closed", "Company is winding down operations."),
    ("Business changes", "closed", "Business closed."),
    ("Business changes", "closed", ""),
    ("Other", "spreadsheets", "Going back to spreadsheets while we figure out our needs."),
    ("Other", "spreadsheets", ""),
    ("Missing features", "shift_sched", "We needed shift scheduling built in."),
    ("Missing features", "shift_sched", "No scheduling for our restaurant staff."),
    ("Missing features", "shift_sched", ""),
    ("Missing features", "union_rules", "Could not model our union contract rules for seniority and leave."),
    ("Missing features", "union_rules", ""),
    ("Missing features", "multi_country", "We expanded to the UK and Mexico and needed one system for all countries."),
    ("Missing features", "multi_country", "International employees are not supported well enough."),
    ("Missing features", "multi_country", ""),
    ("Switched provider", "suite", "Our accounting software vendor launched an HR add-on we get at a discount."),
    ("Switched provider", "suite", "Consolidating vendors, went with a bigger suite."),
    ("Switched provider", "suite", ""),
    ("Other", "none", "No complaints, just a budget cut."),
    ("Other", "none", "Thanks for the help over the years."),
    ("Other", "none", ""),
    ("Business changes", "seasonal", "Seasonal business, we will probably come back next spring."),
    ("Other", "none", "Pinmoor was fine."),
    ("Business changes", "downsized", "Went from 180 employees to 60."),
    ("Other", "none", "Budget cuts across all software."),
    ("Other", "none", ""),
]

# ------------------------------------------------------------ build rows
raises = []  # (company, tag, source, locator)
for kind, items in (("sales-calls", SALES_CALLS), ("forum", FORUM)):
    for it in items:
        for comp, tag in it["raises"]:
            raises.append((comp, tag, kind, it["path"]))

prose_by_theme = {t: sorted({c for c, tag, *_ in raises if tag == t}) for t in THEMES}
# named companies that must not be given a theme (contradicts their prose)
FORBID = {"T1": {"Quenby Foods", "Pellam Outdoor Supply", "Fenwright Engineering", "Moss & Vane Legal", "Lindqvist Architecture"},
          "T2": {"Fenwright Engineering"},
          "T3": {"Lindqvist Architecture", "Everleigh Staffing", "Canterfield Logistics"},
          "T4": set(), "T5": {"Lindqvist Architecture"}}

def pick_theme_company(theme):
    if random.random() < {"T1": 0.05, "T2": 0.25, "T3": 0.3, "T4": 0.5, "T5": 0.6}[theme]:
        c = random.choice(prose_by_theme[theme])
    else:
        c = random.choice(ACTIVE_GEN)
    return c if c not in FORBID[theme] else pick_theme_company(theme)

tickets = []  # dicts
def add_ticket(company, email, when, subject, body, theme, channel=None):
    tickets.append(dict(created=when, requester=email, company=company, subject=subject, body=body, theme=theme,
                        channel=channel or random.choice(["email", "email", "web form", "chat", "in-app"])))

for t in THEMES:
    start, items = TICKETS[t]
    placed = []
    for it in items:
        subj, body = it[0], it[1]
        if len(it) == 3:
            comp, email, when = placed[it[2]]
            when = when + dt.timedelta(days=random.randint(6, 25), hours=random.randint(1, 5))
            when = min(when, dt.datetime(2026, 9, 14, 16, 0))
        else:
            comp = pick_theme_company(t)
            email = contact(comp)
            when = rand_dt(start, "2026-09-12")
        placed.append((comp, email, when))
        add_ticket(comp, email, when, subj, body, t)

tb = "Tollbridge Ceramics"
tb_emails = ["gwen.abernathy@tollbridgeceramics.example", "hr@tollbridgeceramics.example", "d.okafor@tollbridgeceramics.example"]
d1_dates = sorted(rand_dt("2026-08-10", "2026-09-12") for _ in D1_TICKETS)
for (subj, body), when in zip(D1_TICKETS, d1_dates):
    add_ticket(tb, random.choice(tb_emails[:2] * 3 + tb_emails[2:]), when, subj, body, "D1")

for subj, body in D2_TICKETS:
    add_ticket(random.choice(STAFF_TENANTS), random.choice(STAFF[:3]), rand_dt("2026-07-15", "2026-09-10"), subj, body, "D2", "in-app")

noise_use = {}
while len(tickets) < 300:
    topic, subj, body = random.choice(NOISE_TICKETS)
    if noise_use.get(topic, 0) >= 4:
        continue
    noise_use[topic] = noise_use.get(topic, 0) + 1
    body = body.format(name=f"{random.choice(FIRST)} {random.choice(LAST)}", n=random.randint(60, 400),
                       m=random.randint(40, 59), date=f"{random.randint(9, 10)}/{random.randint(1, 28)}/2026",
                       k=random.randint(8, 45), city=random.choice(CITIES))
    comp = random.choice(ACTIVE_GEN)
    add_ticket(comp, contact(comp), rand_dt("2026-07-01", "2026-09-14"), subj, body, "N:" + topic)

tickets.sort(key=lambda r: r["created"])
PRIORITY = ["low", "normal", "normal", "normal", "high"]
TAGS = {"T1": ["payroll", "integrations", "", "export", "payroll-bridge"], "T2": ["time-off", "", "accruals", "pto"],
        "T3": ["mobile", "", "login", "sso"], "T4": ["reviews", "", "performance"], "T5": ["insights", "", "reporting", "performance"],
        "D1": ["benefits", "", "upload"], "D2": ["", "org-chart", "internal-test"]}
for i, r in enumerate(tickets):
    r["ticket_id"] = 48213 + i
    old = r["created"] < dt.datetime(2026, 9, 1)
    r["status"] = random.choice(["solved", "solved", "closed", "pending"] if old else ["open", "pending", "solved"])
    r["tags"] = random.choice(TAGS.get(r["theme"], ["", "", "how-to", "billing", "account", "question"]))
    r["priority"] = "urgent" if "URGENT" in r["subject"] else random.choice(PRIORITY)

# NPS
nps = []
for t in THEMES:
    for score, text in NPS_THEME[t]:
        c = pick_theme_company(t)
        nps.append(dict(company=c, email=contact(c), score=score, comment=text, theme=t))
for score, text in D2_NPS:
    nps.append(dict(company=random.choice(STAFF_TENANTS), email=random.choice(STAFF), score=score, comment=text, theme="D2"))
nps.append(dict(company=tb, email=tb_emails[0], score=D1_NPS[0], comment=D1_NPS[1], theme="D1"))
for score, text, tag in NPS_NOISE:
    c = random.choice(ACTIVE_GEN)
    nps.append(dict(company=c, email=contact(c), score=score, comment=text, theme=("N:" + tag.replace("N:", "")) if tag else "none"))
while len(nps) < 152:
    c = random.choice(ACTIVE_GEN)
    nps.append(dict(company=c, email=contact(c), score=random.choice([7, 8, 8, 9, 9, 9, 10, 10, 6, 4]), comment="", theme="none"))
for r in nps:
    r["submitted"] = rand_dt("2026-08-17", "2026-09-04")
    r["role"] = random.choice(["HR Admin", "HR Manager", "Payroll", "Owner", "Operations", "People Ops", "Office Manager", "Finance"])
nps.sort(key=lambda r: r["submitted"])

# churn
churn = []
churn_companies = CHURN_POOL[:]
random.shuffle(churn_companies)
def churn_company():
    return churn_companies.pop() if churn_companies else random.choice(ACTIVE_GEN[80:])
for t in THEMES:
    for text in CHURN_THEME[t]:
        cat = random.choice(["Product issues", "Product issues", "Switched provider"])
        churn.append(dict(company=churn_company(), primary=cat, comment=text, theme=t))
for cat, tag, text in CHURN_NOISE:
    churn.append(dict(company=churn_company(), primary=cat, comment=text, theme="N:" + tag))
for r in churn:
    r["email"] = contact(r["company"])
    r["effective"] = rand_dt("2026-07-22", "2026-09-30").date()
    r["submitted"] = min(r["effective"] - dt.timedelta(days=random.randint(3, 20)), dt.date(2026, 9, 14))
    r["tenure"] = random.randint(4, 58)
random.shuffle(churn)
churn.sort(key=lambda r: r["submitted"])

# ------------------------------------------------------------ write fixture
if FIX.exists():
    shutil.rmtree(FIX)
FIX.mkdir()
with open(FIX / "tickets.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["ticket_id", "created_at", "requester_email", "company", "channel", "priority", "status", "tags", "subject", "description"])
    for r in tickets:
        w.writerow([r["ticket_id"], r["created"].strftime("%Y-%m-%d %H:%M"), r["requester"], r["company"], r["channel"],
                    r["priority"], r["status"], r["tags"], r["subject"], r["body"]])
with open(FIX / "nps-verbatims.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["response_id", "submitted_at", "respondent_email", "account_name", "role", "score", "comment"])
    for i, r in enumerate(nps):
        w.writerow([f"NPS-26Q3-{i + 1:04d}", r["submitted"].strftime("%Y-%m-%dT%H:%M:00Z"), r["email"], r["company"], r["role"], r["score"], r["comment"]])
with open(FIX / "churn-survey.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["id", "submitted", "company", "contact", "cancellation_effective", "tenure_months", "primary_reason", "anything_we_could_have_done"])
    for i, r in enumerate(churn):
        w.writerow([701 + i, r["submitted"].isoformat(), r["company"], r["email"], r["effective"].isoformat(), r["tenure"], r["primary"], r["comment"]])
for it in SALES_CALLS + FORUM:
    p = FIX / it["path"]
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(it["text"])

# ------------------------------------------------------------ compute counts
rows = []  # (company, tag, source)
rows += [(r["company"], r["theme"], "tickets", r["requester"]) for r in tickets]
rows += [(r["company"], r["theme"], "nps", r["email"]) for r in nps]
rows += [(r["company"], r["theme"], "churn", r["email"]) for r in churn]
rows += [(c, tag, src, "") for c, tag, src, _ in raises]

def external(company, email):
    return not email.endswith("@" + INTERNAL) and company != INTERNAL

def distinct(tag):
    by_src = {}
    for c, t, src, email in rows:
        if t == tag and external(c, email):
            by_src.setdefault(src, set()).add(c)
    return by_src

counts = {}
for t in THEMES + ["D1", "D2"]:
    by_src = distinct(t)
    counts[t] = dict(total=len(set().union(*by_src.values())) if by_src else 0,
                     by_source={k: len(v) for k, v in sorted(by_src.items())},
                     companies=sorted(set().union(*by_src.values())) if by_src else [])
ticket_volume = {t: sum(1 for r in tickets if r["theme"] == t) for t in THEMES + ["D1", "D2"]}
noise_max = max((len(set().union(*distinct(tag).values())), tag) for tag in {t for _, t, _, _ in rows}
                if tag not in THEMES + ["D1", "D2", "none"])

# ------------------------------------------------------------ checklist
def first_sentence(s):
    return re.split(r"(?<=[.?!])\s", s)[0]

THEME_WHAT = {
    "T1": "Payroll Bridge export to the payroll provider is broken or unreliable since the July 3.14 release (Ledgerline file columns shifted, Tallybook sync mapping error 412 or stuck pending, duplicated or missing rows, wrong earnings codes)",
    "T2": "Time Off accrual balances are calculated wrong (part-time and reduced schedules accrue at full time rate, no proration, carryover cap ignored, rehires accruing from original hire date, tiers not applied)",
    "T3": "Pinmoor Go mobile app keeps logging users out (sign in required on every open, lock screen or network change, SSO sessions of minutes, face unlock not remembered)",
    "T4": "Performance review cycles cannot be edited after launch (questions, rating scale and template locked, reviewers cannot be reassigned, cancelling to fix loses submitted responses)",
    "T5": "Insights reports time out or never load for company-wide or large datasets (blank dashboards, 504s, scheduled reports arriving empty)",
}
PROSE_QUOTES = {
    "T1": [("sales-calls/2026-07-22-greyloch-qbr.txt", "Tallybook has kicked back our file twice now with a mapping error, and both times it was the morning payroll was due."),
           ("forum/integrations/4471-ledgerline-export-columns-moved.md", "Has anyone else had their Ledgerline export file change layout after the July release?")],
    "T2": [("sales-calls/2026-07-30-radleigh-senior-living-renewal-risk.eml.txt", "My caregivers don't believe any number in that app anymore."),
           ("forum/time-off/4480-part-time-accruals-full-time-rate.md", "Our part-timers have about 40% more PTO than they should.")],
    "T3": [("sales-calls/2026-07-16-copperlane-hotels-expansion.md", "since the summer app update they get logged out whenever they lock their phones"),
           ("forum/mobile/4502-pinmoor-go-logging-out.md", "Since updating to app version 5.2 our growers have to sign in every time they open Pinmoor Go.")],
    "T4": [("sales-calls/2026-07-22-greyloch-qbr.txt", "The template was locked the second we launched, so we either live with the wording or throw away two weeks of responses."),
           ("forum/performance/4510-edit-review-questions-after-launch.md", "Do I really have to cancel the whole cycle to change one question?")],
    "T5": [("sales-calls/2026-08-11-westmere-retail-exec-sponsor.md", "Since the end of July any Insights report that covers the full company runs until it times out."),
           ("forum/reporting/4519-insights-report-timeouts.md", "Custom reports that include terminated employees now spin for a few minutes and then show Request timed out.")],
}
DERIVE = ("Distinct customers = distinct customer companies (account/company name) that raised the theme in any source this quarter, "
          "unioned across tickets.csv (company column), nps-verbatims.csv (account_name), churn-survey.csv (company), "
          "sales-calls/ (account named in the note) and forum/ (company in each poster's flair, original posts and replies). "
          "Multiple contacts or tickets from one company count once; a company raising it in several sources counts once; "
          "cross-posted forum duplicates add nothing; Pinmoor staff (pinmoor.example addresses, Pinmoor team or support posters, internal notes) "
          "and prospects are not customers.")

findings = []
order = sorted(THEMES, key=lambda t: -counts[t]["total"])
for i, t in enumerate(order):
    c = counts[t]
    tol = max(2, round(c["total"] * 0.15))
    ev = []
    tk = next(r for r in tickets if r["theme"] == t)
    ev.append({"file": "tickets.csv", "quote": first_sentence(tk["body"])})
    ev.append({"file": "nps-verbatims.csv", "quote": first_sentence(NPS_THEME[t][0][1])})
    ev.append({"file": "churn-survey.csv", "quote": CHURN_THEME[t][0]})
    ev += [{"file": f, "quote": q} for f, q in PROSE_QUOTES[t]]
    findings.append(dict(
        id=f"F{i + 1}",
        what=THEME_WHAT[t],
        evidence=ev,
        counts_if=(f"Reports this as a top problem and gives a distinct-customer count between {c['total'] - tol} and {c['total'] + tol} "
                   f"(true count {c['total']}), with at least one quote that appears verbatim in the files."),
        distinct_customers=c["total"],
        derivation=(f"{DERIVE} Per source distinct companies: {c['by_source']}; union = {c['total']} "
                    f"({ticket_volume[t]} tickets). Companies: {', '.join(c['companies'])}."),
    ))
findings.append(dict(
    id=f"F{len(findings) + 1}",
    what="Ranking of the themes by distinct customers",
    evidence=[],
    counts_if="Presents the themes in an order consistent with distinct customers: " + " > ".join(f"{THEME_WHAT[t].split(' (')[0]} ({counts[t]['total']})" for t in order)
              + ". Swapping two themes whose true counts differ by 3 or less is acceptable. The benefits document upload issue and the org chart PDF issue must not be ranked among them.",
))

exclusions = [
    dict(id="X1", what=f"Benefits enrollment document upload failure: {ticket_volume['D1']} tickets, the largest single cluster in tickets.csv",
         evidence=[{"file": "tickets.csv", "quote": "Please escalate. This is the 10th ticket we have opened for the benefits upload failure."},
                   {"file": "forum/general/4565-benefits-document-upload-fails.md", "quote": "Support says they can only reproduce it on our tenant."}],
         why_not=f"Every ticket, the NPS comment and the forum thread come from one customer, Tollbridge Ceramics (tollbridgeceramics.example addresses). Distinct customers = {counts['D1']['total']}. Ranking it as a top problem by ticket volume is wrong; at most it can be noted as a single-account escalation."),
    dict(id="X2", what=f"Org chart PDF export cuts off names ({ticket_volume['D2']} tickets, {len(D2_NPS)} NPS comments, a forum thread, a sales call note)",
         evidence=[{"file": "tickets.csv", "quote": "Exporting the org chart to PDF cuts off the bottom row of names at the page edge."},
                   {"file": "forum/general/4530-org-chart-pdf-cuts-off-names.md", "quote": "Reproduced in two different browsers on the Alderpoint Sample Co tenant."},
                   {"file": "sales-calls/2026-09-11-moss-vane-legal-checkin.md", "quote": "Harriet did not notice."}],
         why_not="Raised only by Pinmoor staff: every ticket and NPS response is from a pinmoor.example address on sample or demo tenants, the forum posters are Pinmoor team, and the sales note is the account manager's internal note that the customer did not notice. Zero external customers."),
    dict(id="X3", what="Forum cross-posts that duplicate threads in a second category",
         evidence=[{"file": "forum/general/4481-part-time-accruals-full-time-rate.md", "quote": "(Also posted in Time Off, posting here too since that category is quiet.)"},
                   {"file": "forum/general/4503-pinmoor-go-logging-out.md", "quote": "Anyone found a setting for this? Cross-posting from Mobile."},
                   {"file": "forum/integrations/4524-huddlepost-integration-time-off-approvals.md", "quote": "Posting here as well as in Ideas since it is an integration."}],
         why_not="Each is the same poster and company as the original thread (4480, 4502, 4523). Counting them adds customers or mentions that do not exist; they add zero distinct customers."),
    dict(id="X4", what="Hallam Veterinary Partners complaint about part-time accruals being wrong",
         evidence=[{"file": "sales-calls/2026-07-14-hallam-veterinary-discovery.md", "quote": "Their accrual engine does not handle part-time schedules, so every quarter she exports balances to a spreadsheet and fixes them by hand."}],
         why_not="Hallam is a prospect describing its current vendor Staffory, not a Pinmoor customer reporting a Pinmoor problem. Must not be counted toward the accrual theme."),
    dict(id="X5", what="Quenby Foods payroll export issue",
         evidence=[{"file": "sales-calls/2026-07-24-quenby-foods-reviews-upsell.md", "quote": "Abby said the export issue they had back in February was fixed within a week and it has been clean every pay period since."}],
         why_not="Historical (February, previous quarter) and resolved; Quenby reports the export working this quarter. Not a count toward the payroll export theme."),
    dict(id="X6", what="Lindqvist Architecture mobile sign in problem",
         evidence=[{"file": "forum/mobile/4502-pinmoor-go-logging-out.md", "quote": "We saw something similar back in March on the old app and it went away after the 5.0 update."},
                   {"file": "sales-calls/2026-08-27-lindqvist-architecture-checkin.md", "quote": "Paul mentioned the mobile app had a sign in bug a while ago but it has been fine for months."}],
         why_not="Lindqvist describes a past issue that went away before this quarter. They are not affected by the current mobile logout problem and do not count toward it."),
    dict(id="X7", what="Minor requests that look like themes (Huddlepost chat integration for approvals, dark mode, pricing complaints, slower support responses)",
         evidence=[{"file": "forum/ideas/4570-dark-mode.md", "quote": "A dark theme would be easier on the eyes."}],
         why_not=f"Each is raised by only a handful of customers (largest non-theme topic reaches {noise_max[0]} distinct customers), far below the smallest true theme ({min(counts[t]['total'] for t in THEMES)}). Listing them as top problems is wrong, though mentioning them as minor is harmless."),
]

checklist = dict(
    id="stage-feedback-synthesis", company="Pinmoor", category="staged", held_out=True,
    summary=("Synthesize Q3 2026 customer feedback across tickets, NPS, churn survey, sales call notes and forum threads into the top problems, "
             "each with a correct distinct-customer count and verbatim quotes; a good answer finds the five real themes, ranks them by distinct customers, "
             "and does not promote the single-customer upload flood, the staff-only org chart issue, or cross-posted duplicates."),
    findings=findings, exclusions=exclusions, answer=None,
    mistakes_that_matter=[
        "Invented or paraphrased-as-verbatim quotes: every quote presented as a customer quote must exist word for word in the files.",
        "Ranking the benefits document upload issue as a top problem because of ticket volume, when it is one customer (Tollbridge Ceramics).",
        "Counting tickets or mentions instead of distinct customers, inflating counts for themes where one company filed several tickets or appears in several sources.",
        "Including Pinmoor staff (pinmoor.example) feedback, such as the org chart PDF issue, as customer demand.",
        "Double counting forum cross-posts, or counting a prospect's complaint about a competitor (Hallam Veterinary Partners) as a Pinmoor customer problem.",
        "Missing one of the five real themes, especially one that is spread thinly across several sources rather than concentrated in tickets.",
    ],
)
(ROOT / "checklist.json").write_text(json.dumps(checklist, indent=2) + "\n")

print("counts:", json.dumps({t: (counts[t]["total"], counts[t]["by_source"]) for t in counts}))
print("ticket volume:", ticket_volume)
print("largest noise topic:", noise_max)
print("rows: tickets", len(tickets), "nps", len(nps), "churn", len(churn))

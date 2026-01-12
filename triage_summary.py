# Simulated referral triage categories
# 1 = Urgent, 2 = Soon, 3 = Routine

triage_categories = [1, 2, 3, 1, 2, 3, 1]

urgent = triage_categories.count(1)
soon = triage_categories.count(2)
routine = triage_categories.count(3)

print("Total referrals:", len(triage_categories))
print("Urgent referrals:", urgent)
print("Soon referrals:", soon)
print("Routine referrals:", routine)

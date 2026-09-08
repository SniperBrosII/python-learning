# Contact records: name -> dictionary of details
contact_book = {
    "Mom": {"phone": "555-1234", "category": "Family", "city": "Fort Wayne"},
    "Dad": {"phone": "555-4321", "category": "Family", "city": "Fort Wayne"},
    "Sister": {"phone": "555-7777", "category": "Family", "city": "Chicago"},
    "Best Friend": {"phone": "555-8888", "category": "Friend", "city": "Indianapolis"},
    "Roommate": {"phone": "555-3141", "category": "Friend", "city": "Fort Wayne"},
    "Boss": {"phone": "555-0000", "category": "Work", "city": "Chicago"},
    "Professor": {"phone": "555-2718", "category": "Work", "city": "Fort Wayne"},
    "Dentist": {"phone": "555-2222", "category": "Business", "city": "Indianapolis"},
}

# Call log: name -> {month -> minutes talked that month}
# Note: not every contact was called every month.
call_log = {
"Mom": {"Jan": 120, "Feb": 95, "Mar": 140},
"Dad": {"Jan": 45, "Feb": 60, "Mar": 30},
"Sister": {"Jan": 80, "Mar": 70},
"Best Friend": {"Jan": 200, "Feb": 180, "Mar": 220},
"Roommate": {"Feb": 15, "Mar": 25},
"Boss": {"Jan": 60, "Feb": 90, "Mar": 75},
"Professor": {"Feb": 20, "Mar": 35},
"Dentist": {"Jan": 10},
}


# Phase 1: Quick Contacts
quick_contacts = {}
quick_contacts["Mom"] = "555-1234"
quick_contacts["Dad"] = "555-5678"
quick_contacts["Best Friend"] = "555-8888"
quick_contacts["Pizza Place"] = "555-9999"
quick_contacts["Work"] = "555-0000"
print("\n=== Phase 1: Quick Contacts ===")
print(f"Contacts: {quick_contacts}")

## Access and Modify
print("\n--- Access and Modify ---")
print(f"Mom's number: {quick_contacts['Mom']}")
quick_contacts["Dad"] = "555-4321"
quick_contacts["Dentist"] = "555-2222"
print(f"Looking up Grandma: {quick_contacts.get("Grandma", "Contact not found")}")
print(f"Updated Contacts: {quick_contacts}")

## Delete and Analyze
print("\n--- Delete and Analyze ---")
del quick_contacts["Pizza Place"]
old_work = quick_contacts.pop("Work")
print(f"Removed work number: {old_work}")
print(f"Contacts remaining: {len(quick_contacts)}")
print(f"Contact names: {list(quick_contacts.keys())}")
print(f"Contact numbers: {list(quick_contacts.values())}")


# Phase 2: Contact Activity
print("\n=== Phase 2: Contact Activity")
for contact, months in call_log.items():
    num_months = len(months)
    total_minutes = sum(months.values())
    average_minutes = total_minutes / num_months
    busiest_month = max(months, key=months.get)
    busiest_minutes = months[busiest_month]
    print(
        f"{contact}: {num_months} month(s), "
        f"{total_minutes} min total, "
        f"avg: {average_minutes:.2f}, "
        f"busiest: {busiest_month} ({busiest_minutes})"
    )


# Phase 3: Aggregations
print("\n=== Phase 3: Aggregations ===")

## Part A: Month Statistics
month_stats = {}
for contact, months in call_log.items():
    for month, minutes in months.items():
        if month not in month_stats:
            month_stats[month] = {
                "minutes": [],
                "total": 0,
                "avg": 0,
                "contacts": 0
            }
        month_stats[month]["minutes"].append(minutes)
        month_stats[month]["contacts"] += 1
for month, stats in month_stats.items():
    stats["total"] = sum(stats["minutes"])
    stats["avg"] = stats["total"] / len(stats["minutes"])
sorted_months = sorted(
    month_stats.items(),
    key=lambda item: item[1]["avg"],
    reverse=True
)
print("Monthly summary (sorted by average, highest first):")
for month, stats in sorted_months:
    print(f"{month}, {stats["total"]} min total, {stats["avg"]:.2f} avg ({stats["contacts"]} contacts)")

## Part B: Category, city, and headcount rollups
minutes_by_category = {}
minutes_by_city = {}
contacts_per_city = {}
for contact, details in contact_book.items():
    category = details["category"]
    city = details["city"]
    for month, minutes in call_log[contact].items():
        minutes_by_category[category] = (minutes_by_category.get(category, 0) + minutes)
        minutes_by_city[city] = (minutes_by_city.get(city, 0) + minutes)
    contacts_per_city[city] = (contacts_per_city.get(city, 0) + 1)
print(f"Minutes by category: {minutes_by_category}")
print(f"Minutes by city: {minutes_by_city}")
print(f"Contacts per city: {contacts_per_city}")


# Phase 4: Comprehensions
print("\n=== Phase 4: Comprehensions ===")
total_minutes = {
    name: sum(months.values())
    for name, months in call_log.items()
}
phone_book = {name: details["phone"] for name, details in contact_book.items()}
local_contacts = {name: details["phone"] for name, details in contact_book.items() if details["city"] == "Fort Wayne"}
activity_level = {name: ("Frequent" if minutes >= 200 else "Occasional") for name, minutes in total_minutes.items()}
print(f"Phone book: {phone_book}")
print(f"Local contacts (Fort Wayne): {local_contacts}")
print(f"Activity level: {activity_level}")


# Phase 5: Tier Report
print("\n=== Phase 5: Tier Report ===")
counts = {
    "Platinum": 0,
    "Gold": 0,
    "Silver": 0,
    "Bronze": 0,
    "Inactive": 0
}

## Part A: Classify
def get_tier(minutes):
    if minutes >= 400:
        counts["Platinum"] += 1
        return "Platinum"
    elif minutes >= 200:
        counts["Gold"] += 1
        return "Gold"
    elif minutes >= 100:
        counts["Silver"] += 1
        return "Silver"
    elif minutes >= 50:
        counts["Bronze"] += 1
        return "Bronze"
    else:
        counts["Inactive"] +=1
        return "Inactive"
for name, minutes in total_minutes.items():
    print(f"{name}: {minutes} min ({get_tier(minutes)})")
    
## Part B: Count
print("\n--- Tier Distribution ---")
for tier, count in counts.items():
    print(f"{tier}: {count}")

## Part C: Rank
print("\n--- Top and Bottom ---")
most_person = ""
most_minutes = 0
least_person = ""
least_minutes = float("inf")
grand_total = 0
for contact, minutes in total_minutes.items():
    grand_total += minutes
    if minutes > most_minutes:
        most_minutes = minutes
        most_person = contact
    if minutes < least_minutes:
        least_minutes = minutes
        least_person = contact
avg = grand_total / len(total_minutes)
print(f"Most Contacted: {most_person} ({most_minutes} min)")
print(f"Least Contacted: {least_person} ({least_minutes} min)")
print(f"Total minutes: {grand_total}")
print(f"Average per contact: {avg:.2f}")
print("\n--- Above Average Contacts ---")
for contact, minutes in total_minutes.items():
    if minutes > avg:
        print(f"{contact}: {minutes} min")


# Phase 6: Contact Hub Report
print("\n=== Phase 6: Contact Hub Report ===")
sorted_contacts = sorted(
    total_minutes.items(),
    key=lambda item: item[1],
    reverse=True
)
print(f"{'Name':<12}{'Category':<12}{'City':<15}{'Minutes':>8} {'Tier':<10}")
print("-" * 60)
for name, total in sorted_contacts:
    category = contact_book[name]["category"]
    city = contact_book[name]["city"]
    tier = get_tier(total)
    print(f"{name:<12}{category:<12}{city:<15}{total:>8} {tier:<10}")
print("-" * 60)
print(f"{len(total_minutes)} contacts | {grand_total} total minutes | {avg} average")
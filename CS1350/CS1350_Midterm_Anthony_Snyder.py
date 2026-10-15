# Problem 1: Library Catalogue
print("Problem 1: Library Catalogue")
class Library:
    def __init__(self):
        self.books = {}
    def add_book(self, isbn, title, author, copies):
        if isbn in self.books:
            self.books[isbn]["copies"] += copies
        else:
            self.books[isbn] = {
                "title": title,
                "author": author,
                "copies": copies
            }
    def checkout(self, isbn):
        if isbn not in self.books:
            return f"{False} (unknown)"
        elif self.books[isbn]["copies"] == 0:
            return f"{False} (none left)"
        else:
            self.books[isbn]["copies"] -= 1
            return True
    def by_author(self, author):
        titles = [
            book["title"]
            for book in self.books.values()
            if book["author"].lower() == author.lower()
        ]
        return sorted(titles)
    def inventory_value(self, prices):
        total = 0
        for isbn, book in self.books.items():
            if isbn in prices:
                total += book["copies"] * prices[isbn]
        return total
    def low_stock(self, threshold):
        return {
            isbn: book["copies"]
            for isbn, book in self.books.items()
            if book["copies"] < threshold
        }
lib = Library()
lib.add_book("111", "Python Basics", "Jane Doe", 2)
lib.add_book("222", "Data Science", "John Roe", 1)
lib.add_book("333", "Advanced Python", "Jane Doe", 3)
lib.add_book("111", "Python Basics", "Jane Doe", 1)
print(lib.checkout("222"))
print(lib.checkout("222"))
print(lib.checkout("999"))
print(lib.by_author("jane doe"))
print(lib.inventory_value({"111": 20.0, "333": 30.0, "999": 5.0}))
print(lib.low_stock(3))


# Problem 2: Conference Sessions with Sets
print("\nProblem 2: Conference Sessions with Sets")
class Session:
    def __init__(self, title):
        self.title = title
        self.attendees = set()
    def register(self, name):
        self.attendees.add(name)
    def unregister(self, name):
        self.attendees.discard(name)
    def attendee_count(self):
        return len(self.attendees)
def attended_all(sessions):
    if not sessions:
        return set()
    result = sessions[0].attendees.copy()
    for session in sessions[1:]:
        result &= session.attendees
    return result
def attended_exactly_one(sessions):
    counts = {}
    for session in sessions:
        for name in session.attendees:
            counts[name] = counts.get(name, 0) + 1
    return {name for name, count in counts.items() if count == 1}
def no_shows(registered, sessions):
    all_attendees = set()
    for session in sessions:
        all_attendees |= session.attendees
    return registered - all_attendees
def summary(sessions):
    all_attendees = set()
    for session in sessions:
        print(f"{session.title}: {session.attendee_count()} attendees")
        all_attendees |= session.attendees
    print(f"Distinct attendees: {len(all_attendees)}")
keynote = Session("Keynote")
for p in ["Ana", "Ben", "Cruz", "Dee"]:
    keynote.register(p)
workshop = Session("Workshop")
for p in ["Ana", "Cruz", "Eli"]:
    workshop.register(p)
panel = Session("Panel")
for p in ["Ana", "Dee", "Eli", "Fay"]:
    panel.register(p)
workshop.unregister("Eli")
workshop.unregister("Zed")
print(workshop.attendee_count())
sessions = [keynote, workshop, panel]
print(attended_all(sessions))
print(attended_exactly_one(sessions))
print(no_shows({"Ana", "Ben", "Fay", "Gus"}, sessions))
summary(sessions)
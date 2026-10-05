# Problem 1: Employee Payroll System with Polymorphism
from abc import ABC, abstractmethod
class Employee(ABC):
    def __init__(self, name: str, employee_id: str):
        self.name = name
        self.employee_id = employee_id
    @abstractmethod
    def calculate_pay(self) -> float:
        pass
    @abstractmethod
    def description(self) -> str:
        pass
    def pay_stub(self) -> str:
        pay = self.calculate_pay()
        return f"{self.name} (ID: {self.employee_id}): ${pay:.2f}"
    @staticmethod
    def validate_positive(value: float, name: str) -> bool:
        if value <= 0:
            raise ValueError(f"{name} must be positive!")
        return True
class SalariedEmployee(Employee):
    def __init__(self, name: str, employee_id: str, annual_salary: float):
        super().__init__(name, employee_id)
        Employee.validate_positive(annual_salary, "annual_salary")
        self.annual_salary = annual_salary
    def calculate_pay(self) -> float:
        return self.annual_salary / 24
    def description(self) -> str:
        return f"Salaried: {self.name}"
class HourlyEmployee(Employee):
    def __init__(self, name: str, employee_id: str, hourly_rate: float, hours_worked: float):
        super().__init__(name, employee_id)
        Employee.validate_positive(hourly_rate, "hourly_rate")
        Employee.validate_positive(hours_worked, "hours_worked")
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
    def calculate_pay(self) -> float:
        if self.hours_worked <= 40:
            return self.hourly_rate * self.hours_worked
        else:
            regular_pay = self.hourly_rate * 40
            overtime_hours = self.hours_worked - 40
            overtime_pay = overtime_hours * (self.hourly_rate * 1.5)
            return regular_pay + overtime_pay
    def description(self) -> str:
        return f"Hourly: {self.name}"
class CommissionEmployee(Employee):
    def __init__(self, name: str, employee_id: str, base_salary: float, sales: float, commission_rate: float):
        super().__init__(name, employee_id)
        Employee.validate_positive(base_salary, "base_salary")
        Employee.validate_positive(sales, "sales")
        if commission_rate <= 0 or commission_rate > 1.0:
            raise ValueError("commission_rate must be positive!")
        self.base_salary = base_salary
        self.sales = sales
        self.commission_rate = commission_rate
    def calculate_pay(self) -> float:
        return self.base_salary + (self.sales * self.commission_rate)
    def description(self) -> str:
        return f"Commission: {self.name}"
class Payroll:
    def __init__(self):
        self.employees = []
    def add_employee(self, employee: Employee):
        self.employees.append(employee)
    def total_payroll(self) -> float:
        return sum(emp.calculate_pay() for emp in self.employees)
    def print_all_stubs(self):
        for emp in self.employees:
            print(emp.pay_stub())
if __name__ == "__main__":
    alice = SalariedEmployee("Alice Johnson", "E001", 84000)
    bob = HourlyEmployee("Bob Smith", "E002", 25.00, 45)
    carol = CommissionEmployee("Carol Davis", "E003", 2000, 50000, 0.05)
    print("Employee Descriptions:")
    for emp in [alice, bob, carol]:
        print(f"  {emp.description()}")
    print("\nPay Stubs:")
    for emp in [alice, bob, carol]:
        print(f"  {emp.pay_stub()}")
    payroll = Payroll()
    payroll.add_employee(alice)
    payroll.add_employee(bob)
    payroll.add_employee(carol)
    print(f"\nTotal Payroll: ${payroll.total_payroll():.2f}")
    print(f"\nTesting validation:")
    try:
        bad = SalariedEmployee("Bad", "E999", -50000)
    except ValueError as e:
        print(f"  Caught: {e}")
    try:
        bad = CommissionEmployee("Bad", "E999", 1000, 5000, 1.5)
    except ValueError as e:
        print(f"  Caught: {e}")


# Problem 2: Music Library with Factory Methods
class Song:
    total_songs = 0
    def __init__(self, title: str, artist: str, duration_seconds: int):
        self.title = title
        self.artist = artist
        self.duration_seconds = duration_seconds
        Song.total_songs += 1
    def display(self) -> str:
        formatted_time = self.format_duration(self.duration_seconds)
        return f"{self.title} - {self.artist} ({formatted_time})"
    @classmethod
    def from_string(cls, s: str):
        parts = [part.strip() for part in s.split("|")]
        title = parts[0]
        artist = parts[1]
        duration_seconds = cls.parse_duration(parts[2])
        return cls(title, artist, duration_seconds)
    @classmethod
    def get_total_songs(cls) -> int:
        return cls.total_songs
    @staticmethod
    def format_duration(seconds: int) -> str:
        minutes = seconds // 60
        rem_seconds = seconds % 60
        return f"{minutes}:{rem_seconds:02d}"
    @staticmethod
    def parse_duration(duration_str: str) -> int:
        minutes, seconds = duration_str.split(":")
        return int(minutes) * 60 + int(seconds)
class Playlist:
    total_playlists = 0
    def __init__(self, name: str):
        Playlist.total_playlists += 1
        self.name = name
        self.playlist_id = f"PL_{Playlist.total_playlists:03d}"
        self.songs = []
    def add_song(self, song: Song):
        self.songs.append(song)
    def total_duration(self) -> int:
        return sum(song.duration_seconds for song in self.songs)
    def display(self) -> str:
        count = len(self.songs)
        formatted_duration = Song.format_duration(self.total_duration())
        return f"Playlist: {self.name} ({count} songs, {formatted_duration})"
    @classmethod
    def get_total_playlists(cls) -> int:
        return cls.total_playlists
class LibraryManager:
    @staticmethod
    def create_playlist_from_strings(name: str, song_strings: list) -> Playlist:
        playlist = Playlist(name)
        for s in song_strings:
            song = Song.from_string(s)
            playlist.add_song(song)
        return playlist
    @staticmethod
    def format_library_report(playlists: list) -> str:
        lines = ["=== Library Report ==="]
        for pl in playlists:
            lines.append(f"Playlist: {pl.name}")
            for idx, song in enumerate(pl.songs, start=1):
                lines.append(f"  {idx}. {song.display()}")
            formatted_dur = Song.format_duration(pl.total_duration())
            lines.append(f"  Duration: {formatted_dur}\n")
        lines.append(f"Total Songs: {Song.get_total_songs()}")
        lines.append("========================")
        return "\n".join(lines)
if __name__ == "__main__":
    s1 = Song("Bohemian Rhapsody", "Queen", 354)
    s2 = Song("Imagine", "John Lennon", 187)
    print("\nIndividual songs:")
    print(f"  {s1.display()}")
    print(f"  {s2.display()}")
    s3 = Song.from_string("Hotel California | Eagles | 6:31")
    print(f"  {s3.display()}")
    print(f"\nFormat 245 seconds: {Song.format_duration(245)}")
    print(f"Parse '4:05': {Song.parse_duration('4:05')} seconds")
    playlist = Playlist("Classic Rock")
    playlist.add_song(s1)
    playlist.add_song(s2)
    playlist.add_song(s3)
    print(f"\n{playlist.display()}")
    chill_songs = [
        "Weightless | Marconi Union | 8:09",
        "Electra | Airstream | 5:51",
        "Mellomaniac | DJ Shah | 7:34"
    ]
    chill = LibraryManager.create_playlist_from_strings("Chill Vibes", chill_songs)
    print(f"{chill.display()}")
    print(f"\n{LibraryManager.format_library_report([playlist, chill])}")
    print(f"Total songs created: {Song.get_total_songs()}")
    print(f"Total playlists created: {Playlist.get_total_playlists()}")


# Problem 3: Smart GradeBook with Operator Overloading
class GradeBook:
    def __init__(self, course_name: str):
        self.course_name = course_name
        self.grades = {}
    def __str__(self) -> str:
        return f"GradeBook: {self.course_name} ({len(self.grades)} students)"
    def __repr__(self) -> str:
        return f"GradeBook('{self.course_name}')"
    def __len__(self) -> int:
        return len (self.grades)
    def __getitem__(self, student: str) -> float:
        if student not in self.grades:
            raise KeyError(f"Student '{student}' not found in GradeBook.")
        return self.grades[student]
    def __setitem__(self, student: str, grade: float):
        """Stores grade; raises ValueError if grade is not between 0 and 100."""
        if not (0 <= grade <= 100):
            raise ValueError("Grade must be between 0 and 100")
        self.grades[student] = float(grade)
    def __contains__(self, student: str) -> bool:
        """Returns True if student has a grade in the gradebook[cite: 10, 25]."""
        return student in self.grades
    def __iter__(self):
        """Allows iterating over student names[cite: 10, 25]."""
        return iter(self.grades)
    def __bool__(self) -> bool:
        """Returns True if the gradebook has any students[cite: 10, 25]."""
        return len(self.grades) > 0
    @property
    def average(self) -> float:
        """Returns mean grade, or 0.0 if empty[cite: 10, 25]."""
        if not self.grades:
            return 0.0
        return sum(self.grades.values()) / len(self.grades)
    def __add__(self, other: "GradeBook") -> "GradeBook":
        """Merges two gradebooks into a NEW one keeping higher grades[cite: 10, 25]."""
        new_name = f"{self.course_name} + {other.course_name}"
        new_gb = GradeBook(new_name)
        for student, grade in self.grades.items():
            new_gb[student] = grade
        for student, grade in other.grades.items():
            if student in new_gb:
                new_gb[student] = max(new_gb[student], grade)
            else:
                new_gb[student] = grade
        return new_gb
    def __iadd__(self, other: "GradeBook") -> "GradeBook":
        """In-place merge (gb1 += gb2), keeping higher grades[cite: 10, 25]."""
        for student, grade in other.grades.items():
            if student in self.grades:
                self.grades[student] = max(self.grades[student], grade)
            else:
                self[student] = grade
        return self
    def __mul__(self, factor: float) -> "GradeBook":
        """Returns new GradeBook with all grades multiplied by factor (capped at 100)[cite: 10, 25]."""
        new_name = f"{self.course_name} (curved)"
        new_gb = GradeBook(new_name)
        for student, grade in self.grades.items():
            curved_grade = min(100.0, grade * factor)
            new_gb[student] = curved_grade
        return new_gb
    def __eq__(self, other: object) -> bool:
        """Equal if averages are within 0.01 tolerance."""
        if not isinstance(other, GradeBook):
            return False
        return abs(self.average - other.average) < 0.01
    def __lt__(self, other: "GradeBook") -> bool:
        """Less than if lower average[cite: 10, 26, 27]."""
        if abs(self.average - other.average) < 0.01:
            return False
        return self.average < other.average
    def __le__(self, other: "GradeBook") -> bool:
        """Less than or equal if lower average or within 0.01 tolerance[cite: 10, 26, 27]."""
        return self < other or self == other
if __name__ == "__main__":
    print("\n=== Part A: Container Protocol ===")
    cs101 = GradeBook("CS 101")
    cs101["Alice"] = 92
    cs101["Bob"] = 78
    cs101["Carol"] = 88
    cs101["David"] = 95
    print(cs101)
    print(repr(cs101))
    print(f"Alice's grade: {cs101['Alice']:.0f}")
    print(f"Bob enrolled? {'Bob' in cs101}")
    print(f"Eve enrolled? {'Eve' in cs101}")
    print(f"Class size: {len(cs101)}")
    print("Students:")
    for student in cs101:
        print(f"  {student}: {cs101[student]:.0f}")
    empty = GradeBook("Empty")
    print(f"cs101 has students? {bool(cs101)}")
    print(f"empty has students? {bool(empty)}")
    print("\nValidation test:")
    try:
        cs101["Eve"] = 150
    except ValueError as e:
        print(f"  Caught: {e}")
    print("\n=== Part B: Arithmetic ===")
    math201 = GradeBook("Math 201")
    math201["Alice"] = 85
    math201["Bob"] = 90
    math201["Eve"] = 76
    combined = cs101 + math201
    print(f"\n{combined}")
    print("Merged grades:")
    for student in combined:
        print(f"  {student}: {combined[student]:.0f}")
    curved = math201 * 1.1
    print(f"\n{curved}")
    print("Curved grades:")
    for student in curved:
        print(f"  {student}: {curved[student]:.1f}")
    big_curve = math201 * 1.5
    print(f"\nBig curve — Bob's grade: {big_curve['Bob']:.0f}")
    print("\n=== Part C: Comparisons ===")
    print(f"CS 101 average: {cs101.average:.2f}")
    print(f"Math 201 average: {math201.average:.2f}")
    print(f"CS 101 == Math 201? {cs101 == math201}")
    print(f"Math 201 < CS 101? {math201 < cs101}")
    print(f"Math 201 <= CS 101? {math201 <= cs101}")
    classes = [math201, cs101, curved]
    classes.sort()
    print("\nSorted by average:")
    for gb in classes:
        print(f"  {gb} — avg: {gb.average:.2f}")
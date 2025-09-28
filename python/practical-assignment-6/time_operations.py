# time_operations.py

class Time:
    def __init__(self, hrs=0, minutes=0):
        self.hrs = hrs
        self.minutes = minutes
        self.normalize()

    def normalize(self):
        """Normalize time so that minutes < 60."""
        if self.minutes >= 60:
            self.hrs += self.minutes // 60
            self.minutes = self.minutes % 60
        elif self.minutes < 0:
            borrow = (-self.minutes + 59) // 60
            self.hrs -= borrow
            self.minutes += borrow * 60
        if self.hrs < 0:
            self.hrs = 0
            self.minutes = 0

    def __add__(self, other):
        return Time(self.hrs + other.hrs, self.minutes + other.minutes)

    def __sub__(self, other):
        total_self = self.hrs * 60 + self.minutes
        total_other = other.hrs * 60 + other.minutes
        diff = abs(total_self - total_other)
        return Time(diff // 60, diff % 60)

    def __mul__(self, factor):
        total_minutes = (self.hrs * 60 + self.minutes) * factor
        return Time(total_minutes // 60, total_minutes % 60)

    def __str__(self):
        return f"{self.hrs} hr(s) {self.minutes} min(s)"

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            f.write(f"{self.hrs},{self.minutes}\n")

    @staticmethod
    def read_from_file(filename):
        try:
            with open(filename, 'r') as f:
                line = f.readline().strip()
                if line:
                    hrs, minutes = map(int, line.split(','))
                    return Time(hrs, minutes)
        except FileNotFoundError:
            print(f"File {filename} not found.")
        return Time()


 # Create two process times
p1 = Time(2, 30)
p2 = Time(3, 40)

print("Process P1:", p1)
print("Process P2:", p2)

# Add times
total_time = p1 + p2
print("Total Time (P1 + P2):", total_time)

# Difference of times
diff_time = p1 - p2
print("Difference (P1 - P2):", diff_time)

# Multiply time
p1_times_3 = p1 * 3
print("P1 * 3:", p1_times_3)

# Save total_time to file
total_time.save_to_file("total_time.txt")
print("Total time saved to total_time.txt")

# Read time from file
loaded_time = Time.read_from_file("total_time.txt")
print("Loaded time from file:", loaded_time)

   
# student.py

class Student:
    def __init__(self, student_id, student_name):
        self._student_id = student_id      # protected data
        self._student_name = student_name  # protected data

    def get_details(self):
        """Return student ID and name as a tuple"""
        return (self._student_id, self._student_name)


class Marks(Student):
    def __init__(self, student_id, student_name, marks_dict):
        super().__init__(student_id, student_name)
        self.marks = marks_dict  # dictionary {subject: mark}

    def total_marks(self):
        """Calculate and return total marks"""
        return sum(self.marks.values())

    def add_subject(self, subject, mark):
        """Add a new subject and mark"""
        self.marks[subject] = mark

    def update_mark(self, subject, mark):
        """Update existing subject mark"""
        if subject in self.marks:
            self.marks[subject] = mark

    def get_subjects(self):
        """Return list of all subjects"""
        return list(self.marks.keys())

    def get_marks(self):
        """Return list of all marks"""
        return list(self.marks.values())

    def average_marks(self):
        """Return average marks"""
        return sum(self.marks.values()) / len(self.marks) if self.marks else 0

#!/usr/bin/env python

from user import User
import random


class Teacher(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = [random.randint(1, 100) for _ in range(15)]

    def teach(self):
        if self.knowledge:
            random_knowledge = random.choice(self.knowledge)
            return f"Teaching about {random_knowledge}..."
        else:
            return "Nothing to teach right now."

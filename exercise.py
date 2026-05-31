# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Function to reverse a string without using [::-1]
def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

# Function to find the most common word in a sentence
def most_common_word(sentence):
    words = sentence.split()
    word_count = {}
    
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    
    most_common = max(word_count, key=word_count.get)
    return most_common


class TodoApp:
    """A simple in-memory to-do app storing tasks in a list."""

    def __init__(self):
        self.tasks = []

    def _validate_task(self, task):
        if task is None:
            raise TypeError("Task must be a string")
        if not isinstance(task, str):
            raise TypeError("Task must be a string")
        if task.strip() == "":
            raise ValueError("Task cannot be empty")

    def add_task(self, task):
        self._validate_task(task)
        if task in self.tasks:
            raise ValueError("Task already exists")
        self.tasks.append(task)

    def remove_task(self, task):
        self._validate_task(task)
        if task not in self.tasks:
            raise ValueError("Task does not exist")
        self.tasks.remove(task)

    def list_tasks(self):
        return list(self.tasks)

    def mark_complete(self, task):
        self._validate_task(task)
        if task not in self.tasks:
            raise ValueError("Task does not exist")
        if task.endswith(" [DONE]"):
            return
        completed_task = f"{task} [DONE]"
        self.tasks[self.tasks.index(task)] = completed_task


todo_app = TodoApp()


def add_task(task):
    return todo_app.add_task(task)


def remove_task(task):
    return todo_app.remove_task(task)


def list_tasks():
    return todo_app.list_tasks()


def mark_complete(task):
    return todo_app.mark_complete(task)

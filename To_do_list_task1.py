class ToDoList:
  def __init__(self):
      self.tasks = []

  def add_task(self, task):
      self.tasks.append(task)
      print(f"Task '{task}' added!")

  def remove_task(self, task):
      if task in self.tasks:
          self.tasks.remove(task)
          print(f"Task '{task}' removed!")
      else:
          print("Task not found!")

  def view_tasks(self):
      if not self.tasks:
          print("No tasks in the list!")
      else:
          print("Your To-Do List:")
          for idx, task in enumerate(self.tasks, 1):
              print(f"{idx}. {task}")

if __name__ == "__main__":
  todo = ToDoList()
  while True:
      print("\n1. Add Task\n2. Remove Task\n3. View Tasks\n4. Exit")
      choice = int(input("Choose an option: "))

      if choice == 1:
          task = input("Enter the task: ")
          todo.add_task(task)
      elif choice == 2:
          task = input("Enter the task to remove: ")
          todo.remove_task(task)
      elif choice == 3:
          todo.view_tasks()
      elif choice == 4:
          print("Exiting To-Do List Application.")
          break
      else:
          print("Invalid option!")

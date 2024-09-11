class Worker:
    def __init__(self, worker_num, fname, lname, work_experience_company, salary, age):
        self.worker_num = worker_num
        self.fname = fname
        self.lname = lname
        self.work_experience_company = work_experience_company
        self.salary = salary
        self.age = age

    def worker_information(self):
        print(f"Worker num: {self.worker_num}")
        print(f"First name: {self.fname}")
        print(f"Last name: {self.lname}")
        print(f"Work experience company: {self.work_experience_company}")
        print(f"Salary: {self.salary}")
        print(f"Age: {self.age}")

    def salary_bonus(self):
        if self.work_experience_company < 5:
            return round(self.salary * (0.5 / 100), 2)
        elif self.work_experience_company > 10:
            return round(self.salary * (2 / 100), 2)
        else:
            return round(self.salary * (1.5 / 100), 2)


def search_by_num(workers_list, worker_num):
    found_worker = [worker for worker in workers_list if worker.worker_num == worker_num]
    if(found_worker):
        print(bool(found_worker))

def search_by_name_experience(workers_list, fname, work_experience_company):
    found_workers = [worker for worker in workers_list if worker.fname.lower() == fname.lower() and
                      worker.work_experience_company == work_experience_company]

    if found_workers:
        for worker in found_workers:
            worker.worker_information()
    else:
        print("No worker found with that name or years of experience")

def add_worker(workers_list, worker):
    workers_list.append(worker)

def remove_worker( worker_num):
    global workers_list
    delete_worker = [worker for worker in workers_list if worker.worker_num == worker_num]
    if delete_worker:
        workers_list.remove(delete_worker[0])
        print("Information deleted")
    else:
        print("Wrong worker_num")


if __name__ == "__main__":
    workers_list = []

    # Adding workers
    add_worker(workers_list, Worker(1, "John", "Doe", 3, 50000, 30))
    add_worker(workers_list, Worker(2, "Jane", "Smith", 6, 60000, 25))

    # Searching for a worker
    print("Searching for John with CompanyA experience:")
    search_by_name_experience(workers_list, "John", 3)

    print("\nSearching worker with num 1:")
    search_by_num(workers_list , 1)


    # Removing a worker
    print("\nRemoving worker with num 1:")
    remove_worker(1)

    # Trying to remove a non-existent worker
    print("\nTrying to remove worker with num 3:")
    remove_worker( 3)

    # Example of using salary_bonus
    print("\nSalary bonus for remaining workers:")
    for worker in workers_list:
        print(f"Worker {worker.worker_num} bonus: {worker.salary_bonus()}")




class Job(object):
    def __init__(self, description):
        self.description = description
        self.previous = None
        self.next = None


    def execute(self):
        pass



class JobPool(object):

    def __init__(self):
        self.jobs = []
        self.head = None
        self.tail = None

    def add_job(self, job):
        # check if there is a head
        if self.head is None:
            self.head = job
            self.tail = job
        else:
            job.previous = self.tail
            self.tail.next = job
            self.tail = self.tail.next


    def get_job(self):
        # get head (job) and we will return this once we reassign head.
        if self.head is None:
            return None

        job = self.head
        # reassign head
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            # new head needs previous to point to None, next is unchanged
            self.head.previous = None

        job.next = None
        return job

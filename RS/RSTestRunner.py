import random
import time


class RSTestRunner(object):
    """
    RSTestRunner is a utility to check the performance of
    different RScoders
    """

    def __init__(self, n, k):
        self.n = n
        self.k = k

    def random_message(self):
        msg = []
        for i in range(self.k):
            msg.append(random.randint(0, 255))
        return msg

    @classmethod
    def corrupt_message(cls, msg, err_count, group_errors=False):
        if group_errors:
            position = random.randint(0,  len(msg) - 1)
            for i in range(err_count):
                pos = (position + i) % len(msg)
                choices = [x for x in range(0, 256) if x != msg[pos]]
                msg[pos] = random.choice(choices)
            return msg
        else:
            positions = random.sample(range(0, len(msg)), err_count)
            for pos in positions:
                choices = [x for x in range(0, 256) if x != msg[pos]]
                msg[pos] = random.choice(choices)
            return msg

    def test(self, coder, err_count, sample_count, group_errors=False):
        success_count = 0
        failure_count = 0
        start_time = time.time()

        for i in range(sample_count):
            print("Checking sample nr: ", i + 1)
            msg = self.random_message()
            msgecc = coder.encode(msg, self.n - self.k)
            corrupted = self.corrupt_message(msgecc, err_count, group_errors)

            corrected_message, corrected_ecc = coder.decode(corrupted,
                                                            self.n - self.k)
            intersection = [i for i, j in zip(msg, corrected_message) if i == j]

            if len(intersection) == len(msg):
                success_count += 1
            else:
                failure_count += 1

        duration = time.time() - start_time
        return success_count, failure_count, duration

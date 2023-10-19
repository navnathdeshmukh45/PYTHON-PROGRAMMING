import time

class CountdownTimer:
    def __init__(self, duration):
        self.duration = duration
        self.start_time = None
        self.paused = False
        self.paused_time = None

    def start(self):
        self.start_time = time.time()
        while True:
            if self.paused:
                continue

            elapsed_time = time.time() - self.start_time
            remaining_time = max(self.duration - elapsed_time, 0)

            minutes, seconds = divmod(remaining_time, 60)
            minutes = int(minutes)
            seconds = int(seconds)

            print(f"Time Remaining: {minutes:02d}:{seconds:02d}", end="\r")

            if remaining_time <= 0:
                break

            time.sleep(1)

    def reset(self):
        self.start_time = None
        self.paused = False
        self.paused_time = None

    def stop(self):
        self.reset()
        print("Timer stopped.")

    def pause(self):
        if self.paused:
            print("Timer is already paused.")
        else:
            self.paused = True
            self.paused_time = time.time()
            print("Timer paused.")

    def resume(self):
        if not self.paused:
            print("Timer is not paused.")
        else:
            self.paused = False
            pause_duration = time.time() - self.paused_time
            self.start_time += pause_duration
            print("Timer resumed.")


# Example usage
timer = CountdownTimer(180)  # Set the duration to 180 seconds (3 minutes)
timer.start()

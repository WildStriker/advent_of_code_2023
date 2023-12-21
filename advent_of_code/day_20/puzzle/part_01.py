"""Part 1 Module"""
import collections
import queue

from .parse import PendingPulse, Pulse, parse_input


def answer_01(file_input: str):
    """Part 1"""

    pulse_count = collections.defaultdict(int)

    modules = parse_input(file_input)

    pending_queue = queue.Queue()
    for _ in range(1000):
        # push the button!
        pending_queue.put(PendingPulse("button", Pulse.LOW, {"broadcaster"}))

        while not pending_queue.empty():
            pending = pending_queue.get()

            for output in pending.outputs:
                pulse_count[pending.pulse] += 1

                if output not in modules:
                    continue

                new_pending = modules[output].send(
                    pending.origin, pending.pulse)

                if not new_pending:
                    continue

                # add new pending pulses to the stack for further processing
                pending_queue.put(new_pending)

    return pulse_count[Pulse.HIGH] * pulse_count[Pulse.LOW]

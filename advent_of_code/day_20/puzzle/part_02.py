"""Part 2 Module"""
import math
import queue

from .parse import Conjuction, PendingPulse, Pulse, parse_input


def answer_02(file_input: str):
    """Part 2"""

    modules = parse_input(file_input)

    target_module = "rx"

    input_module = None
    for module in modules.values():
        if target_module in module.outputs:
            input_module = module

    if not input_module and isinstance(input_module, Conjuction):
        raise ValueError(
            f"Unable to a Conjunction module input for the target module: {target_module}"
        )

    pending_queue = queue.Queue()
    # track all input modules, we need these all to be HIGH at the same time
    # the LCM of each of their button presses should get us the total counts!
    button_presses_per_output = {}
    button_presses = 0
    while True:
        # push the button!
        button_presses += 1
        pending_queue.put(PendingPulse("button", Pulse.LOW, {"broadcaster"}))

        while not pending_queue.empty():
            pending = pending_queue.get()

            # for all inputs that make the conjution store the
            # total button presses to takes to get a HIGH value
            if input_module.name in pending.outputs:
                if pending.pulse == Pulse.HIGH and pending.origin not in button_presses_per_output:
                    button_presses_per_output[pending.origin] = button_presses

                    # all button press counts found, calculate the total and return the result
                    if button_presses_per_output.keys() == input_module.inputs.keys():
                        return math.lcm(*button_presses_per_output.values())

            for output in pending.outputs:

                if output not in modules:
                    continue

                new_pending = modules[output].send(
                    pending.origin,
                    pending.pulse,
                )

                if not new_pending:
                    continue

                # add new pending pulses to the stack for further processing
                pending_queue.put(new_pending)

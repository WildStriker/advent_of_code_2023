"""parse module"""
import collections
import enum
from dataclasses import dataclass, field
from typing import Dict, Set


class Pulse(enum.Enum):
    """Possible Pulse States"""
    LOW = 0
    HIGH = 1


@dataclass
class PendingPulse:
    """Pending Pulse Signal to be processed in Queue"""
    origin: str
    pulse: Pulse
    outputs: Set[str]


@dataclass
class Module:
    """Base Module"""
    name: str
    outputs: Set[str]

    def send(self, name: str, pulse: Pulse):
        """
        Send signal based on the given pulse from a given module to configured output modules

        Args:
            name (str): origin module sending the pulse
            pulse (Pulse): pulse being sent to this module

        Raises:
            NotImplementedError: Raised if this function is not overloaded
        """
        raise NotImplementedError("Unimplemented!")


@dataclass
class Broadcaster(Module):
    """Broadcaster Module

    Sends Pulse to all its outputs
    """

    def send(self, name: str, pulse: Pulse):
        return PendingPulse(self.name, pulse, self.outputs)


@dataclass
class FlipFlop(Module):
    """Flip Flop Module

    Nothing is sent if a HIGH pulse is given

    otherwise it flips it state between HIGH / LOW
    """
    state: Pulse = Pulse.LOW

    def send(self, name: str, pulse: Pulse):
        if pulse == Pulse.HIGH:
            return None

        if self.state == Pulse.LOW:
            self.state = Pulse.HIGH
        else:
            self.state = Pulse.LOW

        return PendingPulse(self.name, self.state, self.outputs)


@dataclass
class Conjuction(Module):
    """Conjuction Module

    All states must be HIGH to send a LOW signal
    otherwise HIGH is sent
    """
    inputs: collections.defaultdict = field(default_factory=dict)

    def send(self, name: str, pulse: Pulse):
        self.inputs[name] = pulse

        send_pulse = Pulse.LOW
        for value in self.inputs.values():
            if value == Pulse.LOW:
                send_pulse = Pulse.HIGH
                break

        return PendingPulse(self.name, send_pulse, self.outputs)


def parse_input(input_file: str) -> Dict[str, Module]:
    """parse input file into a map of all modules

    Args:
        input_file (str): input file to process

    Returns:
        Dict[str, Module]: mapping of modules by name
    """

    modules = {}

    output_to_inputs = {}
    with open(input_file, encoding="utf-8") as file_input:
        for line in file_input:
            line = line.strip()

            module, outputs = line.strip().split(" -> ")
            outputs = set(outputs.split(", "))

            if module == "broadcaster":
                module_name = module
                module = Broadcaster(module_name, outputs)
            else:
                module_type = module[0]
                module_name = module[1:]

                if module_type == "%":
                    module = FlipFlop(module_name, outputs)
                else:
                    module = Conjuction(module_name, outputs)

            for output in outputs:
                if output in output_to_inputs:
                    output_to_input = output_to_inputs[output]
                else:
                    output_to_input = set()
                    output_to_inputs[output] = output_to_input

                output_to_input.add(module_name)

            modules[module_name] = module

    # init input states for conjuctions
    for output, inputs in output_to_inputs.items():
        if not output in modules:
            continue
        module = modules[output]
        if isinstance(module, Conjuction):
            for input_module in inputs:
                module.inputs[input_module] = Pulse.LOW

    return modules

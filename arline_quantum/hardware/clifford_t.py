# Arline Quantum
# Copyright (C) 2019-2020 Turation Ltd
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


from arline_quantum.gate_sets.clifford_t import CliffordTGateSet
from arline_quantum.qubit_connectivities.qubit_connectivity import All2All, Line
from arline_quantum.hardware.hardware import Hardware


class CliffordTAll2All(Hardware):
    """Fully Connected Quantum Hardware Configuration with Clifford + T Gate Set

    **Description:**

        num_qubits : number of qubits

        qubit_connectivity : :class:`.All2All`

        gate_set : :class:`.CliffordTGateSet`

        num_gates : infinity

        qubit_cost : equal, 0
    """

    def __init__(
        self,
        num_qubits,
    ):
        connectivity = All2All(num_qubits)
        super().__init__(
            self.__class__.__name__,
            qubit_connectivity=connectivity,
            gate_set=CliffordTGateSet().reduce_gate_set(num_qubits),
            num_gates=None,
        )


class CliffordTLine(Hardware):
    """Nearest Neighbour Quantum Hardware Configuration with Clifford + T Gate Set

    **Description:**

        num_qubits : number of qubits

        qubit_connectivity : :class:`.Line`

        gate_set : :class:`.CliffordTGateSet`

        num_gates : infinity

        qubit_cost : equal, 0
    """

    def __init__(
        self,
        num_qubits,
    ):
        connectivity = Line(num_qubits)
        super().__init__(
            self.__class__.__name__,
            qubit_connectivity=connectivity,
            gate_set=CliffordTGateSet().reduce_gate_set(num_qubits),
            num_gates=None,
        )

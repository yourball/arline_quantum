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


from arline_quantum.qubit_connectivities.qubit_connectivity import QubitConnectivity


class Agave(QubitConnectivity):
    """Agave Qubit Connectivity

    **Description:**

        Agave Qubit Connectivity

    """

    def __init__(self):
        num_qubits = 8
        connections_list = [
            [0, 1],
            [0, 7],
            [1, 0],
            [1, 2],
            [2, 1],
            [2, 3],
            [3, 2],
            [3, 4],
            [4, 3],
            [4, 5],
            [5, 4],
            [5, 6],
            [6, 5],
            [6, 7],
            [7, 0],
            [7, 6],
        ]
        super().__init__("agave", num_qubits, connections_list=connections_list)


class AgaveSymmetrical(QubitConnectivity):
    """AgaveSymmetrical Qubit Connectivity

    **Description:**

        Agave Symmetrical Qubit Connectivity

    """

    def __init__(self):
        num_qubits = 8
        connections_list = [
            [0, 1],
            [0, 7],
            [1, 0],
            [1, 2],
            [2, 1],
            [2, 3],
            [3, 2],
            [3, 4],
            [4, 3],
            [4, 5],
            [5, 4],
            [5, 6],
            [6, 5],
            [6, 7],
            [7, 0],
            [7, 6],
        ]
        super().__init__("agave", num_qubits, connections_list=connections_list)

class Aspen(QubitConnectivity):
    """Aspen Qubit Connectivity

    **Description:**

        Aspen Qubit Connectivity

    """

    def __init__(self):
        num_qubits = 16
        connections_list = [
            [0, 1],
            [0, 7],
            [0, 15],
            [1, 0],
            [1, 2],
            [1, 14],
            [2, 1],
            [2, 3],
            [3, 2],
            [3, 4],
            [4, 3],
            [4, 5],
            [5, 4],
            [5, 6],
            [7, 0],
            [7, 6],
            [8, 9],
            [8, 15],
            [9, 8],
            [9, 10],
            [10, 9],
            [10, 11],
            [11, 10],
            [11, 12],
            [12, 11],
            [12, 13],
            [13, 12],
            [13, 14],
            [14, 1],
            [14, 13],
            [14, 15],
            [15, 0],
            [15, 8],
            [15, 14],
        ]
        super().__init__("aspen", num_qubits, connections_list=connections_list)


class AspenSymmetrical(QubitConnectivity):
    """AspenSymmetrical Qubit Connectivity

    **Description:**

        Aspen Qubit Connectivity

    """

    def __init__(self):
        num_qubits = 16
        connections_list = [
            [0, 1],
            [1, 0],
            [0, 7],
            [7, 0],
            [0, 15],
            [15, 0],
            [1, 0],
            [0, 1],
            [1, 2],
            [2, 1],
            [1, 14],
            [14, 1],
            [2, 1],
            [1, 2],
            [2, 3],
            [3, 2],
            [3, 4],
            [4, 3],
            [4, 5],
            [5, 4],
            [5, 6],
            [6, 5],
            [7, 0],
            [0, 7],
            [7, 6],
            [6, 7],
            [8, 9],
            [9, 8],
            [8, 15],
            [15, 8],
            [9, 10],
            [10, 9],
            [10, 11],
            [11, 10],
            [11, 12],
            [12, 11],
            [12, 13],
            [13, 12],
            [13, 14],
            [14, 13],
            [14, 15],
            [15, 14],
            [14, 1],
            [1, 14],
            [15, 0],
            [0, 15],
            [15, 8],
            [8, 15],
        ]
        super().__init__("aspen_symmetrical", num_qubits, connections_list=connections_list)

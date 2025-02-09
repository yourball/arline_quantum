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


import numpy as np
import types

from fractions import Fraction

from arline_quantum.gates.instruction import Instruction


class Gate(Instruction):
    """An abstract quantum gate class
    """

    is_discrete = None  #: Flag for discrete or continuous
    num_cregs = 0  # Gate doesn't have classical registers
    num_angles = 0  # The number of angles parameters

    def __init__(self, *args):
        super().__init__(*args)

    @property
    def args(self):
        return self._args

    @args.setter
    def args(self, args):
        self._args = args
        self._u = self.calculate_u(args)

    def calculate_u(self, args):
        r"""Calculate matrix
        """
        raise NotImplementedError()

    @property
    def u(self):
        """Get gate unitary matrix

        :return: gate unitary matrix
        :rtype: np.array
        """
        return self._u.copy()

    @u.setter
    def u(self, v):
        raise Exception("Matrix can not be changed")

    def dagger(self):
        """ Produce daggerd gate

        :return: new dagger gate
        :rtype: Gate
        """
        raise NotImplementedError()

    def _conjugate_u(self, u):
        return u.transpose().conjugate()

    def __str__(self):
        if self.is_discrete:
            return str(self.__class__.__name__)
        else:
            return str(self.__class__.__name__) + self.args_to_str(*self._args)

    def angles(self, representation="rational"):
        r"""Convert args into list of strings.
        """
        return self.format_args(*self._args, representation=representation)

    @staticmethod
    def format_args(*args, representation="rational"):
        r"""Convert args into list of strings.
        """
        angles = []
        for a in args:
            if abs(a) < 1e-7:
                angles.append(str(0))
            else:
                frac = Fraction(a / np.pi).limit_denominator(100)
                num, den = frac.numerator, frac.denominator
                # Compare angle_arg with its rational representation
                if representation == "rational":
                    if np.abs((np.pi * num) / den - a) < 1e-7:
                        # Rational approximation is good enough
                        if abs(num) == 1 and den == 1:
                            a_str = "pi" if num > 0 else "-pi"
                        elif den == 1:
                            a_str = "{:}*pi".format(num)
                        elif num == 1:
                            a_str = "pi/{:}".format(den)
                        elif num == -1:
                            a_str = "-pi/{:}".format(den)
                        else:
                            a_str = "{:}*pi/{:}".format(num, den)
                    else:
                        # Return string representing original angle_arg
                        a_str = str(a)
                elif representation == "decimal":
                    koeff = a / np.pi
                    if abs(koeff - round(koeff, 2)) < 1e-7:
                        # Rational approximation is good enough
                        if abs(num) == 1 and den == 1:
                            a_str = "1*pi" if num > 0 else "-1*pi"
                        elif den == 1:
                            a_str = "{:}*pi".format(num)
                        else:
                            koeff = a / np.pi
                            a_str = "{0:.2f}*pi".format(koeff)
                    else:
                        # Return string representing original angle_arg
                        a_str = str(a)
                angles.append(a_str)
        return angles

    @staticmethod
    def args_to_str(*args):
        r"""Describes how the gate paramaters will be shown.
        """
        return ", ".join(Gate.format_args(*args))

    @classmethod
    def make_discrete(cls, *args, class_name=None):
        if cls.is_discrete:
            return cls
        else:

            def discrete_init(self):
                cls.__init__(self, *args)

            def dagger(self):
                g = self._continuous_dagger()
                g.is_discrete = True
                g._continuous_dagger = g.dagger
                g.dagger = types.MethodType(dagger, g)

                return g

            if class_name is None:
                class_name = f"{cls.__name__}({cls.args_to_str(*args)})"

            discrete_class = type(class_name, (cls,), {"__init__": discrete_init, "is_discrete": True})
            discrete_class._continuous_dagger = discrete_class.dagger
            discrete_class.dagger = dagger
            discrete_class.num_angles = 0

            return discrete_class

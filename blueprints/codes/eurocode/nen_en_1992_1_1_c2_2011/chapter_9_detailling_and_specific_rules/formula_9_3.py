"""This package represents the Eurocode NEN-EN 1992-1-1+C2:2011 code - Chapter 9 - formula (9.3)."""
# pylint: disable=arguments-differ

import numpy as np

from blueprints.codes.eurocode.nen_en_1992_1_1_c2_2011 import NEN_EN_1992_1_1_C2_2011
from blueprints.codes.formula import Formula
from blueprints.type_alias import KN, MM


class Form9Dot3ShiftInMomentDiagram(Formula):
    """Class representing the formula 9.3 for the calculation of anchorage length of bottom reinforcement at an end support using the shift rule"""

    label = "9.3"
    source_document = NEN_EN_1992_1_1_C2_2011

    def __init__(
        self,
        v_ed: KN,
        a_l: MM,
        z: MM,
        n_ed: KN,
    ) -> None:
        """[FEd] Force to be anchored according to the shift rule [kN].

        NEN-EN 1992-1-1+C2:2011 art.9.2.1.4(2) - Formula (9.3)

        Parameters
        ----------
        v_ed: KN
            [VEd] Design value shear force [kN].
        a_l: MM
            [al] Shift in the moment diagram of an element with shear reinforcement based on art. 9.2.1.3 (2) [mm].
        z: MM
            [z] The internal lever arm for an element with constant height, corresponding to the bending moment in the considered element. In the
            shear force calculation of reinforced concrete without axial force, the approximate value z = 0.9d may generally be used [mm].
        n_ed: KN
            [NEd] Design value of axial force [kN].
        """
        super().__init__()
        self.v_ed = v_ed
        self.a_l = a_l
        self.z = z
        self.n_ed = n_ed

    @staticmethod
    def _evaluate(
        v_ed: KN,
        a_l: MM,
        z: MM,
        n_ed: KN,
    ) -> KN:
        """For more detailed documentation see the class docstring."""
        if z < 0:
            raise ValueError(f"Negative z: {z}. z cannot be negative")
        if a_l < 0:
            raise ValueError(f"Negative a_l: {a_l}. a_l cannot be negative")
        return np.abs(v_ed) * a_l / z + n_ed

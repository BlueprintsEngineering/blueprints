"""Formula 5.2 from NEN-EN 1993-5:2008 Chapter 5 - Ultimate limit state."""
from blueprints.codes.eurocode import NEN_EN_1993_5_2008
from blueprints.codes.formula import Formula
from blueprints.type_alias import DIMENSIONLESS, KNM, MM3, MPA
from blueprints.unit_conversion import N_TO_KN
from blueprints.validations import raise_if_less_or_equal_to_zero


class Form5Dot2DesignMomentResistanceClass1Or2(Formula):
    """Class representing a formula 5.2 for design moment resistance for Class 1 or 2 cross-sections."""

    label = "5.2"
    source_document = NEN_EN_1993_5_2008

    def __init__(
        self,
        beta_b: DIMENSIONLESS,
        w_pl: MM3,
        f_y: MPA,
        gamma_m_0: DIMENSIONLESS,
    ) -> None:
        """(Mc,Rd) Calculate design moment resistance of the cross-section (class 1 or 2) in [kNm/m] based on NEN-EN 1993-5:2007(E) art. 5.2.2(2)
        formula 5.2.

        Parameters
        ----------
        beta_b : DIMENSIONLESS
            (β_b) Reduction factor for the bending resistance of the cross-section in [-].
        w_pl : MM3
            (Wpl) Plastic section modulus in [mm³/m].
        f_y : MPA
            (fy) Yield strength in [MPa].
        gamma_m_0 : DIMENSIONLESS
            (γ_M0) Partial factor for material properties in [-].
        """
        super().__init__()
        self.beta_b = beta_b
        self.w_pl = w_pl
        self.f_y = f_y
        self.gamma_m_0 = gamma_m_0

    @staticmethod
    def _evaluate(
        beta_b: DIMENSIONLESS,
        w_pl: MM3,
        f_y: MPA,
        gamma_m_0: DIMENSIONLESS,
    ) -> KNM:
        """Evaluates the formula, for more information see the __init__ method."""
        raise_if_less_or_equal_to_zero(beta_b=beta_b, w_pl=w_pl, f_y=f_y, gamma_m_0=gamma_m_0)
        return (beta_b * w_pl * f_y / gamma_m_0) * N_TO_KN
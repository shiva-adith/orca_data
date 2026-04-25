from dataclasses import dataclass
from typing import Optional


@dataclass
class OrcaJobRecord:
    file: str
    complex_name: str
    job_type: str

    terminated_normally: Optional[bool] = None
    charge: Optional[int] = None
    multiplicity: Optional[int] = None

    energy_h: Optional[float] = None
    energy_kjmol: Optional[float] = None
    dipole_debye: Optional[float] = None

    s2: Optional[float] = None
    s2_ideal: Optional[float] = None
    s2_dev: Optional[float] = None

    n_scf_cycles: Optional[int] = None
    n_opt_steps: Optional[int] = None
    wall_time_s: Optional[float] = None

    n_imag_freq: Optional[int] = None
    lowest_freq_cm1: Optional[float] = None
    highest_freq_cm1: Optional[float] = None
    zpe_kjmol: Optional[float] = None
    thermal_corr_h: Optional[float] = None
    enthalpy_h: Optional[float] = None
    gibbs_h: Optional[float] = None

    g1: Optional[float] = None
    g2: Optional[float] = None
    g3: Optional[float] = None
    giso: Optional[float] = None
    dg1: Optional[float] = None
    dg2: Optional[float] = None
    dg3: Optional[float] = None

    A1_MHz: Optional[float] = None
    A2_MHz: Optional[float] = None
    A3_MHz: Optional[float] = None
    Aiso_MHz: Optional[float] = None

    AFC_MHz: Optional[float] = None
    ASD1_MHz: Optional[float] = None
    ASD2_MHz: Optional[float] = None
    ASD3_MHz: Optional[float] = None
    AORB1_MHz: Optional[float] = None
    AORB2_MHz: Optional[float] = None
    AORB3_MHz: Optional[float] = None

    Cu_spin_lowdin: Optional[float] = None
    Cu_charge_lowdin: Optional[float] = None
    Cu_spin_mulliken: Optional[float] = None
    Cu_charge_mulliken: Optional[float] = None

    Cu_redorb_spin_total_lowdin: Optional[float] = None
    Cu_redorb_s_lowdin: Optional[float] = None
    Cu_redorb_p_lowdin: Optional[float] = None
    Cu_redorb_d_lowdin: Optional[float] = None

    Cu_redorb_spin_total_mulliken: Optional[float] = None
    Cu_redorb_s_mulliken: Optional[float] = None
    Cu_redorb_p_mulliken: Optional[float] = None
    Cu_redorb_d_mulliken: Optional[float] = None
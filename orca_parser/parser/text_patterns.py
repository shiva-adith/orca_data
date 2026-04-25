GENERAL_PATTERNS = {
    "charge_multiplicity": r"\*\s*xyz(?:file)?\s+(-?\d+)\s+(\d+)",
    "final_energy": r"FINAL SINGLE POINT ENERGY\s+(-?\d+\.\d+)",
    "dipole": r"Magnitude \(Debye\)\s*:\s*(-?\d+\.\d+)",
    "s2": r"Expectation value of <S\*\*2>\s*:\s*(-?\d+\.\d+)",
    "s2_ideal": r"Ideal value S\*\(S\+1\).*?:\s*(-?\d+\.\d+)",
    "s2_dev": r"Deviation\s*:\s*(-?\d+\.\d+)",
}

G_PATTERNS = {
    "gtot": r"g\(tot\)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)\s+iso=\s*(-?\d+\.\d+)",
    "delta_g": r"Delta-g\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)",
}

A_PATTERNS = {
    "A_tot": r"A\(Tot\)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)\s+A\(iso\)\s*=\s*(-?\d+\.\d+)",
    "A_fc": r"A\(FC\)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)",
    "A_sd": r"A\(SD\)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)",
    "A_orb_dia": r"A\(ORB\+DIA\)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)",
    "A_orb": r"A\(ORB\)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)",
}
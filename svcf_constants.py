"""
svcf_constants.py
SVCF Open Source Physics — Framework Constants
rxiVerse:2602.0018  |  Zenodo: 10.5281/zenodo.18604376

All constants taken directly from the published repository papers.
"""

# ── Physical Constants ────────────────────────────────────────────────────────
C_LIGHT    = 2.99792458e8        # m/s    speed of light (exact)
HBAR       = 1.054571817e-34     # J·s    reduced Planck constant
G_NEWTON   = 6.67430e-11         # m³ kg⁻¹ s⁻²  gravitational constant
K_BOLTZ    = 1.380649e-23        # J/K    Boltzmann constant
ALPHA_FS   = 7.2973525693e-3     # fine-structure constant (≈ 1/137.036)
M_PROTON   = 1.67262192369e-27   # kg     proton mass
M_ELECTRON = 9.1093837015e-31    # kg     electron mass

# ── Astrophysical Units ───────────────────────────────────────────────────────
M_SUN = 1.98892e30               # kg     solar mass
AU    = 1.495978707e11           # m      astronomical unit
PC    = 3.085677581e16           # m      parsec
KPC   = 3.085677581e19           # m      kiloparsec
LY    = 9.4607304725808e15       # m      light-year

# ── SVCF Substrate Constants ──────────────────────────────────────────────────
# Vacuum substrate viscous fluid parameters (SVCF_Repository_Master.md)

# Dimensionless vacuum stress coupling: derived from D02 3I/ATLAS and D05 Casimir
# a = GAMMA * v^2 / r; at r=0.65 AU, v=32.3 km/s → a ≈ 3.755e-6 m/s^2
GAMMA   = 3.5e-4

# Critical substrate Reynolds number — quantum/classical boundary
# C1 (STAR experiment, 0.0 sigma): Re_crit = 2857
RE_CRIT = 2857

# Chirality parameter: 1 − B = 1/33  (Law #2, Chirality Tax)
B = 32.0 / 33.0

# Luminosity law exponent: L ∝ M^(65/66)  (Law #1, UVLL)
BETA = 65.0 / 66.0

# Phase alignment parameter: 120° compact-dimension period  (Domain 23, C8)
PSI = 2.0 / 3.0

# Topological dimension coupling (substrate turbulence, D02 note)
K_TD = 1.0

# Substrate density [kg/m³]
RHO_C = 9.47e-27

# Dynamic viscosity of substrate [Pa·s]
ETA = 9.47e-34

# Kinematic viscosity of substrate [m²/s]  NU = ETA / RHO_C
NU = ETA / RHO_C

# Photon drift mode number: k = 9  (C2: exact match)
K_MODE = 9.0

# Chirality tax: ε = α²  (Law #2, SVCF_Law2_Chirality_Tax_Law_FINAL.pdf)
EPSILON = ALPHA_FS ** 2

# ── Nuclear Shell Structure (Domain 23) ───────────────────────────────────────
# Shell degeneracy from compact-dimension topology, theta_n = n * PSI * pi
# Cumulative sums reproduce the seven nuclear magic numbers exactly.
SHELL_DEGENERACY = [2, 6, 12, 8, 22, 32, 44]   # d_n  (Δ per shell)
MAGIC_NUMBERS    = [2, 8, 20, 28, 50, 82, 126]  # cumulative nuclear magic numbers

# ── Mode Counting ─────────────────────────────────────────────────────────────
N_ACTIVE    = 3    # active substrate modes (Z₃ symmetry, C10)
N_CHI_MODES = 9    # total χ-modes = K_MODE

import numpy as np


# ============================================================
# SQP for NLP:
# ============================================================
def sqp_eq_newton(
    x0: np.ndarray,
    l0: np.ndarray | None = None,
    max_iter: int = 50,
    tol: float = 1e-9,
    verbose: bool = False,
):
    return x_sqp, l_sqp, info_sqp, res_pri_list, res_dual_list, x_list


# ============================================================
# Augmented Lagrangian method for NLP:
# ============================================================
def alm_solve(
    x0,
    max_outer=200,
    max_inner=200,
    tol_outer=1e-7,
    tol_inner=1e-7,
    rho0=1e-2,
    rho_growth=10.0,
    verbose=False,
    l0=None,
):
    return x_alm, lam_alm, info_alm, res_pri_list, res_dual_list, x_list

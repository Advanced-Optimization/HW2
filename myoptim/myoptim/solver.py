import numpy as np


# ============================================================
# Damped Newton's method for quadratic programming:
# ============================================================
def damped_newton_eq_qp(
    x0, Q, A, b, tol=1e-10, max_iter=50, alpha=0.5
):

    return x_opt, l_opt

# ============================================================
# Augmented Lagrangian method for quadratic programming:
# ============================================================
def augmented_lagrangian_eq_qp(
    x0,
    Q,
    A,
    b,
    rho=5.0,
    alpha=1e-2,
    max_iter=100,
):

    return x_approx, l_approx
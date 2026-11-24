from multipolepdm.models.registry import build_response


def evaluate(job, xi_rad, sigma):
    return build_response(job, xi_rad, sigma)

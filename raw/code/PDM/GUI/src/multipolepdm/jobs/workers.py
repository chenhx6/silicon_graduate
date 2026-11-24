"""Scientific worker functions without a Qt dependency."""

from multipolepdm.models.registry import evaluate_response


class Cancelled(Exception):
    pass


def compute_job(job, cancelled=lambda: False, progress=lambda value: None):
    from multipolepdm.pdm.mapping import map_density
    from multipolepdm.pdm.statistics import summarize_density

    def checkpoint(percent):
        if cancelled():
            raise Cancelled("Cancelled by user.")
        progress(percent)

    checkpoint(5)
    response = evaluate_response(job)
    checkpoint(50)
    result = map_density(job, response)
    checkpoint(80)
    summary = summarize_density(result)
    checkpoint(100)
    return result, summary

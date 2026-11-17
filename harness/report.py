"""Report rendering for completed suite runs."""


def render(metrics, fmt="json"):
    import json
    if fmt == "json":
        return json.dumps(metrics, indent=2)
    raise ValueError(f"unsupported format: {fmt}")

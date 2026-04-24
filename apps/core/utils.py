def dict_to_css(d: dict[str, str]) -> str:
    return " ".join([f"{k}:{v}" for k, v in d.items()])

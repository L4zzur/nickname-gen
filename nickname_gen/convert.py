import json
from pathlib import Path


class FileExtensionError(Exception):
    pass


def _check_path(path: Path, suffix: str) -> None:
    if not path.exists():
        raise FileNotFoundError("File does not exist.")
    if path.suffix != suffix:
        raise FileExtensionError(f"Only {suffix} files are supported.")


def convert_txt_to_json(
    path: Path, out_path: Path | None = None
) -> tuple[Path, list[str]]:
    _check_path(path, suffix=".txt")
    with open(file=path, mode="r", encoding="utf-8") as f:
        WORDS = list(set([line.strip().lower() for line in f]))
    WORDS = list(filter(None, WORDS))
    WORDS.sort()
    if out_path is None:
        out_path = path.parent / f"{path.stem}.json"
    with open(file=out_path, mode="w", encoding="utf-8") as f:
        json.dump(WORDS, f, ensure_ascii=False, indent=4)
    return out_path, WORDS


def convert_json_to_py(
    path: Path, out_path: Path | None = None
) -> tuple[Path, list[str]]:
    _check_path(path, suffix=".json")
    with open(file=path, mode="r", encoding="utf-8") as f:
        WORDS = json.load(f)
    WORDS = list(filter(None, WORDS))
    WORDS.sort()
    if out_path is None:
        out_path = path.parent / f"{path.stem}.py"
    with open(file=out_path, mode="w", encoding="utf-8") as f:
        f.write("WORDS = " + str(WORDS))
    return out_path, WORDS


def convert(path: Path, out_path: Path | None = None) -> list[str]:
    if path.suffix == ".txt":
        return convert_txt_to_json(path, out_path)[1]
    elif path.suffix == ".json":
        return convert_json_to_py(path, out_path)[1]
    else:
        raise FileExtensionError("Only .txt and .json files are supported.")

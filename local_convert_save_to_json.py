"""Local helper script: convert a .retribution save to .json plain-text.

Do not commit this file.
"""

from __future__ import annotations

from pathlib import Path
import sys

from game import persistency


def main() -> None:
    if len(sys.argv) >= 2:
        save_retribution = Path(sys.argv[1])
    else:
        save_retribution = Path(
            r"C:\Users\bob\Saved Games\DCS\Retribution\Saves\long-range-test.retribution"
        )

    if len(sys.argv) >= 3:
        save_json = Path(sys.argv[2])
    else:
        save_json = save_retribution.with_suffix(".json")

    # Configure persistency for plain-text saves.
    persistency.setup(
        user_folder=r"C:\Users\bob\Saved Games\DCS",
        prefer_liberation_payloads=False,
        port=16880,
        save_format=persistency.SAVE_FORMAT_PLAIN_TEXT,
    )

    game = persistency.load_game(str(save_retribution))
    if game is None:
        raise RuntimeError(f"Failed to load save: {save_retribution}")

    game.savepath = str(save_json)
    if not persistency.save_game(game):
        raise RuntimeError(f"Failed to save JSON: {save_json}")

    print(f"Saved JSON to: {save_json}")


if __name__ == "__main__":
    main()

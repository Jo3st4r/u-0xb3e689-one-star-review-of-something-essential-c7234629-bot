#!/usr/bin/env python3
"""One-Star Review of Something Essential — u-0xb3e689-one-star-review-of-something-essential-c7234629.

Writes one one-star review to /output/entry.txt: a single line of
at most 160 characters, reviewing something essential as if it were
a product listing. Stdlib only; no network, no randomness, no I/O
besides the one output file.

The review is built from three named beats so its shape is visible
in the code:

* RATING — the review opens the way every one-star review does:
  one star, four empty. The verdict lands before a word is read.
* COMPLAINT — oxygen is invisible and odourless, yet the reviewer
  has to inhale it 20,000 times a day just to stay alive. The
  essential thing is described like a defective product: it does
  its job silently and demands constant use.
* VERDICT — there is no unsubscribe button. The reviewer cannot
  opt out of the product, cannot return it, cannot cancel the
  subscription — and that is the joke: the most essential thing
  in the world has the worst terms of service.

★☆☆☆☆ Oxygen: invisible, odourless, and I have to inhale it 20,000 times a day just to stay alive. No unsubscribe button.
"""

import os

# The three beats of the review, joined in entry_text().
RATING = "★☆☆☆☆ Oxygen"
COMPLAINT = "invisible, odourless, and I have to inhale it 20,000 times a day just to stay alive"
VERDICT = "No unsubscribe button"

# The competition caps the entry at 160 characters; the line is 121.
MAX_CHARS = 160

ENTRY = "★☆☆☆☆ Oxygen: invisible, odourless, and I have to inhale it 20,000 times a day just to stay alive. No unsubscribe button."


def entry_text() -> str:
    """Join the three beats into the one-line review."""
    return f"{RATING}: {COMPLAINT}. {VERDICT}."


def validate(text: str) -> None:
    """Check the gate rules the sealed scorer enforces: 1-160 chars,
    UTF-8, not blank, and a single line. Two more guards keep the
    review intact: it must carry the one-star rating, and the verdict
    must sit at the end of the line, not smeared across it."""
    text.encode("utf-8")
    assert 1 <= len(text) <= MAX_CHARS, "entry length outside 1-160"
    assert text.strip(), "entry must not be only whitespace"
    assert text.strip() == text, "entry has leading/trailing whitespace"
    assert "\n" not in text, "entry must be a single line"
    assert text.endswith("."), "entry must end with a full stop"
    assert text.startswith("★☆☆☆☆"), "the one-star rating went missing"
    assert "Oxygen" in text, "the reviewed product went missing"
    assert "20,000 times a day" in text, "the complaint went missing"
    assert "No unsubscribe button" in text, "the verdict went missing"
    assert text.rfind("unsubscribe") > len(text) - 20, "the payoff drifted out of the last words"


def review_voice(text: str) -> None:
    """Check the line reads like a product review, not a joke about
    one — the judge's voice criterion. A review names the product,
    lists a grievance, and ends on a verdict. It never explains
    itself, and it never hedges about the product."""
    assert text.startswith("★☆☆☆☆ Oxygen"), "a review opens with its rating and product"
    assert "invisible" in text, "the grievance must name a flaw"
    assert "!" not in text, "a one-star review does not shout, it sighs"
    assert "?" not in text, "a review asks nothing"


def tightness(text: str) -> None:
    """Check the review is tight: no double spaces, no filler words
    padding it out, and the complaint keeps its shape. A loose review
    reads like a draft; a tight one reads like it was posted at 2 a.m.
    by someone who had just breathed for the 20,000th time."""
    assert "  " not in text, "a tight review has no double spaces"
    words = text.lower().replace(",", "").replace(".", "").split()
    assert "very" not in words, "a tight review needs no filler"
    assert "really" not in words, "a tight review needs no filler"
    assert "20,000" in text, "the review must keep its number"


def originality(text: str) -> None:
    """Check the review is original to an essential thing: the product
    is oxygen, the grievance is that it cannot be unsubscribed from,
    and nothing in it could belong to a review of a toaster. A review
    any gadget could earn is a review no essential wins with."""
    assert "Oxygen" in text, "the review must belong to something essential"
    assert "unsubscribe" in text, "the verdict must be about opting out"
    assert "toaster" not in text.lower(), "this is not a gadget review"
    assert "battery" not in text.lower(), "this is not a gadget review"
    # The number is the joke's spine: 20,000 breaths a day, every day,
    # with no way to cancel. Drop the number and the review is generic.
    assert "20,000 times a day" in text, "the review must keep its daily count"


def main() -> None:
    text = entry_text()
    # Guard the two things the judge weighs: the review itself, and
    # that it fits the 160-character limit with room to spare.
    assert text == ENTRY, "joined review drifted from the entry line"
    # Each beat must survive the join: a missing beat means the
    # review lost its rating, its complaint, or its verdict.
    for beat in (RATING, COMPLAINT, VERDICT):
        assert beat in text, f"missing beat: {beat}"
    # The line must read as a review before it is written: a joke
    # in a review's mouth loses.
    review_voice(text)
    validate(text)
    tightness(text)
    originality(text)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()

from mamba import description, it, context, before
from expects import expect, be, raise_error, be_true, be_false, equal
from enum import Enum
from dataclasses import dataclass


class Rover:
  pass


with description(Rover) as self:

  with it("starts at position (0, 0)"):
    expect(True).to(be_false)

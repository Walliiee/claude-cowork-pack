---
name: verify-change
description: Check that a change does what it should by running it, not by reading the diff. Use after a change and before calling it done.
---

# Verify change

1. State in one line what the change should do, as observable behaviour.
2. Pick the cheapest way to exercise it: run the covering test, run the command, call the endpoint, or click through the UI path.
3. Run it and read the real output. Compare it with step 1.
4. Try the obvious failure cases too: empty input, the error path, the boundary.
5. Report what you ran and what you saw. If you could not verify it, say so and name what a person should check before shipping.

Passing tests do not prove the change works, because tests can miss the changed path. Exercise that path when you can.

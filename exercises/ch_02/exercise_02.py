# Exercise 2.2
#
# You could write `applyForce()` in another way, using the static method `div()`
# instead of `copy()`. Rewrite `applyForce()` by using the static method.

def apply_force(self, force: Vector):
    force = Vector.div(force, self.mass)
    self.acceleration.add(force)

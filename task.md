### 🌀 **Task**

A Python script that models a **Mobius strip** using parametric equations and computes key geometric properties.

---

#### **1. Requirements**

* Define a `MobiusStrip` class that:

  * Accepts:

    * Radius `R` (distance from the center to the strip)
    * Width `w` (strip width)
    * Resolution `n` (number of points in the mesh)
  * Computes:

    * A 3D mesh/grid of (x, y, z) points on the surface
    * Surface area (numerically, using integration or approximation)
    * Edge length (numerically along the boundary)

---

#### **2. Parametric Equation of Mobius Strip**

Use the parametric equations:

$$
x(u, v) = \left(R + v \cdot \cos\left(\frac{u}{2}\right)\right) \cdot \cos(u)
$$

$$
y(u, v) = \left(R + v \cdot \cos\left(\frac{u}{2}\right)\right) \cdot \sin(u)
$$

$$
z(u, v) = v \cdot \sin\left(\frac{u}{2}\right)
$$

Where:

* $u \in [0, 2\pi]$
* $v \in [-w/2, w/2]$

---

#### **3. Deliverables**

* Python script (clean, modular, commented).
* 3D plot or screenshot.
* A short write-up explaining:

  * How you structured the code
  * How you approximated surface area
  * Any challenges you faced


This assignment tests:

* Parametric 3D modeling
* Numerical integration / geometry
* Visualization
* Code clarity

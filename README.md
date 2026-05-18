# Utkarsh Joshi

First-year CS undergrad. I build systems software and GPU-accelerated compute — from scratch, because that's the only way to actually understand them.

`C` `C++` `CUDA` `Python` · WSL2 (Debian) · [joshiutkarshntl@gmail.com](mailto:joshiutkarshntl@gmail.com) · [LinkedIn](https://linkedin.com/in/utkarsh-joshi)

---

## Projects

<table>
<tr>
<td width="50%" valign="top">

### 🛰️ [Astrosis](https://github.com/UtkarshJoshiNtl/Astrosis)
**GPU-accelerated orbital propagation engine**

`C++` `CUDA` `Python` `pybind11` `OpenMP`

RK4 integrator with J2/J3/J4 gravity harmonics, atmospheric drag (US Standard Atmosphere), and solar radiation pressure. Brent's method for conjunction refinement. Python bindings via pybind11.

| | vs. Python |
|---|---|
| Batch propagation | **507×** faster |
| Conjunction screening | **83×** faster |
| Energy drift / 24h | **< 1e-7** |

</td>
<td width="50%" valign="top">

### 🌊 [CuFloda](https://github.com/UtkarshJoshiNtl/CuFloda)
**Real-time fluid dynamics simulation**

`Python` `NumPy` `PyGame` `CUDA (in progress)`

D2Q9 Lattice Boltzmann Method with BGK collision operator. Real-time visualization with interactive obstacle drawing. Inflow, outflow, and bounce-back boundary conditions. CUDA port in active development.

```
Method    →  D2Q9 LBM + BGK collision
Boundary  →  inflow · outflow · bounce-back
Target    →  128×128 @ 30+ FPS (CUDA)
```

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 🐚 [Quip](https://github.com/UtkarshJoshiNtl/quip)
**Unix shell, written in C99**

`C` `POSIX` `termios` `Signal Handling`

Built entirely from scratch: raw terminal mode via termios, command pipelines, I/O redirection, background job control, and full signal handling. Arrow-key history and tab completion without readline.

```
Signals   →  SIGINT · SIGTERM · SIGCHLD
Redirect  →  < > >> · pipes · &
Terminal  →  raw termios · history · tab complete
```

</td>
<td width="50%" valign="top">

### 📡 Currently

- Deepening CUDA — memory hierarchy, warp-level primitives, occupancy tuning
- CUDA backend for CuFloda
- Building open-source signal

**Interests:** high-performance computing · GPU architecture · numerical methods · orbital mechanics

</td>
</tr>
</table>

---

## Stack

**Languages** — C · C++ · Python · CUDA

**Tools** — CMake · Make · gdb · valgrind · perf · Nsight

**Environment** — WSL2 (Debian) · Git

---

[![GitHub Streak](https://streak-stats.demolab.com?user=UtkarshJoshiNtl&theme=dark&background=0f0f0f&border=262626&ring=f59e0b&fire=f59e0b&currStreakLabel=f59e0b&sideLabels=e0e0e0&dates=737373)](https://git.io/streak-stats)

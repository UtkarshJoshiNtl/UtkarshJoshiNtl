<div align="center">

# Utkarsh Joshi

<a href="mailto:joshiutkarshntl@gmail.com">![Email](https://img.shields.io/badge/email-EA4335?style=flat-square&logo=gmail&logoColor=white)</a>
<a href="https://linkedin.com/in/utkarsh-joshi">![LinkedIn](https://img.shields.io/badge/linkedin-0A66C2?style=flat-square&logo=linkedin&logoColor=white)</a>
<a href="https://codeforces.com/profile/UtkarshJoshiNtl">![Codeforces](https://img.shields.io/badge/codeforces-1F8ACB?style=flat-square&logo=codeforces&logoColor=white)</a>

First-year CS undergrad. Currently building systems software and GPU-accelerated compute.

</div>

---

## Stack & Activity

<div align="center">

![C](https://img.shields.io/badge/C-00599C?style=flat-square&logo=c&logoColor=white)
![C++](https://img.shields.io/badge/C++-00599C?style=flat-square&logo=cplusplus&logoColor=white)
![CUDA](https://img.shields.io/badge/CUDA-76B900?style=flat-square&logo=nvidia&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![CMake](https://img.shields.io/badge/CMake-064F8C?style=flat-square&logo=cmake&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black)
![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)

<br/>

[![GitHub Streak](https://streak-stats.demolab.com?user=UtkarshJoshiNtl&theme=dark&background=0f0f0f&border=262626&ring=f59e0b&fire=f59e0b&currStreakLabel=f59e0b&sideLabels=e0e0e0&dates=737373)](https://git.io/streak-stats)

<br/>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/UtkarshJoshiNtl/UtkarshJoshiNtl/output/github-contribution-grid-snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/UtkarshJoshiNtl/UtkarshJoshiNtl/output/github-contribution-grid-snake.svg" />
  <img alt="contribution snake" src="https://raw.githubusercontent.com/UtkarshJoshiNtl/UtkarshJoshiNtl/output/github-contribution-grid-snake-dark.svg" />
</picture>

</div>

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

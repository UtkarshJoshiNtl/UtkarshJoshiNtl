#!/usr/bin/env python3
"""
3D Torus Knot — vertex-morphing SVG animation.

Computes a 3D parametric torus knot, rotates it around the Y axis
in N keyframes, projects to 2D, and outputs a single SVG using
<animate> on <path d="…"> to produce smooth 3D rotation.

Pure SVG + SMIL.  No JS, no deps.
"""

import math
from pathlib import Path

WIDTH, HEIGHT = 800, 500
BG = "#080808"

R = 150            # major radius
r = 60             # minor radius
P, Q = 2, 3        # trefoil knot

N_POINTS = 120     # vertices along the curve
N_FRAMES = 18      # keyframes (20° steps)
FOV = 700          # perspective divisor


def knot_point(t):
    x = (R + r * math.cos(Q * t)) * math.cos(P * t)
    y = (R + r * math.cos(Q * t)) * math.sin(P * t)
    z = r * math.sin(Q * t)
    return x, y, z


def rotate_y(x, y, z, rad):
    c, s = math.cos(rad), math.sin(rad)
    return x * c + z * s, y, -x * s + z * c


def project(x, y, z):
    f = FOV / (FOV + z)
    return x * f + WIDTH / 2, -y * f + HEIGHT / 2


def build_path(angle):
    pts = []
    for i in range(N_POINTS):
        t = (i / N_POINTS) * 2 * math.pi
        x, y, z = knot_point(t)
        x, y, z = rotate_y(x, y, z, angle)
        px, py = project(x, y, z)
        pts.append(f"{px:.1f},{py:.1f}")
    return "M" + " ".join(pts)


def generate():
    lines = []
    emit = lines.append

    emit('<?xml version="1.0" encoding="UTF-8"?>')
    emit(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" '
         f'width="100%" height="100%">')

    # ─── defs ────────────────────────────────────────────────────────
    emit('<defs>')
    # Single filter: glow + crisp line from one path
    emit('<filter id="g" x="-20%" y="-20%" width="140%" height="140%">')
    emit('<feGaussianBlur stdDeviation="3" result="b"/>')
    emit('<feComponentTransfer in="b" result="g">'
         '<feFuncA type="linear" slope="0.5"/>'
         '</feComponentTransfer>')
    emit('<feMerge>'
         '<feMergeNode in="g"/>'
         '<feMergeNode in="SourceGraphic"/>'
         '</feMerge>')
    emit('</filter>')

    emit('<linearGradient id="fg" x1="0" y1="0" x2="1" y2="1">')
    emit('<stop offset="0%" stop-color="#5b9bd5"/>')
    emit('<stop offset="50%" stop-color="#b0c4de"/>')
    emit('<stop offset="100%" stop-color="#5b9bd5"/>')
    emit('</linearGradient>')
    emit('</defs>')

    # ─── background ──────────────────────────────────────────────────
    emit(f'<rect width="{WIDTH}" height="{HEIGHT}" fill="{BG}"/>')

    # ─── knot keyframes ──────────────────────────────────────────────
    frames = [build_path((i / N_FRAMES) * 2 * math.pi)
              for i in range(N_FRAMES)]
    val = ";".join(frames)

    emit(f'<path d="{frames[0]}" fill="none" stroke="url(#fg)" '
         f'stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" '
         f'filter="url(#g)">')
    emit(f'<animate attributeName="d" values="{val}" '
         f'dur="10s" repeatCount="indefinite"/>')
    emit('</path>')

    # ─── bottom bar ──────────────────────────────────────────────────
    emit('<text x="16" y="488" font-family="monospace" font-size="32" '
         'fill="rgba(255,255,255,0.2)">Utkarsh Joshi</text>')
    emit('<text x="784" y="488" text-anchor="end" font-family="monospace" '
         'font-size="18" fill="rgba(255,255,255,0.2)">'
         'C  C++  Python </text>')

    emit('</svg>')
    return "\n".join(lines)


if __name__ == "__main__":
    svg = generate()
    dst = Path(__file__).parent / "profile-scene.svg"
    dst.write_text(svg)
    print(f"✨ {dst}  ({len(svg):,} bytes)")

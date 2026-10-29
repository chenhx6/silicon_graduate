#!/usr/bin/env python3
import json

with open("outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/ba-e1-cancellation-sensitivity/cancellation_results.json") as f:
    data = json.load(f)

# Create an SVG plot of D0(DM), D0(p), D0(n), and D0(net) across Ba isotopes
width = 800
height = 500
padding = 60

svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" style="background-color: #ffffff; font-family: sans-serif;">']

# Title
svg.append('<text x="400" y="30" font-size="18" font-weight="bold" text-anchor="middle" fill="#111827">140-150Ba Intrinsic Dipole Moment D0 Cancellation &amp; Sensitivity</text>')

# Coordinate mappings
# X: N from 84 to 94 (A from 140 to 150)
# Y: D0 from -0.85 to +0.25 e*fm
x_min, x_max = 84, 94
y_min, y_max = -0.85, 0.25

def map_x(n):
    return padding + (n - x_min) / (x_max - x_min) * (width - 2 * padding)

def map_y(d0):
    return height - padding - (d0 - y_min) / (y_max - y_min) * (height - 2 * padding)

# Grid lines and axes
y_zero = map_y(0.0)
svg.append(f'<line x1="{padding}" y1="{y_zero}" x2="{width - padding}" y2="{y_zero}" stroke="#9ca3af" stroke-width="2" stroke-dasharray="4,4"/>')
svg.append(f'<text x="{width - padding + 5}" y="{y_zero + 4}" font-size="12" fill="#4b5563">D0 = 0 (Node)</text>')

# Axes
svg.append(f'<line x1="{padding}" y1="{height - padding}" x2="{width - padding}" y2="{height - padding}" stroke="#374151" stroke-width="2"/>')
svg.append(f'<line x1="{padding}" y1="{padding}" x2="{padding}" y2="{height - padding}" stroke="#374151" stroke-width="2"/>')

# X-axis ticks & labels
for n in range(84, 95, 2):
    x = map_x(n)
    a = n + 56
    svg.append(f'<line x1="{x}" y1="{height - padding}" x2="{x}" y2="{height - padding + 6}" stroke="#374151" stroke-width="1.5"/>')
    svg.append(f'<text x="{x}" y="{height - padding + 22}" font-size="12" text-anchor="middle" fill="#374151">{a}Ba (N={n})</text>')

# Y-axis ticks & labels
for d0_val in [-0.8, -0.6, -0.4, -0.2, 0.0, 0.2]:
    y = map_y(d0_val)
    svg.append(f'<line x1="{padding - 6}" y1="{y}" x2="{padding}" y2="{y}" stroke="#374151" stroke-width="1.5"/>')
    svg.append(f'<text x="{padding - 10}" y="{y + 4}" font-size="12" text-anchor="end" fill="#374151">{d0_val:.1f}</text>')

svg.append(f'<text x="{padding - 35}" y="{height // 2}" font-size="13" font-weight="bold" text-anchor="middle" fill="#111827" transform="rotate(-90, {padding - 35}, {height // 2})">D0 [e · fm]</text>')

# Polylines for each component
series = [
    ("D0_DM", "#2563eb", "Droplet Model D0(DM)"),
    ("D0_p", "#16a34a", "Proton Shell D0(p)"),
    ("D0_n", "#dc2626", "Neutron Shell D0(n)"),
    ("D0_net", "#7c3aed", "Net Dipole D0(net)")
]

for key, color, label in series:
    pts = []
    for d in data:
        pts.append(f"{map_x(d['N'])},{map_y(d[key])}")
    svg.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{color}" stroke-width="2.5"/>')
    for d in data:
        x, y = map_x(d['N']), map_y(d[key])
        svg.append(f'<circle cx="{x}" cy="{y}" r="4" fill="{color}"/>')

# Legend
leg_x = 480
leg_y = 60
for idx, (key, color, label) in enumerate(series):
    ly = leg_y + idx * 24
    svg.append(f'<line x1="{leg_x}" y1="{ly}" x2="{leg_x + 30}" y2="{ly}" stroke="{color}" stroke-width="2.5"/>')
    svg.append(f'<circle cx="{leg_x + 15}" cy="{ly}" r="4" fill="{color}"/>')
    svg.append(f'<text x="{leg_x + 40}" y="{ly + 4}" font-size="12" fill="#1f2937">{label}</text>')

# Highlight the cancellation region N=88..90
x_c1 = map_x(87.5)
x_c2 = map_x(90.5)
y_top = map_y(0.22)
y_bot = map_y(-0.35)
svg.append(f'<rect x="{x_c1}" y="{y_top}" width="{x_c2 - x_c1}" height="{y_bot - y_top}" fill="#fef08a" opacity="0.3" rx="6"/>')
svg.append(f'<text x="{(x_c1 + x_c2)/2}" y="{y_top + 20}" font-size="12" font-weight="bold" text-anchor="middle" fill="#854d0e">Cancellation Zone</text>')
svg.append(f'<text x="{(x_c1 + x_c2)/2}" y="{y_top + 36}" font-size="11" text-anchor="middle" fill="#854d0e">B(E1) Node (144Ba)</text>')

svg.append('</svg>')

svg_content = "\n".join(svg)
with open("outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/ba-e1-cancellation-sensitivity/cancellation_curve.svg", "w") as f:
    f.write(svg_content)
print("SVG plot generated successfully.")

#!/usr/bin/python3
import sys

from crosssection import CrossSection, Node


THICKNESS = 4.4
SECTION_NODES = [
    Node(32.0, -25.0, THICKNESS),
    Node(28.44, -25.0, THICKNESS),
    Node(24.89, -25.0, THICKNESS),
    Node(21.33, -25.0, THICKNESS),
    Node(17.78, -25.0, THICKNESS),
    Node(14.22, -25.0, THICKNESS),
    Node(10.67, -25.0, THICKNESS),
    Node(7.11, -25.0, THICKNESS),
    Node(3.56, -25.0, THICKNESS),
    Node(0.0, -25.0, THICKNESS),
    Node(0.0, -21.15, THICKNESS),
    Node(0.0, -17.31, THICKNESS),
    Node(0.0, -13.46, THICKNESS),
    Node(0.0, -9.62, THICKNESS),
    Node(0.0, -5.77, THICKNESS),
    Node(0.0, -1.92, THICKNESS),
    Node(0.0, 0.0, THICKNESS),
    Node(0.0, 1.92, THICKNESS),
    Node(0.0, 5.77, THICKNESS),
    Node(0.0, 9.62, THICKNESS),
    Node(0.0, 13.46, THICKNESS),
    Node(0.0, 17.31, THICKNESS),
    Node(0.0, 21.15, THICKNESS),
    Node(0.0, 25.0, THICKNESS),
    Node(3.56, 25.0, THICKNESS),
    Node(7.11, 25.0, THICKNESS),
    Node(10.67, 25.0, THICKNESS),
    Node(14.22, 25.0, THICKNESS),
    Node(17.78, 25.0, THICKNESS),
    Node(21.33, 25.0, THICKNESS),
    Node(24.89, 25.0, THICKNESS),
    Node(28.44, 25.0, THICKNESS),
    Node(32.0, 25.0, THICKNESS)
]


def main():
    cs = CrossSection(SECTION_NODES)

    print('** Sectorial properties:')
    print('-- Section area (F): {area:.2f} mm^2'.format(
          area=cs.get_section_area()))
    print('-- Center of gravity (x, y): {center} mm'.format(
          center=cs.get_gravity_center()))
    print('-- Main moments of inertia (Ix, Iy): {moments} mm^4'.format(
          moments=cs.get_inertia_moment()))
    print('-- Polar moment of inertia (Ip): {moment:.2f} mm^4'.format(
          moment=cs.get_polar_inertia_moment()))
    print('-- Center of rigidity (x, y): {center} mm'.format(
          center=cs.get_rigidity_center()))
    print('-- Sectorial moment of inertia (Iw): {moment:.2f} mm^6'.format(
          moment=cs.get_sectorial_inertia_moment()))


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)

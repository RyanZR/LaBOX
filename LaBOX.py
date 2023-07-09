#!/usr/bin/env python3

#==============================================================================
#
#                        __        _____ _____ __ __ 
#                       |  |   ___| __  |     |  |  |
#                       |  |__| .|| __ -|  |  |-   -|
#                       |_____|__||_____|_____|__|__|
#
#
#   LaBOX - Gridbox size calculation for ligand docking
#
#   Get more information from https://github.com/RyanZR/LaBOX
#
#   Report bugs and issues to https://github.com/RyanZR/LaBOX/issues
#
#   This software is provided WITHOUT WARRANTY OF ANY KIND
#
#==============================================================================

import os
import sys
import getopt
import statistics

def usage():
    print(f'Usage')
    print(f'╰─○ LaBOX.py [-l] <filename>')
    print(f'')
    print(f'Argument')
    print(f'╰─○ Command description:')
    print(f'        -l  ligand filename (supported: pdb, pdbqt, sdf, mol2)')
    print(f'        -h  help')
    print(f'        -a  about')
    print(f'╰─○ Optional parameters:')
    print(f'        -s  scale factor (default is 2)')
    print(f'        -c  grid box center')

def about():
    print(f'==============================================================================')
    print(f'                         __        _____ _____ __ __                          ')
    print(f'                        |  |   ___| __  |     |  |  |                         ')
    print(f'                        |  |__| .|| __ -|  |  |-   -|                         ')
    print(f'                        |_____|__||_____|_____|__|__|                         ')
    print(f'                                                                              ')
    print(f'   LaBOX - Grid box size calculation for ligand docking                       ')
    print(f'                                                                              ')
    print(f'   Get more information from https://github.com/RyanZR/LaBOX                  ')
    print(f'                                                                              ')
    print(f'   Report bugs and issues to https://github.com/RyanZR/LaBOX/issues           ')
    print(f'                                                                              ')
    print(f'   This software is provided WITHOUT WARRANTY OF ANY KIND                     ')
    print(f'                                                                              ')
    print(f'==============================================================================')

def file_handler(input_file):
    ext = os.path.splitext(input_file)[-1]
    if input_file == None:
        print(f'LaBOX.py')
        print(f'╰─○ Invalid file or incorrect usage')
        sys.exit()
    if not os.path.exists(input_file):
        print(f'LaBOX.py')
        print(f'╰─○ File does not exists')
        print(f'    Is {input_file} mispelled?')
        sys.exit()
    if ext not in ('.pdb', 'pdbqt', '.sdf', '.mol2'):
        print(f'LaBOX.py')
        print(f'╰─○ File format {ext} not supported')
        sys.exit()

def get_coordinates(data, ext):
    if ext == '.mol2':
        commence = next(n for n, line in enumerate(data) if line.strip() != '' and line.split()[0] == '@<TRIPOS>ATOM') + 1
        conclude = next(n for n, line in enumerate(data) if line.strip() != '' and line.split()[0] == '@<TRIPOS>BOND')
        atoms = [line.split()[1] for line in data[commence:conclude]]
        coord = [list(map(float, line.split()[2:5])) for line in data[commence:conclude]]

    if ext == '.sdf':
        blank = int(next(n for n, line in enumerate(data) if line.split() == []))
        atoms = int(data[blank + 1].split()[0])
        commence = blank + 2
        conclude = commence + atoms
        coord = [list(map(float, line.split()[:3])) for line in data[commence:conclude]]

    if ext in ('.pdb', '.pdbqt'):
        coord = [[float(line[31:38]), float(line[39:46]), float(line[47:54])] for line in data if line.split()[0] in ('ATOM', 'HETATM')]

    xcoor, ycoor, zcoor = zip(*coord)
    return [list(xcoor), list(ycoor), list(zcoor)]

def min_max(coord: list):
    return [min(coord), max(coord)]

def center_XYZ(coord_range: list):
    return round(statistics.mean(coord_range), 3)

def length_WHD(coord_range: list, scale: float):
    return round(abs(coord_range[0] - coord_range[1]) * scale, 3)

def LaBOX(data: str, ext: str, scale: float, find_center: bool):
    COOR = get_coordinates(data, ext)
    X,Y,Z = COOR
    ranges = [min_max(X), min_max(Y), min_max(Z)]
    center = [center_XYZ(ranges[0]), center_XYZ(ranges[1]), center_XYZ(ranges[2])] 
    bxsize = [length_WHD(ranges[0], scale), length_WHD(ranges[1], scale), length_WHD(ranges[2], scale)]
    print(f'LaBOX.py')
    if find_center:
        print(f'╰─○ Grid Box Center:  X {center[0]:>8}  Y {center[1]:>8}  Z {center[2]:>8}')
        print(f'    Grid Box Size  :  W {bxsize[0]:>8}  H {bxsize[1]:>8}  D {bxsize[2]:>8}')
    if not find_center:
        print(f'╰─○ Grid Box Size  :  W {bxsize[0]:>8}  H {bxsize[1]:>8}  D {bxsize[2]:>8}')

def main():
    try:
        opts, args = getopt.getopt(
            sys.argv[1:], 
            ':l:s:cha', 
            ['ligand=', 'scale=', 'center', 'help', 'about'])
    except getopt.GetoptError as msg:
        print(f'LaBOX.py')
        print(f'╰─○ {msg}')
        sys.exit(2)
    
    FILENAME = None
    CENTER = False
    SCALE = 2
    xcoor = None
    ycoor = None
    zcoor = None

    if opts == []:
        usage()
        sys.exit()
        
    for opt, arg in opts:
        if opt in ('-l', '--ligand'):
            FILENAME = arg
        if opt in ('-s', '--scale'):
            SCALE = float(arg)
        if opt in ('-c', '--center'):
            CENTER = True
        if opt in ('-h', '--help'):
            usage()
            sys.exit()
        if opt in ('-a', '--about'):
            about()
            sys.exit()

    TARGET = FILENAME
    file_handler(TARGET)
    EXT = os.path.splitext(TARGET)[-1]
    DATA = open(TARGET, 'r').readlines()
    LaBOX(DATA, EXT, SCALE, CENTER)
    
if __name__ == '__main__':
    main()

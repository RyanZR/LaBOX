# LaBOX

[![status](https://img.shields.io/badge/status-pass-green)](https://github.com/RyanZR/LaBOX)
[![version](https://img.shields.io/badge/version-1.0.2-blue)](https://github.com/RyanZR/LaBOX/releases/tag/v1.0.1)
[![size](https://img.shields.io/github/repo-size/RyanZR/LaBOX)](https://github.com/RyanZR/LaBOX)
[![license](https://img.shields.io/badge/license-MIT-informational)](https://github.com/RyanZR/LaBOX/blob/main/LICENSE)
[![DOI](https://zenodo.org/badge/663894936.svg)](https://zenodo.org/badge/latestdoi/663894936)

An automatic ligand-based grid box size calculation tool for molecular docking. \
Supported file formats include `.pdb`, `.pdbqt`, `.sdf` and `.mol2`. \
Revamped from *LABOGRID*.

```
Usage
╰─○ LaBOX.py [-l] <filename>

Argument
╰─○ Command description:
        -l  ligand filename (supported: pdb, pdbqt, sdf, mol2)
        -h  help
        -a  about
╰─○ Optional parameters:
        -s  scale factor (default is 2)
        -c  grid box center

Return
╰─○ Grid Box Center: X  {value} Y  {value} Z  {value}
    Grid Box Size  : W  {value} H  {value} D  {value}
```

## Method
> **NOTE:** The values have been rounded to three decimals for accuracy, and additional testing will be conducted to refine the optimal scale factor.
1. The **`min()`** and **`max()`** functions were employed to identify the minimum and maximum X, Y, and Z atomic coordinates of a ligand.
2. The **`statistics.mean()`** function was used to compute the X, Y, and Z coordinates of the center of the gridbox based on the values obtained in step 1.
3. The absolute difference (**`abs(subtraction)`**) between the minimum and maximum X, Y, and Z coordinates was used to determine the dimensions (width, length, and depth) of the gridbox.
4. A default **scale factor of 2** was applied to adjust the size of the gridbox based on the dimensions obtained in step 3.

## Bug
If you encounter any bugs, please report the issue to https://github.com/RyanZR/LaBOX/issues.

## License
The script is licensed under MIT, see the [LICENSE](https://github.com/RyanZR/LaBOX/blob/main/LICENSE) file for details.

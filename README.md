# LABOGRID

An automatic ligand-based grid box size calculation tool for molecular docking.

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
> **NOTE:** Values are rounded to 3 decimals at the end of calculation. Further testing will be performed to determine the optimal scale factor. 
1. `min()` and `max()` were used to determine the minimum and maximum X, Y, Z atomic coordinate of a ligand.
2. Using the values in 1, `statistics.mean()` was used to determine the X, Y, Z coordinate of a gridbox center.
3. Using the values in 1, the `abs(subtraction)` between the minimum and maximum X, Y, Z coordinate was used to determine the size of gridbox in terms of width, length and depth. 
4. **Scale factor of 2** (default) was used to adjust the gridbox size based on values in 3.

## Bug
If you encounter any bugs, please report the issue to https://github.com/RyanZR/labogrid/issues.

## License
The script is licensed under MIT, see the [LICENSE](https://github.com/RyanZR/labogrid/blob/main/LICENSE) file for details.

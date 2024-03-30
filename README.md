# dicom-compressors
This project aims to test several image algorithms for compressing DICOM images

This repo, accompanies the paper "Improving backup strategies in large DICOM databases based on weighted image compression"

For testing such algorithms (only works on Windows right now), follow these steps:

1. Download sample DICOM images :  https://drive.google.com/file/d/10qcVhKV--OaqO8mYKoPA5BsoP_-1lnuD/view?usp=sharing
   
2. Download uncompressors EXEs : https://drive.google.com/file/d/1NB8MGGsrIaPtkDDIWOQw9MaBLGUhxl9I/view?usp=sharing

3. Uncompress on a selected library

4. Run  "run_MRI_test.bat" . It will create a lot of subfolders, one for each case, with the different algorithms. This is expecting to have 10  NII files. Also, it will generate CSV files with corresponding metrics

5. Plot results running "python mainMetricsPaper.py" (check dependencies)

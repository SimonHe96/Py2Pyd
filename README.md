Python Dynamic Link Library
=
打开命令行，进入目录，执行以下命令。

Mac:
    /Applications/Autodesk/maya201x/Maya.app/Contents/bin/mayapy setup.py build_ext --inplace -I include -L libs
    
Windows:
    "C:/Program Files/Autodesk/Maya201x/bin/mayapy.exe" setup.py build_ext --inplace -I include -L libs


故障排除:
    1. error: Unable to find vcvarsall.bat
       如果系统上已经安装了Visual Studio，这个问题可以通过事先在命令行中设置排除，听说这个选项写死在编译器，只能这么干。
       SET VS90COMNTOOLS=%VS100COMNTOOLS%

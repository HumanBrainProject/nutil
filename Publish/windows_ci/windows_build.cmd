REM echo off
call "C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Auxiliary\Build\vcvarsall.bat" x86_amd64
REM set uploadScript=C:\Users\leuat\Documents\GitHub\uploadScript\upload_win_night.cmd

echo "Qmake.."
qmake Nutil.pro 
echo "Compiling.."
jom.exe -f Makefile.Release
cd release
windeployqt.exe .

cd %dir%\Publish\publish_win
call PublishWindows.cmd
call %uploadScript%

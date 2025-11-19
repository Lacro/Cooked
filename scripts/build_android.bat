@echo off

call cd ..
call C:/ProgramData/miniforge3/Scripts/activate
call conda activate Cooked_main_env

call flet build apk --output ./release/

pause

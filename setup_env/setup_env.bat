@echo off
set PROJECT_NAME=Cooked
set PYTHON_VERSION=3.13

echo[
echo ===================== Find Conda =====================

:find_miniforge
:: find mini forge and activate conda
set MINIFORGE_3_PATH=C:\ProgramData\miniforge3
if not exist %MINIFORGE_3_PATH%\python.exe goto :unable_to_install
call %MINIFORGE_3_PATH%\Scripts\activate.bat
echo Using Miniforge3
goto :check_workspace



:check_workspace
echo[
echo =================== Check workspace ==================

:: get current branch
for /F "tokens=* USEBACKQ" %%F in (`git branch --show-current`) do (
SET BRANCH_NAME=%%F
)
:: init environment name
set ENV_NAME=%PROJECT_NAME%_%BRANCH_NAME%_env
echo env name: %ENV_NAME%

:: check if old env exist
call activate %ENV_NAME%
set ENV_ALREADY_EXISTING=%errorlevel%==0

if %ENV_ALREADY_EXISTING% (
    call conda deactivate
    goto :check_user
) else (
    goto :create_env
)

:check_user
set /P REBUILD_PYTHON_ENV=Env already exist, remove old python env (y/[n]) %? 
if /I "%REBUILD_PYTHON_ENV%" equ "y" (
    goto :create_env
) else (
    goto :build_vs_code
)



:create_env
echo[
echo ================= Create Python env ==================

if %ENV_ALREADY_EXISTING% (
    :: remove old env
    echo removing old env
    call conda env remove -n %ENV_NAME% -y
    if exist %OLD_ENV_PATH% rmdir /S /Q %OLD_ENV_PATH%
)

call conda create -n %ENV_NAME% python=%PYTHON_VERSION% -y

:: install ants_king module
call activate %ENV_NAME%
call pip install -e ..
call pip list



:build_vs_code
echo[
echo ================ build VS Code projet ================
call activate %ENV_NAME%

if not exist ..\.vscode\ (
    :: create folder
    mkdir ..\.vscode\

    echo building settings.json
    :: generate settings.json
    type nul >..\.vscode\settings.json
    echo {>> ..\.vscode\settings.json
    echo     "python.defaultInterpreterPath": "%CONDA_PREFIX:\=/%/python.exe",>> ..\.vscode\settings.json
    echo     "terminal.integrated.defaultProfile.windows": "Command Prompt",>> ..\.vscode\settings.json
    echo }>> ..\.vscode\settings.json
) else (
    echo no change on VS Code config
)



echo[
echo ======================== DONE ========================
pause

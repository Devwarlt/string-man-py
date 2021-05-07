@ECHO OFF

SETLOCAL

ECHO [INFO]:
ECHO    * You must provide virtual environment file path to proceed.
ECHO    * Consider to edit local variable 'VIRTUAL_ENV_PATH' from this file declaration.
ECHO    * Once its declared, in file scope, you don't need to configure again.
ECHO.
ECHO [WARN]:
ECHO    * Remember to do NOT include folder 'Scripts' into virtual environment path.
ECHO.
ECHO [EXAMPLE]:
ECHO    SET VIRTUAL_ENV_PATH="%HOMEDRIVE%%HOMEPATH%\Env\myvenv"
ECHO.
ECHO.

SET VIRTUAL_ENV_PATH=""

IF %VIRTUAL_ENV_PATH%=="" (SET /P VIRTUAL_ENV_PATH="Enter virtual environment (venv) directory path: ") ELSE (CLS)

cmd %VIRTUAL_ENV_PATH%\Scripts\activate

ENDLOCAL

EXIT 0
@echo off
set "%LOCALAPPDATA%\Packages\TheBrowserCompany.Arc_ttt1ap7aakyb4\LocalCache\Local\Arc\StorableWindows.json"

if exist "%file_path%" (
    del /f /q "%file_path%"
    echo File "StorableWindows.json" has been forcefully deleted.
) else (
    echo File "StorableWindows.json" not found.
)

pause

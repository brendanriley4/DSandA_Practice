@echo off
setlocal enabledelayedexpansion

:: Set source directory
set source="C:\Users\rileybc\Source\Utilities\DSandA_Practice\PyCharmDirectory"

:: Loop through each file in the source directory
for %%f in (%source%\*) do (
    echo ---------------------------------------------------
    echo Found file: %%~nxf
    echo Choose a destination folder for this file:
    echo 1. Easy
    echo 2. Medium
    echo 3. Hard

    :: Get user input for the destination folder
    set /p choice="Enter the number (1, 2, or 3): "

    :: Set the destination based on user input
    if "!choice!"=="1" (
        set destination="C:\Users\rileybc\Source\Utilities\DSandA_Practice\Easy"
	echo Moved %%~nxf to "Easy"
    ) else if "!choice!"=="2" (
        set destination="C:\Users\rileybc\Source\Utilities\DSandA_Practice\Medium"
	echo Moved %%~nxf to "Medium"
    ) else if "!choice!"=="3" (
        set destination="C:\Users\rileybc\Source\Utilities\DSandA_Practice\Hard"
	echo Moved %%~nxf to "Hard"
    ) else (
        echo Invalid choice, skipping file...
        goto skip
    )

    :: Use robocopy to copy the selected file to the chosen destination
    robocopy %source% !destination! "%%~nxf" /XO > nul 2>&1
    set exit_code=!errorlevel!

    :: Check if robocopy was successful
    if !exit_code! lss 2 (
        echo File moved successfully, deleting from source...
        del "%%f" > nul 2>&1
    ) else (
        echo Failed to move the file, not deleting.
    )

    :skip
    echo ---------------------------------------------------
)

pause

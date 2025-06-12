@echo off
echo Starting OSRS Cooking Profit Calculator...
echo.

REM Activate virtual environment
call myenv\Scripts\activate

REM Run the main Python script
python main.py

REM Keep the window open to see results
echo.
echo Press any key to exit...
pause >nul 
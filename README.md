# YouTube_Time_Analyser
Python script for calculating time spent watching YouTube videos

## Instruction
1. Download your YouTube history via Google takeout. Select only "YouTube and YouTube Music" and only "History". Also make sure that history is exported in .json faormat
2. Copy .json file with your history from downloaded archive to the script folder. Rename .json file to "history.json"
3. Run the script. It will take a lot time to process all videos. Current progress will be shown in the terminal. Note that length of deleted videos will be assumed as average length of your videos. Also videos with length more than 1 day (extremly long live streams) will be assumed as average length videos too.
4. Get your total wasted time and think what have you spent your life on...

Note: Clearing YouTube history removes all information from Google servers, so this script will only count time spent since last time you have fully cleared your history.  

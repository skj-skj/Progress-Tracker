# Progress Tracker V3 (ptv3)

## Simple CL (Command Line) way to track Series/Movies/Courses from your PC <br /><br />

### A) How to get Stated:
1. run `ptv3.py`
2. enter `N` for new entry
3. Enter `Name` and Main `Folder Location`
    - Example: <br/> Name = `foo Anime` <br/> Folder Location = `E:\Anime\foo Animated Series`
4. Enter if the Folder `is Seasoned` or not (by default is No)
    - `is Seasoned` = `Y`: if `foo Anime` have sub folders like `Season 01` , `Season 02` etc. <br/><br/>
      `is Seasoned` = `N`: if `foo Anime` does't have sub folders just `Episode 01.mkv` , `Episode 02.mp4` etc.
5. Done, Now it will show the episode list one by one.<br/>
   i. enter `0` to watch and it will open in default video player.<br/>
   ii. enter `1` if already watched.<br/>
   iii. enter `x` or `q` or `exit` or `quit` to exit.<br/>
   iv. any other key will show the prompt for the same episode.<br/><br/>
6. After watching the Episode/File prompt will ask if you watched it or not<br/>
   `0`: Watched <br/> `1`/`Any Other Key`: Not Watched 

<br/>

### B) Already Created New Entry
1. run `ptv3.py`
2. Enter number in front of your desire Series/Movies/Courses you want to watch ex: `1` , `2` etc. <br/>
   or Enter `N` for new entry (goto A.)<br/><br/>
3. Done, Now it will show the episode list one by one.<br/>
   i. enter `0` to watch and it will open in default video player.<br/>
   ii. enter `1` if already watched.<br/>
   iii. enter `x` or `q` or `exit` or `quit` to exit.<br/>
   iv. any other key will show the prompt for the same episode.<br/><br/>
4. After watching the Episode/File prompt will ask if you watched it or not<br/>
   `0`: Watched <br/> `1`/`Any Other Key`: Not Watched 

<br/>

### C) To see the Progress Percentage(%)
1. run `ptv3Progress.py`
2. Enter number in front of your desire Series/Movies/Courses ex: `1` , `2` etc. <br/>
3. Done.

### D) To Forcefully Update To a Fixed episode
1. run `ptv3ForceUpdator.py`
2. Enter number in front of your desire Series/Movies/Courses you want to forcefully updated it ex: `1` , `2` etc. <br/>
   or Enter `N` for new entry (goto A - 1. to 4.)
3. Enter last episode/file you watched
    - Example:<br/>
      Last Watched File = `foo Anime Episode 20.mkv`
4. Done, Series/Movies/Courses are forcefully updated till the last episode/file entered

### E) To Delete 
1. run `ptv3Delete.py`
2. Enter number in front of your desire Series/Movies/Courses to Delete ex: `1` , `2` etc.
3. Enter `Y` in Confirm prompt
4. Delete

( Note: Once Deleted tracker file of that Series/Movies/Courses can't be recoverd, if you deleted you tracker file it is recommanded to use `ptv3ForceUpdator.py` to initialised it.<br> `ptv3Delete.py` won't delete your episodes/files )

<br/>

## Happy Watching
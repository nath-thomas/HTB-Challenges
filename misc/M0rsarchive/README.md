Path traversal is really hard once you hit the following error:
```
OSError: [Errno 36] File name too long
```
You can move the the bottom of the directory tree with:
```bash
while [ $? -eq 0 ]; do cd flag/; done
```
Move everything back up to root level, delete the higher numbered flag archives and restart the process.

Once it finishes at error:
```
ls: cannot access '*.zip': No such file or directory
```
Traverse to the bottom of the file tree again and cat the flag file. 

These manually steps could probably be extended into the bash script but... meh I only intend on doing this once.

# Different file operation modes in python
- 'r': Opens a file for reading (default mode); raises an error if the file does not exist.
- 'w': Opens a file for writing; creates a new file or truncates an existing file.
- 'a': Opens a file for appending; data is written at the end of the file without truncating it.
- 'b': Opens a file in binary mode; used for non-text files (e.g., images).
- 'x': Opens a file for exclusive creation; fails if the file already exists.
  - If the file does not exist: Python will create the file and open it in write mode.
  - If the file already exists: Python will prevent any changes and immediately raise a FileExistsError.
- 't': Opens a file in text mode (default mode); used for text files.
- 'rb': Opens file for read operation in binary mode
- 'rw': Opens file for write operation in binary mode


  

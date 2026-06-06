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

# Examples
- [Reading a word document](https://github.com/varugheseben/edurek-data_science/blob/main/Python-Assignment-1/file_reading_word_document.ipynb)
  To install library for opening a docx file in google colab you can use below command in google colab code space
  
  **!pip install python-docx**
  
        !pip install python-docx
  
        Collecting python-docx
          Downloading python_docx-1.2.0-py3-none-any.whl.metadata (2.0 kB)
        Requirement already satisfied: lxml>=3.1.0 in /usr/local/lib/python3.12/dist-packages (from python-docx) (6.1.1)
        Requirement already satisfied: typing_extensions>=4.9.0 in /usr/local/lib/python3.12/dist-packages (from python-docx) (4.15.0)
        Downloading python_docx-1.2.0-py3-none-any.whl (252 kB)
           ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 253.0/253.0 kB 5.7 MB/s eta 0:00:00
        Installing collected packages: python-docx
        Successfully installed python-docx-1.2.0
- [Reading a PDF document]()
    To install library for opening a docx file in google colab you can use below command in google colab code space
  
  **!pip install pypdf**

       !pip install pypdf

       Collecting pypdf
         Downloading pypdf-6.13.0-py3-none-any.whl.metadata (7.2 kB)
       Downloading pypdf-6.13.0-py3-none-any.whl (345 kB)
          ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 346.0/346.0 kB 12.8 MB/s eta 0:00:00
       Installing collected packages: pypdf
       Successfully installed pypdf-6.13.0




  

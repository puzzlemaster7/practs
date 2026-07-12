# Practical 2A Commands

## Sleuth Kit Setup

Install Sleuth Kit and add this folder to the environment `PATH`:

```text
C:\Program Files (x86)\sleuthkit-4.14.0-win32\bin\
```

## Commands Shown In The Practical

```powershell
fls "C:\Users\spdc\Downloads\Test_Image.E01"
fstat "C:\Users\spdc\Downloads\Test_Image.E01"
fsstat -o 2414960 "C:\Users\spdc\Downloads\Test_Image.E01"
fsstat -o 8 "C:\Users\spdc\Downloads\Test_Image.E01"
fsstat -o 16384 "C:\Users\spdc\Downloads\Test_Image.E01"
```

## Notes

- `fls` lists files and directories inside the forensic image.
- `fstat` shows file metadata.
- `fsstat` displays file system information.
- The `-o` value is the image offset and may vary depending on the image.

# Practical 4A Commands

## Folder And Text File Setup

```bash
mkdir forensiclab
cd forensiclab
echo "This is a forensic lab file" > evidence.txt
cat evidence.txt
```

## Package Update And Zip Encryption

```bash
sudo apt update
sudo apt install zip -y
zip -e evidence.zip evidence.txt
ls -l
```

## John The Ripper Steps

```bash
sudo apt install john -y
locate zip2john
zip2john evidence.zip > password_hash.txt
cat password_hash.txt
```

## Notes

- `zip -e` creates an encrypted ZIP archive.
- `ls -l` is used to confirm the encrypted archive was created.
- `zip2john` extracts the hash from the ZIP file for password cracking with John the Ripper.

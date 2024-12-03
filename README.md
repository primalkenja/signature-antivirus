Extra info:
The way this works is that signatures.txt contains a list of SHA-256 hashes of known malicious files.
The program will scan test_files directory to look for any files that match these hashes.
Program output shows all the files in the directory as either safe/clean or alert/malware detected.

Initially, I just wrote any random word, like "banana", in the file that's supposed to be
detected as malware in the test_files folder. Then, I would calculate the SHA-256 hash of "banana" and add it to
the signatures.txt file. This helped me test the program and ensure that it worked.

Now that I know it works, I wanted to make it a bit more realistic.
https://github.com/romainmarcoux/malicious-hash/tree/main
^has a txt file of 58379 SHA-256 hashes of known malware.
This is now put in the signatures.txt file.

I then went to
https://bazaar.abuse.ch/browse/
and searched some of the malware hashes to get their unhashed file. I put some of these
files in the test_files directory. So now the corresponding hash for the malware file is in the
signatures.txt and it will be flagged as malware in our program. This makes the program feel
much more realistic and legit as it is doing signature-based malware detection on files that contain actual
malicious content. Its basically a mini version of a real antivirus.

(Don't worry, the test files won't give you a virus, they're all in .txt and when I print the output
I just write .exe instead. Unless you change the extension back into .exe and actually execute it
without any antivirus{like manually turning off windows defender}, nothing will happen.)

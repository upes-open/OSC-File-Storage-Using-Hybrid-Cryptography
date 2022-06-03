# Open Summer of Code: File Storage Using Hybrid Cryptography

About

The main aim of this project is to securely store and retrieve data on the cloud that is only controlled by the owner of the data. Cloud storage issues of data security are solved using cryptography and steganography techniques.The user can store the file safely in online cloud storage as these files will be stored in encrypted form in the cloud and only the authorized user has access to their files.

Tech Stack

Front end: React Native, JS

Python-Flask for Backend Developemnt

Methodology
To achieve the above goal, the following methodology needs to be followed:

Load the file on the server.
Dividing the uploaded file into N parts.
Encrypting all the parts of the file using any one of the selected algorithms (Algorithm is changed with every part in round robin fashion).
The keys for cryptography algorithms is then secured using a different algorithm and the key for this algorithm is provided to the user as public key.
After the above 4 steps you will have a N files which are in encrypted form which are stored on the server and a key which is downloaded as public key for decrypting the file and downloading it.

To restore the file, follow the following steps:

Load the key on the server.
Decrypt the keys of the algorithms.
Decrypt all the N parts of the file using the same algorithms which were used to encrypt them.
Combine all the N parts to form the original file and provide it to the user for downloading.


## Setup
Here's a brief intro about what a contributor must do in order to start developing the project further:
1. Open VSCode 
2. Copy the given command
```shell
git clone (https://github.com/upes-open/OSC-File-Storage-Using-Hybrid-Cryptography.git)
```
3. Go to folder according to the issue you are working and save your work
```shell
git add .
```
4. Now commit your changes
```shell
git commit -m "your message"
```
5. Raise your first PR 

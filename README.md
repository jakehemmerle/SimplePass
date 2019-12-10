## Password Manager featuring AES-128-GCB encryption and the Argon2id KDF

NOTE: I haven't figured out how to manipulate the decrypted DB without writing it to disk yet. Don't use this for real data.
Go download [BitWarden](https://bitwarden.com/).

### Features
- Stores usernames and passwords.
- These secrets are stored in an AES-128-GCB encrypted SQLite3 database
- AES key is derived from a user-specified password and a predefined salt using the Argon2id KDF, winner of the 
Password Hashing Competition (https://password-hashing.net/).


### Intro 
For my final project for CS2021, I decided to implement a basic password vault in Python using the Argon2 KDF and
AES-128-GCB.


### Installation and Configuration
NOTE: precompiled binaries are in the **dist** folder. You can run these instead of installing dependencies and 
building from source.
1. Make sure that Conda is installed.
2. Create a new Conda environment from the **environment.yaml** file by running `conda env create -f environment.yaml`


### Running the password manager

Actually you have to implement it. Run the tests to see it work. It is in the **vault.py** file. 

### Running tests
In the root folder (SimplePass), run the following: `python -m unittest discover -s test`.
This will run all the unit tests in the **test** directory.


### Folders

**password_manager** - contains the source code

**test** - contains test files for understanding the functionality of Argon2 and the AES module


### Improvements and considerations
- Writing the unencrypted SQLite3 database to disk is a SERIOUS security risk, since it could be copied or stored after deleting.
    - This can probably be solved by exporting the DB as SQL, encrypting the SQL, writing to disk, and then importing and decrypting the SQL,
    and rebuilding the DB in memory. Or by just using SQLCipher
- After talking with some Python devs, it sounds like an object that acts 
like a file object that you simply specify the encryption/decryption settings for doesn't exist. Maybe this will be the 
next open source project I start and never finish.

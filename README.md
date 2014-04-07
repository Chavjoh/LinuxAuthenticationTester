LinuxAuthenticationTester
=========================

Test windows authentication of a user with multiple password given in a dictionary.

## Requirements

* Python 2.7.3
* Python Pam 0.4.2

## Tests

Tested on Ubuntu 12.04 LTS with Python 2.7.3 and Python Pam 0.4.2-12.2ubuntu4

**Warning** : Python Pam 0.4.2 have a security issue : supplying a password containing a NULL-byte to the module trigger a double-free condition. It may allow remote code execution. Be careful to use a version that patch this issue.

## Tester with PAM module

Launch the script with :
```
python LinuxAuthenticationTesterPam.py username dictionary
```

Arguments : 
* **username** : Username used to test each password in given dictionary file.
* **dictionary** : Dictionary file path that contains all password to test.

Benchmark :
* It takes more than **1 hour** to test a dictionary with 3905 passwords. 

Analysis : 
* The benchmark is terribly long because of the presence of a fail delay setting. If you have root access, you can change this setting in **/etc/pam.d/common-auth**. Otherwise, you can make a work-around that know that the password is false if the response is not arrived after 0.5 seconds (this value need to be adjusted for better performance), for example.

Improvement idea :
* Whenever the password is correct or not, PAM should wait a random time (for example between 0.3 and 0.6 seconds) to respond. In this case, the work-around quoted above is no more functional.

## Tester with /etc/shadow

Launch the script with :
```
python LinuxAuthenticationTesterShadow.py username dictionary
```

Arguments : 
* **username** : Username used to test each password in given dictionary file.
* **dictionary** : Dictionary file path that contains all password to test.

Benchmark :
* It takes about **15 seconds** to test a dictionary with 3905 passwords.

## Dictionary

### Content

Each line of the dictionary correspond to a password and is terminated by a newline character ```\n```.

For example :
```
a
b
c
...
aa
ab
ac
...
```

### Generator

Have a look to the project [DictionaryGeneratorPHP](https://github.com/Chavjoh/DictionaryGeneratorPHP).

## Feedback

Don't hesitate to fork this project, improve it and make a pull request.

## License

This project is under Apache 2.0 License.

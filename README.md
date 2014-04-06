LinuxAuthenticationTester
=========================

Test windows authentication of a user with multiple password given in a dictionary.

## Requirements

* Python >= 2.7.3
* Python Pam >= 0.4.2

## Tests

Tested on Ubuntu 12.04 LTS with Python 2.7.3 and Python Pam 0.4.2-12.2ubuntu4

**Warning** : This version of Python Pam have a security issue : supplying a password containing a NULL-byte to the module trigger a double-free condition. It may allow remote code execution. Please use a newer version.

## Tester with PAM module

Launch the script with :
```
python LinuxAuthenticationTesterPam.py username dictionary
```

Arguments : 
* **username** : Username used to test each password in given dictionary file.
* **dictionary** : Dictionary file path that contains all password to test.

Benchmark :
* It takes more than **30 minutes** to test a dictionary with 3905 passwords. 

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

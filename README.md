# Sample project scaffold for Python
Template repository for repeatable project setup that suport continuous integration and delivery

![image](https://user-images.githubusercontent.com/77303576/193753136-8cd5f66e-7b9b-455a-95f4-eb48508ff639.png)

## Setting up

### Create a new github repository
* Add a README and gitignore file for a Python template
* Copy your Github SSH link (git@github.com:[your_github_username]/[your_repository].git) under 'Code > Clone > SSH'

### Create an encripted bi-direction communication with SSH keys
```
$ ssh-keygen -t rsa
```
will put a public/private key pair on your current directory.

![image](https://user-images.githubusercontent.com/77303576/193754120-1003ec65-8fbe-49a4-a771-76f56b3b0a68.png)
```
$ cat /home/ec2-user/.ssh/id_rsa.pub
```
Copy the output key. This is not a secret key and can be stored publicly.
Under Github profile settings:
* SSH and GPG keys
* New SSH key
* Paste key and name it to your current project/environment
* Confirm password / authentication
* 

### Project basic structure
Clone your recently created repository.
```
$ git clone git@github.com:[your_github_username]/scaffold.git
$ cd scaffold
```
Create your project structure:
* your_app.py
* test_your_app.py
* Makefile
* requirements.txt
```
$ touch your_app.py
$ touch test_your_app.py
$ touch Makefile
$ touch requirements.txt
```

### Create a Python virtual environment
Use python venv modul to create a hiden (/.) virtual environment.
```
$ python3 -m venv ~/.scaffold
$ source ~/.scaffold/bin/activate
```
You can now see your current python environment living under your project directory:
![image](https://user-images.githubusercontent.com/77303576/193755675-6f07ec47-23e9-4c9b-ae28-bb0002e65cc6.png)

### Configuring your Makefile and requirements.txt
Switch Makefile structure to Tabs (from spaces):

![image](https://user-images.githubusercontent.com/77303576/193756433-f1907785-1bdc-4a6a-bfe3-797951806532.png)

You can reffer to the [Makefile](https://github.com/erich-hs/scaffold/blob/main/Makefile) in this repository as a basic example.

Define your basic requirements for initial package installations. You can refer to the [requirements.txt](https://github.com/erich-hs/scaffold/blob/main/requirements.txt) in this repository as an example for packages listed under our Makefile.

### Commit, push, and continue development
Commit initial project structure and configure your global user information.
```
$ git commit -m "adding initial structure"
$ git config --global user.name "[Your Name]"
$ git config --global user.email "[Your E-mail]"
```
And push it to GitHub
```
$ git push
```

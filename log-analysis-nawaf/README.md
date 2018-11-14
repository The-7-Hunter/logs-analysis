# Logs-analysis

This project has been developed in response to the newspaper request to analyse their articles and authors based on logs.

## Getting Started

  Follow these steps to run the code locally.
Download and install Vagrant 2.2.0
Download Vagrantfile and install the virtual box:
https://github.com/udacity/fullstack-nanodegree-vm.git
```sh
$ cd FSND_VM/vagrant
$ vagrant up
```
this may take some time, make sure you are connected to the internet otherwise if you disconnect then you should run it again.

Download the database file then extract it, you can download it from here:
https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

Make sure that you've downloaded it on the same vagrant directory so that it will be accessible inside the virtual box.

## Installing
First log into the virtual box using ```sh
$ vagrant ssh
```  
Then go to the shared directory inside the virtual box
```sh
cd /vagrant.
``` 
set log-analysis-nawaf folder inside vagrant directory.

## Import database:
```sh
psql -d news -f newsdata.sql
```
## Running code:
After completing all previous steps sucssefuly, run the code with:
```sh
$ python main.py
```

#!/bin/bash

echo 'Running the script...'

echo 'Setting up alias "helo"'

hello(){
	echo "
		# Alias for ls cmd
		alias helo='ls'
	" >> ~/.bashrc

	echo 'Alias helo setup done'
}

type helo || hello

echo 'Hi'

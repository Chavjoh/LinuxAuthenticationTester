#!/usr/bin/python
# coding: latin-1

#------------------------------------------------------------------------------#
# Security - Linux Authentication Tester with /etc/shadow                      #
# ============================================================================ #
# Note:         To be used for test purpose only                               #
# Developer:    Chavaillaz Johan                                               #
# Filename:     LinuxAuthenticationTesterShadow.py                             #
# Version:      1.0                                                            #
#                                                                              #
# Licensed to the Apache Software Foundation (ASF) under one                   #
# or more contributor license agreements. See the NOTICE file                  #
# distributed with this work for additional information                        #
# regarding copyright ownership. The ASF licenses this file                    #
# to you under the Apache License, Version 2.0 (the                            #
# "License"); you may not use this file except in compliance                   #
# with the License. You may obtain a copy of the License at                    #
#                                                                              #
# http://www.apache.org/licenses/LICENSE-2.0                                   #
#                                                                              #
# Unless required by applicable law or agreed to in writing,                   #
# software distributed under the License is distributed on an                  #
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY                       #
# KIND, either express or implied. See the License for the                     #
# specific language governing permissions and limitations                      #
# under the License.                                                           #
#                                                                              #
#------------------------------------------------------------------------------#

#------------------------------------------------------------------------------#
#                                                                              #
#                               LIBRARIES IMPORT                               #
#                                                                              #
#------------------------------------------------------------------------------#

import sys
import crypt
import spwd
import argparse

#------------------------------------------------------------------------------#
#                                                                              #
#                             UTILITIES FUNCTIONS                              #
#                                                                              #
#------------------------------------------------------------------------------#

def checkAuthentication(user, password):
	"""
	Test authentication in linux
	
	:param username: Account username to test
	:type username: str
	:param password: Account password to test
	:type password: str
	"""
	try:
		# Return the shadow password database entry for the given user name
		shadowPasswordDatabase = spwd.getspnam(user)[1]
		
		if crypt.crypt(password, shadowPasswordDatabase) == shadowPasswordDatabase:
			return True
		else:
			return False
			
	except KeyError:
		print("user '%s' not found" % user)
		sys.exit()

def bruteForce(username, dictionary):
	"""
	Authentication test for each password in the dictionary
	with the given user name and domain
	
	:param username: Username used to test each password in given dictionary file
	:type username: str
	:param dictionary: Dictionary file path that contains all password
	:type dictionary: str
	"""
	
	# Open dictionary file
	with open(dictionary) as file:
		# Read each line : One line = One password
		for line in file:
			# Delete new line character
			password = line.rstrip('\n')
			# Check authentication
			if checkAuthentication(username, password):
				return password
				
	return False

#------------------------------------------------------------------------------#
#                                                                              #
#                               "MAIN" FUNCTION                                #
#                                                                              #
#------------------------------------------------------------------------------#

# If this is the main module, run this
if __name__ == '__main__':
	argsCount = len(sys.argv)
	
	# Create argument parser to help user
	parser = argparse.ArgumentParser(
		description='Test user authentication with a given dictionary.'
	)
	parser.add_argument(
		'username', 
		type=str,
		help='Username used to test each password in given dictionary file.'
	)
	parser.add_argument(
		'dictionary', 
		type=str,
		help='Dictionary file path that contains all password to test.'
	)
	
	# Show help if one of the arguments is missing
	if argsCount != 3:
		parser.print_help()
		sys.exit()
	
	# User and dictionary file in scripts arguments
	username = sys.argv[1]
	dictionary = sys.argv[2]
	
	# Launch script
	try:
		password = bruteForce(username, dictionary)
	
		if not password:
			print("Password not found in dictionary")
		else:
			print("Password found : " + password)
	
	except (OSError, IOError) as e:
		print("Dictionary not found")
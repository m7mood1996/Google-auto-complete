# Auto-completion-project-python

> An CLI auto complation program that suggest a complation for your search using a ser of text files.

<div align="center"><img src="https://i.ibb.co/cL2BsGZ/1-m-Wgm8-Gugi3r3-Pv-Kv-Zl-F-Yw.png" width="400" height="300"/></div>

<br>

--

### Table of Contents

- [Description](#description)
- [How To Use](#how-to-use)
- [References](#references)
- [License](#license)
- [Author Info](#author-info)

---

## Description

From a data-set (text files), generating a trie tree of all the prefixes in these text files, which give an advantage to search efficintlly for a phrase and return the top-k auto comletion based on score of uncorrect writting of the phrase.


### Technologies

- Python
- VS Code

[Back To The Top](#Auto-completion-project-python)

---

## How To Use

### Installation

- Copy this link ***https://github.com/bashbash96/PartnerFinder.git*** then on cmd or bash do:

		cd ~/Desktop
		git clone {{the link you just copied}} Project

- This creates a directory named "Project", clones the repository there and adds a remote named "origin" back to the source.

		cd Project
		git checkout develop

- If that last command fails

		git checkout -b develop

------------
### Updating/The Development Cycle

You now have a git repository, likely with two branches: master and develop. Now bake these laws into your mind and process:

You will never commit to ***master*** or ***develop*** directly  .

Instead, you will create ***feature branches*** on your machine that exist for the purpose of solving singular issues. You will always base your features off the develop branch.

		git checkout develop
		git checkout -b my-feature-branch

This last command creates a new branch named "my-feature-branch" based off of develop. You can name that branch whatever you like. You should not have to push it to Github unless you intend to work on multiple machines on that feature.

Make changes.

	git add .
	git commit -am "I have made some changes."

This adds any new files to be tracked and makes a commit. Now let's add them to develop.

	git checkout develop
	git merge --no-ff my-feature-branch
	git push origin develop
------------
### Releasing

Finished with your project?

- Create a feature branch as normal.
- Update the version history in the README.md file
- Update this to develop as normal.

		git checkout master
		git merge --no-ff develop
		git push origin master
		git tag v1.0.0
		git push origin v1.0.0
------------

To run locally, in the project dirictory do the following in the terminal/cmd:
```
python manage.py runserver
```

[Back To The Top](#partner-finder-search-engine)

---
## References
[`Python`](https://www.python.org/)
[`VS Code`](https://code.visualstudio.com/)
[`Trie tree`](https://www.geeksforgeeks.org/trie-insert-and-search/)


---
## License

GPL License

Copyright (c) [2020] [Amjad Bashiti]

  The licenses for most software and other practical works are designed
to take away your freedom to share and change the works.  By contrast,
the GNU General Public License is intended to guarantee your freedom to
share and change all versions of a program--to make sure it remains free
software for all its users.  We, the Free Software Foundation, use the
GNU General Public License for most of our software; it applies also to
any other work released this way by its authors.  You can apply it to
your programs, too.

  When we speak of free software, we are referring to freedom, not
price.  Our General Public Licenses are designed to make sure that you
have the freedom to distribute copies of free software (and charge for
them if you wish), that you receive source code or can get it if you
want it, that you can change the software or use pieces of it in new
free programs, and that you know you can do these things.

  To protect your rights, we need to prevent others from denying you
these rights or asking you to surrender the rights.  Therefore, you have
certain responsibilities if you distribute copies of the software, or if
you modify it: responsibilities to respect the freedom of others.

  For example, if you distribute copies of such a program, whether
gratis or for a fee, you must pass on to the recipients the same
freedoms that you received.  You must make sure that they, too, receive
or can get the source code.  And you must show them these terms so they
know their rights.

[Back To The Top](#Auto-completion-project-python)

---
## Author Info

- Github - [m7mood1996](https://github.com/m7mood1996)
- Linkedin - [Mahmood-Qawasmi](https://www.linkedin.com/in/mahmood-qawasmi-457013163)

[Back To The Top](#Auto-completion-project-python)

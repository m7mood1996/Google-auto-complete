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

- Copy this link ***https://github.com/m7mood1996/Auto-completion-project-python.git*** then on cmd or bash do:

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

[Back To The Top](#Auto-completion-project-python)

---
## References
[`Python`](https://www.python.org/)
[`VS Code`](https://code.visualstudio.com/)
[`Trie tree`](https://www.geeksforgeeks.org/trie-insert-and-search/)


---
## License

GPL License

Copyright (C) [2021]  [Mahmood Qawasmi]

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

[Back To The Top](#Auto-completion-project-python)

---
## Author Info

- Github - [m7mood1996](https://github.com/m7mood1996)
- Linkedin - [Mahmood-Qawasmi](https://www.linkedin.com/in/mahmood-qawasmi-457013163)

[Back To The Top](#Auto-completion-project-python)

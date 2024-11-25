# **Git Workflow for Project Management**

## **Before Starting Work on the Project**

1. **Ensure You Are in the Right Directory**:
   ```bash
   git init
   git status  # Check the current branch
   git checkout main  # Switch to the main branch
   git pull  # Fetch the latest changes from GitHub

Start Working on a New Branch

Git Commands:

	1.	Check the current status:

git status


	2.	List all branches:

git branch -l


	3.	Create a new branch (e.g., lisa_branch):

git branch lisa_branch


	4.	Verify the new branch is created:

git branch -l


	5.	Switch to the new branch:

git checkout lisa_branch


	6.	Confirm you are on the correct branch:

git branch -l

Code Changes and Push

	1.	Add your changes:

git add .


	2.	Commit your changes:

git commit -m "Give the commit name"


	3.	Push the changes to the remote branch:

git push --set-upstream origin lisa_branch


	4.	Push again to ensure everything is up-to-date:

git push origin lisa_branch

Validate and Merge

	1.	Go to GitHub:
	•	Validate the code and check if there are any conflicts with other changes.
	2.	If everything is okay, create a Pull Request (PR) for merging the branch:
	•	Compare your branch (lisa_branch) with the main branch.
	•	Submit the merge request.
	3.	Once reviewed and validated, merge the branch into main.

Tips:

	•	Always pull the latest changes from the main branch before starting new work.
	•	Regularly check for conflicts while pushing your branch to avoid merge issues.
	•	Provide meaningful commit messages to describe your changes clearly.


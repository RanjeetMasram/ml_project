# ml_project
ML Project

`Software and Account Requirements to Run`
1. [Github](https://github.com/)
2. [Heroku Account](https://herokuapp.com/)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT CLI](https://git-scm.com/downloads)
5. [Ananconda](https://www.anaconda.com/products/distribution)

### Creating conda environment
```
conda create -p venv python==3.7 -y
```

### Activate conda environment

```
conda activate venv
```
OR
```
conda activate venv/
```

### Installing Requirements
```
pip install -r requirements.txt
```

### Git commands
To check git status
```
git status
```
To add a file
```
git add <file_name>
```

To add all the files
```
git add .
```
> Note: to ignore some files and folder to be send at remote add those files and folder names to .gitignore file 

To commit changes
```
git commit -m "commit msg"
```

To edit local commit message
```
git commit --amend
```

To push the changes to remote
```
git push origin <branch_name>
```

To check all version maintained by git
```
git log
```

To check remote url
```
git remote -v
```

### Connect to Heroku
```
HEROKU_EMAIL:masram.ranjeet@gmail.com
HEROKU_API_KEY:<>
HEROKU_APP_NAME:rj-ml-regression-app
```

### Build docker image
```
docker build -t <image_name>:<tag_name>
```
> Note: Image name for docker should be in lower case

To list docker images
```
docker images
```

To run docker image
```
docker run -p 5000:5000 -e PORT=5000 <IMAGE_ID>
```

To check running containers in docker
```
docker ps
```

To stop docker container
```
docker stop <container_id>
```
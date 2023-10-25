---
title: Master class CI/CD
author: Zeger Hendrikse
date: 2023-09-29
---

## Exercises

![Exercise](./images/exercise-722x406.jpg)

---

### Introduction

- What are we going to build
- During the day, we will complete our course

---

### Prerequisites

- Clone the toy project
  - Generate SSH key
  - Upload it to GitLab
- Run the toy project (and tests)

---

### Add SSH key to GitLab

- [Generate an SSH key](https://docs.gitlab.com/ee/ssh/#ed25519-ssh-keys) _without_ passphrase:

  ```bash
  $ ssh-keygen -t rsa -b 4096
  Generating public/private rsa key pair.
  Enter file in which to save the key (/home/zwh/.ssh/id_rsa):
  Enter passphrase (empty for no passphrase):
  Enter same passphrase again:
  Your identification has been saved in /home/zwh/.ssh/id_rsa.
  Your public key has been saved in /home/zwh/.ssh/id_rsa.pub.
        .
        .
        .
   ```

- Next, [add the public SSH key to your GitLab account](https://docs.gitlab.com/ee/ssh/#add-an-ssh-key-to-your-gitlab-account)

---

### Clone the repo and run tests

- Clone the repo:
  ```bash
  $ git clone git@gitlab.com:cicd-masterclass/excercise.git
  ```

- Make sure dependencies are up-to-date:
  ```bash
  $ pip install -r requirements.txt
  ```

- Run the unit tests:
  ```bash
  $ pytest
  ```

---

## Intermezzo: Falcon

---

### Rest in Python:
- Flask with Flask-RESTFul
- Django + REST Framework
- [Falcon](https://falconframework.org/) (very good light-weight API framework)

---

### According to [this site](https://dev.to/_mertsimsek/falcon-api-framework-on-docker-5eid):
> Accordingly, Falcon claims (I agree with them), other frameworks weigh you down with tons of dependencies and unnecessary abstractions. Falcon cuts to the chase with a clean design that embraces HTTP and the REST architectural style.

---

### Run the Fibonacci API

- Run the application using plain Python:
  ```bash
  $ python fibonacci.py
  ```

- Run the application using [gunicorn](https://www.digitalocean.com/community/tutorials/how-to-deploy-falcon-web-applications-with-gunicorn-and-nginx-on-ubuntu-16-04):
  ```bash
  $ gunicorn --bind 0.0.0.0:8000 fibonacci:app
  ```

- Test it (manually) by opening it using:
  - your webbrowser [http://localhost:8000/api/fibonacci/8](http://localhost:8000/api/fibonacci/8) _or_
  - using curl: 
    ```bash
    $ curl localhost:8000/api/fibonacci/8
    ```

---

### Run the application using Docker

- Build and run the container
  ```bash
  $ docker build -t fibonacci:latest .
  $ docker run --rm -d -p80:80 fibonacci:latest
  ```

- Test it (manually) by opening it using:
  - your webbrowser [http://localhost/api/fibonacci/8](http://localhost/api/fibonacci/8) _or_
  - using curl: 
    ```bash
    $ curl localhos/api/fibonacci/8
    ```

- Don't forget to stop the container!

---

### Set up your playground

- Complete your GitLab sign-up

- Your playground will be a branch, so [let's branch](https://www.gitkraken.com/learn/git/problems/create-git-branch):
    ```bash
    $ git checkout -b participant_zeger
    ```

- Optionally, add [branch info to your command prompt](https://thucnc.medium.com/how-to-show-current-git-branch-with-colors-in-bash-prompt-380d05a24745)

  ![Git command prompt](images/git-command-prompt.png)

---

## Intermezzo: GitLab CI definitions

Definitions in CI pipelines:

<ul>
<div>
<li><i>pipeline</i>: a series of actions triggered by a single Git commit</li>
</div>
<div class="fragment">

<li><i>runner</i>: build server
  <ul>
  <li>Any machine with GitLab runner software</li>
  <li>Can also be based on Docker</li>
  </ul>
</li>
</div>
<div class="fragment">
<li><i>job</i>: single action (package step, test step, quality step)</li>
</div>
<div class="fragment">
<li><i>stage</i>: group of related actions in a pipeline</li>
</div>
</ul>

---

## Intermezzo: [GitLab CI](https://www.patricksoftwareblog.com/setting-up-gitlab-ci-for-a-python-application/) 
[![Exercise](./images/GitLab_CI_Pipeline_Screenshot.png)](https://www.patricksoftwareblog.com/setting-up-gitlab-ci-for-a-python-application/) 

---

## Intermezzo: GitLab runners

- A GitLab runner is like a build server:
  - Shell based
  - Docker based
--

- A runner can be tailor-made
--

- Let's look at them in GitLab!

---

## Setting Up GitLab CI: unit tests

![.gitlab-ci.yml](images/unit-test-yml.png)


---

### Create a CI pipeline

```yml
image: "python:3.7"

default:
  before_script:
    - cd app
    - pip install -r requirements.txt

stages:
  - Unit tests

tests:
  stage: Unit tests
  script:
    - pytest --junitxml=report.xml
  artifacts:
    when: always
    expire_in: 2 days
    reports:
      junit: app/report.xml
  tags:
    - docker

```

---

### Commit and run the pipeline

1. Commit
  ```bash
  $ git commit -am "Unit tests"
  ```
2. Push
  ```bash
  $ git push
  ```
3. Go to GitLab and check if it runs the pipeline!

---

### Assignment unit testing

1. Can you access/download/inspect [the unit test report](https://docs.gitlab.com/ee/ci/unit_test_reports.html)
2. Can you access/inspect the log file?
3. Try to add a unit test and see if it executes.
4. At which stage(s) should unit tests be executed? Why?


---

## Code quality assurance in pipeline

1. Linting with Flake8
2. Linting with pylint
3. Type checking with mypy

---

### Linting with Flake8

- Create an additional stage called "Static analysis"
- Add job

```yml
flake8:
  stage: Static analysis
  script:
    - flake8 --max-line-length=120 *.py
  tags:
    - docker
```
- Extend the "requirements.txt" with "flake8==3.9.1"
- Commit your changes and see what happens
- Try to fix the errors, as these break the build!
- When do/should you get feedback about
  - Your linting process?
  - Your changes to the pipeline?
  - The changes/fixes you make in the code?

---

## Intermezzo: Testing the pipeline locally

1. [Install the GitLab runner package](https://docs.gitlab.com/runner/install/)
2. For Ubuntu, this worked:
  ```bash
  $ curl -LJO "https://gitlab-runner-downloads.s3.amazonaws.com/latest/deb/gitlab-runner_amd64.deb"
  $ sudo dpkg -i gitlab-runner_amd64.deb
  $ gitlab-runner exec shell flake8
  ```

---

### Optional: adding a pylint job

1. Extend the "requirements.txt" with "pylint==2.8.2"
2. Create a pylint job in the pipeline:
  - The pylint command is
    ```bash
    pylint -d C0301 *.py
    ```
  - You may want to add the following attribute
    ```yml
    allow_failure: true
    ```
  - Try to run the job locally before committing!
3. What happens when the pipeline finishes?

---

## Optional: adding type checking

1. Extend the "requirements.txt" with "mypy==0.812"
2. The command to run mypy is
  ```bash
  $ python -m mypy *.py
  ```
3. Fixing the "mypy" errors will be too time consuming 
  - add "allow_failure: true" for now

---

## Optional: more shift left: use your IDE

1. Import the existing project into PyCharm
2. You may need the "GitLab Projects 2020" plugin as well
3. Link PyCharm to GitLab

  ![PyCharm settings](images/pycharm-gitlab.png)

---

## Optional: more shift left: plugins

1. Install the "mypy" and "pylint" plugins
2. pylint may suffer [this problem](https://stackoverflow.com/questions/38134086/how-to-run-pylint-with-pycharm)
3. Try to fix some scanning issues using the IDE

---

## HOWTO add integration tests

- We will spin up a container and test our endpoint
--

- Which Docker image for execution is needed?
--

- But does that mean we run Docker in Docker (dind)?!


---

## Intermezzo: Defining environment variables

- This is how we do it:
  ```yml
  variables:
    DOCKER_IMAGE_NAME: "zhendrikse/harvest-masterclass:latest"
  ```

#### Leave the zhendrikse but change the name!

---

## Define the integration test job

```yml

fibonacci_8:
  image: docker:latest
  services:
    - docker:dind 
  stage: Integration test
  before_script:
    - echo "Running integration test"
  script:
    - docker build --tag $DOCKER_IMAGE_NAME .
    - docker run --rm --name integration-test -d $DOCKER_IMAGE_NAME
    - docker exec integration-test apk add curl
    - docker exec integration-test curl -i localhost/api/fibonacci/8
    - docker stop integration-test

```

#### Do not commit yet!

---

### Testing the integration test 

1. Can you test this integration test locally?
2. Inspect the log; was the test succesful?
3. Make the Curl URL invalid. 
   - Is the test still successful? 
   - Does/will the pipeline break? 
   - Why? 
4. Commit and see if the pipeline breaks?
5. What do we learn from this and how do we fix it?

---

## Finishing up the CI cycle

- What should the artifact be?
--

  - Docker image? 
  - Raw Python files? 
  - Packed Python files (Python wheels)?
  - ...

---

## Delivering the build artifact

Uploading our Docker image to Docker hub:

```yml
build:
  image: docker:latest
  services:
    - docker:dind 
  stage: Build
  before_script:
    - echo "Running build"
  script:
    - docker build --tag $DOCKER_IMAGE_NAME .
    - echo "$DOCKER_HUB_TOKEN" | docker login --username zhendrikse --password-stdin
    - docker push $DOCKER_IMAGE_NAME
```

#### Do not commit yet!

- Where/how do we get Docker hub credentials?
--

- Where/how do we store the DOCKER_HUB_TOKEN?
--

- Could/should we do it differently?

---

## Retrospective CI

--
- How would this work for other technologies?

--
- What could we refactor?
--

  - The scripts in the YML!
  - Linting the ".gitlab-ci.yml"
  - ...
--

- Code quality checks before or after the unit tests?
--

- Security?

---
## Deployment to AWS cloud

- We pull the Docker image using Ansible
- We start the Docker image using Ansible
- How do we test this?
- Can/should we automate this?

---

### The Ansible Playbook

```yml
&minus;&minus;&minus;
- hosts: all:!localhost
  gather_facts: no
  vars:
    ansible_python_interpreter: /usr/bin/python3

  tasks:
    - name: install pip3
      become: true
      command: apt install python3-pip -y

    - name: install docker-py
      command: pip3 install docker-py

    - name: pull docker image
      command: docker pull zhendrikse/harvest-masterclass:latest

    - name: start docker container
      docker_container:
        state: started
        restart_policy: always
        name: fibonacci-api
        image: zhendrikse/harvest-masterclass:latest
        ports:
          - 80:80
```

---

### Running Ansible 

Running Ansible requires some additional variables

- What should we use as EC2_INSTANCE value?!

```yml
variables:
  DOCKER_IMAGE_NAME: "zhendrikse/harvest-masterclass:latest"
  EC2_INSTANCE: "3.142.232.122"
  ANSIBLE_HOST_KEY_CHECKING: 'false'
  ANSIBLE_FORCE_COLOR: 'true'
```
- Create a folder "ansible"
  - with a file "docker_playbook.yml"
  - with contents of previous slide

- Create the GitLab job (next slide)

---

### Deployment job

```yml
deploy:
  image: gableroux/ansible:2.7.10
  stage: Deploy prod
  before_script:
    - echo "Creating private key to access instance via SSH"
    - mkdir ~/.ssh 
    - echo "-----BEGIN RSA PRIVATE KEY-----" &gt; ~/.ssh/id_rsa
    - echo $EC2_SSH_PRIVATE_KEY | tr ' ' '\n' | tail -n+5 | head -n-4 &gt;&gt; ~/.ssh/id_rsa
    - echo "-----END RSA PRIVATE KEY-----" &gt;&gt; ~/.ssh/id_rsa
    - chmod og-rw ~/.ssh/id_rsa
  script:
    - ansible-playbook -i"$EC2_INSTANCE", ansible/docker_playbook.yml -u ubuntu --private-key=~/.ssh/id_rsa
  environment:
    name: production
    url: http://$EC2_INSTANCE

```

- Can we explain what happens here?
- What does the "environment" do?

---

### Executing the deployment

1. Make sure the ***EC2 IP address*** is set correctly
2. Make sure ***your user is correct***, ask the trainer!
3. Create the Ansible playbook
4. Create the deployment job
5. Commit and watch the deployment
6. How do we check the service is up?
7. How can we automate this check?

---

### Smoke testing our deployment

Add this smoke test

```yml
smoke:
  image: curlimages/curl
  stage: Smoke test
  before_script:
    - echo "Running smoke test"
  script:
    - curl $EC2_INSTANCE/api/ping
```

---

## Where do we go from here?

- Build a DTAP street?
- Shouldn't we do something with [semantic versioning](https://semver.org/lang/nl/)?
- Shouldn't we provide the infrastructure too?
  - Terraform, CloudFormation, etc.
  - Infra as code, pipeline as code, configuration as code
  - SaaS over PaaS over IaaS
- Do we really want to stick to Docker for this app?

---

## Advanced suggestions

- Let's try to use our template to deploy [a ML app](https://github.com/jgvaraujo/ml-deployment-on-gcloud)
- What are the differences for [CD for machine learning](https://martinfowler.com/articles/cd4ml.html)
- Extend the API with a database [like so](https://dev.to/_mertsimsek/falcon-api-framework-on-docker-5eid)
- Other suggestions...?
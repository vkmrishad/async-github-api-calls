# async-github-api-calls
async-github-api-calls

Using black for Pylint - [Black](https://black.readthedocs.io/en/stable/)


## Environment and Package Management

Install Poetry

    $ pip install poetry
    or
    $ pip3 install poetry

Activate or Create Env

    $ poetry shell

Install Packages from Poetry

    $ poetry install

NB: When using virtualenv, install from `$ pip install -r requirements.txt`.

## .Env
    export GITHUB_TOKEN=ghp_xxxxxxxxxxxxxxxxxxxx
Generate GitHub Token - [Link](https://github.com/settings/tokens)

## Runserver

    $ uvicorn main:app
    or
    $ uvicorn main:app --host 0.0.0.0 --port 8000
    or
    $ uvicorn main:app --reload

## API Endpoints

    http://127.0.0.1:8080/users?usernames=vkmrishad,mojombo - Users
    http://127.0.0.1:8080/users?usernames=vkmrishad,mojombo&include=commit_latest -  Include Latest Commit


### Users

request:

    GET /users?usernames=vkmrishad,mojombo HTTP/1.1
    Host: 127.0.0.1:8000

response:

    [
        {
            "id": 18536460,
            "login_name": "vkmrishad",
            "url": "https://github.com/vkmrishad",
            "public_repos": [
                {
                    "id": 383526409,
                    "repo_name": "cryptoserver",
                    "created_at": "2021-07-06T16:04:02Z",
                    "updated_at": "2021-07-17T04:57:37Z",
                    "url": "https://github.com/vkmrishad/cryptoserver"
                },
                ...
                ...
                ...
                {
                    "id": 97393599,
                    "repo_name": "inpycon2017",
                    "created_at": "2017-07-16T15:47:28Z",
                    "updated_at": "2017-07-16T15:47:30Z",
                    "url": "https://github.com/vkmrishad/inpycon2017"
                }
            ]
        },
        {
            "id": 1,
            "login_name": "mojombo",
            "url": "https://github.com/mojombo",
            "public_repos": [
                {
                    "id": 330651,
                    "repo_name": "bert",
                    "created_at": "2009-10-08T06:06:25Z",
                    "updated_at": "2021-08-06T09:34:52Z",
                    "url": "https://github.com/mojombo/bert"
                },
                ...
                ...
                ...
                {
                    "id": 1015,
                    "repo_name": "fixture-scenarios",
                    "created_at": "2008-02-23T04:25:57Z",
                    "updated_at": "2021-01-13T19:25:22Z",
                    "url": "https://github.com/mojombo/fixture-scenarios"
                }
            ]
        }
    ]

### Include Latest Commit

request:

    GET /users?usernames=vkmrishad,mojombo&include=commit_latest HTTP/1.1
    Host: 127.0.0.1:8000

response:

    [
        {
            "id": 18536460,
            "login_name": "vkmrishad",
            "url": "https://github.com/vkmrishad",
            "public_repos": [
                {
                    "id": 383526409,
                    "repo_name": "cryptoserver",
                    "created_at": "2021-07-06T16:04:02Z",
                    "updated_at": "2021-07-17T04:57:37Z",
                    "url": "https://github.com/vkmrishad/cryptoserver",
                    "commit_latest": [
                        {
                            "sha": "688c43d198c78febb2fa8edab24694da1e96b436",
                            "url": "https://github.com/vkmrishad/cryptoserver/commit/688c43d198c78febb2fa8edab24694da1e96b436",
                            "commit": {
                                "author": {
                                    "name": "vipindasvg",
                                    "email": "51224648+vipindasvg@users.noreply.github.com",
                                    "date": "2021-06-21T18:34:27Z"
                                },
                                "committer": {
                                    "name": "GitHub",
                                    "email": "noreply@github.com",
                                    "date": "2021-06-21T18:34:27Z"
                                }
                            }
                        }
                    ]
                },
                ...
                ...
                ...
                {
                    "id": 97393599,
                    "repo_name": "inpycon2017",
                    "created_at": "2017-07-16T15:47:28Z",
                    "updated_at": "2017-07-16T15:47:30Z",
                    "url": "https://github.com/vkmrishad/inpycon2017",
                    "commit_latest": [
                        {
                            "sha": "89066fe7fed5e8f58e51161d65727057827bbe57",
                            "url": "https://github.com/vkmrishad/inpycon2017/commit/89066fe7fed5e8f58e51161d65727057827bbe57",
                            "commit": {
                                "author": {
                                    "name": "Sanyam Khurana",
                                    "email": "sanyam@sanyamkhurana.com",
                                    "date": "2017-07-12T12:39:14Z"
                                },
                                "committer": {
                                    "name": "Saurabh Kumar",
                                    "email": "thes.kumar@gmail.com",
                                    "date": "2017-07-12T12:39:14Z"
                                }
                            }
                        }
                    ]
                }
            ]
        },
        {
            "id": 1,
            "login_name": "mojombo",
            "url": "https://github.com/mojombo",
            "public_repos": [
                {
                    "id": 330651,
                    "repo_name": "bert",
                    "created_at": "2009-10-08T06:06:25Z",
                    "updated_at": "2021-08-06T09:34:52Z",
                    "url": "https://github.com/mojombo/bert",
                    "commit_latest": [
                        {
                            "sha": "c2abcc4868bb47909696c6a42c606de34e83ef70",
                            "url": "https://github.com/mojombo/bert/commit/c2abcc4868bb47909696c6a42c606de34e83ef70",
                            "commit": {
                                "author": {
                                    "name": "Aman Gupta",
                                    "email": "aman@tmm1.net",
                                    "date": "2012-05-25T22:03:29Z"
                                },
                                "committer": {
                                    "name": "Aman Gupta",
                                    "email": "aman@tmm1.net",
                                    "date": "2012-05-25T22:03:29Z"
                                }
                            }
                        }
                    ]
                },
                ...
                ...
                ...
                {
                    "id": 1015,
                    "repo_name": "fixture-scenarios",
                    "created_at": "2008-02-23T04:25:57Z",
                    "updated_at": "2021-01-13T19:25:22Z",
                    "url": "https://github.com/mojombo/fixture-scenarios",
                    "commit_latest": [
                        {
                            "sha": "318923c237a82d867545f60acd6a5ecbb1496776",
                            "url": "https://github.com/mojombo/fixture-scenarios/commit/318923c237a82d867545f60acd6a5ecbb1496776",
                            "commit": {
                                "author": {
                                    "name": "Tom Preston-Werner",
                                    "email": "tom@mojombo.com",
                                    "date": "2007-05-04T21:47:27Z"
                                },
                                "committer": {
                                    "name": "Tom Preston-Werner",
                                    "email": "tom@mojombo.com",
                                    "date": "2007-05-04T21:47:27Z"
                                }
                            }
                        }
                    ]
                }
            ]
        }
    ]


## Test

    $ pytest


## Version

* Python: 3.8+

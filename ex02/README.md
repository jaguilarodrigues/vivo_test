# Count Element API


Stack used was Python, Flask

![Stack](./images/stack.png)

API that recive an list of numbers and count how many times its elements appear in a matrix

## Installation

For the installation use

`python3 -m venv venv`

`source venv/bin/activate`

`pip install -r requirements.txt`

and export the vars to the anv

`export FLASK_APP=counter/app.py`

## Getting Started
	
### The root

`http://127.0.0.1:5000/`


**Method** : `GET`

```json
[
    {
  		"Introduction": "Give me a vector and i'll count how many times its elements appear"
	}
]
```

### Example of use

**URL** : `/count/?vector=0&vector=7`

**Method** : `GET`

Resposta:

```json
[
   {
        "0": "5",
        "7": "6"
   }
]
```


# Number Classification API

This project contains a public API that an API that takes a number and returns interesting mathematical properties about it, along with a fun fact.

## Technologies Used
- Python
- Flask
- Git
- Vercel

## Prerequisite
- Python 3.8 or higher
- pip (Python package manager)

## Local Development
1. Clone repo
`git clone https://github.com/Ibotyle/1stage.git`

1.1. Change Directory to 1stage
`cd code12`

3. Create Virtual Environment
   `python -m venv venv`
   
4. Activate Virtual Environment
   `source venv/bin/activate`

5. Install dependencies
`pip install -r requirements.txt`

6. Run the application
`flask run`

API should be running on http://127.0.0.1:5000/api/classify-number?number=44


## To access Project
Send a get request to https://1stage.vercel.app/api/classify-number?number=44

## Example Usage

### Request
`curl -X GET https://1stage.vercel.app/api/classify-number?number=44
`
### Response
`
{
  "number": "44",
  "is_prime": false,
  "is_perfect": false,
  "properties": [
    "even"
  ],
  "digit_sum": 8,
  "fun_fact": "44 is the number of derangements of 5 items."
}
`

## Backlink
<a href="https://hng.tech/hire/python-developers">Python Developers</a>

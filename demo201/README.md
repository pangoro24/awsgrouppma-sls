Deploy 
npx serverless deploy --stage dev

Testing locally
Online
npx serverless invoke local -f hello --stage dev
Offline
npx serverless offline --stage dev


Notes about mock data
json.loads take a string as input and returns a dictionary as output.
json.dumps take a dictionary as input and returns a string as output.

curl --location --request POST 'http://localhost:3000/dev/public/hello' --header 'Content-Type: application/json' --data-raw '{"name": "Pablo","cloud": "AWS"}'

curl -X POST https://xeegkcu5kk.execute-api.us-east-1.amazonaws.com/dev/public/hello -d {"name":"Pablo","cloud":"AWS"}
# Create a webapp using sls thru lift
* serverless plugin install -n serverless-lift
* flutter create mywebsite --platforms web
* cd mywebsite
* flutter run -d chrome
* Edit application code in mywebsite\lib\main.dart
* flutter build web
* npx serverless deploy


##### Output
https://dtgilwjdbs8h0.cloudfront.net


# How to update files
* flutter build web* 
* cd ..
* npx serverless landing-page:upload

##### Output
Deployed https://dtgilwjdbs8h0.cloudfront.net
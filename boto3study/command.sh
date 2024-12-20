aws s3 cp ~/enviornment s3://vincent-sample/enviornment --endpoint-url=http://localhost:4566
aws s3 cp s3://vincent-sample/enviornment s3://vincent-sample/enviornment-v2 --endpoint-url=http://localhost:4566
aws s3 mv s3://vincent-sample/enviornment-v2 s3://vincent-sample/enviornment-v3 --endpoint-url=http://localhost:4566
aws s3 rm s3://vincent-sample/enviornment-v3 --endpoint-url=http://localhost:4566


aws s3 mb s3://vincent-sample --endpoint-url=http://localhost:4566
name: Build and Deploy to EC2

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout Repository
      uses: actions/checkout@v2

    - name: Setup Node.js
      uses: actions/setup-node@v4
      with:
        node-version: '14'

    - name: Install Dependencies
      run: npm install

    - name: Build Project
      run: npm run build

    - name: Install AWS CLI
      run: |
        sudo apt-get update
        sudo apt-get install -y awscli

    - name: Transfer Build Artifacts to EC2
      run: aws ssm send-command --targets Key=instanceids,Values=your-ec2-instance-id --document-name "AWS-RunShellScript" --parameters commands="mkdir -p /path/to/your/app && scp -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -r build/* ec2-user@localhost:/path/to/your/app/"

    - name: Deploy to EC2
      run: aws ssm send-command --targets Key=instanceids,Values=your-ec2-instance-id --document-name "AWS-RunShellScript" --parameters commands="cd /path/to/your/app && ./deploy.sh"

FROM public.ecr.aws/lambda/python:3.10

# Update the package repositories and install dependencies
RUN yum -y update

# Install Node.js and npm
RUN yum -y groupinstall "Development Tools" && \
    curl --silent --location https://rpm.nodesource.com/setup_16.x | bash - && \
    yum install -y nodejs && \
    yum clean all

# Install Python packages
RUN pip3 install --upgrade pip && \
    pip3 install cfn-lint awscli pipenv twine

# Install AWS CDK
RUN npm install -g npm aws-cdk

USER root

# Set the working directory
WORKDIR /app

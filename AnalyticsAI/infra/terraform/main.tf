# Example: Provision a simple Kubernetes cluster for AnalyticsAI

provider "aws" {
  region = "us-east-1"
}

module "eks" {
  source          = "terraform-aws-modules/eks/aws"
  cluster_name    = "analyticsai-eks"
  cluster_version = "1.29"
  subnets         = ["subnet-xxxxxx"]
  vpc_id          = "vpc-xxxxxx"
}